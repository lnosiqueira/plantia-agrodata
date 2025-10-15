
<p align="center">
  <img src="assets/img/banner_plantia.png" width="100%" alt="PlantIA Agrodata - FIAP">
</p>

---

# 🌾 **PlantIA Agrodata - FIAP**
### _Sistema Inteligente de Gestão de Colheita de Cana-de-Açúcar_

📘 Projeto acadêmico desenvolvido na disciplina de **Python (Capítulos 3 a 6)**  
📍 Curso de **Inteligência Artificial - FIAP 2025**

---

## 🧭 Sumário <a id="sumario"></a>
- [👥 Integrantes do Grupo](#integrantes)
- [📘 Sobre o Projeto](#sobre)
- [🎯 Objetivo](#objetivo)
- [⚙️ Funcionalidades](#funcionalidades)
- [🗂️ Estrutura do Projeto](#estrutura)
- [▶️ Como Executar o Sistema](#execucao)
- [🧠 Integração com Banco de Dados Oracle (FIAP)](#oracle)
- [📊 Geração de Gráficos](#graficos)
- [🧩 Demonstração do Menu Principal](#menu)
- [👨‍💻 Autores e Créditos](#autores)
- [📜 Licença](#licenca)

---

## 👥 Integrantes do Grupo <a id="integrantes"></a>
| Nome | RM | LinkedIn |
|------|----|-----------|
| | [**Leno Siqueira**](https://linkedin.com/in/leno-siqueira-36789544) | **RM567893** |  |
| **Fred Vilagra** | **RM567187** | https://www.linkedin.com/in/federico-villagra-97378838a) |
| **Paulo Benfica** | **RM567648** | (https://www.linkedin.com/in/paulo-benfica-76057a7b) |
| **Mateus Lima** | **RM568518** | (https://www.linkedin.com/in/andr%C3%A9a-mendes-b8959238a) |
| **Maria Mendes** | **RM568518** | (https://www.linkedin.com/in/math-penteado-1b4807200/) |

---

## 📘 Sobre o Projeto <a id="sobre"></a>
O **PlantIA Agrodata** é um sistema desenvolvido em **Python** com foco no **agronegócio**, voltado ao **monitoramento e análise de dados da colheita de cana-de-açúcar**.  
O sistema integra análise de dados, automação de processos e conexão real com o banco de dados **Oracle Cloud (FIAP)**.

💡 Este projeto une conceitos de:
- Inteligência Artificial aplicada ao Agronegócio  
- Estruturas de Dados em Python  
- Persistência com arquivos JSON e Oracle  
- Visualização analítica com **Matplotlib**

---

## 🎯 Objetivo <a id="objetivo"></a>
Criar uma ferramenta simples e didática para:
- Monitorar colheitas de cana-de-açúcar  
- Calcular perdas e produtividade automaticamente  
- Armazenar dados em JSON e no Oracle Database  
- Gerar gráficos analíticos para suporte à decisão  

---

## ⚙️ Funcionalidades <a id="funcionalidades"></a>

| Nº | Funcionalidade | Descrição |
|----|----------------|-----------|
| 1️⃣ | **Cadastro de Colheita** | Inserção manual de dados de colheita |
| 2️⃣ | **Cálculo de Perdas** | Cálculo automático da perda (%) |
| 3️⃣ | **Resumo Analítico** | Exibe médias e totais de produtividade |
| 4️⃣ | **Persistência JSON** | Salva e lê dados localmente |
| 5️⃣ | **Conexão Oracle FIAP** | Envia dados do JSON para o banco Oracle |
| 6️⃣ | **Geração de Gráficos** | Gera e exporta gráficos em PNG |
| 7️⃣ | **Interface CLI** | Menu intuitivo via terminal |

---

## 🗂️ Estrutura do Projeto <a id="estrutura"></a>
```
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
├── data/
│   └── colheita.json
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

## ▶️ Como Executar o Sistema <a id="execucao"></a>

### Pré-requisitos:
- Python 3.11+  
- Oracle Database (ou conta Oracle FIAP)  
- Pacotes do `requirements.txt`

### Instalação:
```bash
pip install -r requirements.txt
```

### Execução:
```bash
python src/main.py
```

**Menu Principal:**
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

## 🧠 Integração com Banco de Dados Oracle (FIAP) <a id="oracle"></a>

O PlantIA integra-se ao banco **Oracle Cloud (FIAP)** para armazenar registros de colheitas.

### Teste de Conexão:
```bash
python src/test_oracle.py
```
✅ Resultado esperado:
```
✅ Conexão bem-sucedida com o Oracle (FIAP)!
🔹 Mensagem: PlantIA conectado à FIAP!
🔒 Conexão encerrada.
```

---

## 📊 Geração de Gráficos <a id="graficos"></a>

### Média de perda por campo:
`assets/img/media_perda_por_campo.png`

### Série temporal (exemplo: field_id = 101):
`assets/img/serie_perda_field_101.png`

💡 Os gráficos são salvos automaticamente em `assets/img/`.

---

## 🧩 Demonstração do Menu Principal <a id="menu"></a>
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

## 👨‍💻 Autores e Créditos <a id="autores"></a>
**Desenvolvido por:**  
👤 **Leno Siqueira** – `lnosiqueira@gmail.com`  
📘 **FIAP — Faculdade de Informática e Administração Paulista**  
📅 **Ano:** 2025  
📚 **Curso:** Inteligência Artificial  

---

## 📜 Licença <a id="licenca"></a>
Este projeto está licenciado sob a **Licença MIT** — uso livre para fins acadêmicos e de aprendizado.  
© 2025 — FIAP / PlantIA Agrodata

<p align="center">
  <img src="https://www.fiap.com.br/wp-content/themes/fiap2016/images/logo-fiap.svg" width="180">
</p>
