from http import HTTPStatus
from fastapi import APIRouter, HTTPException

from utils import EndpointName
from utils.metadata_loader import load_metadata

router = APIRouter(prefix="/metadata", tags=["metadata"])


@router.get("/{endpoint_path:path}")
async def get_metadata(endpoint_path: EndpointName):
    endpoint_path = endpoint_path.value
    metadata = load_metadata(endpoint_path)

    if not metadata:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail={
                "message": f"Metadado não encontrado para '{endpoint_path}'"
            }
        )

    return {
        "status_code": HTTPStatus.OK,
        "message": f"Metadado encontrado para '{endpoint_path}'",
        "metadata": metadata
    }
