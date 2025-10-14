# src/main.py

import os
from typing import List, Dict

from coleta_dados import registrar_colheita
from analise_dados import resumo_por_campo, resumo_geral
from persistencia import salvar_json, ler_json
from graficos import (
    plot_media_perda_por_campo,
    plot_serie_perda_por_campo,
    save_media_perda_por_campo_png,
    save_serie_perda_por_campo_png,
)

# Oracle (opcional, mas tentamos habilitar)
ORACLE_OK = False
ORACLE_ERR = None
try:
    from persistencia_oracle import criar_tabela, inserir_em_lote
    ORACLE_OK = True
except Exception as _e:
    ORACLE_OK = False
    ORACLE_ERR = _e

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
    print("5) Gráficos (mostrar / salvar PNG)")
    print("6) Enviar JSON ao Oracle")
    print("0) Sair")

def main():
    # Sinal de vida
    print(">> Iniciando PlantIA...")

    memoria: List[Dict] = carregar_memoria()

    # Tenta garantir a tabela no Oracle (se o módulo existir)
    if ORACLE_OK:
        try:
            criar_tabela()
        except Exception as e:
            print("Aviso: Oracle não configurado agora (criar_tabela falhou):", e)
    else:
        if ORACLE_ERR:
            print("Oracle desabilitado (persistencia_oracle indisponível):", ORACLE_ERR)

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
            print("1) Média de perda por campo (barras) [mostrar]")
            print("2) Série temporal de perda por campo (linha) [mostrar]")
            print("3) Salvar PNG: Média de perda por campo")
            print("4) Salvar PNG: Série por field_id")
            sub = input("Escolha: ").strip()

            if sub == "1":
                plot_media_perda_por_campo(memoria)

            elif sub == "2":
                try:
                    fid = int(input("Informe o field_id: ").strip())
                except ValueError:
                    print("ID inválido.")
                else:
                    plot_serie_perda_por_campo(memoria, fid)

            elif sub == "3":
                path = save_media_perda_por_campo_png(memoria)
                if path:
                    print("PNG salvo em:", os.path.abspath(path))

            elif sub == "4":
                try:
                    fid = int(input("Informe o field_id: ").strip())
                except ValueError:
                    print("ID inválido.")
                else:
                    path = save_serie_perda_por_campo_png(memoria, fid)
                    if path:
                        print("PNG salvo em:", os.path.abspath(path))

            else:
                print("Opção de gráfico inválida.")

        elif opc == "6":
            try:
                data_path = DATA_PATH  # já calculado acima
                if not os.path.exists(data_path):
                    print("Arquivo JSON não encontrado em:", data_path)
                else:
                    registros = ler_json(data_path)
                    if not ORACLE_OK:
                        print("Oracle desabilitado. Verifique persistencia_oracle.py.")
                    else:
                        inserir_em_lote(registros)
            except Exception as e:
                print("❌ Falha ao enviar ao Oracle:", e)

        elif opc == "0":
            print("Saindo... Até logo!")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()



