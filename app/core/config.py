from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API Settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG_MODE: bool = False

    # Model Settings
    MODEL_PATH: str = "model/model.cbm"
    MODEL_VERSION: str = "1.0.0"

    class Config:
        case_sensitive = True


settings = Settings()
