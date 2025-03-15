# ----------------------------------------------------------------------------------+
#                                                                                   |
#                                      IMPORTS                                      |
#                                                                                   |
# ----------------------------------------------------------------------------------+


from pathlib import Path
import os
import datetime


# ----------------------------------------------------------------------------------+
#                                                                                   |
#                                     ADMIN PANEL                                   |
#                                                                                   |
# ----------------------------------------------------------------------------------+

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Library Admin",
    "site_header": "Library",
    "site_brand": "FORTEENALL",
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    "custom_css": "main.css",
    "copyright": "black castle forteenall",
    "order_with_respect_to" : [
        'user',
        'karjoModel',
        'user.karfarmaModel',
        'blogModel',
        'drugstoresModel',
        'storesModel',
        'repotageModel',
        'resomeModel',
        'contactModel',
        'messageModel']
}

# ----------------------------------------------------------------------------------+
#                                                                                   |
#                                      SECURITY                                     |
#                                                                                   |
# ----------------------------------------------------------------------------------+


BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "jc)%%gzt!r+&t$fmkg42a+_-svpx$bsa^r7!bu9bs0qx#dfxg)"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    )
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(days=5),
}


# ----------------------------------------------------------------------------------+
#                                                                                   |
#                                        CORS                                       |
#                                                                                   |
# ----------------------------------------------------------------------------------+


ALLOWED_HOSTS = ["*"]


# cors
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://niaz.liara.run",
    "https://niazpharmacy.ir",
]


# ----------------------------------------------------------------------------------+
#                                                                                   |
#                                   INSTALLED APPS                                  |
#                                                                                   |
# ----------------------------------------------------------------------------------+


DEPENDENCIES = [
    "rest_framework",
    "corsheaders",
    "import_export",
]

MAIN_APPS = [
    'user',
    'models.drugstoresModel.apps.DrugstoresmodelConfig',
    'models.storesModel.apps.StoresmodelConfig',
    'models.contactModel.apps.ContactmodelConfig',
    'models.blogsModel.apps.BlogsmodelConfig',
    'models.repotageModel.apps.RepotagemodelConfig',
    'models.messagesModel.apps.MessagesmodelConfig',
    'models.resomeModel.apps.ResomemodelConfig',
    'core',]


INSTALLED_APPS = [
    "jazzmin",
    "django_jalali",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "ckeditor",
    *DEPENDENCIES,
    *MAIN_APPS,
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 600,
    },
}

# ----------------------------------------------------------------------------------+
#                                                                                   |
#                                     DEFINITION                                    |
#                                                                                   |
# ----------------------------------------------------------------------------------+






ROOT_URLCONF = "server.urls"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "server.wsgi.application"


# ----------------------------------------------------------------------------------+
#                                                                                   |
#                                  DATABASE & FILES                                 |
#                                                                                   |
# ----------------------------------------------------------------------------------+


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "data/db.sqlite3",
    }
}

STATIC_URL = "static/"
STATICFILES_DIRS = ((os.path.join(BASE_DIR, "static")),)
AUTH_USER_MODEL = 'user.AllUsers'


# ----------------------------------------------------------------------------------+
#                                                                                   |
#                               INTERNATIONALIZATION                                |
#                                                                                   |
# ----------------------------------------------------------------------------------+

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "default_acl": 'public-read',
            "querystring_auth": False
        },
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}


AWS_S3_ENDPOINT_URL = "https://niaz.storage.c2.liara.space"
AWS_STORAGE_BUCKET_NAME = "niaz"

AWS_S3_ACCESS_KEY_ID = "5cmc0slub2ctgndr"
AWS_S3_SECRET_ACCESS_KEY = "857c4e3c-713f-44b8-9d76-3d6dfa992d9c"

AWS_DEFAULT_ACL = 'public-read'
AWS_BUCKET_ACL = 'public-read'


LANGUAGE_CODE = "en"

TIME_ZONE = "Asia/Tehran"

USE_I18N = True

USE_TZ = True
