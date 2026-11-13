# Ссылка на задание 

https://github.com/avito-tech/python-trainee-assignment

# Структура проекта

    Python
    ├─── Test.py
    └─── spiralmatrix
         ├─── __init__.py
         └─── code.py

# Запуск проекта

## Требования для запуска:
1) Python 3.12.8 или выше
2) aiohttp

## Как запустить

1) Клонирование репозитория
    git clone 
    
    https://github.com/UzerName6666/Python.git

2) Перейти в директорию с репозиторием

        cd Python

3) Запустить тестирование

        python test.py

## Возможные ошибки

### Отсутствует библиотека 'aiohttp'

    ModuleNotFoundError: No module named 'aiohttp'

Решение: Установить aiohttp или сменить версию Python

    python.exe pip install aiohttp

### Ошибки при проведении тестирования

    Не пройден: Ошибка сети/HTTP: Cannot connect to host raw.githubusercontent.com:443 ssl:default [getaddrinfo failed]

Возможно отсутствует подключение к Github. В случае возникновения такой ошибки сначала требуется проверить подключение к сети и настройки фаервола