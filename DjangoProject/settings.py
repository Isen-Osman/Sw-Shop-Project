from pathlib import Path
from decouple import config

# -------------------------------
# Base directory
# -------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------
# Security
# -------------------------------
SECRET_KEY = config('SECRET_KEY')
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
]

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUD_NAME'),
    'API_KEY': config('API_KEY'),
    'API_SECRET': config('API_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


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
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'app.context_processors.categories_processor',
                'app.context_processors.wishlist_counter',

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
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
from urllib.parse import urlparse

url = urlparse(config('MY_SQL_DATABASE'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': url.path[1:],  # отстрануваме почетен /
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port,
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

EMAIL_HOST_USER = config('EMAIL_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_PASSWORD')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

ALLOWED_HOSTS = ['192.168.1.196', '192.168.1.187', 'localhost', '127.0.0.1', '192.168.1.185',
                 'your-railway-app.up.railway.app', ]

SOCIALACCOUNT_LOGIN_ON_GET = True

# ==========================================
# Django Security Settings
# ==========================================

# --- HTTPS & SSL ---
SECURE_SSL_REDIRECT = True  # Принудува HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')  # Ако имаш reverse proxy
SECURE_HSTS_SECONDS = 3600  # HTTP Strict Transport Security (HSTS)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# --- Cookies Security ---
SESSION_COOKIE_SECURE = True  # Сесиите само преку HTTPS
CSRF_COOKIE_SECURE = True  # CSRF cookies само преку HTTPS
SESSION_COOKIE_HTTPONLY = True  # JavaScript не може да чита session cookie
CSRF_COOKIE_HTTPONLY = False  # CSRF треба да биде достапен за формите
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Сесијата се брише при затворање на прелистувач

# --- XSS & Content Type ---
SECURE_BROWSER_XSS_FILTER = True  # Вграден XSS филтер во прелистувач
SECURE_CONTENT_TYPE_NOSNIFF = True  # Браузерот не ја „угаѓа“ MIME type

X_FRAME_OPTIONS = 'DENY'  # Забранува вчитување на сајтот во iframe

SECURE_REFERRER_POLICY = 'same-origin'  # Не праќа referrer информации надвор од твојот домен

# --- Admin & Permissions ---
# Само superusers треба да имаат пристап до admin site
# Ограничувај пристап преку IP (опционално)
# Ограничувај create/update/delete права за корисници
# Препорачливо е да користиш custom user групи

# --- Rate Limiting & Brute Force Protection (Optional) ---
# pip install django-ratelimit
# Можеш да го додадеш во login views или forms

# --- Other Security Best Practices ---
# DEBUG = False  # Никогаш не го оставај на True во production
# ALLOWED_HOSTS = ['tvojdomain.com', 'www.tvojdomain.com']  # Сите дозволени домени
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True


#
# HTTPS & HSTS (SECURE_SSL_REDIRECT, SECURE_HSTS_SECONDS) – гарантира дека целиот сообраќај е криптиран. Без тоа, податоците можат да се пресретнат.
# Cookies Security (SESSION_COOKIE_SECURE, CSRF_COOKIE_SECURE) – без овие, cookies можат да се крадат или користат во XSS напади.
# XSS & Content Type Filters (SECURE_BROWSER_XSS_FILTER, SECURE_CONTENT_TYPE_NOSNIFF) – штити од најчести напади преку веб прелистувачи.
# Clickjacking (X_FRAME_OPTIONS) – без ова, некој може да вгради твојот сајт во iframe и да изведува „clickjacking“ напади.
# Referrer & CSP – го ограничуваат кој може да вчитува ресурси и од каде се праќаат информации. Не е задолжително, но многу го зголемува security.
# DEBUG = False & ALLOWED_HOSTS – задолжително за production, во спротивно сајтот е ранлив.
# Admin & Permissions – само superuser треба да има пристап до admin; без ова, секој може да модифицира data.
