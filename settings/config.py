from builtins import bool, int, str
from pathlib import Path
from pydantic import Field, AnyUrl, DirectoryPath
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # application behavior
    max_login_attempts: int = Field(
        default=3, description="Background color of QR codes"
    )

    # Server configuration
    server_base_url: AnyUrl = Field(
        default="http://localhost", description="Base URL of the server"
    )
    server_download_folder: str = Field(
        default="downloads", description="Folder for storing downloaded files"
    )

    # Security / Auth
    secret_key: str = Field(
        default="secret-key", description="Secret key for encryption"
    )
    algorithm: str = Field(
        default="HS256", description="Algorithm used for encryption"
    )
    access_token_expire_minutes: int = Field(
        default=30, description="Expiration time for access tokens in minutes"
    )
    admin_user: str = Field(
        default="admin", description="Default admin username"
    )
    admin_password: str = Field(
        default="secret", description="Default admin password"
    )
    debug: bool = Field(
        default=False, description="Debug mode outputs errors and SQLAlchemy queries"
    )

    # JWT settings
    jwt_secret_key: str = "a_very_secret_key"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 15      # 15 minutes
    refresh_token_expire_minutes: int = 1440   # 24 hours

    # Database
    database_url: str = Field(
        default="postgresql+asyncpg://user:password@postgres/myappdb",
        description="URL for connecting to the database",
    )
    postgres_user: str = Field(
        default="user", description="PostgreSQL username"
    )
    postgres_password: str = Field(
        default="password", description="PostgreSQL password"
    )
    postgres_server: str = Field(
        default="localhost", description="PostgreSQL server address"
    )
    postgres_port: str = Field(
        default="5432", description="PostgreSQL port"
    )
    postgres_db: str = Field(
        default="myappdb", description="PostgreSQL database name"
    )

    # Discord
    discord_bot_token: str = Field(
        default="NONE", description="Discord bot token"
    )
    discord_channel_id: int = Field(
        default=1234567890,
        description="Default Discord channel ID for the bot to interact",
        example=1234567890,
    )

    # OpenAI
    openai_api_key: str = Field(
        default="NONE", description="OpenAI API Key"
    )

    # Email / Mailtrap
    send_real_mail: bool = Field(
        default=False, description="Use real SMTP or mock"
    )
    smtp_server: str = Field(
        default="smtp.mailtrap.io", description="SMTP server"
    )
    smtp_port: int = Field(
        default=2525, description="SMTP port"
    )
    smtp_username: str = Field(
        default="your-mailtrap-username", description="SMTP username"
    )
    smtp_password: str = Field(
        default="your-mailtrap-password", description="SMTP password"
    )

    # MinIO
    MINIO_ENDPOINT: str = Field(
        default="minio:9000", description="MinIO endpoint"
    )
    MINIO_ACCESS_KEY: str = Field(
        default="your_minio_access_key", description="MinIO access key"
    )
    MINIO_SECRET_KEY: str = Field(
        default="your_minio_secret_key", description="MinIO secret key"
    )
    MINIO_USE_SSL: bool = Field(
        default=False, description="MinIO use SSL"
    )
    MINIO_BUCKET_NAME: str = Field(
        default="picture", description="MinIO bucket name"
    )

    # Optional: expose TESTING for your test suite
    testing: bool = Field(
        default=False, description="Flag to indicate test mode"
    )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        # allow undefined env vars like TESTING
        extra = "ignore"

# module‐level instance
settings = Settings()
