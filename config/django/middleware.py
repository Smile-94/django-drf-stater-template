from pydantic import model_validator
from pydantic_settings import BaseSettings

from config.environment import env_config


class MiddlewareSettings(BaseSettings):
    """
    Django middleware configuration assembled via Pydantic.
    """

    # Core Django middleware (order-sensitive)
    MIDDLEWARE: list[str] = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    # Third-party middleware shared across environments
    THIRD_PARTY_MIDDLEWARE: list[str] = ["whitenoise.middleware.WhiteNoiseMiddleware"]

    # Project-specific custom middleware
    CUSTOM_MIDDLEWARE: list[str] = []

    # Environment-specific middleware toggles (e.g. debug tools in local only)
    ENVIRONMENT_BASE_MIDDLEWARE: dict[str, list[str]] = {
        "local": ["debug_toolbar.middleware.DebugToolbarMiddleware"],
        "development": [],
        "staging": [],
        "production": [],
    }

    @model_validator(mode="after")
    def set_middleware(self):
        # Inject environment-specific middleware first
        self.MIDDLEWARE += list(self.ENVIRONMENT_BASE_MIDDLEWARE[env_config.ENVIRONMENT.value])

        # Append third-party middleware after core middleware
        if self.THIRD_PARTY_MIDDLEWARE:
            self.MIDDLEWARE += self.THIRD_PARTY_MIDDLEWARE

        # Append custom middleware last to preserve override behavior
        if self.CUSTOM_MIDDLEWARE:
            self.MIDDLEWARE += self.CUSTOM_MIDDLEWARE

        return self


# Singleton middleware configuration instance
middleware_config = MiddlewareSettings()
