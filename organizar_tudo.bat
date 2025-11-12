@echo off
echo Iniciando organização completa do projeto PlantIA Agrodata...

:: Caminho raiz do projeto
cd "C:\Users\Leno Siqueira\OneDrive - Fiap-Faculdade de Informática e Administração Paulista\PlantIA Agrodata - FIAP\plantia-agrodata_v2"

:: Executa os scripts de organização
call organizar_projeto.bat
call organizar_estrutura.bat
call organizar_dados.bat

echo Organização concluída com sucesso!
pause
