import os
import oracledb

# DSN com SID (igual ao SQL Developer)
dsn = oracledb.makedsn("oracle.fiap.com.br", 1521, sid="ORCL")

# Use o mesmo usuário/senha do SQL Developer
user = os.getenv("ORACLE_USER", "rm567893")
pwd  = os.getenv("ORACLE_PWD",  "Fiap#2025")

try:
    with oracledb.connect(user=user, password=pwd, dsn=dsn) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT CURRENT_TIMESTAMP FROM dual")
            print("✅ Conectado! Hora do servidor:", cur.fetchone()[0])

            cur.execute("""
                INSERT INTO PLANTIA_AGRO_LOG (source, message)
                VALUES (:1, :2)
            """, ["python_test", "Log inserido via script Python"])
            conn.commit()

            cur.execute("""
                SELECT id, created_at, source, message
                FROM PLANTIA_AGRO_LOG
                ORDER BY id DESC FETCH FIRST 2 ROWS ONLY
            """)
            for row in cur:
                print(row)
except Exception as e:
    print("❌ Falha na conexão:", e)
