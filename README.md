<p align="center">
  <img src="assets/img/banner_plantia.png" width="100%" alt="PlantIA Agrodata - FIAP">
</p>

---

# 🌱 PlantIA Agrodata — Sistema Inteligente de Plantio e Monitoramento Agrícola
**Fase 3 – Etapas de uma Máquina Agrícola (FIAP / FarmTech Solutions)**

> **Visão:** Plataforma de IA e sensoriamento que **monitora, prevê e recomenda ações agronômicas** para a etapa de **plantio** — do dado ao campo, com inteligência.

📘 Projeto acadêmico desenvolvido na disciplina de **Python (Capítulos 3 a 6)**  
📍 Curso de **Inteligência Artificial – FIAP 2025**

---

## 📑 Sumário
- [Descrição Geral](#-descrição-geral)
- [🧭 Manifesto – PlantIA Agrodata](#-manifesto--plantia-agrodata)
- [🎯 Objetivo da Fase 3](#-objetivo-da-fase-3)
- [🏗 Arquitetura Técnica (Visão Geral)](#-arquitetura-técnica-visão-geral)
- [🗄️ Banco Oracle – Passo a Passo e Evidências](#️-banco-oracle--passo-a-passo-e-evidências)
- [🛰️ Integração IoT – ESP32/Wokwi → Oracle](#️-integração-iot--esp32wokwi--oracle)
- [📊 Programa “Ir Além” (Dashboard & ML)](#-programa-ir-além-dashboard--ml)
- [📂 Estrutura de Pastas](#-estrutura-de-pastas)
- [▶️ Como Executar (CLI/API)](#️-como-executar-cliapi)
- [✅ Conclusão](#-conclusão)
- [👨‍💻 Integrantes do Grupo S](#-integrantes-do-grupo-s)
- [👩‍🏫 Professores](#-professores)
- [🪪 Autores e Créditos](#-autores-e-créditos)
- [🗃 Histórico de Lançamentos](#-histórico-de-lançamentos)

---

## 🧠 Descrição Geral
O **PlantIA Agrodata** evoluiu para um **sistema inteligente de plantio e monitoramento agrícola**, integrando **sensores IoT (ESP32/Wokwi)**, **Oracle Database (FIAP)**, **dashboards** e **modelos preditivos** para otimizar **preparo, irrigação e cultivo** de forma sustentável e automatizada.

---

## 🧭 Manifesto – PlantIA Agrodata
**Propósito:** Transformar dados agrícolas em decisões inteligentes e sustentáveis.  
**Missão:** Unir sensores, dados e IA para monitorar, prever e otimizar o **plantio**.  
**Visão:** Ser referência nacional em IA agronômica, conectando o campo físico ao digital.  
**Diferenciais:** Multicultivo • IoT + IA + Oracle • Escalável em Cloud • Autoria real • Evolução contínua.

---

## 🎯 Objetivo da Fase 3
- Importar dados de sensores (Fase 2) para o **Oracle Database**;  
- Executar **consultas SQL** e gerar **evidências (prints)**;  
- Organizar o repositório (`document/docs/oracle_evidences.pdf`);  
- Preparar base para **Streamlit (Dashboard)** e **Scikit-learn (ML)**.

---

## 🏗 Arquitetura Técnica (Visão Geral)
```
Sensores/Simulação (ESP32 / Wokwi / CSV Fase 2)
        │
        ▼
Ingestão / API (Python + FastAPI/Requests)
        │
        ▼
Banco Relacional (Oracle FIAP)
        │
        ▼
Dashboard (Streamlit / AgroView)
        │
        ▼
Machine Learning (AgroPredict – Scikit-learn)```

---

## 🗄️ Banco Oracle – Passo a Passo e Evidências

**Conexão FIAP**
| Parâmetro | Valor |
|---|---|
| Host | `oracle.fiap.com.br` |
| Porta | `1521` |
| SID | `ORCL` |
| Usuário | `RMxxxxx` |
| Senha | `DDMMYY` |

**Consultas utilizadas como evidência:**

```sql
-- Amostra
SELECT * FROM SENSORS_DATA_V2 FETCH FIRST 10 ROWS ONLY;

-- Contagem
SELECT COUNT(*) AS TOTAL_REGISTROS FROM SENSORS_DATA_V2;

-- Médias consolidadas
SELECT
  ROUND(AVG(CASE WHEN UPPER(TRIM(TIPO_SENSOR))='UMIDADE SOLO' THEN LEITURA_VALOR END),2) AS UMIDADE_MEDIA,
  ROUND(AVG(CASE WHEN UPPER(TRIM(TIPO_SENSOR))='TEMPERATURA SOLO' THEN LEITURA_VALOR END),2) AS TEMPERATURA_MEDIA,
  ROUND(AVG(CASE WHEN UPPER(TRIM(TIPO_SENSOR))='PH SOLO' THEN LEITURA_VALOR END),2) AS PH_MEDIO
FROM SENSORS_DATA_V2;
```
---

📎 As capturas de tela das consultas e estrutura estão em document/docs/oracle_evidences.pdf.

---

## 🛰️ Integração IoT – ESP32/Wokwi → Oracle

**Protótipo Wokwi:**  
https://wokwi.com/projects/447381740224169985

**Fluxo de dados**
```
ESP32 (Wokwi) → Leituras (Temp/Umidade/Umidade Solo)
          │
          ▼
Script Python (requests + cx_Oracle)
          │
          ▼
Tabela Oracle: SENSORS_DATA_V2
```

**Exemplo de integração (pseudo):**

```python
import cx_Oracle, requests, time, json
dsn = cx_Oracle.makedsn("oracle.fiap.com.br", 1521, service_name="orcl")
conn = cx_Oracle.connect(user="RMxxxxx", password="DDMMYY", dsn=dsn)
cur = conn.cursor()

def inserir(row):
    cur.execute(
      '''INSERT INTO SENSORS_DATA_V2 (CAMPO_ID, TIPO_SENSOR, LEITURA_VALOR, UNIDADE, DATA_LEITURA)
         VALUES (:1,:2,:3,:4,SYSDATE)''',
      (row["id"], row["tipo"], row["valor"], row["unidade"])
    )
    conn.commit()
```
---

## 📊 Programa “Ir Além” (Dashboard & ML)

Dashboard (Streamlit): KPIs de Umidade | pH | Temperatura + filtros por período.

ML (Scikit-learn): preparação de modelos de recomendação de irrigação/plantio.

---

## 📂 Estrutura de Pastas

| Pasta / Arquivo | Descrição |

|---|---|
| **assets/** | Banners/prints (inclui Wokwi e Oracle) |
| **document/** | Relatórios e anexos (ex.: `docs/oracle_evidences.pdf`) |
| **src/** | Código-fonte (CLI/API, integração Oracle) |
| **scripts/** | Utilitários (backup, migração) |
| **config/** | Parâmetros e credenciais locais |
| **README.md** | Este arquivo |

---
## ▶️ Como Executar (CLI/API)

CLI
python src/main.py

API (FastAPI)
uvicorn src.api:app --reload
# depois abra: http://127.0.0.1:8000/docs

Menu (atualizado para Plantio/Monitoramento):

=== PlantIA Agrodata — Sistema Inteligente de Plantio (FIAP) ===
1) Registrar leitura de sensores
2) Resumo por campo (plantio)
3) Monitorar condições ambientais
4) Exportar dados em JSON
5) Enviar dados ao Oracle
0) Sair

---

## ✅ Conclusão

A Fase 3 consolidou a camada de dados (Oracle) e evidenciou a análise de sensores.
Com a integração IoT (ESP32/Wokwi) e a base pronta para Dashboard/ML, o PlantIA Agrodata avança de um protótipo de colheita para um sistema inteligente de plantio e monitoramento, demonstrando evolução técnica e escalabilidade.

---

## 👨‍💻 Integrantes do Grupo S

Nome	RM
Leno Siqueira	RM567893
Fred Villagra	RM567187
Paulo Benfica	RM567648
Maria Mendes	RM568563
Mateus Lima	    RM568518

---

## 🧑‍🏫 Professores

Tutor(a): Sabrina Otoni
Coordenador(a): André Godoi

---

## 🪪 Autores e Créditos

INTEGRANTES DO GRUPO S - FIAP • 2025 • Curso de Inteligência Artificial
Repositório: https://github.com/lnosiqueira/plantia-agrodata

---

## 🗃 Histórico de Lançamentos
| Versão | Data | Descrição |
|---|---|---|
| **2.0.0** | 12/11/2025 | Evolução para **Sistema Inteligente de Plantio** (ESP32/Wokwi + Oracle + evidências) |
| **1.0.0** | 14/10/2025 | Entrega FIAP: JSON + Gráficos + Oracle (UPSERT) |
