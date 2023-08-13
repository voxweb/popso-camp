FROM python:3.10.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ="Europe/Moscow"

WORKDIR /app

# install dependencies
COPY ./backend/ /app
RUN pip install -r requirements.txt

# run entrypoint.sh
COPY ./docker/bash/ /app/bash/
RUN ["chmod", "+x", "/app/bash/entrypoint.sh"]
ENTRYPOINT ["sh", "/app/bash/entrypoint.sh"]