FROM python:3.8-alpine3.11

COPY . /chemical-extraction-backend

WORKDIR /chemical-extraction-backend

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

COPY pyproject.toml /manager-backend/pyproject.toml
COPY poetry.lock /manager-backend/poetry.lock
RUN pip install poetry
RUN POETRY_VIRTUALENVS_CREATE=false poetry install --no-dev
