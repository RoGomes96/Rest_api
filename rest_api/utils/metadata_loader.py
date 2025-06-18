import yaml
from pathlib import Path


def load_metadata(endpoint_path: str):
    path = Path(f"rest_api/metadata/{endpoint_path}") / f"{endpoint_path}.yaml"

    if not path.exists():
        return None

    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)
