"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os

from environs import Env
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = Env()
env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)
# ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(',')
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://radius.bibliografiya.uz', 'https://bibliografiya.uz']
TELEGRAM_CHAT_ID = env.str("TELEGRAM_CHAT_ID")
TELEGRAM_BOT_TOKEN = env.str("TELEGRAM_BOT_TOKEN")
HOST = env.str("HOST")

# Application definition


DEFAULT_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    # local
    'apps.auth_user',
    'apps.books',
    'apps.events',
    'apps.msg',
    'apps.writers',
    'apps.toponym',
    'apps.monitoring',
]

THIRD_APP = [
    # lib
    'environs',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'ckeditor',
    'django_filters',
]

INSTALLED_APPS = DEFAULT_APPS + LOCAL_APPS + THIRD_APP

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'utils.middlewares.VisitorMiddleware',  # monitoring middleware
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {'default': env.dj_db_url('DATABASE_URL')}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "custom_static"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Authorization User
AUTH_USER_MODEL = 'auth_user.User'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --------------------------------------------------------CASHING-------------------------------------------------------
CACHE_TTL = 60 * 15  # 15 minutes

# -------------------------------------------------JAZMIN SETTINGS------------------------------------------------------

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Karmana AKM",
    #
    # # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Admin",
    #
    # # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Bibliografiya",
    #
    # # Logo to use for your site, must be present in static files, used for brand on top left
    # "site_logo": r'logo\taxi.png',

    # # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    # "login_logo": r'logo\logo.png',
    #
    # # Logo to use for login form in dark themes (defaults to login_logo)
    # "login_logo_dark": None,
    #
    # # CSS classes that are applied to the logo above
    # "site_logo_classes": "img-circle",
    #
    # # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    # "site_icon": r'logo\taxi.png',

    # # Welcome text on the login screen
    "welcome_sign": "Karmana AKM Admin panel",
    #
    # # Copyright on the footer
    "copyright": "rustamovdev.uz",
    #
    # # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "auth_user.User",
    #
    # # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": 'profile_photo',
    #
    # ############
    # # Top Menu #
    # ############
    #
    # # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        # {"name": "Дашбоард", "url": "dashboard", "new_window": True},

        # model admin to link to (Permissions checked against model)
        # {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        # {"app": "order"},
        # {"app": "shop"},
    ],
    #
    # #############
    # # User Menu #
    # #############
    #
    # # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    # "usermenu_links": [
    #     {"name": "Support", "url": "http:/", "new_window": True},
    #     {"model": "auth.user", "icon": ''}
    # ],
    #
    # #############
    # # Side Menu #
    # #############
    #
    # # Whether to display the side menu
    # "show_sidebar": True,
    #
    # # Whether to aut expand the menu
    # "navigation_expanded": True,
    #
    # # Hide these apps when generating side menu e.g (auth)
    # "hide_apps": ['auth_user'],
    #
    # # Hide these models when generating side menu (e.g auth.user)
    # "hide_models": [],
    #
    # # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["order", "user", "apartment", "advertising", "sendEmail", "selenium"],
    #
    # # Custom links to append to app groups, keyed on app name
    # "custom_links": {
    #     "order": [
    #         {
    #             "name": "Телеграм канал ",
    #             "url": "https://t.me/+rHSr3iwZxV1kYTNiassdf",
    #             "new_window": True,
    #             "icon": "fas fa-comments",
    #         },
    #     ]
    # },
    # # for the full list of 5.13.0 free icon classes
    "icons": {
        "user.User": "fas fa-user",
        "sendEmail.Email": "fas fa-envelope",  # "fas fa-envelope"
        "apartment.Apartment": "fas fa-building",
        "shop.shop": "fas fa-store",
        "shop.orderGroup": "fas fa-shopping-basket",
        "auth_user.CustomUser": "fas fa-users-cog",
        "auth_user.Manager": "fas fa-user-tie",
        "auth_user.Seller": "fas fa-user",
        "auth_user.BlackListUser": "fas fa-user-slash",
        "auth.Group": "fas fa-users",

    },
    # # Icons that are used when one is not manually specified
    # "default_icon_parents": "fas fa-chevron-circle-right",
    # "default_icon_children": "fas fa-circle",
    #
    # #################
    # # Related Modal #
    # #################
    # # Use modals instead of popups
    # "related_modal_active": False,
    #
    # #############
    # # UI Tweaks #
    # #############
    # # Relative paths to custom CSS/JS scripts (must be present in static files)
    # "custom_css": None,
    # "custom_js": None,
    # # Whether to show the UI customizer on the sidebar
    # "show_ui_builder": False,
    #
    # ###############
    # # Change view #
    # ###############
    # # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # # - vertical_tabs
    # # - collapsible
    # # - carousel
    # "changeform_format": "horizontal_tabs",
    # # override change forms on a per modeladmin basis
    # "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    # # Add a language dropdown into the admin
    # "language_chooser": True,
}

# -----------------------------------------Ckeditor-----------------------------------------
CKEDITOR_UPLOAD_PATH = "ckeditor/"
# -------------------------------------------MONITORING-------------------------------------------
APIIP_KEY = env.str("APIIP_KEY")
APIIP_URL = env.str("APIIP_URL")

try:
    from .local_settings import *
except ImportError:
    pass
