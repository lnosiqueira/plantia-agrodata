from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Dict, Any
import os

def get_oracle_conn():
    user = os.getenv("ORACLE_USER")
    pwd  = os.getenv("ORACLE_PASS")
    dsn  = os.getenv("ORACLE_DSN")
    if not all([user, pwd, dsn]):
        raise RuntimeError("Variáveis de ambiente ORACLE_USER/ORACLE_PASS/ORACLE_DSN não configuradas.")
    try:
        import cx_Oracle
        return cx_Oracle.connect(user=user, password=pwd, dsn=dsn)
    except Exception as e:
        raise RuntimeError(f"Falha ao abrir conexão Oracle: {e}")

app = FastAPI(title="PlantIA Agrodata API", version="3.0.0")

@app.get("/health")
def health():
    return {"ok": True, "service": "PlantIA API", "version": "3.0.0"}

@app.get("/dashboard/metrics")
def dashboard_metrics(city: str = Query(..., description="Cidade (ex.: 'São Paulo')")) -> Dict[str, Any]:
    try:
        conn = get_oracle_conn()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    cur = conn.cursor()
    out: Dict[str, Any] = {"city": city}

    medias_sql_join = """
    SELECT
      ROUND(AVG(CASE WHEN UPPER(TRIM(s.TIPO_SENSOR))='UMIDADE SOLO'     THEN s.LEITURA_VALOR END),2) AS UMIDADE_MEDIA,
      ROUND(AVG(CASE WHEN UPPER(TRIM(s.TIPO_SENSOR))='TEMPERATURA SOLO' THEN s.LEITURA_VALOR END),2) AS TEMPERATURA_MEDIA,
      ROUND(AVG(CASE WHEN UPPER(TRIM(s.TIPO_SENSOR))='PH SOLO'          THEN s.LEITURA_VALOR END),2) AS PH_MEDIO
    FROM SENSORS_DATA_V2 s
    JOIN FIELDS_V2 f ON f.ID = s.CAMPO_ID
    WHERE UPPER(TRIM(f.CIDADE)) = UPPER(TRIM(:city))
    """

    fallback_map = {
    "SÃO PAULO": [201, 205],
    "MATO GROSSO (CUIABÁ)": [202],
    "PARANÁ (CURITIBA)": [203],
    # ...
}

    try:
        try:
            cur.execute(medias_sql_join, {"city": city})
            r = cur.fetchone()
            if r and any(r):
                out.update({"UMIDADE_MEDIA": r[0], "TEMPERATURA_MEDIA": r[1], "PH_MEDIO": r[2], "source": "JOIN_FIELDS_V2"})
            else:
                raise Exception("Sem join")
        except Exception:
            ids = fallback_map.get(city.upper(), [])
            if ids:
                q = f"""
                SELECT
                  ROUND(AVG(CASE WHEN UPPER(TRIM(TIPO_SENSOR))='UMIDADE SOLO'     THEN LEITURA_VALOR END),2),
                  ROUND(AVG(CASE WHEN UPPER(TRIM(TIPO_SENSOR))='TEMPERATURA SOLO' THEN LEITURA_VALOR END),2),
                  ROUND(AVG(CASE WHEN UPPER(TRIM(TIPO_SENSOR))='PH SOLO'          THEN LEITURA_VALOR END),2)
                FROM SENSORS_DATA_V2
                WHERE CAMPO_ID IN ({",".join([str(i) for i in ids])})
                """
                cur.execute(q)
                r = cur.fetchone()
                out.update({"UMIDADE_MEDIA": r[0], "TEMPERATURA_MEDIA": r[1], "PH_MEDIO": r[2], "source": "fallback-map"})
            else:
                out.update({"UMIDADE_MEDIA": None, "TEMPERATURA_MEDIA": None, "PH_MEDIO": None, "source": "fallback-empty"})
    except Exception as e:
        cur.close()
        conn.close()
        raise HTTPException(status_code=500, detail=f"Erro ao calcular médias: {e}")

    try:
        clima_sql = """
        SELECT TEMP_C, HUMIDITY_PCT
        FROM (
          SELECT CIDADE, TEMP_C, HUMIDITY_PCT, DATA_MEDICAO
          FROM WEATHER_DATA_V2
          WHERE UPPER(TRIM(CIDADE)) = UPPER(TRIM(:city))
          ORDER BY DATA_MEDICAO DESC
        ) WHERE ROWNUM = 1
        """
        cur.execute(clima_sql, {"city": city})
        c = cur.fetchone()
        if c:
            out.update({"WEATHER_TEMP_C": c[0], "WEATHER_HUMIDITY_PCT": c[1]})
        else:
            out.update({"WEATHER_TEMP_C": None, "WEATHER_HUMIDITY_PCT": None})
    except Exception as e:
        out.update({"WEATHER_TEMP_C": None, "WEATHER_HUMIDITY_PCT": None, "weather_error": str(e)})

    cur.close()
    conn.close()
    return out

class SensorRow(BaseModel):
    id: int
    tipo: str
    valor: float
    unidade: str

class IngestRequest(BaseModel):
    leituras: List[SensorRow]

@app.post("/oracle/ingest")
def ingest(req: IngestRequest):
    try:
        conn = get_oracle_conn()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    cur = conn.cursor()
    inserted = 0
    try:
        for row in req.leituras:
            cur.execute(
                """
                INSERT INTO SENSORS_DATA_V2 (CAMPO_ID, TIPO_SENSOR, LEITURA_VALOR, UNIDADE, DATA_LEITURA)
                VALUES (:1, :2, :3, :4, SYSDATE)
                """,
                (row.id, row.tipo, row.valor, row.unidade),
            )
            inserted += 1
        conn.commit()
        return {"ok": True, "inserted": inserted}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao inserir leituras: {e}")
    finally:
        cur.close()
        conn.close()
