import json
from typing import List, Dict

# ========= JSON =========
def salvar_json(path: str, dados: List[Dict]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

def ler_json(path: str) -> List[Dict]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# ========= Oracle (esqueleto) =========
# Observação: requer 'cx_Oracle' instalado e Oracle Client configurado.
# Você pode ignorar esta parte por enquanto; o menu base não chama isso ainda.

try:
    import cx_Oracle  # type: ignore
except Exception:
    cx_Oracle = None  # permite rodar sem Oracle

def conectar_oracle(user: str, password: str, dsn: str):
    if cx_Oracle is None:
        raise RuntimeError(
            "cx_Oracle não está disponível no ambiente. "
            "Instale e configure o Oracle Client para usar esta função."
        )
    conn = cx_Oracle.connect(user=user, password=password, dsn=dsn, encoding="UTF-8")
    return conn

def inserir_harvests(conn, harvests: List[Dict]) -> None:
    sql = """
    INSERT INTO harvests (
        field_id, harvest_date, method, tons_expected,
        tons_collected, loss_percentage, notes
    )
    VALUES (
        :field_id, TO_DATE(:harvest_date, 'YYYY-MM-DD'), :method,
        :tons_expected, :tons_collected, :loss_percentage, :notes
    )
    """
    cur = conn.cursor()
    binds = [{
        "field_id": h["field_id"],
        "harvest_date": h["harvest_date"],
        "method": h["method"],
        "tons_expected": h["tons_expected"],
        "tons_collected": h["tons_collected"],
        "loss_percentage": h["loss_percentage"],
        "notes": h.get("notes", "")
    } for h in harvests]
    cur.executemany(sql, binds)
    conn.commit()
    cur.close()
