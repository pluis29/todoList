from decouple import config

# Carregar a URL do banco de dados do arquivo .env
DATABASE_URL = config("DATABASE_URL")
SQLALCHEMY_DATABASE_URL = config("SQLALCHEMY_DATABASE_URL")
DATABASE_TEST_URL = config("DATABASE_TEST_URL")