from fastapi import FastAPI
from . import routes, database

app = FastAPI()

# Inicializar banco de dados
database.init_db()

app.include_router(routes.router, prefix="/tasks", tags=["tasks"])
