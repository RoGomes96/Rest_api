from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, Query
from rest_api.models.Oracle import OracleDatabase, OracleDb
from rest_api.schemas.oracle import ResponseList, ProductInput
from rest_api.utils import FilterPage, Proccessing422, get_template_environment

router = APIRouter(prefix="/produtos", tags=["Oracle"])


@router.get(
    "/oracle",
    response_model=ResponseList,
    responses={422: {"model": Proccessing422}},
)
async def list_products_oracle(
    filter_users: Annotated[FilterPage, Query()],
    produto: ProductInput,
    template_dir: any = Depends(get_template_environment),
):
    """ """
    oracle_db_1 = OracleDatabase(dsn="", user="user1", password="senha1")
    oracle_db_2 = OracleDatabase(dsn="", user="user2", password="senha2")
    response = await OracleDb.get(
        params={"produto": produto, "filter_users": filter_users},
        query_dir_template=template_dir,
        oracle_db_1=oracle_db_1,
        oracle_db_2=oracle_db_2,
    )

    return {
        "status_code": HTTPStatus.OK,
        "message": "Usuário Atualizado com sucesso",
        "new_item": response,
    }
