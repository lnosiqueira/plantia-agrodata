import requests

def get_weather(city="São Paulo"):
    print(f"Buscando previsão do tempo para {city}...")
    # Aqui você integraria com a API OpenWeather
    return {"city": city, "temp": 25, "condition": "Ensolarado"}
