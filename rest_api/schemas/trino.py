
from typing import Optional
from pydantic import BaseModel
from pydantic.dataclasses import dataclass


@dataclass
class Response(BaseModel):
    message: str


@dataclass
class ReponseList:
    status_code: int
    message: str
    new_item: Response


@dataclass
class Product:
    Produto: Optional[str] = None
