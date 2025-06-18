from fastapi import FastAPI
from routes import oracle, trino, metadata

app = FastAPI(title="Rest API", version="0.0.1")
app.include_router(oracle.router)
app.include_router(trino.router)
app.include_router(metadata.router)
