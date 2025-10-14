
🚀 README FINAL — copie e cole no seu README.md
<p align="center">
  <img src="docs/img/banner_plantia.png" alt="PlantIA Agrodata" width="820" />
</p>

<h1 align="center"><b>🌾 PlantIA Agrodata — FIAP</b></h1>
<p align="center">
  Sistema Inteligente de Gestão e Análise da Colheita de Cana-de-Açúcar
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-ativo-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/python-3.11+-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/oracle-integrado-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/licença-MIT-black?style=for-the-badge" />
</p>

---

## 📑 SUMÁRIO

- [Sobre o Projeto](#sobre-o-projeto)
- [Objetivo](#objetivo)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Instalação](#instalação)
- [Como Executar](#como-executar)
- [Gráficos](#gráficos)
- [JSON de Exemplo](#json-de-exemplo)
- [Integração com Oracle (FIAP)](#integração-com-oracle-fiap)
- [FAQ Oracle](#faq-oracle)
- [Requisitos (Capítulos 3 a 6)](#requisitos-capítulos-3-a-6)
- [Entrega FIAP](#entrega-fiap)
- [Autor](#autor)
- [Licença](#licença)

---

## 🧩 **SOBRE O PROJETO**

O **PlantIA Agrodata** é um sistema em **Python** voltado para **análise e gestão de colheita de cana-de-açúcar**.

Ele permite o **registro, processamento e visualização** dos dados de colheita, com integração direta ao **banco de dados Oracle (FIAP)**.

---

## 🎯 **OBJETIVO**

- Registrar colheitas (manual ou mecânica)  
- Calcular **perdas (%)** e gerar **resumos**  
- Armazenar dados em **JSON local** e **Oracle Cloud FIAP**  
- Gerar **gráficos automáticos** de produtividade e perdas

---

## 🗂️ **ESTRUTURA DO REPOSITÓRIO**

plantia-agrodata/
│
├── src/
│ ├── main.py → Menu principal CLI
│ ├── coleta_dados.py → Entrada e validação dos dados
│ ├── analise_dados.py → Cálculos e resumos
│ ├── graficos.py → Geração de gráficos e PNGs
│ ├── persistencia.py → Leitura e gravação de JSON
│ ├── persistencia_oracle.py → Integração Oracle (tabela, UPSERT, listar)
│ └── test_oracle.py → Teste isolado de conexão
│
├── data/
│ └── colheita.json → Base de dados local
│
├── docs/
│ ├── img/
│ │ ├── banner_plantia.png
│ │ ├── media_perda_por_campo.png
│ │ └── serie_perda_field_101.png
│ └── relatorio.md
│
├── requirements.txt
├── LICENSE
└── README.md

---

## ⚙️ **INSTALAÇÃO**

### 📦 Dependências
```bash
pip install -r requirements.txt
💡 Ambiente virtual (recomendado)
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
________________________________________
▶️ Como Executar
python src/main.py
Menu Principal
=== PlantIA Agrodata — Gestão de Colheita (FIAP) ===
1) Registrar colheita
2) Resumo por campo (field_id)
3) Resumo geral
4) Salvar dados em JSON
5) Gráficos (mostrar/salvar PNG)
6) Enviar JSON ao Oracle
0) Sair
________________________________________
📊 GRÁFICOS
Média de Perda por Campo
<p align="center"> <img src="docs/img/media_perda_por_campo.png" width="640" /> </p> 
Série Temporal de Perdas
<p align="center"> <img src="docs/img/serie_perda_field_101.png" width="640" /> </p> 
Os gráficos podem ser exibidos ou salvos automaticamente via menu opção 5.
________________________________________
💾 JSON de Exemplo
Arquivo: data/colheita.json
[
  {"field_id": 101, "method": "mecanica", "area_ha": 12.5, "loss_percentage": 3.2, "date": "2025-10-14"},
  {"field_id": 102, "method": "manual", "area_ha": 10.0, "loss_percentage": 1.8, "date": "2025-10-14"},
  {"field_id": 103, "method": "mecanica", "area_ha": 15.0, "loss_percentage": 2.7}
]
Se o campo "date" não for informado, o sistema usa automaticamente a data atual (TRUNC(SYSDATE)).
________________________________________
☁️ INTEGRAÇÃO COM ORACLE (FIAP)
1️⃣ Teste de Conexão
Edite src/test_oracle.py com seu usuário e senha FIAP, depois execute:
python src/test_oracle.py
Saída esperada:
✅ Conexão bem-sucedida com o Oracle (FIAP)!
🔹 Mensagem: PlantIA conectado à FIAP!
🔒 Conexão encerrada.
________________________________________
2️⃣ Configuração com Variáveis de Ambiente
setx ORACLE_USER "SEU_USUARIO_FIAP"
setx ORACLE_PASSWORD "SUA_SENHA_FIAP"
setx ORACLE_DSN "oracle.fiap.com.br:1521/ORCL"
Após configurar, feche e reabra o terminal para aplicar.
________________________________________
3️⃣ Envio de Dados (UPSERT)
No menu principal, escolha a opção 6:
✅ 3 registros upsert (sem duplicar).
O sistema utiliza um MERGE Oracle, evitando duplicações com base em (field_id, TRUNC(data_colheita)).
________________________________________
🧠 Exemplo de MERGE (UPSERT)
MERGE INTO colheita c
USING (
  SELECT :field_id AS field_id,
         :tipo_colheita AS tipo_colheita,
         :area_ha AS area_ha,
         :perda AS perda_percent,
         NVL(TO_DATE(:data_str, 'YYYY-MM-DD'), TRUNC(SYSDATE)) AS dt
  FROM dual
) src
ON (c.field_id = src.field_id AND TRUNC(c.data_colheita) = src.dt)
WHEN MATCHED THEN
  UPDATE SET
    c.tipo_colheita = src.tipo_colheita,
    c.area_ha = src.area_ha,
    c.perda_percent = src.perda_percent
WHEN NOT MATCHED THEN
  INSERT (field_id, tipo_colheita, area_ha, perda_percent, data_colheita)
  VALUES (src.field_id, src.tipo_colheita, src.area_ha, src.perda_percent, src.dt);
________________________________________
🧩 FAQ ORACLE
Erro	Causa	Solução
ORA-01017	Usuário/senha incorretos	Confirme credenciais FIAP
ORA-12541	Listener não encontrado	Verifique DSN e VPN
ORA-00001	Registro duplicado	O UPSERT resolve automaticamente
________________________________________
📚 REQUISITOS (Capítulos 3 a 6)
Capítulo	Implementação
3️⃣ Subalgoritmos	coleta_dados.py, analise_dados.py, graficos.py, persistencia.py
4️⃣ Estruturas de Dados	Listas e dicionários
5️⃣ Arquivos	JSON (persistencia.py)
6️⃣ Banco de Dados	Oracle (persistencia_oracle.py)
________________________________________
🚀 ENTREGA FIAP
Para criar a versão final da entrega:
git tag -a v1.0-entrega-fiap -m "Entrega PlantIA: JSON + Gráficos + Oracle UPSERT"
git push origin v1.0-entrega-fiap
________________________________________
👤 AUTORES
Leno Siqueira
📧 lnosiqueira@gmail.com
💼 FIAP — Inteligência Artificial
________________________________________
📜 LICENÇA
Distribuído sob a licença MIT.
