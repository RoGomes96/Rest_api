from http import HTTPStatus
from metamorfo.database.trino_database import TrinoDatabase
from fastapi import HTTPException, Response
from asgiref.sync import sync_to_async
from pydantic import TypeAdapter

from schemas.trino import ResponseList


class TrinoDb:
    @staticmethod
    async def get(params, query_dir_template):
        try:
            db = TrinoDatabase()
            query = query_dir_template.get_template("")
            query = query.render()
            rows = await sync_to_async(db.execute_query)(query, params)
            items = [r._asdict() for r in rows.fetchall()]
            items = [Response(**r) for r in items]

            response = ResponseList(
                status_code=HTTPStatus.OK,
                message="Consulta realizada com sucesso",
                items=items,
            )
            return TypeAdapter(ResponseList).dump_python(response, by_alias=True)
        except Exception as e:
            raise HTTPException(
                status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                detail={
                    "message": "Erro no processamento da consulta",
                    "error": str(e),
                },
            )
