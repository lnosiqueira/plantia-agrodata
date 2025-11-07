import os
import sys
import time
from datetime import datetime, timedelta
import pandas as pd
import streamlit as st

# Dependência do Oracle
try:
    import oracledb
except Exception as e:
    st.error("Pacote 'oracledb' não encontrado. Instale com: pip install oracledb")
    st.stop()

# =========================
# Configurações da Página
# =========================
st.set_page_config(
    page_title="PlantIA Agrodata • Telemetria de Colheita",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 Telemetria de Colheita — PlantIA Agrodata (FIAP)")
st.caption("Dashboard analítico conectado ao Oracle | v1.1.0")

# =========================
# Sidebar • Parâmetros
# =========================
with st.sidebar:
    st.header("⚙️ Configurações")

    # Credenciais (usando variáveis de ambiente)
    default_user = os.getenv("ORACLE_USER", "")
    default_pwd = os.getenv("ORACLE_PWD", "")
    show_creds = st.checkbox("Exibir campos de usuário/senha (opcional)", value=False)

    if show_creds:
        user = st.text_input("Usuário Oracle (FIAP)", value=default_user, type="default")
        pwd = st.text_input("Senha Oracle (FIAP)", value=default_pwd, type="password")
    else:
        user = default_user
        pwd = default_pwd

    st.divider()

    # Host/porta/serviço padrão FIAP
    host = st.text_input("Host", value=os.getenv("ORACLE_HOST", "oracle.fiap.com.br"))
    port = st.number_input("Porta", value=int(os.getenv("ORACLE_PORT", "1521")), step=1)
    service = st.text_input("SID/Service Name", value=os.getenv("ORACLE_SVC", "ORCL"))

    # Nome esperado da tabela de colheitas
    st.caption("A tabela padrão esperada é 'PLANTIA_COLHEITA'. Ajuste se necessário.")
    table_name = st.text_input("Tabela de Colheita", value=os.getenv("PLANTIA_TABLE", "PLANTIA_COLHEITA")).upper()

    st.divider()

    st.caption("Mapeie os nomes de colunas conforme existentes no seu schema Oracle.")
    col_field = st.text_input("Coluna Campo (FIELD_ID)", value=os.getenv("PLANTIA_COL_FIELD", "FIELD_ID")).upper()
    col_date = st.text_input("Coluna Data (DATA_COLHEITA)", value=os.getenv("PLANTIA_COL_DATE", "DATA_COLHEITA")).upper()
    col_prod = st.text_input("Coluna Produção (ton) (PROD_TON)", value=os.getenv("PLANTIA_COL_PROD", "PROD_TON")).upper()
    col_loss = st.text_input("Coluna Perda (%) (PERDA_PCT)", value=os.getenv("PLANTIA_COL_LOSS", "PERDA_PCT")).upper()

    st.divider()

    days_back = st.slider("Janela inicial (dias para trás)", min_value=7, max_value=365, value=90, step=1)
    start_date = st.date_input("Data inicial", value=(datetime.today() - timedelta(days=days_back)))
    end_date = st.date_input("Data final", value=datetime.today())
    st.caption("Dica: você pode filtrar depois por campo específico na própria tela.")

    st.divider()
    run_btn = st.button("🚀 Atualizar Dashboard", type="primary")

# =========================
# Conexão e Consulta
# =========================
def make_dsn(host: str, port: int, service: str) -> str:
    # Usa SID (ORCL) como valor padrão; se o usuário quiser SERVICE_NAME, também funciona
    try:
        return oracledb.makedsn(host, int(port), sid=service)
    except Exception:
        # fallback para service_name
        return oracledb.makedsn(host, int(port), service_name=service)

@st.cache_data(ttl=60)
def query_oracle_dataframe(user, pwd, dsn, table, col_field, col_date, col_prod, col_loss, dt_ini, dt_fim):
    sql = f"""
        SELECT
            {col_field} AS FIELD_ID,
            CAST({col_date} AS DATE) AS DATA_COLHEITA,
            CAST({col_prod} AS NUMBER) AS PROD_TON,
            CAST({col_loss} AS NUMBER) AS PERDA_PCT
        FROM {table}
        WHERE {col_date} BETWEEN :dtini AND :dtfim
        ORDER BY {col_date} ASC
    """
    with oracledb.connect(user=user, password=pwd, dsn=dsn) as conn:
        df = pd.read_sql(sql, con=conn, params={"dtini": dt_ini, "dtfim": dt_fim})
    # Normalizações
    if not df.empty:
        df["FIELD_ID"] = df["FIELD_ID"].astype(str)
        df["DATA_COLHEITA"] = pd.to_datetime(df["DATA_COLHEITA"])
        df = df.sort_values("DATA_COLHEITA")
    return df

def safe_query(*args, **kwargs):
    try:
        return query_oracle_dataframe(*args, **kwargs), None
    except oracledb.DatabaseError as db_err:
        return pd.DataFrame(), f"Erro Oracle: {str(db_err)}"
    except Exception as e:
        return pd.DataFrame(), f"Falha ao consultar: {e}"

# =========================
# Execução
# =========================
if run_btn:
    if not user or not pwd:
        st.error("Defina as credenciais via variáveis de ambiente (ORACLE_USER / ORACLE_PWD) ou exponha os campos na sidebar.")
        st.stop()

    dsn = make_dsn(host, port, service)
    with st.spinner("Conectando ao Oracle e carregando dados..."):
        df, err = safe_query(
            user, pwd, dsn, table_name,
            col_field, col_date, col_prod, col_loss,
            datetime.combine(start_date, datetime.min.time()),
            datetime.combine(end_date, datetime.max.time())
        )

    if err:
        st.error(err)
        st.info("Verifique: tabela/colunas, período, credenciais ou conectividade. Ajuste o mapeamento das colunas na sidebar.")
        st.stop()

    if df.empty:
        st.warning("Nenhum registro encontrado no intervalo selecionado. Ajuste as datas ou valide a tabela/colunas.")
        st.stop()

    # =========================
    # Filtros e KPIs
    # =========================
    with st.container():
        left, mid, right = st.columns(3)
        with left:
            total_ton = float(df["PROD_TON"].sum())
            st.metric("Total Colhido (t)", f"{total_ton:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        with mid:
            media_perda = float(df["PERDA_PCT"].mean())
            st.metric("Média de Perda (%)", f"{media_perda:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        with right:
            qtd_reg = int(len(df))
            st.metric("Registros no Período", f"{qtd_reg}")

    st.divider()

    # Filtro por campo
    campos = ["(Todos)"] + sorted(df["FIELD_ID"].unique().tolist())
    field_pick = st.selectbox("Filtrar por Campo (FIELD_ID)", options=campos, index=0)
    if field_pick != "(Todos)":
        dff = df[df["FIELD_ID"] == field_pick].copy()
    else:
        dff = df.copy()

    # =========================
    # Tabelas e Gráficos
    # =========================
    st.subheader("📋 Registros")
    st.dataframe(dff, use_container_width=True)

    st.subheader("📈 Série Temporal — Perda (%) ao longo do tempo")
    # Dados para linha temporal
    serie = dff.groupby("DATA_COLHEITA", as_index=True)["PERDA_PCT"].mean().sort_index()
    st.line_chart(serie)

    st.subheader("🏆 Ranking por Produção Total (t) — por Campo")
    ranking = (
        dff.groupby("FIELD_ID", as_index=False)["PROD_TON"]
        .sum()
        .sort_values("PROD_TON", ascending=False)
        .reset_index(drop=True)
    )
    st.bar_chart(ranking.set_index("FIELD_ID"))

    st.subheader("📊 Média de Perda (%) — por Campo")
    perda_media = (
        dff.groupby("FIELD_ID", as_index=False)["PERDA_PCT"]
        .mean()
        .sort_values("PERDA_PCT", ascending=True)
        .reset_index(drop=True)
    )
    st.bar_chart(perda_media.set_index("FIELD_ID"))

    st.success("Dashboard atualizado com sucesso ✅")

    with st.expander("🔎 Detalhes técnicos da consulta"):
        st.code(f"""
DSN: {dsn}
Tabela: {table_name}
Colunas: FIELD={col_field}, DATA={col_date}, PROD={col_prod}, PERDA={col_loss}
Período: {start_date} → {end_date}
Registros retornados: {len(df)}
        """.strip())

else:
    st.info("Defina os parâmetros na barra lateral e clique em **🚀 Atualizar Dashboard** para carregar os dados.")
    st.code("""
# Dica: no Windows, rode antes (no terminal) as variáveis de ambiente:
set ORACLE_USER=<seu_usuario_FIAP>
set ORACLE_PWD=<sua_senha_FIAP>

# Depois, execute o Streamlit na raiz do projeto:
python -m streamlit run pages/2_Telemetria_Colheita.py
    """.strip(), language="bash")