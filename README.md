🌾 PlantIA Agrodata — FIAP

Sistema de Gestão Inteligente de Colheita de Cana-de-Açúcar
Projeto acadêmico — Python (Cap. 3 a 6) — Curso de Inteligência Artificial (FIAP)

📘 Sobre o Projeto

O PlantIA Agrodata é um sistema em Python para monitoramento e análise de dados da colheita de cana-de-açúcar.
Foco em Agrotech: registro de colheita, cálculo de perdas, visualização de gráficos e persistência em JSON e Oracle (com UPSERT para evitar duplicação).

Conteúdos cobrados (Cap. 3–6):

Subalgoritmos (funções e procedimentos)

Estruturas de dados (lista, tupla, dicionário, “tabela de memória”)

Manipulação de arquivos (texto/JSON)

Conexão com Banco de Dados (Oracle)

🧠 Objetivo

Fornecer uma ferramenta didática que:

Cadastre dados da colheita (manual/mecânica), com validações;

Calcule perdas (%) e gere resumos por campo/geral;

Persista dados em JSON e Oracle (FIAP);

Gere gráficos de médias e séries temporais.

🗂️ Estrutura do Repositório
plantia-agrodata/
│
├── src/                      # Código-fonte
│   ├── main.py               # Menu CLI principal
│   ├── coleta_dados.py       # Entrada e validação de dados
│   ├── analise_dados.py      # Cálculos e resumos
│   ├── graficos.py           # Gráficos (mostrar e salvar PNG)
│   ├── persistencia.py       # JSON (ler/gravar)
│   ├── persistencia_oracle.py# Oracle (criar tabela, UPSERT, listar)
│   └── test_oracle.py        # Teste isolado de conexão Oracle
│
├── data/
│   └── colheita.json         # Dataset de exemplo (editável)
│
├── docs/
│   ├── img/
│   │   ├── media_perda_por_campo.png     # Exemplo (gerado no menu)
│   │   └── serie_perda_field_XXX.png     # Exemplo (gerado no menu)
│   └── relatorio.md          # (opcional) relatório do projeto
│
├── requirements.txt
├── LICENSE
└── README.md

⚙️ Instalação

Pré-requisitos:

Python 3.11+

(Windows) Prompt de Comando / PowerShell

(Opcional) SQL Developer / SQL*Plus (para ver o Oracle)

Instale as dependências:

pip install -r requirements.txt

▶️ Como Executar

Menu do sistema

python src/main.py


Você verá:

=== PlantIA Agrodata — Gestão de Colheita (FIAP) ===
1) Registrar colheita
2) Resumo por campo (field_id)
3) Resumo geral
4) Salvar dados em JSON
5) Gráficos (mostrar/salvar PNG)
6) Enviar JSON ao Oracle
0) Sair


Gráficos (opção 5)

1: mostra Média de perda (%) por campo

2: mostra Série temporal de perda por field_id

3 e 4: salvam PNG em docs/img/

Exemplos (adicione seus prints no repo):
docs/img/media_perda_por_campo.png
docs/img/serie_perda_field_101.png

💾 JSON de Exemplo (data/colheita.json)
[
  {"field_id": 101, "method": "mecanica", "area_ha": 12.5, "loss_percentage": 3.2, "date": "2025-10-14"},
  {"field_id": 102, "method": "manual",   "area_ha": 10.0, "loss_percentage": 1.8, "date": "2025-10-14"},
  {"field_id": 103, "method": "mecanica", "area_ha": 15.0, "loss_percentage": 2.7}
]


date é opcional. Se não informado, o sistema usa a data de hoje na integração Oracle.

☁️ Integração com Oracle (FIAP)

A integração com Oracle foi implementada usando o driver oracledb e realiza UPSERT (MERGE) para não duplicar registros. A chave natural é (field_id, TRUNC(data_colheita)).

1) Testar a conexão (isolado)

Edite src/test_oracle.py com seu usuário, senha e DSN FIAP:

import oracledb

username = "SEU_USUARIO_FIAP"             # ex.: rm567893
password = "SUA_SENHA_FIAP"                # ex.: 040782
dsn      = "oracle.fiap.com.br:1521/ORCL"  # confirme com a FIAP

try:
    con = oracledb.connect(user=username, password=password, dsn=dsn)
    print("✅ Conexão bem-sucedida com o Oracle (FIAP)!")
    with con.cursor() as cur:
        cur.execute("SELECT 'PlantIA conectado à FIAP!' FROM dual")
        print("🔹 Mensagem:", cur.fetchone()[0])
    con.close()
    print("🔒 Conexão encerrada.")
except oracledb.DatabaseError as e:
    err, = e.args
    print("❌ Erro ao conectar:", err.message)


Execute:

