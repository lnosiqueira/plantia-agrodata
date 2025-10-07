from typing import Dict, List

def calcula_perda(tons_previstas: float, tons_colhidas: float) -> float:
    if tons_previstas <= 0:
        raise ValueError("tons_previstas deve ser > 0")
    perda = (tons_previstas - tons_colhidas) / tons_previstas * 100.0
    return round(perda, 2)

def resumo_por_campo(registros: List[Dict], field_id: int) -> Dict:
    entradas = [r for r in registros if r.get("field_id") == field_id]
    if not entradas:
        return {"field_id": field_id, "count": 0, "avg_loss_pct": 0.0, "total_collected": 0.0}
    media_perda = sum(e["loss_percentage"] for e in entradas) / len(entradas)
    total_colhido = sum(e["tons_collected"] for e in entradas)
    return {
        "field_id": field_id,
        "count": len(entradas),
        "avg_loss_pct": round(media_perda, 2),
        "total_collected": round(total_colhido, 2)
    }

def resumo_geral(registros: List[Dict]) -> Dict:
    if not registros:
        return {"count": 0, "avg_loss_pct": 0.0, "total_collected": 0.0}
    media_perda = sum(e["loss_percentage"] for e in registros) / len(registros)
    total_colhido = sum(e["tons_collected"] for e in registros)
    return {"count": len(registros), "avg_loss_pct": round(media_perda, 2), "total_collected": round(total_colhido, 2)}
