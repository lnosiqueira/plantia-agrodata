
# FIAP - Faculdade de Informática e Administração Paulista

![FIAP](assets/img/banner_plantia.png)

# PlantIA Agrodata — FIAP
## Grupo: *inserir nome do grupo*

## ‍ Integrantes:

- [Leno Siqueira](http://linkedin.com/in/leno-siqueira-36789544) — RM: *567893*
- [Fred Villagra](https://www.linkedin.com/in/federico-villagra-97378838a) — RM: *567187*
- [Paulo Benfica](https://www.linkedin.com/in/paulo-benfica-76057a7b) — RM: *567648*
- [Andréa Mendes](https://www.linkedin.com/in/SEU-LINK) — RM: *568563*
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

##  Como executar o código

### Pré-requisitos

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


Menu:

=== PlantIA Agrodata — Gestão de Colheita (FIAP) ===
1) Registrar colheita
2) Resumo por campo (field_id)
3) Resumo geral
4) Salvar dados em JSON
5) Gráficos (mostrar / salvar PNG)
6) Enviar JSON ao Oracle
0) Sair

Gráficos

Salvar PNG pelo menu → opção 5 (subopções 3 e 4)

Saída:

assets/img/media_perda_por_campo.png

assets/img/serie_perda_field_101.png

Abrir no Windows:

explorer "assets\img"

Integração com Oracle (FIAP)
Teste de conexão

Edite src/test_oracle.py com suas credenciais FIAP e execute:

python src/test_oracle.py


Saída esperada:

✅ Conexão bem-sucedida com o Oracle (FIAP)!
🔹 Mensagem: PlantIA conectado à FIAP!
🔒 Conexão encerrada.

Variáveis de ambiente (recomendado)
setx ORACLE_USER "SEU_USUARIO_FIAP"
setx ORACLE_PASSWORD "SUA_SENHA_FIAP"
setx ORACLE_DSN "oracle.fiap.com.br:1521/ORCL"

Criar tabela e enviar dados (menu)

A tabela é verificada/criada ao iniciar o app. Para enviar o JSON:

6) Enviar JSON ao Oracle


O sistema faz UPSERT (MERGE) baseado em (field_id, TRUNC(data_colheita)) (não duplica).

SQL útil (no SQL Developer)
SELECT id, field_id, metodo, produtividade, perda, TRUNC(data_colheita) AS dia
FROM colheita
ORDER BY id DESC FETCH FIRST 10 ROWS ONLY;

SELECT field_id, TRUNC(data_colheita) AS dia, COUNT(*) qtd
FROM colheita
GROUP BY field_id, TRUNC(data_colheita)
HAVING COUNT(*) > 1;

FAQ Oracle
Erro	Causa	Solução
ORA-01017	usuário/senha incorretos	revisar credenciais FIAP
ORA-12541	listener indisponível	checar DSN/VPN
ORA-00001	violação de UNIQUE	UPSERT já evita duplicar; revise chave/índice
Histórico de lançamentos

1.0.0 — 14/10/2025 — Entrega FIAP: JSON + Gráficos + Oracle (UPSERT)

0.5.0 — 10/2025 — Integração Oracle inicial, gráficos PNG

0.4.0 — 10/2025 — Menu CLI estável

0.3.0 — 10/2025 — Persistência JSON

0.2.0 — 10/2025 — Cálculos/Análises

0.1.0 — 10/2025 — Estrutura do projeto

Licença

Projeto licenciado sob MIT (ver arquivo LICENSE).
“MODELO GIT FIAP” por FIAP está licenciado sob CC BY 4.0. 
GitHub

---

# 3) Ajustar imagens no README e fazer push

Como agora as imagens vivem em `assets/img/`, o README acima já aponta para lá.  
Se você ainda vai gerar o banner com script:

```bat
python scripts\gera_banner.py
git add assets\img\banner_plantia.png
git commit -m "docs: adiciona banner FIAP no padrão do template"
git push


Depois, faça o commit geral da reorganização:

git add .
git commit -m "docs: adapta README ao template FIAP e realoca assets/document/scripts"
git push