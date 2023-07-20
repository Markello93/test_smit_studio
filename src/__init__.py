from fastapi import FastAPI


from src.core.settings import settings

from src.api.routers import cargo_router


def create_app() -> FastAPI:
    app = FastAPI(debug=settings.DEBUG, root_path=settings.CARGO_ROOT_PATH)
    app.include_router(cargo_router.router_cargo)

    return app
