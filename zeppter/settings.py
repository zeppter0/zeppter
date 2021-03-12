"""
Django settings for zeppter project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
BASE_DIR = Path(__file__).resolve().parent.parent

'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myzeppter',
        'USER': 'dkboss650',
        'PASSWORD': 'Sorry9023@',
        'HOST': 'localhost',
        'PORT': '',


    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'zeppter',
        'USER': 'dkboss650',
        'PASSWORD': 'Sorry9023@',
        'HOST': 'localhost',
        'PORT': '',
    } 
    
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from admin_dashboard import apps

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from pathlib import Path

#BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a9u^k1a3@8%33v1^hj&@c0do%npc$(r$it4#%w=g2vs%0vzzxe'

# SECURITY WARNING: do3qn't run with debug turned on in production!
DEBUG = True
APPEND_SLASH=False

ALLOWED_HOSTS = [
    # "103.138.96.225",
    # "192.168.42.211"
    "www.zeppter.com",
    "192.168.1.107",
    'zeppter.com'
    "18.215.82.54",
    '127.0.0.1',
    'eb5ea0c1323fc679c30dbad2a88da814.zeppter.com',

    
    

]
BASE_URL = 'http://www.zeppter.com'

# Application definition

INSTALLED_APPS = [

    'dashboard.apps.DashboardConfig',
    'admin_dashboard.apps.AdminDashboardConfig',
    'comment.apps.CommentConfig',
    "teacher",
    "students",





    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.sitemaps',
'myuser',


]
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'zeppter.urls'
#AUTH_USER_MODEL = 'register.MyUser'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',

            ],
        },
    },
]

WSGI_APPLICATION = 'zeppter.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {


    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'zeppter',
        'USER': 'dkboss650',
        'PASSWORD': 'Sorry9023@',
        'HOST': 'localhost',
        'PORT': '',
    }

}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),

]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'media/'

SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))
TEMPLATE_DIRS = (
    os.path.join(SETTINGS_PATH, 'template'),
)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ zeppter }}.settings")
