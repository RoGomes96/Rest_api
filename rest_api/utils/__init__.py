from jinja2 import Environment, FileSystemLoader
from pydantic import BaseModel, Field
from pydantic.dataclasses import dataclass
from pathlib import Path


@dataclass
class Proccessing422:
    detail: dict[str, str] = Field(description="")


class FilterPage(BaseModel):
    page: int = Field(default=1, ge=1)
    limit: int = Field(default=100, ge=1, le=5000)


def get_template_environment():
    loader = FileSystemLoader(
        Path(__file__).parent.parent.resolve() / "database" / "queries"
    )
    return Environment(loader=loader, autoescape=False)
