from fastapi import FastAPI
from . import routes, database
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Inicializar banco de dados
database.init_db()


app.include_router(routes.router, prefix="/tasks", tags=["tasks"])

Instrumentator().instrument(app).expose(app)
