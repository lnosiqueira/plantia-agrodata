from graficos import plot_media_perda_por_campo, plot_serie_perda_por_campo
from coleta_dados import registrar_colheita
from analise_dados import resumo_por_campo, resumo_geral
from persistencia import salvar_json, ler_json
from typing import List, Dict
import os


# Caminho do JSON
DATA_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "colheita.json"
)


def carregar_memoria() -> List[Dict]:
    if os.path.exists(DATA_PATH):
        try:
            return ler_json(DATA_PATH)
        except Exception as e:
            print("Aviso: não foi possível ler colheita.json:", e)
    return []


def salvar_memoria(mem: List[Dict]) -> None:
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    try:
        salvar_json(DATA_PATH, mem)
        print("Dados salvos em:", DATA_PATH)
    except Exception as e:
        print("Erro ao salvar JSON:", e)


def menu():
    print("\n=== PlantIA Agrodata — Gestão de Colheita (FIAP) ===")
    print("1) Registrar colheita")
    print("2) Resumo por campo (field_id)")
    print("3) Resumo geral")
    print("4) Salvar dados em JSON")
    print("5) Gráficos (média por campo / série por campo)")
    print("0) Sair")


def main():
    memoria: List[Dict] = carregar_memoria()

    while True:
        menu()
        opc = input("Escolha: ").strip()

        if opc == "1":
            try:
                registrar_colheita(memoria)
            except Exception as e:
                print("Erro ao registrar:", e)

        elif opc == "2":
            try:
                fid = int(input("Informe o field_id: ").strip())
            except ValueError:
                print("ID inválido.")
                continue
            r = resumo_por_campo(memoria, fid)
            print("\nResumo por campo:", r, "\n")

        elif opc == "3":
            r = resumo_geral(memoria)
            print("\nResumo geral:", r, "\n")

        elif opc == "4":
            salvar_memoria(memoria)

        elif opc == "5":
            print("\n=== Gráficos ===")
            print("1) Média de perda por campo (barras)")
            print("2) Série temporal de perda por campo (linha)")
            sub = input("Escolha: ").strip()
            if sub == "1":
                plot_media_perda_por_campo(memoria)
            elif sub == "2":
                try:
                    fid = int(input("Informe o field_id: ").strip())
                except ValueError:
                    print("ID inválido.")
                    continue
                plot_serie_perda_por_campo(memoria, fid)
            else:
                print("Opção de gráfico inválida.")

        elif opc == "0":
            print("Saindo... Até logo!")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()


