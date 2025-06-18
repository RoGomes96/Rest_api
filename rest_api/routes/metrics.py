from fastapi import APIRouter
from http import HTTPStatus
from rest_api.utils.metrics import metrics_analise
from rest_api.utils.metrics import get_resource_usage

router = APIRouter(prefix="/metrics", tags=["metrics"])


@router.get("/")
def get_metrics():
    resource_usage = get_resource_usage()
    return {
        "status_code": HTTPStatus.OK,
        "message": "Métricas coletadas com sucesso",
        "data": {
            "resource_usage": resource_usage,
            "total_requests": metrics_analise.total_requests,
            "requests_by_endpoint": metrics_analise.requests_by_endpoint,
            "latency_distribution": metrics_analise.latency_req,
        },
    }
