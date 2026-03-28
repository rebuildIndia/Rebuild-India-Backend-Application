import os
from typing import Optional
from urllib.parse import quote_plus


def _build_mysql_url_from_env() -> Optional[str]:
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    db_name = os.getenv("DB_NAME")
    port = os.getenv("DB_PORT", "3306")

    if not all([user, password, host, db_name]):
        return None

    safe_password = quote_plus(password)
    return f"mysql+pymysql://{user}:{safe_password}@{host}:{port}/{db_name}"


DATABASE_URL = (
    os.getenv("DATABASE_URL")
    or _build_mysql_url_from_env()
    or "sqlite:///./db.sqlite"
)
