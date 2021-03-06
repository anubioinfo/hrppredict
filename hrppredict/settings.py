"""
Django settings for hrppredict project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&jb(q9f91luq=$v+#9olsx0xfj5%un^ozjq7##eby&1wk@o79z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hrp'
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

ROOT_URLCONF = 'hrppredict.urls'

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

WSGI_APPLICATION = 'hrppredict.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# For demo purpose I have defined these as constant variables. We can pick them from database later.
NORMAL = '''Your prediction is <b>normal</b> !<br/>'''

HRP = '''Your prediction is showing that there may be a chance of <b>High Risk Pregnancy </b>but 
still is is just a prediction so take 
proper care and follow following instructions to avoid such situations.<br/>'''

LOW_HB = '''<br/>Seems your hemoglobin level is low than normal. Please do following to increase it:<br/>
- Eat Iron-Rich Foods like  red meat, shrimp, tofu, spinach, almonds, dates, lentils, fortified breakfast cereals and 
almonds <br/>
- You can also take an iron supplement. Consult your doctor for the correct dosage as high doses of iron can be harmful
 to your body. <br/>
- Increase Vitamin C Intake like papaya, oranges, lemon, strawberries and tomatoes. <br/>
- Take Folic Acid. Some good food sources of folic acid are green leafy vegetables, liver, rice, sprouts, dried beans, 
wheat germ, fortified cereals, peanuts and bananas <br/>
- An apple a day can help maintain a normal hemoglobin level.<br/> 
'''

HIGH_BP = '''<br/>Seems your blood pressure is higher than normal so you need to do following: <br/>
- Avoid salt and high-sodium foods.<br/>
- Foods you should add include sweet potatoes, tomatoes, kidney beans, orange juice, bananas, peas, potatoes, dried 
fruits and melon.<br/>
- Try to exercise for at least 30 minutes a day or most days throughout the week.<br/>
- Monitor your weight.<br/>
- Reduce stress.<br/>
'''