python src/test_oracle.py


Saída esperada:

✅ Conexão bem-sucedida com o Oracle (FIAP)!
🔹 Mensagem: PlantIA conectado à FIAP!
🔒 Conexão encerrada.

2) Configurar credenciais de forma segura (opcional, recomendado)

No Windows, defina variáveis de ambiente (uma vez):

setx ORACLE_USER "SEU_USUARIO_FIAP"
setx ORACLE_PASSWORD "SUA_SENHA_FIAP"
setx ORACLE_DSN "oracle.fiap.com.br:1521/ORCL"


No src/persistencia_oracle.py, as variáveis são lidas se existirem:

import os
DB_USER = os.getenv("ORACLE_USER", "SEU_USUARIO_FIAP")
DB_PASSWORD = os.getenv("ORACLE_PASSWORD", "SUA_SENHA_FIAP")
DB_DSN = os.getenv("ORACLE_DSN", "oracle.fiap.com.br:1521/ORCL")


Feche e reabra o terminal após setx.

3) Criar tabela e enviar dados (menu integrado)

Ao iniciar o app, a tabela é garantida:

>> Iniciando PlantIA...
✅ Tabela 'colheita' pronta no banco.


Para enviar o JSON ao Oracle, use a opção 6:

6) Enviar JSON ao Oracle
✅ 3 registros upsert (sem duplicar).


Executando novamente:

✅ 3 registros upsert (sem duplicar).


(Não duplica — atualiza se já existir para aquele field_id no mesmo dia).

4) Como funciona o UPSERT (MERGE)

Trecho essencial (persistencia_oracle.py):

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
    c.area_ha       = src.area_ha,
    c.perda_percent = src.perda_percent
WHEN NOT MATCHED THEN
  INSERT (field_id, tipo_colheita, area_ha, perda_percent, data_colheita)
  VALUES (src.field_id, src.tipo_colheita, src.area_ha, src.perda_percent, src.dt)


Opcional (no banco): criar unicidade para reforçar:

-- após deduplicar dados existentes:
CREATE UNIQUE INDEX ux_colheita_field_date
  ON colheita (field_id, TRUNC(data_colheita));

5) Consultas úteis no Oracle
-- Amostra dos últimos registros
SELECT id, field_id, tipo_colheita, area_ha, perda_percent, TRUNC(data_colheita) dia
FROM colheita
ORDER BY id DESC FETCH FIRST 10 ROWS ONLY;

-- Ver duplicidades por (field_id, dia)
SELECT field_id, TRUNC(data_colheita) dia, COUNT(*) qtd
FROM colheita
GROUP BY field_id, TRUNC(data_colheita)
HAVING COUNT(*) > 1;

6) Solução de Problemas (FAQ)

ORA-01017: invalid username/password

Verifique usuário/senha/DSN (mesmos do test_oracle.py).

Teste no SQL*Plus:
sqlplus USUARIO/SENHA@oracle.fiap.com.br:1521/ORCL

ORA-12541: TNS: no listener

Servidor FIAP indisponível, DSN incorreto ou necessidade de VPN.

ORA-00001: unique constraint violated

Você já tem restrição UNIQUE em (field_id, TRUNC(data_colheita)) e tentou INSERT repetido.

Use a opção 6 (UPSERT) ou garanta que o persistencia_oracle.py usa o MERGE.

🧩 Requisitos (Cap. 3–6) — Onde está no código

Subalgoritmos: coleta_dados.py, analise_dados.py, graficos.py, persistencia.py, persistencia_oracle.py

Estruturas de dados: uso de list[dict] para “tabela de memória”

Arquivos (JSON): persistencia.py e data/colheita.json

Banco (Oracle): persistencia_oracle.py (criação de tabela, UPSERT, listagem)

📦 Entrega (FIAP)

Rodar localmente:
python src/main.py → registrar, salvar JSON, gerar gráficos, enviar ao Oracle.

Prints no README:
Inclua prints do menu, gráficos (docs/img/*.png) e execução do UPSERT.

Versionamento no GitHub:

git add .
git commit -m "release: v1.0 PlantIA (JSON + Gráficos + Oracle UPSERT)"
git tag -a v1.0-entrega-fiap -m "Primeira entrega completa"
git push && git push origin v1.0-entrega-fiap

🧪 Reprodutibilidade
git clone https://github.com/SEU_USUARIO/plantia-agrodata.git
cd plantia-agrodata
pip install -r requirements.txt
python src/test_oracle.py         # (opcional) testa Oracle
python src/main.py                # roda o sistema

👤 Autor

Leno Siqueira, 
📧 lnosiqueira@gmail.com

💡 FIAP — Inteligência Artificial
🌱 Projeto: PlantIA Agrodata

📜 Licença

MIT