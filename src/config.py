import os

from dotenv import load_dotenv

load_dotenv()


def get_env_var(key: str, allow_none=False) -> str | None:
    env_value = os.getenv(key, None)
    if env_value is None and allow_none is False:
        raise Exception("No env variable found")
    return env_value


class Config:
    DJANGO_SECRET_KEY = get_env_var("DJANGO_SECRET_KEY")


config = Config()
