"""
Django settings for intra project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/ im pull this on main
"""

from pathlib import Path
import os
from storages.backends.sftpstorage import SFTPStorage

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@+(msxey(!#4z&x(2lmv2&cpt$r=&1@xyt5*u6*j64j!pf74d&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost','127.0.0.1','34.124.183.52','hub.ttvision-tech.com','www.hub.ttvision-tech.com']

#DEFAULT_FILE_STORAGE = 'storages.backends.sftpstorage.SFTPStorage'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'homebase',
    'trvrequest',
    'itasset',
    'labassets',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'intra.urls'

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
                'intra.context_processors.context',
            
            ],
        },
    },
]

WSGI_APPLICATION = 'intra.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
   'default':{
       'ENGINE':'mssql',
       'NAME':'ttvintra',
       'USER':'root',
       'PASSWORD':'123456',
       #'HOST':'1.9.119.137\SQLEXPRESS,2433',
       'HOST':'DESKTOP-MER2ENS\SQLEXPRESS',
       #'HOST':'10.10.150.250\SQLEXPRESS',
       'OPTION':{
           'drive':'ODBC Driver 17 for SQL Server',
       },
       'extra_params':'PORT=1433'
   }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


DATE_INPUT_FORMAT = ['%Y-%m-%d',      # '2006-10-25'
                    '%m/%d/%Y',       # '10/25/2006'
                    '%m/%d/%y']       # '10/25/06'

DATE_FORMAT = "d/m/y"

DATETIME_INPUT_FORMATS = ['%d/%m/%Y %H:%M']     # '25/10/2006 14:30'


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

SFTP_STORAGE_HOST = '10.10.150.250'
SFTP_STORAGE_ROOT = '/SFTP_Root'
SFTP_STORAGE_PARAMS = {
    'username': 'ttvhub',
    'password': '123456',
    'port':'22',
}


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

VENV_PATH = os.path.dirname(BASE_DIR)
STATIC_ROOT = os.path.join(VENV_PATH, 'static_root')
MEDIA_ROOT = os.path.join(VENV_PATH, 'media_root')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# MSAL ms_identity_web middleware configs
from ms_identity_web.configuration import AADConfig
from ms_identity_web import IdentityWebPython
AAD_CONFIG = AADConfig.parse_json(file_path='aad.config.json')
MS_IDENTITY_WEB = IdentityWebPython(AAD_CONFIG)
ERROR_TEMPLATE = 'auth/{}.html' # for rendering 401 or other errors from msal_middleware
MIDDLEWARE.append('ms_identity_web.django.middleware.MsalMiddleware')
