# from pathlib import Path


# import os
# import pymysql
# pymysql.install_as_MySQLdb()

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
# TEMPLATE_DIR = BASE_DIR / 'Trvels' / 'templates'
# STATIC_URL = '/static/'

# # Quick-start development settings - unsuitable for production

# SECRET_KEY = os.getenv("SECRET_KEY", get_random_secret_key())
# DEBUG = os.getenv("DEBUG", "False") == "True"
# ALLOWED_HOSTS = []
# SITE_ID = 1
# ALLOWED_HOSTS = ['.vercel.app', '127.0.0.1']


# # Application definition
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'django.contrib.sites',

#     'allauth',
#     'allauth.account',
#     'allauth.socialaccount',
#     'allauth.socialaccount.providers.google',
#     'Trvels',
# ]





# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#      "whitenoise.middleware.WhiteNoiseMiddleware",  

#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#    'allauth.account.middleware.AccountMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]
# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend',  # Default authentication
#     'allauth.account.auth_backends.AuthenticationBackend',  # Required for social login
# ]

# ROOT_URLCONF = 'DD_Tours.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [TEMPLATE_DIR],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'DD_Tours.wsgi.application'

# # Database

# <<<<<<< HEAD

# # DATABASES = {
# #     'default': {
# #         'ENGINE': 'django.db.backends.sqlite3',
# #         'NAME': BASE_DIR / "my.sqlite3",
# #     }
# # }
# =======
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': '',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': '',
#         'PORT': '',
#         'OPTIONS': {
#             'charset': 'utf8mb4',
#         },
#     }
# }



# LOGIN_REDIRECT_URL = '/'   # Redirect after login
# LOGOUT_REDIRECT_URL = '/'  # Redirect after logout
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_EMAIL_VERIFICATION = 'none'  # Change to 'optional' or 'mandatory' if needed

# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'SCOPE': ['profile', 'email'],
#         'AUTH_PARAMS': {'access_type': 'online'},
#     }
# }


# # Password validation
# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
# ]

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True

# # Static files (CSS, JavaScript, Images)
# STATICFILES_DIRS = [BASE_DIR / 'Trvels' / 'static']

# # Media files (uploads)
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'#email backend
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST = 'smtp.gmail.com' #smtp server address
# EMAIL_HOST_USER = '.21.ce@iite.indusuni.ac.in'
# EMAIL_HOST_PASSWORD = ''
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# DEFAULT_TO_EMAIL = '@gmail.com'

# CONTACT_EMAIL = 'gohilpratishtha57@gmail.com'  

# CONTACT_EMAIL = 'gohilpratishtha57@gmail.com'  

# settings.py
import os
from pathlib import Path
import pymysql
pymysql.install_as_MySQLdb()
from dotenv import load_dotenv

load_dotenv()  # Load .env file
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv("GOOGLE_OAUTH_CLIENT_ID")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv("GOOGLE_OAUTH_CLIENT_SECRET")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}


# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / 'trvels' / 'templates'

# Security
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-k483xsd(sz&2%%u)51%f&k18d_k+6y8&1h%+g!o2s&ss6^i6p^')
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'
ALLOWED_HOSTS = [
    '.vercel.app',  # Allows all Vercel subdomains
    'localhost',
    '127.0.0.1',
    'dd-tours.vercel.app',  # Your Vercel domain
]

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'trvels' / 'static']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # For Whitenoise

# Database (configure with environment variables for security)
import os
print("Loading DD_Tours/settings.py START")



print("DATABASES set to:", DATABASES)

# Ensure Whitenoise is configured correctly
# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django_otp',
    'django_otp.plugins.otp_email',
    'trvels',
]



AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]





ROOT_URLCONF = 'DD_Tours.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

# <<<<<<< HEAD
# WSGI
# WSGI_APPLICATION = 'DD_Tours.wsgi.application'

# # Database
# # import os

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / "db.sqlite3",  # Check this path
#     }
# }


# Authentication & Allauth Settings

WSGI_APPLICATION = 'DD_Tours.wsgi.application'


SITE_ID = 1
ACCOUNT_LOGIN_METHODS = {'email'}
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
LOGIN_REDIRECT_URL = '/'

# ACCOUNT_EMAIL_VERIFICATION = 'none'


ACCOUNT_EMAIL_VERIFICATION = 'optional'  # Recommended to use 'mandatory' in production
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': "",
            'secret': "",
            'key': ''
        }
    }
}

# Password Validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True



# STATIC_ROOT = BASE_DIR / 'staticfiles'  # Add this for production deployments

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email Configuration

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST = 'smtp.gmail.com'

# EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
# EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")  # Keep password secret
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# DEFAULT_TO_EMAIL = '@gmail.com'

# Contact Email
# CONTACT_EMAIL = 'gohilpratishtha57@gmail.com'

AUTH_USER_MODEL = 'trvels.CustomUser'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'pratishthabagohil.21.ce@iite.indusuni.ac.in'
EMAIL_HOST_PASSWORD = 'priti2103'# Default Auto Field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Security Enhancements
SECURE_SSL_REDIRECT = os.environ.get('SECURE_SSL_REDIRECT', 'False') == 'True'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

DEBUG = True

