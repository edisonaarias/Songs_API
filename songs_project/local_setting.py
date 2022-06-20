# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-clb24l^jlc8pl*7sp#s5t3k41dxl(-ueg71xz+-7wj))(@dx!1'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'songs_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '555429ea'
    }
}