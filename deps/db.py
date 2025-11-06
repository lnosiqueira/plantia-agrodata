import os
import oracledb
from fastapi import HTTPException

def check_db():
    dsn = oracledb.makedsn("oracle.fiap.com.br", 1521, sid="ORCL")
    user = os.getenv("ORACLE_USER", "rm567893")
    pwd  = os.getenv("ORACLE_PWD",  "Fiap#2025")

    try:
        with oracledb.connect(user=user, password=pwd, dsn=dsn) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1 FROM dual")
                return True
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"DB down: {e}")
