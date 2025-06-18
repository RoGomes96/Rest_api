from http import HTTPStatus
from fastapi import HTTPException
from asgiref.sync import sync_to_async
import oracledb
from pydantic import TypeAdapter

from schemas.oracle import ResponseList, Response


class OracleDb:
    @staticmethod
    async def get(params, query_dir_template, oracle_db_1, oracle_db_2):
        try:

            def parse(cursor):
                items = [r._asdict() for r in rows1.fetchall()]
                return [Response(**r) for r in items]

            # Banco 1
            query1 = query_dir_template.get_template(query_dir_template).render()
            rows1 = await sync_to_async(oracle_db_1.execute_query)(query1, params)

            # Banco 2
            query2 = query_dir_template.get_template(query_dir_template).render()
            rows2 = await sync_to_async(oracle_db_2.execute_query)(query2, params)

            # Agregamento de resultados: a definir
            items = parse(rows1) + parse(rows2)

            response = ResponseList(
                status_code=HTTPStatus.OK,
                message="Consulta realizada com sucesso nos bancos Oracle.",
                items=items,
            )

            return TypeAdapter(ResponseList).dump_python(response, by_alias=True)

        except Exception as e:
            raise HTTPException(
                status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                detail={
                    "message": "Erro ao consultar os bancos Oracle",
                    "error": str(e),
                },
            )


class OracleDatabase:
    def __init__(self, user, password, dsn):
        self.connection = oracledb.connect(
            user=user,
            password=password,
            dsn=dsn
        )

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params or {})
        return cursor
