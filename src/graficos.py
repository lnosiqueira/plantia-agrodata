# src/graficos.py
from typing import List, Dict
from collections import defaultdict
from datetime import datetime
import os
import matplotlib.pyplot as plt

def _valida_dados(registros: List[Dict]) -> bool:
    if not registros:
        print("⚠️ Não há registros na memória. Cadastre colheitas ou carregue o JSON.")
        return False
    return True

# ==========================
# VISUALIZAÇÃO NA TELA
# ==========================
def plot_media_perda_por_campo(registros: List[Dict]) -> None:
    if not _valida_dados(registros):
        return
    perdas_por_campo = defaultdict(list)
    for r in registros:
        try:
            perdas_por_campo[int(r["field_id"])].append(float(r["loss_percentage"]))
        except Exception:
            continue
    if not perdas_por_campo:
        print("⚠️ Não foi possível calcular as médias (dados insuficientes).")
        return
    campos = sorted(perdas_por_campo.keys())
    medias = [round(sum(perdas_por_campo[c]) / len(perdas_por_campo[c]), 2) for c in campos]

    plt.figure()
    plt.bar([str(c) for c in campos], medias)
    plt.title("Média de Perda (%) por Field")
    plt.xlabel("Field ID")
    plt.ylabel("Perda (%)")
    for i, v in enumerate(medias):
        plt.text(i, v, f"{v}%", ha="center", va="bottom")
    plt.tight_layout()
    plt.show()

def plot_serie_perda_por_campo(registros: List[Dict], field_id: int) -> None:
    if not _valida_dados(registros):
        return
    serie = []
    for r in registros:
        try:
            if int(r["field_id"]) == int(field_id):
                dt = datetime.strptime(str(r["harvest_date"]), "%Y-%m-%d")
                serie.append((dt, float(r["loss_percentage"])))
        except Exception:
            continue
    if not serie:
        print(f"⚠️ Não há registros para o field_id {field_id}.")
        return

    serie.sort(key=lambda x: x[0])
    datas = [d.strftime("%Y-%m-%d") for d, _ in serie]
    perdas = [p for _, p in serie]

    plt.figure()
    plt.plot(datas, perdas, marker="o")
    plt.title(f"Evolução da Perda (%) — Field {field_id}")
    plt.xlabel("Data")
    plt.ylabel("Perda (%)")
    for x, y in zip(datas, perdas):
        plt.text(x, y, f"{y}%", ha="center", va="bottom")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# ==========================
# SALVAR EM PNG
# ==========================
def save_media_perda_por_campo_png(registros: List[Dict], out_path: str = "docs/img/media_perda_por_campo.png") -> str:
    """Gera o gráfico de média de perda por campo e salva como PNG."""
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    if not _valida_dados(registros):
        return ""
    perdas_por_campo = defaultdict(list)
    for r in registros:
        try:
            perdas_por_campo[int(r["field_id"])].append(float(r["loss_percentage"]))
        except Exception:
            continue
    if not perdas_por_campo:
        print("⚠️ Não foi possível calcular as médias (dados insuficientes).")
        return ""
    campos = sorted(perdas_por_campo.keys())
    medias = [round(sum(perdas_por_campo[c]) / len(perdas_por_campo[c]), 2) for c in campos]

    plt.figure()
    plt.bar([str(c) for c in campos], medias)
    plt.title("Média de Perda (%) por Field")
    plt.xlabel("Field ID")
    plt.ylabel("Perda (%)")
    for i, v in enumerate(medias):
        plt.text(i, v, f"{v}%", ha="center", va="bottom")
    plt.tight_layout()
    plt.savefig(out_path, dpi=120, bbox_inches="tight")
    plt.close()
    print("✅ Gráfico salvo em:", out_path)
    return out_path

def save_serie_perda_por_campo_png(registros: List[Dict], field_id: int, out_path: str = None) -> str:
    """Gera a série temporal de perda de um field e salva como PNG."""
    if out_path is None:
        out_path = f"docs/img/serie_perda_field_{field_id}.png"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    if not _valida_dados(registros):
        return ""
    serie = []
    for r in registros:
        try:
            if int(r["field_id"]) == int(field_id):
                dt = datetime.strptime(str(r["harvest_date"]), "%Y-%m-%d")
                serie.append((dt, float(r["loss_percentage"])))
        except Exception:
            continue
    if not serie:
        print(f"⚠️ Não há registros para o field_id {field_id}.")
        return ""

    serie.sort(key=lambda x: x[0])
    datas = [d.strftime("%Y-%m-%d") for d, _ in serie]
    perdas = [p for _, p in serie]

    plt.figure()
    plt.plot(datas, perdas, marker="o")
    plt.title(f"Evolução da Perda (%) — Field {field_id}")
    plt.xlabel("Data")
    plt.ylabel("Perda (%)")
    for x, y in zip(datas, perdas):
        plt.text(x, y, f"{y}%", ha="center", va="bottom")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(out_path, dpi=120, bbox_inches="tight")
    plt.close()
    print("✅ Gráfico salvo em:", out_path)
    return out_path

