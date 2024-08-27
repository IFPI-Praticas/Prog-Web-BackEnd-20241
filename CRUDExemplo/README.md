pip install Flask-SQLAlchemy
pip install Flask-Migrate
pip install Flask-Script
pip install python-dotenv

flask db init
flask db migrate -m "Migração inicial"
flask db upgrade