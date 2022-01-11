from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "+2-r!5r*sr31ac-3awm@e^%4+&5=dcvambg1e*e5-=5g$5w5lu"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = [
    "jmplibrary.com",
    "www.jmplibrary.com",
    "localhost",
    "127.0.0.1",
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "home",
    "main",
    "account",
    "library",
    "entities",
    "crispy_forms",
    "django_countries",
    "paypal.standard.ipn",
    "django_extensions",
]

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "lms.urls"

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

WSGI_APPLICATION = "lms.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'JMP',
#        'USER': 'JMP_User',
#        'HOST': 'jmplibrary.com',
#        'PORT': '3306',
#       'PASSWORD': 'S0m4Vit4b00',
#    }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# STATIC_URL = "/static/"
STATIC_URL = "/staticfiles/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

CRISPY_TEMPLATE_PACK = "bootstrap4"

LOGIN_REDIRECT_URL = "home:libraries"


STRIPE_PUBLIC_KEY = "pk_test_epUupxLsRwt7QNm2aiDE7Wa800fTNMCkBH"

STRIPE_PRIVATE_KEY = "sk_test_pNre034ewYPh6rm8OK5MPUYm005DbF1Ivd"

PAYPAL_TEST = False
PAYPAL_RECEIVER_EMAIL = "vrepublics@gmail.com"

fedex_test_key = "3kWyadILwhnan9fW"
Test_FedEx_Office_Integrator_ID = 123
Test_Client_Product_ID = "TEST"

Test_Client_Product_Version = 9999
