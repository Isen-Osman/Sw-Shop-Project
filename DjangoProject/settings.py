from pathlib import Path
from decouple import config
import os


# -------------------------------
# Base directory
# -------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------
# Security
# -------------------------------
SECRET_KEY = config('SECRET_KEY')
# DEBUG = config("DEBUG", default=False, cast=bool)
DEBUG = True


# -------------------------------
# Installed Apps
# -------------------------------
INSTALLED_APPS = [
    # Django default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',

    # My apps
    'app',
    'wishlist',
    'orders',
    'widget_tweaks',
    'sslserver',

    # Allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # Social providers
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',

    # Cloudinary
    'cloudinary',
    'cloudinary_storage',

    'django_extensions',
]

# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': config('CLOUD_NAME'),
#     'API_KEY': config('API_KEY'),
#     'API_SECRET': config('API_SECRET'),
# }

# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# Основна директорија на проектот

# Локална папка за медија фајлови
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# -------------------------------
# Authentication backends
# -------------------------------
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # default
    'allauth.account.auth_backends.AuthenticationBackend',  # allauth
]

# -------------------------------
# Middleware
# -------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

    # Allauth middleware
    'allauth.account.middleware.AccountMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -------------------------------
# URLs
# -------------------------------
ROOT_URLCONF = 'DjangoProject.urls'

# -------------------------------
# Templates
# -------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': False,  # Исклучи го за кешираниот loader
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'app.context_processors.categories_processor',
                'app.context_processors.wishlist_counter',
            ],
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],
        },
    },
]

# -------------------------------
# WSGI
# -------------------------------
WSGI_APPLICATION = 'DjangoProject.wsgi.application'

# -------------------------------
# Database
# -------------------------------
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'swshopdb',
        'USER': 'isen',
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


from urllib.parse import urlparse

url = urlparse(config('MY_SQL_DATABASE'))

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}

# -------------------------------
# Password validators
# -------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------------------
# Internationalization
# -------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -------------------------------
# Static files
# -------------------------------
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -------------------------------
# Sites framework
# -------------------------------
SITE_ID = 1

# -------------------------------
# Allauth settings
# -------------------------------
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

ACCOUNT_LOGIN_METHODS = {'username', 'email'}
ACCOUNT_SIGNUP_FIELDS = ['email*', 'username*', 'password1*', 'password2*']

# -------------------------------
# Google OAuth
# -------------------------------
SOCIAL_AUTH_GOOGLE_CLIENT_ID = config('CLIENT_ID')
SOCIAL_AUTH_GOOGLE_SECRET = config('SECRET')

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': SOCIAL_AUTH_GOOGLE_CLIENT_ID,
            'secret': SOCIAL_AUTH_GOOGLE_SECRET,
            'key': ""
        }
    }
}

EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'
SENDGRID_API_KEY = config('SENDGRID_API_KEY')
DEFAULT_FROM_EMAIL = 'info@dolnaobleka.store'

SENDGRID_SANDBOX_MODE_IN_DEBUG = False

ALLOWED_HOSTS = ['192.168.1.196', '192.168.1.187', 'localhost', '127.0.0.1', '192.168.1.185',
                 'your-railway-app.up.railway.app', 'sw-shop-project-3.onrender.com', '165.227.170.149',]

SOCIALACCOUNT_LOGIN_ON_GET = True

# ==========================================
# Django Security Settings
# ==========================================

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# --- HTTPS & SSL ---
SECURE_SSL_REDIRECT = True  # Принудува HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')  # Ако имаш reverse proxy
SECURE_HSTS_SECONDS = 3600  # HTTP Strict Transport Security (HSTS)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# --- Cookies Security ---
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = False

# --- XSS & Content Type ---
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 1209600  # 2 недели

X_FRAME_OPTIONS = 'DENY'

SECURE_REFERRER_POLICY = 'same-origin'


# gunicorn --bind 0.0.0.0:8000 DjangoProject.wsgi:application

# [Unit]
# Description=gunicorn daemon
# After=network.target
#
# [Service]
# User=sammy
# Group=www-data
# WorkingDirectory=/home/isen/Sw-Shop-Project
# ExecStart=/home/isen/Sw-Shop-Project/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/isen/Sw-Shop-Project/DjangoProject.sock DjangoProject.wsgi:application
#
# [Install]
# WantedBy=multi-user.target

# sudo nano /etc/nginx/sites-available/Sw-Shop-Project


# server {
#     listen 80;
#     server_name 165.227.170.149;
#
#     location = /favicon.ico { access_log off; log_not_found off; }
#     location /static/ {
#         root /home/isen/Sw-Shop-Project;
#     }
#
#     location /media/ {
#         root /home/isen/Sw-Shop-Project;
#     }
#
#     location / {
#         include proxy_params;
#         proxy_pass http://unix:/home/isen/gunicorn.sock;
#     }
# }

# sudo ln -s /etc/nginx/sites-available/Sw-Shop-Project /etc/nginx/sites-enabled

ACCOUNT_SIGNUP_REDIRECT_URL = '/'  # Пренасочување по успешна најава