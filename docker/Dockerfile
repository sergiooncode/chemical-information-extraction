FROM chemical-extraction-backend-base as base

COPY . /chemical-extraction-backend

WORKDIR /chemical-extraction-backend
COPY ./public/wsgi.py ./wsgi.py

COPY ./docker/deployment/uwsgi.ini /etc/uwsgi/conf.d/uwsgi.ini
COPY ./docker/deployment/entrypoint.sh /tmp/entrypoint.sh

FROM base as dev

ENTRYPOINT ["sh", "/tmp/entrypoint.sh"]
CMD ["uwsgi", "--ini", "/etc/uwsgi/conf.d/uwsgi.ini"]
