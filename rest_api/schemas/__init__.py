from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Dict


@dataclass
class MetricsData:
    total_requests: int = 0
    requests_by_endpoint: Dict[str, int] = field(default_factory=dict)
    latency_req: Dict[str, int] = field(default_factory=dict)
