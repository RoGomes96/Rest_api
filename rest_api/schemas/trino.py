from dataclasses import field
from typing import Annotated
from pydantic import BaseModel, Field
from pydantic.dataclasses import dataclass


class Response(BaseModel):
    message: str


@dataclass
class ResponseList:
    status_code: int
    message: str
    new_item: Response


@dataclass
class ProductInput:
    produto: Annotated[
        str | None,
        Field(
            title="produto",
            alias="produto",
            description="Produto a ser buscado no banco de dados Trino.",
        ),
    ] = field(default=None)
