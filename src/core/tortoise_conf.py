from src.core.settings import get_settings

settings = get_settings()

TORTOISE_ORM = {
    "connections": {"default": settings.database_url},
    "apps": {
        "models": {
            "models": [settings.APPS_MODELS, "aerich.models"],
            "default_connection": "default",
        }
    },
}
