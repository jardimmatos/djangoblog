from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'dev65dcyy7%(gfkn%9g(f4d_@%h&61r@xfme1%zgl4bc#$%wm^#'
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    #{ 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    #{ 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    #{ 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    #{ 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Fortaleza'
USE_TZ = False
STATIC_URL = '/static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

