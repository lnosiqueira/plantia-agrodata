# 🌾 PlantIA Agrodata - FIAP

**Sistema de Gestão Inteligente de Colheita de Cana-de-Açúcar**  
Projeto acadêmico desenvolvido na disciplina de **Python (Capítulos 3 a 6)** do curso de **Inteligência Artificial - FIAP**.  

---

## 📘 Sobre o Projeto

O **PlantIA Agrodata** é um sistema desenvolvido em **Python** com foco no **agronegócio**, voltado para o **monitoramento e análise de dados da colheita de cana-de-açúcar**.  
A aplicação simula o uso de tecnologias **Agrotech** no campo, automatizando registros, cálculos de produtividade e perdas, e geração de gráficos de desempenho agrícola.

---

## 🧠 Objetivo

Fornecer uma ferramenta simples e didática que demonstre:
- O uso de **funções, procedimentos e estruturas de dados** em Python;
- Manipulação de **arquivos JSON** e conexão simulada com banco de dados **Oracle**;
- Aplicação de **tecnologia e inovação no agronegócio**, reduzindo perdas e otimizando o processo de colheita.

---

## ⚙️ Funcionalidades

✅ Cadastro de dados de colheita (manual ou mecânica)  
✅ Cálculo automático de perdas (%) por hectare  
✅ Armazenamento e leitura de dados em **JSON**  
✅ Exibição de **resumos por campo e geral**  
✅ Visualização de **gráficos de produtividade e perdas** com **Matplotlib**  
✅ Estrutura pronta para integração com **Oracle Database**

---

## 🗂️ Estrutura do Projeto

```bash
plantia-agrodata/
│
├── src/                      # Códigos-fonte
│   ├── main.py               # Programa principal e menu interativo
│   ├── coleta_dados.py       # Entrada e validação dos dados
│   ├── analise_dados.py      # Cálculos e resumos
│   ├── graficos.py           # Gráficos de perdas e médias
│   ├── persistencia.py       # Leitura e gravação JSON
│   └── utils.py              # Funções auxiliares
│
├── data/
│   └── colheita.json         # Dados simulados da colheita
│
└── docs/
└── relatorio.pdf # Documentação do projeto


---

## 🧩 Tecnologias Utilizadas

| Tecnologia | Função |
|-------------|--------|
| Python 3.12+ | Lógica e processamento de dados |
| JSON | Armazenamento de dados |
| Oracle Database | Persistência relacional |
| Pandas | Manipulação de dados |
| Matplotlib | Visualização gráfica |
| GitHub | Versionamento e colaboração |

---

## 👤 Autor

**Desenvolvido por [Leno Siqueira](https://github.com/Inosiqueira)**  
💡 Projeto acadêmico FIAP — Curso de Inteligência Artificial  
🌱 Marca do projeto: **PlantIA**

---

## 📜 Licença

Este projeto está sob a **licença MIT**, permitindo o uso acadêmico e livre, desde que os créditos sejam mantidos.
