from fastapi import FastAPI
from deps.db import check_db

app = FastAPI(title="PlantIA Agrodata API", version="1.0-fase3")

@app.get("/health/db")
def health_db():
    ok = check_db()
    return {"db": "up" if ok else "down"}
