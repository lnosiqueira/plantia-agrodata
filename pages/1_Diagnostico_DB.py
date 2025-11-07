import streamlit as st
import oracledb
from src.config import get_oracle_cfg

st.set_page_config(page_title="Diagnóstico Oracle – PlantIA", page_icon="🌾", layout="wide")

cfg = get_oracle_cfg()
dsn = oracledb.makedsn(cfg["host"], cfg["port"], sid=cfg["sid"])
if not pwd:
    raise RuntimeError("ORACLE_PWD não definida. Configure via .env/variável de ambiente.")

try:
    with oracledb.connect(user=user, password=pwd, dsn=dsn) as conn:
        st.success("Conectado ao Oracle ✅")
        with conn.cursor() as cur:
            cur.execute("SELECT CURRENT_TIMESTAMP FROM dual")
            st.write("Hora do servidor:", cur.fetchone()[0])

            cur.execute("""
                INSERT INTO PLANTIA_AGRO_LOG (source, message)
                VALUES (:1, :2)
            """, ["streamlit", f"Acesso via Streamlit em {datetime.now()}"])
            conn.commit()

            cur.execute("""
                SELECT id, created_at, source, message
                FROM PLANTIA_AGRO_LOG
                ORDER BY id DESC FETCH FIRST 5 ROWS ONLY
            """)
            rows = cur.fetchall()
            st.table(rows)
except Exception as e:
    st.error(f"Falha na conexão: {e}")
