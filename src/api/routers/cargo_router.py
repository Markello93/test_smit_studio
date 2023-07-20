from http import HTTPStatus
from fastapi import APIRouter
from src.api.schemas import (
    CargoAddResponse,
    CargoListRequest,
    CargoListResponse,
    CargoRequest,
)
from src.api.services.cargo_service import CargoService
from src.db.db import init_db


router_cargo = APIRouter(prefix="/cargo", tags=["Cargo"])

cargo_service = CargoService()


@router_cargo.on_event("startup")
async def startup_event():
    await init_db()


@router_cargo.post(
    "/price/",
    response_model=CargoListResponse,
    response_model_exclude_none=True,
    status_code=HTTPStatus.OK,
    summary="Checking insurance price",
    response_description=HTTPStatus.OK.phrase,
)
async def calculate_insurance_price(request: CargoListRequest):
    return await cargo_service.all_dates(request)


@router_cargo.post(
    "/add_cargo/",
    status_code=HTTPStatus.OK,
    response_model=CargoAddResponse,
    response_model_exclude_none=True,
    summary="Adding cargo_types",
    response_description=HTTPStatus.OK.phrase,
)
async def add_cargo(request: CargoRequest):
    return await cargo_service.add_cargo(request)
