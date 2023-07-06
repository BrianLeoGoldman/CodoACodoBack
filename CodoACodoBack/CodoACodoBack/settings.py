"""
Django settings for CodoACodoBack project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

BASE_URL = 'http://127.0.0.1:8000'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%@j0qgiv_jwvsbun9@ff9t%f=7)4mcp+ww@4n7*+1$p3x1-ngo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'marylu',
    'prueba'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware', 
    # TODO: descomentar el middleware CsrfViewMiddleware
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CodoACodoBack.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'CodoACodoBack.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = { 
    'default': { 
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'codo-a-codo', 
        'USER': os.environ.get('POSTGRESQL_USER', ''), 
        'PASSWORD': os.environ.get('POSTGRESQL_PASSWORD', ''), 
        'HOST': '127.0.0.1', 
        'PORT': os.environ.get('POSTGRESQL_PORT', ''), 
    } 
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es-eu' # en-us

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_WHITELIST = ['http://127.0.0.1:5500']
# TODO: cambiar el localhost por la url una vez hecho el deployment
CORS_ALLOW_METHODS = ['GET', 'POST']

# Configuración del servidor de correo saliente (SMTP)
""" 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Reemplaza con la dirección del servidor SMTP
EMAIL_PORT = 587  # Reemplaza con el puerto del servidor SMTP
EMAIL_USE_TLS = True  # Usar TLS para cifrar la conexión (recomendado)
EMAIL_HOST_USER = 'coderbebop@gmail.com'  # Reemplaza con tu dirección de correo electrónico
EMAIL_HOST_PASSWORD = 'heladito'  # Reemplaza con tu contraseña de correo electrónico
"""

# Configuración adicional (opcional)
""" 
EMAIL_SUBJECT_PREFIX = '[Marylu]'  # Prefijo opcional para los asuntos de los correos electrónicos
DEFAULT_FROM_EMAIL = 'coderbebop@gmail.com'  # Dirección de correo electrónico predeterminada para los correos salientes 
"""
