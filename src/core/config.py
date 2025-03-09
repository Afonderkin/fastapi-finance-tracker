from pathlib import Path

from pydantic import BaseModel, PostgresDsn
from pydantic_settings import SettingsConfigDict, BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent


class RunConfig(BaseModel):
    debug: bool = True
    title: str = "fastapi-finance-tracker"
    description: str = ("Финансовый трекер, где вы можете отслеживать доходы и расходы, планировать свой бюджет и "
                        "просматривать отчеты о доходах и расходах.")
    version: str = "0.5.0"
    host: str = "0.0.0.0"
    port: int = 8000
    url: str = "http://localhost:8000/api/v1"


class ApiV1PrefixConfig(BaseModel):
    prefix: str = "/v1"
    categories_prefix: str = "/categories"
    transactions_prefix: str = "/transactions"
    reports_prefix: str = "/reports"
    budgets_prefix: str = "/budgets"


class ApiPrefixConfig(BaseModel):
    prefix: str = "/api"
    v1: ApiV1PrefixConfig = ApiV1PrefixConfig()


class DataBaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    naming_conventions: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
        env_file=(f"{BASE_DIR}/.env.template", f"{BASE_DIR}/.env"),
    )

    app: RunConfig = RunConfig()
    api: ApiPrefixConfig = ApiPrefixConfig()
    db: DataBaseConfig


settings = Settings()
