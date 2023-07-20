from typing import Dict, List
from pydantic import BaseModel


class CargoRateRequest(BaseModel):
    cargo_type: str
    rate: str


class CargoListRequest(BaseModel):
    __root__: Dict[str, List[CargoRateRequest]]


class CargoResponse(BaseModel):
    cargo_type: str
    price: str


class CargoListResponse(BaseModel):
    __root__: Dict[str, List[CargoResponse]]


class CargoRequest(BaseModel):
    cargotypes: List[CargoResponse]


class CargoAddResponse(BaseModel):
    message: str
