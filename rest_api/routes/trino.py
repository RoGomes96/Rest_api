from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, Query

from rest_api.models.Trino import TrinoDb
from rest_api.schemas.trino import ProductInput, ResponseList
from rest_api.utils import FilterPage, Proccessing422, get_template_environment

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
