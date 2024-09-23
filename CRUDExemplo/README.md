## Dependências para trabalhar com banco de dados
pip install Flask-SQLAlchemy

pip install Flask-Migrate

pip install Flask-Script

pip install python-dotenv

## Depois de criar o database.py, fazer as devidas configurações e criar os modelos, executar esses comandos:

flask db init

flask db migrate -m "Migração inicial"

flask db upgrade