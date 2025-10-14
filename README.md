
# FIAP - Faculdade de Informática e Administração Paulista

![FIAP](assets/img/banner_plantia.png)

# PlantIA Agrodata — FIAP
## Grupo: *inserir nome do grupo*

## ‍ Integrantes:

- [Leno Siqueira](http://linkedin.com/in/leno-siqueira-36789544) — RM: *567893*
- [Fred Villagra](https://www.linkedin.com/in/federico-villagra-97378838a) — RM: *567187*
- [Paulo Benfica](https://www.linkedin.com/in/paulo-benfica-76057a7b) — RM: *567648*
- [Andréa Mendes](https://www.linkedin.com/in/andr%C3%A9a-mendes-b8959238a) — RM: *568563*
- [Mateus Lima](https://www.linkedin.com/in/SEU-LINK) — RM: *568518*

## ‍ Professores:

### Tutor(a)

- [Sabrina Otoni]

### Coordenador(a)

- [André Godoi]

---

##  Descrição

**PlantIA Agrodata** é um sistema em **Python** para **gestão e análise da colheita de cana-de-açúcar**, aplicando os conteúdos dos **Capítulos 3 a 6** da disciplina (FIAP):
- **Subalgoritmos** (funções/procedimentos)
- **Estruturas de dados** (listas/tuplas/dicionários; “tabela de memória”)
- **Arquivos** (leitura/gravação em **JSON**)
- **Banco de Dados** (**Oracle**), com **UPSERT (MERGE)** para evitar duplicações

Funcionalidades:
- Cadastro de colheitas (manual/mecânica) com validação
- Resumos por campo e gerais
- **Gráficos** (média de perda por campo, série temporal por field_id) — salvamento **PNG**
- Integração com **Oracle (FIAP)**: criação automática da tabela, *upsert* e listagem

---

##  Estrutura de pastas

- **.github/**: configs específicas do GitHub Actions/Issues
- **assets/**: arquivos não estruturados (imagens do README, gráficos)
  - **assets/img/**
- **config/**: parâmetros/ajustes do projeto (ex.: `.env.example`, se desejar)
- **document/**: documentos da entrega (relatórios, PDFs)
  - **document/other/**: anexos/apoio
- **scripts/**: scripts auxiliares (ex.: gerar banner, gerar gráficos em lote)
- **src/**: **código-fonte**
  - `main.py` — menu CLI principal  
  - `coleta_dados.py` — entrada/validação  
  - `analise_dados.py` — cálculos/resumos  
  - `graficos.py` — exibição/salvamento de gráficos  
  - `persistencia.py` — JSON (ler/gravar)  
  - `persistencia_oracle.py` — Oracle (criar tabela, **UPSERT**, listar)  
  - `test_oracle.py` — teste de conexão FIAP  
- **README.md**: guia do projeto

> Estrutura alinhada ao template FIAP e às instruções de organização (pasta `assets` para imagens; `document` para documentos). :contentReference[oaicite:2]{index=2}

 ---

## 🚀 Como executar o código

### ✅ Pré-requisitos

- **Python 3.11+**
- Bibliotecas:
  ```txt
  pandas==2.1.0
  matplotlib==3.10.6
  numpy==1.25.2
  oracledb==2.4.1

  ---
  
  Instalação
pip install -r requirements.txt


Recomendado no Windows:

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

Executar o sistema

python src/main.py


Menu Principal (CLI)

=== PlantIA Agrodata — Gestão de Colheita (FIAP) ===
1) Registrar colheita
2) Resumo por campo (field_id)
3) Resumo geral
4) Salvar dados em JSON
5) Gráficos (mostrar / salvar PNG)
6) Enviar JSON ao Oracle
0) Sair

Descrição das Opções

Opção	Função
1️⃣ Registrar colheita	Adiciona um novo registro de colheita (manual ou mecânica).
2️⃣ Resumo por campo	Mostra estatísticas de um campo específico (field_id).
3️⃣ Resumo geral	Exibe dados consolidados de todos os campos.
4️⃣ Salvar JSON	Armazena as colheitas no arquivo data/colheita.json.
5️⃣ Gráficos	Visualiza ou salva PNGs de produtividade/perdas.
6️⃣ Enviar JSON ao Oracle	Integra os dados locais com o banco Oracle FIAP.
0️⃣ Sair	Finaliza o programa.

---

Gráficos (mostrar / salvar PNG)
1. Rode:

python src/main.py

2. Escolha5) Gráficos.
3. Subopções:

1) Média de perda por campo (barras) [mostrar]
2) Série temporal de perda por campo (linha) [mostrar]
3) Salvar PNG: Média de perda por campo
4) Salvar PNG: Série por field_id

4. Saídas Esperadas

assets/img/media_perda_por_campo.png
assets/img/serie_perda_field_101.png

Dica (Windows);

explorer "assets\img"

 ---
 
 ☁️ Integração com Oracle (FIAP)
1) Teste de conexão

Edite src/test_oracle.py com suas credenciais FIAP e execute:

python src/test_oracle.py

Saída esperada:

✅ Conexão bem-sucedida com o Oracle (FIAP)!
🔹 Mensagem: PlantIA conectado à FIAP!
🔒 Conexão encerrada.

2) Variáveis de ambiente (recomendado)

setx ORACLE_USER "SEU_USUARIO_FIAP"
setx ORACLE_PASSWORD "SUA_SENHA_FIAP"
setx ORACLE_DSN "oracle.fiap.com.br:1521/ORCL"

Feche e reabra o terminal após definir.

3) Criar tabela e enviar dados (menu)

A tabela é verificada/criada ao iniciar o app. Para enviar o JSON:

6) Enviar JSON ao Oracle


O sistema faz UPSERT (MERGE) baseado na chave (field_id, TRUNC(data_colheita)), evitando duplicação.

4) SQL útil (SQL Developer)
-- Dados mais recentes
SELECT id, field_id, metodo, produtividade, perda, TRUNC(data_colheita) AS dia
FROM colheita
ORDER BY id DESC
FETCH FIRST 10 ROWS ONLY;

-- Verificar duplicidade por dia/campo
SELECT field_id, TRUNC(data_colheita) AS dia, COUNT(*) qtd
FROM colheita
GROUP BY field_id, TRUNC(data_colheita)
HAVING COUNT(*) > 1;

5) FAQ Oracle

Erro	Causa	Solução
ORA-01017	Usuário/senha incorretos	Corrija usuário/senha FIAP
ORA-12541	Listener indisponível	Verifique DSN/VPN
ORA-00001	Violação de UNIQUE	O UPSERT já previne duplicações

 ---
 
 Banner e Imagens

Banner do projeto: assets/img/banner_plantia.png

Gráficos:

assets/img/media_perda_por_campo.png

assets/img/serie_perda_field_101.png

Se ainda não existirem, gere o banner:

python scripts/gera_banner.py

 ---
 
 Entrega FIAP (Tag)

Crie a tag final da entrega:

git tag -a v1.0-entrega-fiap -m "Entrega PlantIA Agrodata (JSON + Gráficos + Oracle UPSERT)"
git push origin v1.0-entrega-fiap


> Esse bloco já corrige **quebras de linha, blocos de código, ancoragem e o menu** com “0) Sair”. Também aponta as imagens para `assets/img/`.

---

## 4) Commit & push

Depois de colar e salvar o README:

```bat
git add README.md assets\img\banner_plantia.png
git commit -m "docs: corrige README (menu 0) Sair, blocos e paths assets/img) + banner"
git push


 ---

Licença

Projeto licenciado sob MIT (ver arquivo LICENSE).
“MODELO GIT FIAP” por FIAP está licenciado sob CC BY 4.0. 
GitHub

---