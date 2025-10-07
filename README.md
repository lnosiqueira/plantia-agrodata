# 🌾 PlantIA Agrodata - FIAP

**Sistema de Gestão Inteligente de Colheita de Cana-de-Açúcar**  
Projeto acadêmico desenvolvido na disciplina de **Python (Capítulos 3 a 6)** do curso de **Inteligência Artificial - FIAP**.

---

## 📘 Sobre o Projeto
O **PlantIA Agrodata** é um sistema em **Python** voltado ao **monitoramento e análise de dados da colheita de cana-de-açúcar**.  
Ele simula tecnologias **Agrotech** no campo, automatizando registros, cálculos de produtividade/perdas e a geração de gráficos.

---

## 🧠 Objetivo
Demonstrar:
- **Funções, procedimentos e estruturas de dados** em Python;
- **Manipulação de arquivos JSON** e esqueleto de conexão com **Oracle**;
- Aplicação de **tecnologia e inovação no agronegócio** para reduzir perdas e otimizar colheita.

---

## ⚙️ Funcionalidades
- ✅ Cadastro de dados de colheita (manual ou mecânica)  
- ✅ Cálculo automático de **perdas (%)**  
- ✅ Armazenamento/leitura em **JSON**  
- ✅ **Resumos** por campo e geral  
- ✅ **Gráficos** (Matplotlib): médias por campo e série temporal  
- ✅ Estrutura pronta para integração com **Oracle Database**

---

## 🗂️ Estrutura do Projeto
```bash
plantia-agrodata/
│
├── src/                      # Códigos-fonte
│   ├── main.py               # Programa principal e menu interativo
│   ├── coleta_dados.py       # Entrada e validação dos dados
│   ├── analise_dados.py      # Cálculos e resumos
│   ├── graficos.py           # Gráficos (mostrar/salvar PNG)
│   ├── persistencia.py       # Leitura e gravação JSON
│   └── utils.py              # Funções auxiliares
│
├── data/
│   └── colheita.json         # Dados simulados da colheita
│
├── docs/
│   ├── relatorio.md          # Documentação do projeto
│   └── img/
│       ├── media_perda_por_campo.png
│       └── serie_perda_field_101.png
│
├── requirements.txt          # Dependências do projeto
├── LICENSE                   # Licença MIT
└── README.md                 # Este arquivo
