from fastapi import FastAPI
from rest_api.routes import oracle, trino

app = FastAPI(title="Rest API", version="0.0.1")
app.include_router(oracle.router)
app.include_router(trino.router)
