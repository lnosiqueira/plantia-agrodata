# PlantIA Agrodata – Fase 3 (Simplificado)
**Objetivo:** importar dados no **Oracle**, validar com **SQL**, e visualizar no **Streamlit** (com fallback para CSV).  
> Mantém seu layout do Grupo S. Edite apenas as seções marcadas com ⚠️ EDITAR.

---

## 1) O que vem neste pacote
- `database/create_table.sql` → cria tabela no Oracle
- `database/queries.sql` → consultas de validação
- `dashboard/app.py` → dashboard Streamlit (Oracle → fallback CSV)
- `api/main.py` → API FastAPI base (`/health` e exemplo `/sensors/sample`)
- `requirements.txt` → dependências
- `.env.example` → modelo de credenciais (copie para `.env`)
- `data/plantia_sensores_fase2_sample.csv` → CSV de exemplo (pra testes locais)
- `docs/oracle_evidences_template.md` → roteiro de prints para gerar PDF

---

## 2) Passo a passo (iniciante)
### 2.1 Preparar ambiente
**Windows:**
```bat
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Edite o arquivo `.env` e preencha:
```
ORACLE_HOST=oracle.fiap.com.br
ORACLE_PORT=1521
ORACLE_SID=ORCL
ORACLE_USER=RMxxxxx
ORACLE_PASSWORD=DDMMYY
ORACLE_TABLE=PLANTIA_AGRODATA_SENSOR_DATA
```

### 2.2 Criar tabela no Oracle (SQL Developer)
1. Conectar no Oracle (host/porta/SID/usuário/senha acima).
2. **Abrir** `database/create_table.sql` e **executar**.
3. Importar o CSV da Fase 2 (ou use o de exemplo em `data/plantia_sensores_fase2_sample.csv`).  
   Botão direito em **Tabelas (Filtrado)** → **Importar Dados** → selecione o CSV → **Finalizar**.

### 2.3 Validar consultas
No SQL Developer, execute o conteúdo de `database/queries.sql`.  
Faça **prints** e depois gere um PDF com esses prints.

### 2.4 Rodar o Dashboard (Streamlit)
```bash
streamlit run dashboard/app.py
```
- Se conseguir conectar no Oracle, ele lê do banco.
- Se a conexão falhar, ele usa automaticamente o CSV de exemplo para demonstrar o painel.

### 2.5 Rodar a API (opcional)
```bash
uvicorn api.main:app --reload
# Abra http://127.0.0.1:8000/docs
```

### 2.6 Subir para o GitHub
```bash
git add .
git commit -m "Fase 3: Oracle + Dashboard (pacote simplificado)"
git push origin main
```

---

## 3) ⚠️ EDITAR: Seções do seu README principal
- **Integrantes do Grupo S (NOME + RM)** — manter exatamente como está no seu repositório.
- **Professores** — mesma lista do seu repositório.
- **Autores & Crédititos** — manter igual; só acrescente “Fase 3 concluída”.

---

## 4) Troubleshooting rápido
- Erro de login no Oracle → confirme `RMxxxxx` e senha `DDMMYY`.  
- `oracledb` sem client → este projeto usa **modo Thin** (não requer Instant Client).  
- Porta 8501 ocupada → `streamlit run dashboard/app.py --server.port 8502`.

Boa prática: versionar o **PDF de evidências** em `docs/` após concluir.
