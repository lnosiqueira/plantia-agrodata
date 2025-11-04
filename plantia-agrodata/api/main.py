from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI(title="PlantIA Agrodata API - Fase 3")

@app.get("/health")
def health():
    return {"status": "ok", "service": "plantia-agrodata-api"}

class SensorRow(BaseModel):
    N: float | None = None
    P: float | None = None
    K: float | None = None
    temperature: float | None = None
    humidity: float | None = None
    ph: float | None = None
    rainfall: float | None = None

@app.get("/sensors/sample")
def sensors_sample():
    # Retorna 5 linhas do CSV de exemplo
    df = pd.read_csv("data/plantia_sensores_fase2_sample.csv")
    return {"rows": df.head(5).to_dict(orient="records")}
