FROM python:3.8-alpine3.11 as base

COPY . /chemical-extraction-backend

WORKDIR /chemical-extraction-backend
COPY ./public/wsgi.py ./wsgi.py

RUN apk update && \
    apk add gcc \
    build-base \
    linux-headers \
    python3-dev \
    libressl-dev \
    musl-dev \
    libffi-dev \
    libxml2-dev \
    libxslt-dev

RUN pip install poetry
RUN POETRY_VIRTUALENVS_CREATE=false poetry install --no-dev

COPY ./docker/deployment/uwsgi.ini /etc/uwsgi/conf.d/uwsgi.ini
COPY ./docker/deployment/entrypoint.sh /tmp/entrypoint.sh

FROM base as production

ENTRYPOINT ["sh", "/tmp/entrypoint.sh"]
CMD ["uwsgi", "--ini", "/etc/uwsgi/conf.d/uwsgi.ini"]

FROM base as dev

RUN POETRY_VIRTUALENVS_CREATE=false poetry install
CMD ["uwsgi", "--ini", "/etc/uwsgi/conf.d/uwsgi.ini"]
