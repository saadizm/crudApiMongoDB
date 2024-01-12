from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    
    DATABASE_URL : str
    JWT_SECRET_KEY: str
    MONGODB_NAME: str
    
    JWT_ALGORITHM: str
    REFRESH_TOKEN_EXPIRES_IN: int
    ACCESS_TOKEN_EXPIRES_IN: int
    
    CLIENT_ORIGIN: str
    
    class Config:
        env_file = "./.env"
        
@lru_cache
def getSettings() -> Settings:
    return Settings()