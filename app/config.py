from decouple import config

# Carregar a URL do banco de dados do arquivo .env
DATABASE_URL = config("DATABASE_URL", default="sqlite:///./test.db")
