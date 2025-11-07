# app/deps/db.py
import oracledb
from src.config import get_oracle_cfg

def connect():
    cfg = get_oracle_cfg()
    dsn = oracledb.makedsn(cfg["host"], cfg["port"], sid=cfg["sid"])
    return oracledb.connect(user=cfg["user"], password=cfg["pwd"], dsn=dsn)

def ping() -> dict:
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT CURRENT_TIMESTAMP FROM dual")
            ts = cur.fetchone()[0]
    return {"ok": True, "db_time": str(ts)}

