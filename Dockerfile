FROM python:3.10.3-slim-buster as base
COPY . /app/
WORKDIR /app
RUN pip install poetry
RUN poetry config virtualenvs.create false --local && poetry install

FROM base as development
EXPOSE 5000
ENTRYPOINT ["sh", "./flask.sh" ]

FROM base as test
ENV PATH = "${PATH}:/root/todo_app"
ENTRYPOINT ["poetry", "run", "pytest"]
CMD ["todo_app"]

FROM base as production
EXPOSE 80
RUN chmod +x ./gunicorn.sh
CMD poetry run gunicorn "todo_app.app:create_app()" --bind 0.0.0.0:${PORT:-80}