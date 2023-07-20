from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "cargo_type_info" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "cargo_type" VARCHAR(100) NOT NULL UNIQUE,
    "price" DECIMAL(10,2) NOT NULL
);
COMMENT ON TABLE "cargo_type_info" IS 'The Cargo model';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
