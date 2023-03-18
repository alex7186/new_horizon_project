"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join(BASE_DIR, "new_horizon_project")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "!^_6%0so9$a@u-w22nc56xcp0^spoo4k^3q!j016o5hll+#c#o"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DEV = False
PROD_NO_DOCKER = True

ALLOWED_HOSTS = [
    "повесть-лет-словесных.рф",
    "www.повесть-лет-словесных.рф",
    "194.87.191.45",
]

if DEV:
    ALLOWED_HOSTS = [*ALLOWED_HOSTS, "0.0.0.0", "localhost", "127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "apps.main",
    "apps.projects",
    "apps.articles",
    "apps.quiz",
    "apps.popular_element",
    "rest_framework",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "apps.main.urls"

templates_dirs = [
    "apps/main/templates/",
    "apps/projects/templates/",
    "apps/articles/templates/",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": templates_dirs,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "wsgi.application"

# ❌ ну нет
# ✅ верно

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# DB_DIR = f"{BASE_DIR}/misc/db.sqlite3"
DB_DIR = f"/usr/src/new_horizon_project/misc/db.sqlite3"

if DEV:
    DB_DIR = f"{BASE_DIR}/misc/db.sqlite3"

elif PROD_NO_DOCKER:
    DB_DIR = f"/root/new_horizon_project/misc/db.sqlite3"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": DB_DIR,
    }
}


# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'postgres',
#        'USER': 'postgres',
#        'PASSWORD': 'postgres',
#        'HOST': '0.0.0.0',
#        'PORT': '5432',
#    }
# }

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation"
        + ".UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation" + ".MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation" + ".CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation" + ".NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "RU"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = "static/"
STATIC_URL = "/static/"


LOG_FILENAME = "users_logfile.log"
LOG_FILEPATH = f"{BASE_DIR}/misc"

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
