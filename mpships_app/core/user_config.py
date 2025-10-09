from pydantic_settings import BaseSettings


class UserSettings(BaseSettings):
    APP_NAME: str | None = None
    AUTHOR: str | None = None
    AUTHOR_GIT: str | None = None
    DESCRIPTION: str | None = None
    PREVIEW_IMG: str | None = None


user_settings = UserSettings()
