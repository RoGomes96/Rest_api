from http import HTTPStatus
from fastapi import HTTPException
from asgiref.sync import sync_to_async
from pydantic import TypeAdapter

from rest_api.schemas.oracle import ResponseList, Response
from metamorfo.database import OracleDatabase


class OracleDb:

    @staticmethod
    async def get(params, query_dir_template):
        try:
            # Banco 1
            oracle_db_1 = OracleDatabase(
                dsn="",
                user="user1",
                password="senha1"
            )
            query1 = query_dir_template.get_template(
                query_dir_template
                ).render()
            rows1 = await sync_to_async(
                oracle_db_1.execute_query
            )(query1, params)

            items1 = [r._asdict() for r in rows1.fetchall()]
            items1 = [Response(**r) for r in items1]

            # Banco 2
            oracle_db_2 = OracleDatabase(
                dsn="",
                user="user2",
                password="senha2"
            )
            query2 = query_dir_template.get_template(
                query_dir_template
            ).render()
            rows2 = await sync_to_async(
                oracle_db_2.execute_query
            )(query2, params)
            items2 = [r._asdict() for r in rows2.fetchall()]
            items2 = [Response(**r) for r in items2]

            # Agregamento de resultados: a definir
            all_items = items1 + items2

            response = ResponseList(
                status_code=HTTPStatus.OK,
                message="Consulta realizada com sucesso nos bancos Oracle.",
                items=all_items
            )

            return TypeAdapter(ResponseList).dump_python(
                response,
                by_alias=True
            )

        except Exception as e:
            raise HTTPException(
                status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                detail={
                    "message": "Erro ao consultar os bancos Oracle",
                    "error": str(e)
                }
            )
