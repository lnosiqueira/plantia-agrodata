import streamlit as st
import os, oracledb
from datetime import datetime

st.title("Diagnóstico Oracle – PlantIA Agrodata")

dsn = oracledb.makedsn("oracle.fiap.com.br", 1521, sid="ORCL")
user = os.getenv("ORACLE_USER", "rm567893")
pwd  = os.getenv("ORACLE_PWD",  "Fiap#2025")

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
