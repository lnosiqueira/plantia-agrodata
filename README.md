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
├── docs/
│   └── relatorio.md          # Documentação do projeto
│
├── requirements.txt          # Dependências do projeto
├── LICENSE                   # Licença MIT
└── README.md                 # Este arquivo

| Tecnologia       | Função                      |
| ---------------- | --------------------------- |
| **Python 3.12+** | Lógica e processamento      |
| **JSON**         | Armazenamento local         |
| **cx_Oracle**    | Conexão com banco Oracle    |
| **Pandas**       | Manipulação de dados        |
| **Matplotlib**   | Geração de gráficos         |
| **GitHub**       | Versionamento e colaboração |

git clone https://github.com/lnosiqueira/plantia-agrodata.git
cd "plantia-agrodata"

pip install -r requirements.txt

python src/main.py

=== PlantIA Agrodata — Gestão de Colheita (FIAP) ===
1) Registrar colheita
2) Resumo por campo (field_id)
3) Resumo geral
4) Salvar dados em JSON
5) Gráficos (média por campo / série por campo)
0) Sair

Exemplo de saída de gráfico:

📈 Média de perda (%) por campo

📊 Série temporal de perda por campo

👨‍💻 Autor

Desenvolvido por:
Leno Siqueira

📧 lnosiqueira@gmail.com

💡 Projeto acadêmico — FIAP - Inteligência Artificial
🌱 Marca: PlantIA Agrodata

📜 Licença

Este projeto está licenciado sob a Licença MIT
 — uso livre para fins acadêmicos e de aprendizado.
