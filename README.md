# drf-light-test

Перед запуском нужно скорректировать данные о БД в файлах settings.py и docker-compose.yml.


    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'db_django',
            'USER': 'root',
            'PASSWORD': 'password',
            'HOST': 'HOST',
            'PORT': PORT,
        }
    }


    MYSQL_DATABASE: 'db_django'
    MYSQL_USER: 'root'
    MYSQL_PASSWORD: 'password'
    MYSQL_ROOT_PASSWORD: 'password'

Собираем и запускаем контейнеры командами 

    docker-compose build
    docker-compose up -d