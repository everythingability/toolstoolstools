"""
Django settings for toolstoolstools project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'seuj2&zwro$%ifqx3lyr513m#639)edj4i^4(*e0_i=l&sp1r8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', ]

# https://github.com/adamchainz/django-cors-headers
CORS_ORIGIN_ALLOW_ALL = True
'''CORS_ORIGIN_WHITELIST = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000"
]'''

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.staticfiles',
    'tools',
    'django.contrib.admin',     
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    
     'tinymce',
    
      'accounts',
    
]

MIDDLEWARE = [
      'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
   
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'toolstoolstools.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'toolstoolstools.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '.data/db.sqlite3'),
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

LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'GMT'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_ROOT = BASE_DIR + "/static"

STATIC_URL = '/static/'

STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'admin')
]
print("STATIC_ROOT", STATIC_ROOT)

MEDIA_ROOT = BASE_DIR + "/uploads"
MEDIA_URL = "/uploads/"

# https://django-tinymce.readthedocs.io/en/latest/usage.html

TINYMCE_DEFAULT_CONFIG = {
        'theme': "advanced", # default value
        'content_style': ".mceContentBody {font-size:18px;font-family: 'HelveticaNeue-Light', 'Helvetica Neue Light', 'Helvetica Neue', Helvetica, Arial, 'Lucida Grande', sans-serif; }",

        'relative_urls': False, # default value
        'plugins': 'table,spellchecker,paste,searchreplace',
        'theme_advanced_buttons1': 'bold,italic,underline,bullist,numlist,link,unlink,styleselect,fontselect,fontsizeselect, code',
        'width': '800',
        'height': 300,
        'paste_text_sticky': True,
        'paste_text_sticky_default': True,
        'valid_styles': 'font-weight,font-style,text-decoration',
        'fontsize_formats': "14pt 16pt 18pt 20pt 24pt 36pt 48pt 56pt",
        'font_formats': "Andale Mono=andale mono,times;" +
            "Arial=arial,helvetica,sans-serif;" +
            "Arial Black=arial black,avant garde;" +
            "Book Antiqua=book antiqua,palatino;" +
            "Comic Sans MS=comic sans ms,sans-serif;" +
            "Courier New=courier new,courier;" +
            "Georgia=georgia,palatino;" +
            "Helvetica=helvetica;" +
            "Impact=impact,chicago;" +
            "Symbol=symbol;" +
            "Tahoma=tahoma,arial,helvetica,sans-serif;" +
            "Terminal=terminal,monaco;" +
            "Times New Roman=times new roman,times;" +
            "Trebuchet MS=trebuchet ms,geneva;" +
            "Verdana=verdana,geneva;" +
            "Webdings=webdings;" +
            "Wingdings=wingdings,zapf dingbats",
    }
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True
