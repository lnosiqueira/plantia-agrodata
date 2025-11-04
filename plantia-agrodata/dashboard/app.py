import os
import streamlit as st
import pandas as pd
import plotly.express as px
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="PlantIA Agrodata - Dashboard", layout="wide")
st.title("🌱 PlantIA Agrodata – Dashboard (Fase 3)")

# Preferência Oracle -> fallback CSV
use_oracle = True
host = os.getenv("ORACLE_HOST")
port = os.getenv("ORACLE_PORT")
sid = os.getenv("ORACLE_SID")
user = os.getenv("ORACLE_USER")
pwd = os.getenv("ORACLE_PASSWORD")
table = os.getenv("ORACLE_TABLE", "PLANTIA_AGRODATA_SENSOR_DATA")

df = None

if use_oracle and all([host, port, sid, user, pwd]):
    try:
        import oracledb
        dsn = oracledb.makedsn(host, int(port), sid=sid)
        with oracledb.connect(user=user, password=pwd, dsn=dsn) as con:
            query = f"""SELECT ID_REGISTRO, TIMESTAMP, NITROGENIO, FOSFORO, POTASSIO,
                                   PH_SOLO, UMIDADE, TEMPERATURA, STATUS_BOMBA, RECOMENDACAO
                            FROM {table}
                            ORDER BY TIMESTAMP DESC"""
            df = pd.read_sql(query, con)
            st.success("✅ Conectado ao Oracle e dados carregados!")
    except Exception as e:
        st.warning(f"⚠️ Não foi possível conectar ao Oracle. Usando CSV de fallback. Detalhe: {e}")
        df = None

if df is None:
    csv_path = os.path.join("data", "plantia_sensores_fase2_sample.csv")
    df = pd.read_csv(csv_path)
    st.info("ℹ️ Dados carregados do CSV de exemplo (fallback).")
    # converter timestamp se existir
    for col in ["TIMESTAMP", "timestamp"]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

# KPIs simples
col1, col2, col3 = st.columns(3)
col1.metric("Umidade média (%)", f"{df['UMIDADE'].mean():.2f}" if 'UMIDADE' in df else "-")
col2.metric("pH médio", f"{df['PH_SOLO'].mean():.2f}" if 'PH_SOLO' in df else "-")
col3.metric("Temperatura média (°C)", f"{df['TEMPERATURA'].mean():.2f}" if 'TEMPERATURA' in df else "-")

# Gráficos
if "TIMESTAMP" in df.columns and "UMIDADE" in df.columns:
    fig = px.line(df.sort_values("TIMESTAMP").tail(200), x="TIMESTAMP", y="UMIDADE", title="Umidade do Solo (últimas leituras)")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Dados (amostra)")
st.dataframe(df.head(50))
