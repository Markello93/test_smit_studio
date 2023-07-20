from tortoise import run_async

from src.db.db import init_db
from src.db.models import Cargo


async def main():
    await init_db()

    data = [
        {"cargo_type": "Glass", "price": "142200"},
        {"cargo_type": "Other", "price": "1002200"},
        {"cargo_type": "Paper", "price": "31100"},
        {"cargo_type": "Plastic", "price": "20020"},
        {"cargo_type": "Computers", "price": "12200"}
    ]

    for item in data:
        cargo_type = item["cargo_type"]
        existing_cargo = await Cargo.filter(cargo_type=cargo_type).first()
        if existing_cargo:
            existing_cargo.price = item["price"]
            await existing_cargo.save()
        else:
            await Cargo.create(**item)


if __name__ == "__main__":
    run_async(main())
