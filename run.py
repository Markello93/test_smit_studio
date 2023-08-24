import uvicorn
from tortoise.contrib.fastapi import register_tortoise
from src import create_app, settings

app = create_app()
register_tortoise(
    app,
    db_url=settings.database_url,
    modules={"models": [settings.APPS_MODELS, "aerich.models"]},
    generate_schemas=False,
    add_exception_handlers=True,
)

if __name__ == '__main__':
    uvicorn.run('run:app', host='0.0.0.0', port=8000, reload=True)