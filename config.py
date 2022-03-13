from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FastAPI Jobs"
    deta_key: str
    job_base: str
    company_base: str

    class Config:
        env_file = ".env"


settings = Settings()