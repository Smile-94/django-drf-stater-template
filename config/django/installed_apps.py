from typing import List

from pydantic import model_validator
from pydantic_settings import BaseSettings

from config.env import env_config


class InstalledAppsSettings(BaseSettings):
    """
    Django INSTALLED_APPS configuration assembled via Pydantic.
    """

    # Core Django framework applications (always enabled)
    DJANGO_APPS: List[str] = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    ]

    # Third-party applications common across environments
    THIRD_PARTY_APPS: List[str] = ["django_filters", "rest_framework"]

    # Environment-specific app toggles (e.g. debug tools in local only)
    ENVIRONMENT_APPS: dict[str, List[str]] = {
        "local": ["debug_toolbar"],
        "development": [],
        "staging": [],
        "production": [],
    }

    # Project-specific Django apps
    LOCAL_APPS: List[str] = [
        "apps.common.apps.CommonConfig",
    ]

    # Final Django-compatible INSTALLED_APPS list
    INSTALLED_APPS: List[str] = []

    @model_validator(mode="after")
    def set_apps(self):
        # Inject environment-specific apps based on active runtime environment
        self.THIRD_PARTY_APPS += list(
            self.ENVIRONMENT_APPS[env_config.ENVIRONMENT.value]
        )

        # Preserve Django app loading order: core → third-party → local
        self.INSTALLED_APPS = list(
            self.DJANGO_APPS + self.THIRD_PARTY_APPS + self.LOCAL_APPS
        )
        return self


# Singleton instance used by Django settings
installed_apps_config = InstalledAppsSettings()
