from pathlib import Path



# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key secret in production!
SECRET_KEY = 'django-insecure-your-dev-secret-key-here'

# DEVELOPMENT SETTINGS
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

    'dashboard',  # your custom app
    'tailwind',
    'theme',  # <- You’ll create this in step 4


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

ROOT_URLCONF = 'mydashboard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # You can set template dirs if needed
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

WSGI_APPLICATION = 'dashboard.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
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
TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
]
# Language and Time
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'  # or your local timezone
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JS, images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#LOGIN_REDIRECT_URL = '/'        # After successful login
LOGOUT_REDIRECT_URL = '/login/'  # After logout

LOGIN_REDIRECT_URL = '/dashboard/chart/'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'admin@mydashboard.com'
