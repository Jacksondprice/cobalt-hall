import os


class Settings:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///local.sqlite3")
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only")
    PAGE_SIZE = int(os.environ.get("PAGE_SIZE", "50"))
