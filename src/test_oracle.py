import oracledb

# 🔧 Substitua pelos seus dados FIAP
USER = "SEU_USUARIO_FIAP"          # ex: rm123456
PASSWORD = "SUA_SENHA_FIAP"        # ex: Fiap@2025
DSN = "oracle.fiap.com.br:1521/ORCL"  # exato conforme fornecido pela FIAP

try:
    conn = oracledb.connect(
    user="rm567893",
    password="040782",
    dsn="oracle.fiap.com.br:1521/ORCL"
)

    print("✅ Conexão bem-sucedida com o Oracle (FIAP)!")
    cur = conn.cursor()
    cur.execute("SELECT 'PlantIA conectado à FIAP!' FROM dual")
    print("🔹 Mensagem:", cur.fetchone()[0])
    cur.close()
    conn.close()
    print("🔒 Conexão encerrada.")
except oracledb.DatabaseError as e:
    err, = e.args
    print("❌ Erro ao conectar ao Oracle:")
    print("Código:", err.code)
    print("Mensagem:", err.message)
