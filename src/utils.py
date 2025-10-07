from typing import Literal

MetodoColheita = Literal["manual", "mecanica"]

def normalizar_metodo(txt: str) -> MetodoColheita:
    t = (txt or "").strip().lower()
    if t in ("manual", "m"):
        return "manual"  # type: ignore
    if t in ("mecanica", "mec", "mecânica"):
        return "mecanica"  # type: ignore
    raise ValueError("method deve ser 'manual' ou 'mecanica'")
