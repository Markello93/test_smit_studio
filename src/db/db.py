from tortoise import Tortoise

from src import settings


async def init_db():
    await Tortoise.init(
        db_url=settings.database_url,
        modules={"models": [settings.APPS_MODELS, "aerich.models"]},
    )
