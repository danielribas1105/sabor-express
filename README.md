## Crie o ambiente virtual:

python -m venv venv

## Ative o ambiente virtual de acordo com o terminal que você usa:

### Prompt de Comando (cmd):

venv\Scripts\activate

### PowerShell:

.\venv\Scripts\Activate.ps1

### Git Bash:

source venv/Scripts/activate

## Para desativar o ambiente virtual

deactivate

## Instale as dependências:

pip install -r requirements.txt

## ▶️ Rodando o servidor

uvicorn app.main:app --reload

## Verificar pacotes instalados

pip freeze

## Criar o requirements.txt a partir do pip freeze

pip freeze > requirements.txt
