# test_oracle_conn.py
import oracledb
from src.config import get_oracle_cfg

def main():
    cfg = get_oracle_cfg()
    dsn = oracledb.makedsn(cfg["host"], cfg["port"], sid=cfg["sid"])
    with oracledb.connect(user=cfg["user"], password=cfg["pwd"], dsn=dsn) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 'OK' AS STATUS FROM dual")
            print("✅ Conexão bem-sucedida com o Oracle (FIAP)! ->", cur.fetchone()[0])

if __name__ == "__main__":
    main()

