import streamlit as st
import requests
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="PlantIA Agrodata - Dashboard", layout="wide")
st.markdown("<h1 style='color:#2e7d32;'>🌱 PlantIA Agrodata - Dashboard Interativo</h1>", unsafe_allow_html=True)

API = "http://127.0.0.1:8000"

CIDADES = [
    "São Paulo",
    "Mato Grosso (Cuiabá)",
    "Paraná (Curitiba)",
    "Goiás (Goiânia)",
    "Minas Gerais (Belo Horizonte)",
]

with st.sidebar:
    st.header("🌍 Localização Agrícola")
    cidade = st.selectbox("Selecione a cidade", CIDADES, index=0)
    if st.button("Atualizar clima"):
        st.cache_data.clear()

@st.cache_data(ttl=30)
def get_metrics(city: str):
    try:
        r = requests.get(f"{API}/dashboard/metrics", params={"city": city}, timeout=6)
        if r.ok:
            return r.json()
    except Exception as e:
        st.warning(f"Falha ao consultar API: {e}")
    return None

dados = get_metrics(cidade)

tabs = st.tabs(["✅ Monitoramento", "💰 Impacto Econômico", "🌎 Sustentabilidade"])

with tabs[0]:
    st.subheader("Indicadores Agronômicos")
    c1,c2,c3,c4 = st.columns(4)
    if dados:
        c1.metric("Umidade Média", f"{dados.get('UMIDADE_MEDIA') if dados.get('UMIDADE_MEDIA') is not None else '-'} %")
        c2.metric("pH Médio", f"{dados.get('PH_MEDIO') if dados.get('PH_MEDIO') is not None else '-'}")
        c3.metric("NPK Médio", "N:22.5 | P:15.3 | K:32.5")
        t = dados.get("WEATHER_TEMP_C")
        c4.metric("Temperatura do Tempo", f"{t} °C" if t is not None else "-")

        df = pd.DataFrame({
            "Dia": list(range(1, 8)),
            "Umidade (%)": [62, 61, 60, 58, 59, 61, 62],
            "Temperatura (°C)": [26.5, 27, 27.5, 28, 28.5, 27, 26.5],
        })
        fig1 = px.line(df, x="Dia", y="Umidade (%)", title="Umidade ao longo do tempo")
        fig2 = px.line(df, x="Dia", y="Temperatura (°C)", title="Temperatura ao longo do tempo")
        st.plotly_chart(fig1, use_container_width=True)
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.info("Sem dados para a cidade selecionada.")

with tabs[1]:
    st.subheader("Comparativo: Com vs Sem Tecnologia")
    df = pd.DataFrame({
        "Indicador": ["Produção (ton/ha)", "Lucro (R$ mil)", "Economia de Insumos (%)"],
        "Com Tecnologia": [8.5, 120, 25],
        "Sem Tecnologia": [6.0, 80, 0],
    })
    df_melt = df.melt(id_vars="Indicador", var_name="Cenário", value_name="Valor")
    fig = px.bar(df_melt, x="Indicador", y="Valor", color="Cenário", barmode="group", text_auto=True,
                 color_discrete_map={"Com Tecnologia":"#2e7d32", "Sem Tecnologia":"#c62828"})
    st.plotly_chart(fig, use_container_width=True)

with tabs[2]:
    st.subheader("Indicadores Sustentáveis")
    df = pd.DataFrame({
        "Indicador": ["Economia de Água", "Redução de Fertilizantes", "Emissão de CO₂"],
        "Valor (%)": [30, 20, -15],
    })
    fig = px.bar(df, x="Indicador", y="Valor (%)", text_auto=True, color="Indicador",
                 color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(fig, use_container_width=True)

st.caption("Dica: menu ⋮ do Streamlit → Record a screencast para gravar o vídeo da demonstração.")
