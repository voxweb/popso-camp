# popso-camp

## Запуск приложения(локальная разработка)

- Создать .env файл в корне проекта и записать в него следующие данные:

```
    APPLICATION_DEBUG_MODE=1                               # включает режим dеbug
    
    REDIS_HOST=redis                                       # Redis хост
    REDIS_PORT=6379                                        # Redis порт    
    REDIS_DATABASE=0                                       # Redis номер базы данных
    REDIS_PASSWORD=your_secret_password                    # Redis пароль
    
    CELERY_BROKER_URL=redis://redis:6379/1                 # Celery broker url
    CELERY_RESULT_BACKEND=redis://redis:6379/1             # Celery result backend url
    
    DJANGO_SECRET_KEY=your_secret_key                      # Django подпись
```
- Создать виртуальное окружение
```python -m venv venv```

- Активировать виртуальное окружение
```source django_env/bin/activate``` - для Linux и MacOS
```venv\Scripts\activate``` для Windows

- Запустить docker compose командой: ```docker compose up -d```
