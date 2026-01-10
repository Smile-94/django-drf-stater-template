# ------------------------------------------------------------------------------
# Import modular Django configuration sections
# Each config is isolated to keep settings clean, testable, and environment-safe
# ------------------------------------------------------------------------------
from config.django.authentication import authentication_config
from config.django.base import base_config
from config.django.database import database_config
from config.django.installed_apps import installed_apps_config
from config.django.middleware import middleware_config
from config.django.rest_framework import drf_config
from config.django.security import security_config
from config.django.static import static_config
from config.django.templates import template_config

# ------------------------------------------------------------------------------
# Core project paths and base configuration
# ------------------------------------------------------------------------------
# Absolute base directory of the Django project (used across settings)
BASE_DIR = base_config.BASE_DIR


# ------------------------------------------------------------------------------
# Security settings
# ------------------------------------------------------------------------------
# Secret key used for cryptographic signing (must be unique per environment)
SECRET_KEY = security_config.SECRET_KEY

# Debug should ALWAYS be False in production
DEBUG = security_config.DEBUG

# Hosts/domain names that this Django site can serve
# Prevents HTTP Host header attacks
ALLOWED_HOSTS = base_config.ALLOWED_HOSTS


# ------------------------------------------------------------------------------
# Application definition
# ------------------------------------------------------------------------------
# All installed Django, third-party, and local apps
INSTALLED_APPS = installed_apps_config.INSTALLED_APPS

# Middleware stack executed on every request/response cycle
# Order matters — security middleware should come first
MIDDLEWARE = middleware_config.MIDDLEWARE


# ------------------------------------------------------------------------------
# URL and application entry points
# ------------------------------------------------------------------------------
# Root URL configuration module
ROOT_URLCONF = base_config.ROOT_URLCONF

# ASGI entry point (used for async support, WebSockets, and background tasks)
WSGI_APPLICATION = base_config.ASGI_APPLICATION


# ------------------------------------------------------------------------------
# Templates configuration
# ------------------------------------------------------------------------------
# Django template engine configuration
# Includes template loaders, context processors, and directories
TEMPLATES = template_config.TEMPLATES


# ------------------------------------------------------------------------------
# Database configuration
# ------------------------------------------------------------------------------
# Database connections (PostgreSQL / MySQL / SQLite etc.)
# Loaded dynamically per environment
DATABASES = database_config.DATABASES


# ------------------------------------------------------------------------------
# Authentication and password validation
# ------------------------------------------------------------------------------
# Password validators enforce strong passwords and security best practices
AUTH_PASSWORD_VALIDATORS = authentication_config.AUTH_PASSWORD_VALIDATORS


# ------------------------------------------------------------------------------
# Internationalization
# ------------------------------------------------------------------------------
# Default language for the application
LANGUAGE_CODE = "en-us"

# Application time zone (UTC recommended for production systems)
TIME_ZONE = "UTC"

# Enable Django’s translation system
USE_I18N = True

# Store datetimes in UTC and convert to local time when needed
USE_TZ = True


# ------------------------------------------------------------------------------
# Static and media files
# ------------------------------------------------------------------------------
# URL prefix for static files (CSS, JS, images)
STATIC_URL = static_config.STATIC_URL

# Directory where static files are collected for production
STATIC_ROOT = static_config.STATIC_ROOT

# Storage backends (local, S3, CDN, etc.)
STORAGES = static_config.STORAGES

# URL prefix for user-uploaded media files
MEDIA_URL = static_config.MEDIA_URL

# Filesystem path for uploaded media
MEDIA_ROOT = static_config.MEDIA_ROOT


# ------------------------------------------------------------------------------
# REST Framework configuration
# ------------------------------------------------------------------------------
# DRF settings loaded via Pydantic
REST_FRAMEWORK = drf_config.REST_FRAMEWORK
