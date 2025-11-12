@echo off
setlocal enabledelayedexpansion

echo [INFO] Navegando para a pasta do projeto...
cd /d "%~dp0"

echo [INFO] Diretório atual: %cd%

:: Verifica se o ambiente virtual existe
if not exist ".venv\" (
    echo [INFO] Ambiente virtual não encontrado. Criando...
    python -m venv .venv
)

:: Ativa o ambiente virtual
echo [INFO] Ativando ambiente virtual...
call .venv\Scripts\activate

:: Corrige nome do arquivo app sem extensão
if exist "dashboard\app" (
    echo [INFO] Corrigindo nome do arquivo 'app' para 'app.py'...
    ren "dashboard\app" "app.py"
)

:: Verifica se requirements.txt existe, senão cria
if not exist "requirements.txt" (
    echo [INFO] Criando arquivo requirements.txt com dependências básicas...
    echo streamlit> requirements.txt
    echo pandas>> requirements.txt
    echo plotly>> requirements.txt
)

:: Instala dependências
echo [INFO] Instalando dependências...
pip install -r requirements.txt

:: Verifica se a pasta dashboard existe
if not exist "dashboard\" (
    echo [INFO] Criando pasta dashboard...
    mkdir dashboard
)

:: Lista arquivos .py na pasta dashboard
echo.
echo [INFO] Arquivos disponíveis na pasta 'dashboard':
set i=0
for %%f in (dashboard\*.py) do (
    set /a i+=1
    set "file[!i!]=%%f"
    echo   !i!^) %%f
)

if %i%==0 (
    echo [ERRO] Nenhum arquivo .py encontrado na pasta dashboard.
    echo Criando arquivo dashboard\app.py com exemplo básico...
    echo import streamlit as st> dashboard\app.py
    echo st.title("Dashboard Inicial")>> dashboard\app.py
    echo st.write("Bem-vindo ao Streamlit!")>> dashboard\app.py
    set "file[1]=dashboard\app.py"
    set i=1
)

echo.
set /p choice=[INPUT] Digite o número do arquivo que deseja executar: 

if not defined file[%choice%] (
    echo [ERRO] Escolha inválida.
    goto :EOF
)

set "target=!file[%choice%]!"

echo [INFO] Executando Streamlit com !target!...
streamlit run "!target!"

pause
