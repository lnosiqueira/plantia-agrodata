from typing import Dict, List
from analise_dados import calcula_perda
from utils import normalizar_metodo

def ler_float(msg: str) -> float:
    while True:
        val = input(msg).replace(",", ".").strip()
        try:
            f = float(val)
            if f < 0:
                print("Valor não pode ser negativo.")
                continue
            return f
        except ValueError:
            print("Digite um número válido.")

def ler_int(msg: str) -> int:
    while True:
        val = input(msg).strip()
        try:
            i = int(val)
            if i < 0:
                print("Valor não pode ser negativo.")
                continue
            return i
        except ValueError:
            print("Digite um inteiro válido.")

def ler_str(msg: str) -> str:
    return input(msg).strip()

def registrar_colheita(mem_table: List[Dict]) -> None:
    print("\n=== Registrar Colheita ===")
    field_id = ler_int("ID do Talhão (field_id): ")
    data = ler_str("Data (YYYY-MM-DD): ")
    metodo_raw = ler_str("Método (manual/mecanica): ")
    metodo = normalizar_metodo(metodo_raw)
    tons_prev = ler_float("Toneladas previstas: ")
    tons_colh = ler_float("Toneladas colhidas: ")
    perda_pct = calcula_perda(tons_prev, tons_colh)
    notes = ler_str("Observações (opcional): ")

    registro = {
        "field_id": field_id,
        "harvest_date": data,
        "method": metodo,
        "tons_expected": tons_prev,
        "tons_collected": tons_colh,
        "loss_percentage": perda_pct,
        "notes": notes
    }
    mem_table.append(registro)
    print(f"Registro adicionado! Perda: {perda_pct}%\n")
