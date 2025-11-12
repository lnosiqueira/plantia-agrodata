import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import os

# Configuração da página
st.set_page_config(page_title="PlantIA Agrodata - Dashboard", layout="wide")
st.markdown("<h1 style='text-align: center; color: #2E8B57;'>🌱 PlantIA Agrodata - Dashboard Interativo</h1>", unsafe_allow_html=True)

# Sidebar: seleção de cidade e botão de atualização
st.sidebar.header("🌍 Localização Agrícola")
cidades = {
    "São Paulo": "Sao Paulo",
    "Mato Grosso (Cuiabá)": "Cuiaba",
    "Paraná (Curitiba)": "Curitiba",
    "Goiás (Goiânia)": "Goiania",
    "Minas Gerais (Belo Horizonte)": "Belo Horizonte"
}
cidade_selecionada = st.sidebar.selectbox("Selecione a cidade", list(cidades.keys()))
atualizar = st.sidebar.button("🔄 Atualizar clima")

# Função para buscar clima via OpenWeather
def get_clima(cidade, api_key):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"
        response = requests.get(url)
        if response.status_code == 200:
            dados = response.json()
            temperatura = dados['main']['temp']
            umidade = dados['main']['humidity']
            condicao = dados['weather'][0]['description']
            return temperatura, umidade, condicao
    except Exception as e:
        print(f"Erro ao buscar clima: {e}")
    return None, None, None

# API Key e clima atual
API_KEY = "d2c194b9addf80b6aefbffeb0e409ef4"
cidade_api = cidades[cidade_selecionada]
temp_real, umid_real, cond_real = get_clima(cidade_api, API_KEY) if atualizar else (None, None, None)

# Tabs para organizar
tab1, tab2, tab3 = st.tabs(["📈 Monitoramento", "💰 Impacto Econômico", "🌍 Sustentabilidade"])

# ================= TAB 1: MONITORAMENTO =================
with tab1:
    # Carregar dados do JSON ou usar simulados
    try:
        df = pd.read_json("data/colheita.json")
        colunas_esperadas = ["Data", "Umidade", "pH", "Nitrogênio", "Fósforo", "Potássio", "Temperatura"]
        if not all(col in df.columns for col in colunas_esperadas):
            raise ValueError("Formato inválido, usando dados simulados.")
    except:
        df = pd.DataFrame({
            "Data": pd.date_range(start="2025-11-01", periods=10, freq="D"),
            "Umidade": [60, 62, 58, 65, 63, 61, 59, 64, 66, 62],
            "pH": [6.5, 6.4, 6.6, 6.5, 6.7, 6.4, 6.5, 6.6, 6.5, 6.4],
            "Nitrogênio": [20, 22, 21, 23, 24, 22, 21, 23, 25, 24],
            "Fósforo": [15, 14, 16, 15, 17, 16, 15, 14, 16, 15],
            "Potássio": [30, 32, 31, 33, 34, 32, 31, 33, 35, 34],
            "Temperatura": [25, 26, 24, 27, 28, 26, 25, 27, 29, 28]
        })
        if not os.path.exists("data"):
            os.makedirs("data")
        df.to_json("data/colheita.json", orient="records")

    # KPIs principais com cards estilizados
    st.markdown("## 📊 Indicadores Agronômicos")
    kpi_style = """
    <style>
    .card {
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 18px;
        color: #333;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    </style>
    """
    st.markdown(kpi_style, unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"<div class='card'>💧<br>Umidade Média<br><b>{df['Umidade'].mean():.1f}%</b></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='card'>⚗️<br>pH Médio<br><b>{df['pH'].mean():.2f}</b></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='card'>🧪<br>NPK Médio<br><b>N:{df['Nitrogênio'].mean():.1f} | P:{df['Fósforo'].mean():.1f} | K:{df['Potássio'].mean():.1f}</b></div>", unsafe_allow_html=True)
    with col4:
        if temp_real is not None:
            st.markdown(f"<div class='card'>🌡️<br>Clima Atual<br><b>{temp_real:.1f}°C | {umid_real}% | {cond_real.capitalize()}</b></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='card'>🌡️<br>Temperatura Média<br><b>{df['Temperatura'].mean():.1f}°C</b></div>", unsafe_allow_html=True)

    # Filtro por período
    st.markdown("---")
    dias = st.slider("🔍 Filtrar últimos dias", 1, len(df), 5)
    df_filtrado = df.tail(dias)

    # Gráficos lado a lado
    fig_umidade = px.line(df_filtrado, x="Data", y="Umidade", title="Umidade ao longo do tempo", markers=True, color_discrete_sequence=["#1f77b4"])
    fig_temp = px.line(df_filtrado, x="Data", y="Temperatura", title="Temperatura ao longo do tempo", markers=True, color_discrete_sequence=["#d62728"])
    fig_umidade.update_layout(height=350, template="plotly_white")
    fig_temp.update_layout(height=350, template="plotly_white")

    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.plotly_chart(fig_umidade, width="stretch")
    with col_g2:
        st.plotly_chart(fig_temp, width="stretch")

    st.markdown("### 📋 Dados filtrados")
    st.dataframe(df_filtrado, use_container_width=True)

# ================= TAB 2: IMPACTO ECONÔMICO =================
with tab2:
    st.markdown("## 💰 Comparativo: Com vs Sem Tecnologia")
    impacto_data = pd.DataFrame({
        "Cenário": ["Com Tecnologia", "Sem Tecnologia"],
        "Produção (ton/ha)": [8.5, 6.0],
        "Lucro (R$ mil)": [120, 80],
        "Economia de Insumos (%)": [25, 0]
    })

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='card'>🌾<br>Produção<br><b>{impacto_data['Produção (ton/ha)'][0]} vs {impacto_data['Produção (ton/ha)'][1]}</b></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='card'>💰<br>Lucro<br><b>R$ {impacto_data['Lucro (R$ mil)'][0]}k vs R$ {impacto_data['Lucro (R$ mil)'][1]}k</b></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='card'>📉<br>Economia de Insumos<br><b>{impacto_data['Economia de Insumos (%)'][0]}%</b></div>", unsafe_allow_html=True)

    impacto_long = impacto_data.melt(id_vars="Cenário", var_name="Indicador", value_name="Valor")
    fig_impacto = px.bar(
        impacto_long,
        x="Indicador",
        y="Valor",
        color="Cenário",
        barmode="group",
        title="Impacto Econômico da Tecnologia",
        text="Valor",
        color_discrete_map={"Com Tecnologia": "#2ca02c", "Sem Tecnologia": "#d62728"}
    )
    fig_impacto.update_traces(texttemplate='%{text}', textposition='inside')
    fig_impacto.update_layout(height=400, template="plotly_white")
    st.plotly_chart(fig_impacto, width="stretch")

# ================= TAB 3: SUSTENTABILIDADE =================
with tab3:
    st.markdown("## 🌍 Indicadores Sustentáveis")
    sustentabilidade = pd.DataFrame({
        "Indicador": ["Economia de Água", "Redução de Fertilizantes", "Emissão de CO₂"],
        "Valor (%)": [30, 20, -15]
    })
    fig_sust = px.bar(
        sustentabilidade,
        x="Indicador",
        y="Valor (%)",
        title="Indicadores Sustentáveis",
        text="Valor (%)",
        color="Indicador",
        color_discrete_sequence=["#1f77b4", "#2ca02c", "#d62728"]
    )
    fig_sust.update_traces(texttemplate='%{text}%', textposition='outside')
    fig_sust.update_layout(height=400, template="plotly_white")
    st.plotly_chart(fig_sust, width="stretch")