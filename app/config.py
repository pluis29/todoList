from decouple import config

# Carregar a URL do banco de dados do arquivo .env
DATABASE_URL = config("DATABASE_URL", default="sqlite:///./prod.db")
SQLALCHEMY_DATABASE_URL = config("SQLALCHEMY_DATABASE_URL", default="sqlite:///:memory:")
DATABASE_TEST_URL = config("DATABASE_TEST_URL", default="sqlite:///./test.db")