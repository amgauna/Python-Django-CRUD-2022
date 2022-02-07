INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app'
]


# Dentro do arquivo de configurações precisamos setar o novo banco de dados:

STATIC_ROOT = os.path.join(BASE_DIR, 'static') [
'ENGINE': 'django.db.backends.mysql',
'NAME': "testa",
'HOST': 'localhost',
'USER': 'root',
'PASSWORD': '',
'PORT': '3306',
'OPTIONS': { 'init_command': 'SET default_storage_engine=InnoDB', }
]
