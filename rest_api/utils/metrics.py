import time
import psutil
from fastapi import Request

from rest_api.schemas import MetricsData

metrics_analise = MetricsData()


def categorize_latency(duration_ms):
    if duration_ms < 100:
        return "<100ms"
    elif duration_ms < 500:
        return "100-500ms"
    else:
        return ">500ms"


async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = (time.time() - start_time) * 1000  # em ms

    path = request.url.path
    metrics_analise.total_requests += 1
    metrics_analise.requests_by_endpoint[path] = metrics_analise.requests_by_endpoint.get(path, 0) + 1
    bucket = categorize_latency(duration)
    metrics_analise.latency_req[bucket] = metrics_analise.latency_req.get(
        bucket, 0
    ) + 1
    return response


def get_resource_usage():
    return {
        "cpu_percent": psutil.cpu_percent(interval=0.1),
        "memory_mb": psutil.virtual_memory().used / 1024 / 1024
    }
