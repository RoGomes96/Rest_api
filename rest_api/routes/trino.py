from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query

from models.Trino import TrinoDb
from schemas.trino import ProductInput, ResponseList
from utils import FilterPage, Proccessing422, get_template_environment
from utils.metadata_loader import load_metadata

router = APIRouter(prefix="/produtos", tags=["Trino"])


@router.get(
    "/trino",
    response_model=ResponseList,
    responses={422: {"model": Proccessing422}},
)
async def list_products_trino(
    filter_users: Annotated[FilterPage, Query()],
    produto: ProductInput,
    template_dir: any = Depends(get_template_environment),
):
    """ """

    response = await TrinoDb.get(
        params={"produto": produto, "filter_users": filter_users}, query_dir_template=template_dir
    )

    return {
        "status_code": HTTPStatus.OK,
        "message": "Usuário Atualizado com sucesso",
        "new_item": response,
    }



