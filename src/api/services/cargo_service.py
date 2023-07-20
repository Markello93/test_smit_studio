from decimal import Decimal
from fastapi import HTTPException, status
from src.api.schemas import CargoAddResponse, CargoListRequest, CargoRequest
from src.db.models import Cargo


class CargoService:
    model = Cargo
    """Сервис для работы с типами товаров."""

    async def all_dates(self, request: CargoListRequest):
        """Возвращает цены страховки для всех товаров."""

        response = {}
        for date, cargo_data in request.__root__.items():
            all_cargo_per_date = []
            for cargo_rate_request in cargo_data:
                cargo_type = cargo_rate_request.cargo_type
                rate = Decimal(cargo_rate_request.rate)
                cargo_obj = await self.model.get_or_none(cargo_type=cargo_type)
                price = round(cargo_obj.price * rate, 2)
                resp = {"cargo_type": cargo_type, "price": str(price)}
                all_cargo_per_date.append(resp)
            response[date] = all_cargo_per_date
        return response

    async def add_cargo(self, request: CargoRequest):
        """Добавляет данные о типах товара и их стоимости в БД."""

        data = request.cargotypes
        added_cargo_types = []
        for item in data:
            cargo_type = item.cargo_type
            price = item.price
            existing_cargo = await Cargo.filter(cargo_type=cargo_type).first()
            if existing_cargo:
                existing_cargo.price = price
                await existing_cargo.save()
            else:
                try:
                    await Cargo.create(cargo_type=cargo_type, price=price)
                    added_cargo_types.append(cargo_type)
                except Exception as e:
                    raise HTTPException(
                        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        detail=f"Не удалось добавить товар '{cargo_type}'. Error: {str(e)}",
                    )
        if added_cargo_types:
            added_cargo_str = ", ".join(added_cargo_types)
            return CargoAddResponse(
                message=f"Данные о товарах {added_cargo_str} успешно добавлены в базу данных."
            )
        else:
            return CargoAddResponse(
                message="Эти товары уже были в базе, у них обновилась цена."
            )
