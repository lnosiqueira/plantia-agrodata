import sqlite3

def connect_db(db_path="data/plantia.db"):
    conn = sqlite3.connect(db_path)
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS sensores (id INTEGER PRIMARY KEY, tipo TEXT, valor REAL)")
    conn.commit()
    conn.close()
