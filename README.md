<p align="center">
  <img src="assets/img/banner_plantia.png" width="100%" alt="PlantIA Agrodata - FIAP">
</p>

---

# 🌾 **PlantIA Agrodata - FIAP**
### _Sistema Inteligente de Gestão de Colheita de Cana-de-Açúcar_

📘 Projeto acadêmico desenvolvido na disciplina de **Python (Capítulos 3 a 6)**  
📍 Curso de **Inteligência Artificial - FIAP 2025**

---

## 🧭 Sumário
- [👥 Integrantes do Grupo](#integrantes)
- [🧑‍🏫 Professores](#professores)
- [📘 Sobre o Projeto](#sobre-o-projeto)
- [🎯 Objetivo](#objetivo)
- [⚙️ Funcionalidades](#funcionalidades)
- [🗂️ Estrutura do Projeto](#estrutura-projeto)
- [📁 Estrutura de Pastas (FIAP)](#estrutura-de-pastas-fiap)
- [▶️ Como Executar o Sistema](#como-executar)
- [🧠 Integração com Banco de Dados Oracle (FIAP)](#integracao-com-banco-de-dados-oracle-fiap)
- [🌐 Diagnóstico Oracle e Streamlit (Fase 3)](#diagnostico-oracle-e-streamlit-fiap)
- [📊 Geração de Gráficos](#geração-de-gráficos)
- [🧩 Demonstração do Menu Principal](#demonstração-do-menu-principal)
- [🗃 Histórico de Lançamentos](#histórico-de-lançamentos)
- [👨‍💻 Autores e Créditos](#autores-e-créditos)
- [🔗 Repositório e Evidência de Versionamento](#repositorio-e-evidencia-de-versionamento)
- [📜 Licença](#licenca)

---

## 👥 Integrantes do Grupo S <a name="integrantes"></a>

| Nome | RM |
|------|----|
| [**Leno Siqueira**](https://www.linkedin.com/in/leno-siqueira-36789544) | **RM567893** |
| [**Fred Villagra**](https://www.linkedin.com/in/federico-villagra-97378838a) | **RM567187** |
| [**Paulo Benfica**](https://www.linkedin.com/in/paulo-benfica-76057a7b) | **RM567648** |
| [**Maria Mendes**](https://www.linkedin.com/in/andr%C3%A9a-mendes-b8959238a) | **RM568563** |
| [**Mateus Lima**](https://www.linkedin.com/in/math-penteado-1b4807200) | **RM568518** |

---

## 🧑‍🏫 Professores <a id="professores"></a>

**Tutor(a)**  
- [**Sabrina Otoni**](https://www.linkedin.com/in/sabrina-otoni-22525519b)

**Coordenador(a)**  
- [**André Godoi**](https://www.linkedin.com/company/inova-fusca)

---

## 📘 Sobre o Projeto <a id="sobre-o-projeto"></a>

O **PlantIA Agrodata** é um sistema desenvolvido em **Python** com foco no **agronegócio**, voltado ao **monitoramento e análise de dados da colheita de cana-de-açúcar**.  

O sistema integra análise de dados, automação de processos e conexão real com o banco de dados **Oracle Cloud (FIAP)**.

💡 Este projeto une conceitos de:
- Inteligência Artificial aplicada ao Agronegócio  
- Estruturas de Dados em Python  
- Persistência com arquivos JSON e Oracle  
- Visualização analítica com **Matplotlib**  
- Interface interativa com **FastAPI e Streamlit**

---

## 🎯 Objetivo <a id="objetivo"></a>

Criar uma ferramenta inteligente e didática para:
- Monitorar colheitas de cana-de-açúcar  
- Calcular perdas e produtividade automaticamente  
- Armazenar dados em JSON e no Oracle Database  
- Gerar gráficos analíticos para suporte à decisão  
- Exibir diagnósticos de conectividade via API e interface Streamlit  

---

## ⚙️ Funcionalidades <a id="funcionalidades"></a>

| Nº | Funcionalidade | Descrição |
|----|----------------|-----------|
| 1️⃣ | **Cadastro de Colheita** | Inserção manual de dados de colheita |
| 2️⃣ | **Cálculo de Perdas** | Cálculo automático da perda (%) |
| 3️⃣ | **Resumo Analítico** | Exibe médias e totais de produtividade |
| 4️⃣ | **Persistência JSON** | Salva e lê dados localmente |
| 5️⃣ | **Conexão Oracle FIAP** | Envia dados do JSON para o banco Oracle |
| 6️⃣ | **Diagnóstico Oracle via Streamlit** | Verifica a conectividade com o Oracle e exibe logs em tempo real |
| 7️⃣ | **Interface CLI e Web** | Menu interativo via terminal e dashboard via navegador |
| 8️⃣ | **Geração de Gráficos** | Exibe e exporta gráficos analíticos em PNG |

---

## 🗂️ Estrutura do Projeto <a name="estrutura-projeto"></a>

```text
plantia-agrodata/
│
├── src/
│   ├── main.py
│   ├── coleta_dados.py
│   ├── analise_dados.py
│   ├── graficos.py
│   ├── persistencia.py
│   └── persistencia_oracle.py
│
├── app/
│   ├── deps/
│   │   └── db.py
│   ├── main.py
│   └── __init__.py
│
├── pages/
│   └── 1_Diagnostico_DB.py
│
├── data/
│   └── colheita.json
│
├── assets/
│   └── img/
│       ├── banner_plantia.png
│       ├── media_perda_por_campo.png
│       └── serie_perda_field_101.png
│
├── evidencias/
│   └── 03-diagnostico/
│       ├── img/
│       │   └── streamlit_conexao_oracle.png
│       └── README_EVIDENCIAS.md
│
└── README.md
```

---

## 📁 Estrutura de Pastas <a id="estrutura-de-pastas-fiap"></a>

| Pasta / Arquivo | Descrição |
|------------------|-----------|
| **src/** | Código-fonte base do sistema CLI |
| **app/** | Estrutura FastAPI e dependências |
| **pages/** | Dashboards Streamlit |
| **assets/** | Imagens e gráficos gerados |
| **data/** | Arquivos de dados (JSON) |
| **evidencias/** | Prints e relatórios da execução real |
| **requirements.txt** | Pacotes necessários para execução |
| **README.md** | Guia completo do projeto |

---

## ▶️ Como Executar o Sistema <a id="como-executar"></a>

### Instalação de dependências
```bash
pip install -r requirements.txt
```

### Execução da aplicação CLI
```bash
python src/main.py
```

### Execução da API FastAPI
```bash
set ORACLE_USER=rm567893
set ORACLE_PWD=Fiap#2025
python -m uvicorn app.main:app --reload
```

### Execução da interface Streamlit
```bash
set ORACLE_USER=rm567893
set ORACLE_PWD=Fiap#2025
python -m streamlit run pages/1_Diagnostico_DB.py
```

Acesse: **http://localhost:8501**

---

## 🧠 Integração com Banco de Dados Oracle (FIAP) <a id="integracao-com-banco-de-dados-oracle-fiap"></a>

Teste rápido via script:
```bash
python test_oracle_conn.py
```

---

## 🌐 Diagnóstico Oracle e Streamlit (Fase 3) <a id="diagnostico-oracle-e-streamlit-fiap"></a>

O módulo de diagnóstico monitora em tempo real a conexão com o Oracle Cloud FIAP usando **FastAPI + Streamlit + oracledb**, exibindo logs diretamente da tabela **PLANTIA_AGRO_LOG**.

**Estrutura técnica**
- `app/deps/db.py` → verificação do Oracle  
- `app/main.py` (FastAPI) → endpoint `/health/db`  
- `pages/1_Diagnostico_DB.py` (Streamlit) → interface visual  

**Tela de diagnóstico**  
Imagem em: `evidencias/03-diagnostico/img/streamlit_conexao_oracle.png`

**Resultado**
- Conectado ao Oracle com sucesso  
- Hora do servidor Oracle exibida  
- Logs de acesso registrados no banco  
- Dashboard em `http://localhost:8501`

---

## 📊 Geração de Gráficos <a id="geração-de-gráficos"></a>

- Média de perda por campo: `assets/img/media_perda_por_campo.png`  
- Série temporal (ex.: `field_id = 101`): `assets/img/serie_perda_field_101.png`  

💡 Os gráficos são salvos automaticamente em `assets/img/`.

---

## 🧩 Demonstração do Menu Principal <a id="demonstração-do-menu-principal"></a>

```text
=== PlantIA Agrodata — Gestão de Colheita (FIAP) ===
1) Registrar colheita
2) Resumo por campo (field_id)
3) Resumo geral
4) Salvar dados em JSON
5) Gráficos (mostrar/salvar PNG)
6) Enviar JSON ao Oracle
0) Sair
```

---

## 🗃 Histórico de Lançamentos <a id="histórico-de-lançamentos"></a>

| Versão | Data | Descrição |
|-------:|:----:|-----------|
| **1.1.0** | 06/11/2025 | Integração com Oracle via FastAPI e Streamlit |
| **1.0.0** | 14/10/2025 | Entrega final FIAP: JSON + Gráficos + Oracle (UPSERT) |
| **0.4.0** | 12/10/2025 | Persistência Oracle/JSON e testes |
| **0.3.0** | 10/10/2025 | Menu principal e cálculo de perdas |
| **0.2.0** | 08/10/2025 | Estrutura de pastas, coleta e validações |
| **0.1.0** | 06/10/2025 | Kickoff do projeto e setup inicial |

---

## 👨‍💻 Autores e Créditos <a id="autores-e-créditos"></a>

**Desenvolvido por:**

- **Leno Siqueira** – lnosiqueira@gmail.com  
- **Fred Villagra** – federicoenriquevillagra@gmail.com  
- **Paulo Benfica** – paulo.benfica@outlook.com  
- **Maria Mendes** – mdea.mendes@gmail.com  
- **Mateus Lima** – mateusstockcar@gmail.com

📘 **FIAP — Faculdade de Informática e Administração Paulista**  
📅 **Ano:** 2025  
📚 **Curso:** Inteligência Artificial

---

## 🔗 Repositório e Evidência de Versionamento <a id="repositorio-e-evidencia-de-versionamento"></a>

**GitHub:** https://github.com/lnosiqueira/plantia-agrodata

O repositório contém:
- Histórico completo de commits e versões;  
- Estrutura modular (src, app, assets, pages, evidencias);  
- Documentos FIAP (README, guias e prints técnicos);  
- Scripts originais do PlantIA Agrodata (Grupo S).

---

## 📜 Licença <a id="licenca"></a>

Este projeto está licenciado sob a **Licença MIT** — uso livre para fins acadêmicos e de aprendizado.  
© 2025 — FIAP / PlantIA Agrodata
