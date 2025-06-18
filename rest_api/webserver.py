from fastapi import FastAPI
from rest_api.routes import oracle, trino, metadata, metrics
from rest_api.utils.metrics import metrics_middleware

app = FastAPI(title="Rest API", version="0.0.1")
app.include_router(oracle.router)
app.include_router(trino.router)
app.include_router(metadata.router)
app.middleware("http")(metrics_middleware)
app.include_router(metrics.router)
