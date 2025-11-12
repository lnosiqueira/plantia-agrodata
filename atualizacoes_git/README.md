<p align="center">
  <img src="assets/img/banner_plantia.png" width="100%" alt="PlantIA Agrodata - FIAP">
</p>

---

# 🌾 **PlantIA Agrodata - FIAP**
### _Sistema Inteligente de Gestão de Colheita de Cana-de-Açúcar_

📘 Projeto acadêmico desenvolvido na disciplina de **Python (Capítulos 3 a 6)**  
📍 Curso de **Inteligência Artificial - FIAP 2025**

> ⚠️ **Segurança**: Nunca commitar `.env` e `.streamlit/secrets.toml`. Credenciais são lidas de variáveis de ambiente ou de `st.secrets`.

---

## 🧭 Sumário
- [👥 Integrantes do Grupo](#integrantes)
- [🧑‍🏫 Professores](#professores)
- [📘 Sobre o Projeto](#sobre-o-projeto)
- [🎯 Objetivo](#objetivo)
- [⚙️ Funcionalidades](#funcionalidades)
- [🗂️ Estrutura do Projeto](#estrutura-projeto)
- [📁 Estrutura de Pastas (FIAP)](#estrutura-de-pastas-fiap)
- [▶️ Como Executar](#como-executar)
- [🧠 Integração Oracle (FIAP)](#integracao-oracle)
- [🌐 Diagnóstico (FastAPI + Streamlit)](#diagnostico)
- [🤖 IA de Predição (prototipo)](#ia)
- [📊 Gráficos](#graficos)
- [🗃 Histórico de Lançamentos](#historico)
- [👨‍💻 Autores](#autores)
- [🔗 Repositório](#repo)
- [📜 Licença](#licenca)

---

## 👥 Integrantes do Grupo S <a name="integrantes"></a>

| Nome | RM |
|------|----|
| **Leno Siqueira** | **RM567893** |
| **Fred Villagra** | **RM567187** |
| **Paulo Benfica** | **RM567648** |
| **Maria Mendes** | **RM568563** |
| **Mateus Lima**  | **RM568518** |

---

## 🧑‍🏫 Professores <a id="professores"></a>

**Tutor(a)**: Sabrina Otoni · **Coordenador(a)**: André Godoi

---

## 📘 Sobre o Projeto <a id="sobre-o-projeto"></a>

O **PlantIA Agrodata** integra Python + Oracle (FIAP) + FastAPI + Streamlit.
Inclui protótipo de IA (RandomForest) para estimativa de **tons_collected**.

---

## 🎯 Objetivo <a id="objetivo"></a>

- Monitorar colheitas
- Calcular perdas & produtividade
- Persistir dados (JSON e Oracle)
- Gerar análises & gráficos
- Exibir diagnósticos de conectividade
- Prototipar predição de produtividade (IA)

---

## ⚙️ Funcionalidades <a id="funcionalidades"></a>

1. CLI de colheita (src/)
2. API FastAPI `/health/db`
3. Dashboard Streamlit (diagnóstico + telemetria)
4. Integração Oracle (sem secrets no repositório)
5. Protótipo de IA com `scikit-learn`

---

## 🗂️ Estrutura do Projeto <a name="estrutura-projeto"></a>

```
plantia-agrodata/
├── app/
│   ├── deps/
│   │   └── db.py
│   ├── main.py
│   └── __init__.py
├── pages/
│   ├── 1_Diagnostico_DB.py
│   └── 2_Telemetria_Colheita.py
├── src/
│   ├── ai/
│   │   ├── colheita_predict.py
│   │   └── __init__.py
│   ├── main.py
│   ├── coleta_dados.py
│   ├── analise_dados.py
│   ├── graficos.py
│   ├── persistencia.py
│   └── persistencia_oracle.py
├── sql/
│   ├── 01_schema.sql
│   ├── 02_seed.sql
│   ├── 03_indexes.sql
│   ├── 04_views.sql
│   └── 05_examples.sql
├── data/colheita.json
├── assets/img/banner_plantia.png
├── .env.example
├── .streamlit/secrets.toml.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 📁 Estrutura de Pastas (FIAP) <a id="estrutura-de-pastas-fiap"></a>

- **app/** FastAPI e dependências
- **pages/** dashboards Streamlit
- **src/** código de negócio e IA
- **sql/** scripts Oracle
- **data/** dados locais
- **assets/** imagens
- **.streamlit/** segredos locais (não commitar)
- **.env** variáveis locais (não commitar)

---

## ▶️ Como Executar <a id="como-executar"></a>

### 1) Ambiente
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2) Configurar credenciais (1 das opções)
**Opção A — Variáveis de ambiente (recomendado local):**
```powershell
$env:ORACLE_USER="SEU_RM"
$env:ORACLE_PWD="SUA_SENHA"
$env:ORACLE_HOST="oracle.fiap.com.br"
$env:ORACLE_PORT="1521"
$env:ORACLE_SID="ORCL"
```

**Opção B — Streamlit secrets (local, não versionar):**
Crie `.streamlit/secrets.toml` com:
```toml
[oracle]
user = "SEU_RM"
pwd  = "SUA_SENHA"
host = "oracle.fiap.com.br"
port = 1521
sid  = "ORCL"
```

### 3) FastAPI (health)
```powershell
python -m uvicorn app.main:app --reload
# abrir http://127.0.0.1:8000/health/db
```

### 4) Streamlit
```powershell
python -m streamlit run pages/1_Diagnostico_DB.py
# ou
python -m streamlit run pages/2_Telemetria_Colheita.py
```

---

## 🧠 Integração Oracle (FIAP) <a id="integracao-oracle"></a>

Os scripts estão em `/sql`. A tabela de log é `PLANTIA_AGRO_LOG`.  
As views criadas: `V_HARVESTS_DAILY` e `V_HARVESTS_METRICS`.

---

## 🌐 Diagnóstico (FastAPI + Streamlit) <a id="diagnostico"></a>

- FastAPI `/health/db` usa `app/deps/db.py` para testar o DSN.
- Streamlit `1_Diagnostico_DB.py` exibe health & últimos logs.

---

## 🤖 IA de Predição (prototipo) <a id="ia"></a>

Arquivo `src/ai/colheita_predict.py` com RandomForest.  
Treinamento rápido pela página Streamlit de telemetria.

---

## 📊 Gráficos <a id="graficos"></a>

A página `2_Telemetria_Colheita.py` exibe métricas e gráficos (Altair).

---

## 🗃 Histórico <a id="historico"></a>

| Versão | Data | Descrição |
|-------:|:----:|-----------|
| **1.2.0** | 09/11/2025 | Limpeza geral, imports corrigidos, segredos fora do repo, páginas ajustadas |
| **1.1.0** | 06/11/2025 | Integração FastAPI + Streamlit + Oracle |
| **1.0.0** | 14/10/2025 | Entrega FIAP: JSON + Gráficos + Oracle |

---

## 👨‍💻 Autores <a id="autores"></a>

Leno Siqueira · Fred Villagra · Paulo Benfica · Maria Mendes · Mateus Lima

---

## 🔗 Repositório <a id="repo"></a>

https://github.com/lnosiqueira/plantia-agrodata

---

## 📜 Licença <a id="licenca"></a>

MIT — uso acadêmico/educacional.
