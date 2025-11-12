import plotly.graph_objects as go

def create_dashboard():
    print("Dashboard iniciado com gráficos gauge e donut.")
    # Exemplo de gráfico gauge
    fig_gauge = go.Figure(go.Indicator(mode="gauge+number", value=70, title={'text': 'Umidade'}))
    fig_gauge.write_image("assets/gauge.png")

    # Exemplo de gráfico donut
    fig_donut = go.Figure(go.Pie(labels=['Solo', 'Ar'], values=[60, 40], hole=.4))
    fig_donut.write_image("assets/donut.png")
