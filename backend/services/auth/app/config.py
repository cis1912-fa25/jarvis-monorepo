class Settings:
    database_url: str = "sqlite:///../../jarvis.db"
    jwt_secret_key: str = "super-secret-key-dont-use-this-in-production"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 30
    cookie_secure: bool = True
    cookie_samesite: str = "None"

settings = Settings()