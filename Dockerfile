FROM python:3.10.3-slim-buster as base
RUN apt-get update
COPY . /opt/
WORKDIR /opt
RUN pip install poetry
RUN poetry install

FROM base as production
EXPOSE 80
RUN chmod +x /opt/gunicorn.sh
ENTRYPOINT ["/opt/gunicorn.sh"]