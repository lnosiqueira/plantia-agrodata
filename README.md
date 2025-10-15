<p align="center">
  <img src="assets/img/banner_plantia.png" width="100%" alt="PlantIA Agrodata - FIAP">
</p>

---

# 🌾 **PlantIA Agrodata - FIAP**
### _Sistema Inteligente de Gestão de Colheita de Cana-de-Açúcar_

📘 Projeto acadêmico desenvolvido na disciplina de **Python (Capítulos 3 a 6)**  
📍 Curso de **Inteligência Artificial - FIAP 2025**

---

## 🧭 **Sumário**
1. [Sobre o Projeto](#sobre-o-projeto)
2. [Objetivo](#objetivo)
3. [Funcionalidades](#funcionalidades)
4. [Estrutura do Projeto](#estrutura-do-projeto)
5. [Como Executar o Sistema](#como-executar-o-sistema)
6. [Integração com Banco de Dados Oracle (FIAP)](#integração-com-banco-de-dados-oracle-fiap)
7. [Geração de Gráficos](#geração-de-gráficos)
8. [Demonstração do Menu Principal](#demonstração-do-menu-principal)
9. [Autores e Créditos](#autores-e-créditos)
10. [Licença](#licença)

---

## 📘 **Sobre o Projeto**
O **PlantIA Agrodata** é um sistema desenvolvido em **Python** com foco no **agronegócio**, voltado ao **monitoramento e análise de dados da colheita de cana-de-açúcar**.  
O sistema integra análise de dados, automação de processos e conexão real com banco de dados **Oracle Cloud (FIAP)**.

💡 O projeto une conceitos de:
- Inteligência Artificial aplicada ao Agronegócio  
- Estrutura de dados em Python  
- Persistência e integração com banco de dados Oracle  
- Visualização analítica com **Matplotlib**

---

## 🎯 **Objetivo**
Criar uma ferramenta simples e didática para:
- Monitorar colheitas de cana-de-açúcar;
- Calcular perdas e produtividade automaticamente;
- Armazenar dados em **JSON** e no **Oracle Database**;
- Gerar **gráficos analíticos** para tomada de decisão no campo.

---

## ⚙️ **Funcionalidades**
| Nº | Funcionalidade | Descrição |
|----|----------------|------------|
| 1️⃣ | **Cadastro de Colheita** | Inserção manual de dados da colheita |
| 2️⃣ | **Cálculo de Perdas** | Cálculo automático da perda (%) por campo |
| 3️⃣ | **Resumo Analítico** | Exibe médias e totais de produtividade |
| 4️⃣ | **Persistência JSON** | Salva e lê dados localmente |
| 5️⃣ | **Conexão Oracle FIAP** | Envia dados do JSON para o banco Oracle |
| 6️⃣ | **Geração de Gráficos** | Gera e exporta gráficos em PNG |
| 7️⃣ | **Interface CLI** | Menu intuitivo via terminal |

---

## 🗂️ **Estrutura do Projeto**
```
plantia-agrodata/
│
├── src/
│   ├── main.py                # Menu principal e orquestração
│   ├── coleta_dados.py        # Registro e validação de entradas
│   ├── analise_dados.py       # Cálculos de perda e produtividade
│   ├── graficos.py            # Geração de gráficos (PNG)
│   ├── persistencia.py        # Manipulação JSON
│   └── persistencia_oracle.py # Integração com Oracle
│
├── data/
│   └── colheita.json          # Base local
│
├── assets/
│   └── img/
│       ├── banner_plantia.png
│       ├── media_perda_por_campo.png
│       └── serie_perda_field_101.png
│
└── README.md
```

---

## ▶️ **Como Executar o Sistema**

### 🔧 Pré-requisitos
- Python 3.11+
- Oracle Database (ou conta Oracle FIAP)
- Pacotes do `requirements.txt`

### 💻 Instalação
```bash
pip install -r requirements.txt
```

### ▶️ Execução
```bash
python src/main.py
```

📋 **Menu Principal:**
```
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

## 🧠 **Integração com Banco de Dados Oracle (FIAP)**
O PlantIA integra-se ao banco **Oracle Cloud (FIAP)** para armazenar registros de colheitas.

### 🧩 Teste de Conexão
```bash
python src/test_oracle.py
```
✅ Retorno esperado:
```
✅ Conexão bem-sucedida com o Oracle (FIAP)!
🔹 Mensagem: PlantIA conectado à FIAP!
🔒 Conexão encerrada.
```

### 🗃️ Inserção de Dados via Menu
Ao selecionar a opção **6 - Enviar JSON ao Oracle**, os registros são enviados automaticamente, utilizando **UPSERT** (sem duplicar dados).

---

## 📊 **Geração de Gráficos**

### 📈 Média de perda por campo
`assets/img/media_perda_por_campo.png`

### 📉 Série temporal por campo (ex: field_id = 101)
`assets/img/serie_perda_field_101.png`

💡 Gráficos são salvos automaticamente no diretório `assets/img/`.

---

## 🧩 **Demonstração do Menu Principal**
```
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

## 👨‍💻 **Autores e Créditos**
**Desenvolvido por:**  
👤 **Leno Siqueira** — `lnosiqueira@gmail.com`

**FIAP - Faculdade de Informática e Administração Paulista**  
**Curso:** Inteligência Artificial — **Ano:** 2025

---

## 📜 **Licença**
Este projeto está licenciado sob a **Licença MIT** — uso livre para fins acadêmicos e de aprendizado.  
© 2025 - FIAP / PlantIA Agrodata
