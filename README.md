
<p align="center">
  <img src="assets/img/banner_plantia.png" alt="Banner PlantIA Agrodata — FIAP" width="100%">
</p>

# PlantIA Agrodata

# FIAP - Faculdade de Informática e Administração Paulista


##  👥 Grupo
- **Nome do Grupo** _GRUPO S_

## ‍👤 Integrantes

- [Leno Siqueira](http://linkedin.com/in/leno-siqueira-36789544) — RM: *567893*
- [Fred Villagra](https://www.linkedin.com/in/federico-villagra-97378838a) — RM: *567187*
- [Paulo Benfica](https://www.linkedin.com/in/paulo-benfica-76057a7b) — RM: *567648*
- [Andréa Mendes](https://www.linkedin.com/in/andr%C3%A9a-mendes-b8959238a) — RM: *568563*
- [Mateus Lima](https://www.linkedin.com/in/SEU-LINK) — RM: *568518*

## 👩‍🏫 Professores

- **Tutor(a):** _Sabrina Otoni_
- **Coordenador(a):** _André Godoi_

---

## 📑 Sumário
- [Sobre o Projeto](#sobre-o-projeto)
- [Objetivo](#objetivo)
- [Estrutura de Pastas (template FIAP)](#estrutura-de-pastas-template-fiap)
- [Requisitos (Capítulos 3 a 6)](#requisitos-capítulos-3-a-6)
- [Instalação](#instalação)
- [Como Executar (CLI)](#como-executar-cli)
- [Gráficos (PNG)](#gráficos-png)
- [Integração com Oracle (FIAP)](#integração-com-oracle-fiap)
  - [Teste de Conexão](#1-teste-de-conexão)
  - [Variáveis de Ambiente](#2-variáveis-de-ambiente)
  - [Criação de Tabela & UPSERT](#3-criação-de-tabela--upsert)
  - [Envio do JSON ao Oracle](#4-envio-do-json-ao-oracle)
  - [SQL Útil](#5-sql-útil)
  - [FAQ Oracle](#6-faq-oracle)
- [JSON de Exemplo](#json-de-exemplo)
- [Entrega FIAP (Tag/Release)](#entrega-fiap-tagrelease)
- [Licença](#licença)

---

## Sobre o Projeto
O **PlantIA Agrodata** é um sistema em **Python** para **gestão e análise da colheita de cana-de-açúcar**.  
Atende aos requisitos acadêmicos da FIAP (Cap. 3 a 6): **funções/procedimentos**, **estruturas de dados**, **manipulação de arquivos (JSON)** e **conexão com banco de dados (Oracle)**.

**Funcionalidades:**
- Cadastro de colheitas (manual/mecânica) com validações
- Resumo por campo e resumo geral
- **Gráficos** (média de perda por campo; série temporal por field_id), com **salvamento em PNG**
- Integração com **Oracle (FIAP)**, incluindo **UPSERT (MERGE)** para evitar duplicações

---

## Objetivo
Demonstrar, de forma didática, como **organizar, analisar e persistir** dados do agronegócio usando Python:
- **reduzindo perdas**,  
- **aumentando a produtividade**,  
- **armazenando localmente (JSON)** e **no Oracle (FIAP)**.

---

## Estrutura de Pastas (template FIAP)
plantia-agrodata/
├── assets/
│ └── img/
│ ├── banner_plantia.png
│ ├── media_perda_por_campo.png
│ └── serie_perda_field_101.png
├── config/
├── document/
│ └── other/
├── scripts/
│ └── gera_banner.py
├── src/
│ ├── main.py
│ ├── coleta_dados.py
│ ├── analise_dados.py
│ ├── graficos.py
│ ├── persistencia.py
│ ├── persistencia_oracle.py
│ └── test_oracle.py
├── data/
│ └── colheita.json
├── LICENSE
├── requirements.txt
└── README.md

yaml
Copiar código

---

## Requisitos (Capítulos 3 a 6)
| Capítulo | Implementação |
|---|---|
| **3. Subalgoritmos** | Funções/procedimentos em `coleta_dados.py`, `analise_dados.py`, `graficos.py`, `persistencia.py` |
| **4. Estruturas de Dados** | Listas & dicionários; “tabela de memória” no `main.py` |
| **5. Arquivos** | Leitura/Gravação em **JSON** (`persistencia.py`) |
| **6. Banco de Dados** | **Oracle** (`persistencia_oracle.py`) com **UPSERT (MERGE)** |

---

## Instalação
> Recomendado usar ambiente virtual

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
requirements.txt:

ini
Copiar código
pandas==2.1.0
matplotlib==3.10.6
numpy==1.25.2
oracledb==2.4.1
Como Executar (CLI)
bash
Copiar código
python src/main.py
Menu:

java
Copiar código
=== PlantIA Agrodata — Gestão de Colheita (FIAP) ===
1) Registrar colheita
2) Resumo por campo (field_id)
3) Resumo geral
4) Salvar dados em JSON
5) Gráficos (mostrar / salvar PNG)
6) Enviar JSON ao Oracle
0) Sair
Gráficos (PNG)
Rode python src/main.py

Vá em 5) Gráficos

Subopções:

java
Copiar código
1) Média de perda por campo (mostrar)
2) Série temporal de perda por campo (mostrar)
3) Salvar PNG: Média de perda por campo
4) Salvar PNG: Série por field_id
Saídas esperadas:

assets/img/media_perda_por_campo.png

assets/img/serie_perda_field_101.png

Abrir no Windows:
explorer "assets\img"

Integração com Oracle (FIAP)
1) Teste de Conexão
Edite src/test_oracle.py com seu usuário e senha FIAP e execute:

bash
Copiar código
python src/test_oracle.py
Saída esperada:

java
Copiar código
✅ Conexão bem-sucedida com o Oracle (FIAP)!
🔹 Mensagem: PlantIA conectado à FIAP!
🔒 Conexão encerrada.
2) Variáveis de Ambiente
bat
Copiar código
setx ORACLE_USER "SEU_USUARIO_FIAP"
setx ORACLE_PASSWORD "SUA_SENHA_FIAP"
setx ORACLE_DSN "oracle.fiap.com.br:1521/ORCL"
Feche e reabra o terminal após definir.

3) Criação de Tabela & UPSERT
A tabela é criada/validada automaticamente ao iniciar o app (criar_tabela()).

Modelo lógico:

sql
Copiar código
CREATE TABLE colheita (
  id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  field_id NUMBER NOT NULL,
  metodo VARCHAR2(50),
  produtividade NUMBER(10,2),
  perda NUMBER(10,2),
  data_colheita DATE DEFAULT SYSDATE
);

CREATE UNIQUE INDEX ux_colheita_field_date
ON colheita (field_id, TRUNC(data_colheita));
UPSERT (MERGE) usado no envio:

sql
Copiar código
MERGE INTO colheita c
USING (
  SELECT :field_id AS field_id,
         :metodo AS metodo,
         :produtividade AS produtividade,
         :perda AS perda,
         NVL(TO_DATE(:data_str, 'YYYY-MM-DD'), TRUNC(SYSDATE)) AS dt
  FROM dual
) src
ON (c.field_id = src.field_id AND TRUNC(c.data_colheita) = src.dt)
WHEN MATCHED THEN
  UPDATE SET c.metodo = src.metodo,
             c.produtividade = src.produtividade,
             c.perda = src.perda
WHEN NOT MATCHED THEN
  INSERT (field_id, metodo, produtividade, perda, data_colheita)
  VALUES (src.field_id, src.metodo, src.produtividade, src.perda, src.dt);
4) Envio do JSON ao Oracle
Na aplicação (menu):

javascript
Copiar código
6) Enviar JSON ao Oracle
Saída típica:

java
Copiar código
✅ 3 registros upsert (sem duplicar).
5) SQL Útil
sql
Copiar código
-- Últimos registros
SELECT id, field_id, metodo, produtividade, perda, TRUNC(data_colheita) AS dia
FROM colheita
ORDER BY id DESC
FETCH FIRST 10 ROWS ONLY;

-- Verificar duplicação por dia/campo
SELECT field_id, TRUNC(data_colheita) AS dia, COUNT(*) qtd
FROM colheita
GROUP BY field_id, TRUNC(data_colheita)
HAVING COUNT(*) > 1;
6) FAQ Oracle
Erro	Causa	Solução
ORA-01017	Usuário/senha incorretos	Corrigir credenciais FIAP
ORA-12541	Listener indisponível	Conferir DSN/VPN
ORA-00001	UNIQUE violado	UPSERT evita duplicação; revisar chave

JSON de Exemplo
Arquivo: data/colheita.json

json
Copiar código
[
  {"field_id": 101, "method": "mecanica", "area_ha": 12.5, "loss_percentage": 3.2, "date": "2025-10-14"},
  {"field_id": 102, "method": "manual",   "area_ha": 10.0, "loss_percentage": 1.8, "date": "2025-10-14"},
  {"field_id": 103, "method": "mecanica", "area_ha": 15.0, "loss_percentage": 2.7}
]
Se date estiver vazio, o sistema utiliza TRUNC(SYSDATE).

Entrega FIAP (Tag/Release)
Crie uma tag para a entrega final:

bash
Copiar código
git tag -a v1.0-entrega-fiap -m "Entrega PlantIA Agrodata (JSON + Gráficos + Oracle UPSERT)"
git push origin v1.0-entrega-fiap
Licença
Projeto: MIT (ver LICENSE)

Template FIAP: CC BY 4.0

yaml
Copiar código
