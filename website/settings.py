#!/usr/bin/env python
# encoding:utf-8
"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from yaml import load

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

YAML_CONFIG_FILE = BASE_DIR+'/config.yml'


class Conf(object):
    '''
    说明： 该类是映射配置文件为对象
    '''

    def __init__(self):
        with open(YAML_CONFIG_FILE,
                  'r') as stream:
            self.yaml = load(stream)

    def __getattr__(self, item):
        get_val = self.yaml.get(item)
        if get_val:
            return type(item, (object,), get_val)
        else:
            raise AttributeError

CONFIG = Conf()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w4(-2s2l+4m(da8=@-6gy39dkpnb2s9g1*58j&=yuop&&s=vk1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', ]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'taggit',
    'blog',
    'core',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'website.urls'

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

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

mysql = CONFIG.mysql

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': mysql.DATABASE,  # Or path to database file if using sqlite3.
        'USER': mysql.USERNAME,
        'PASSWORD': mysql.PASSWORD,
        'HOST': mysql.IP,  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': mysql.PORT,
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

#LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = 'zh-Hans'
#
# TIME_ZONE = 'UTC'
#
# USE_I18N = True
#
# USE_L10N = True
#
# USE_TZ = True


FILE_CHARSET = 'utf-8'
DEFAULT_CHARSET = 'utf-8'

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(os.path.dirname(__file__), "../static/")

STATICFILES_DIRS = (
    ('css', os.path.join(STATIC_ROOT, 'css').replace('\\', '/')),
    ('js', os.path.join(STATIC_ROOT, 'js').replace('\\', '/')),
    ('images', os.path.join(STATIC_ROOT, 'images').replace('\\', '/')),
)
