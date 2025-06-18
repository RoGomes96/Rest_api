from typing import Optional
from pydantic import BaseModel
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
    produto: Optional[str] = None
