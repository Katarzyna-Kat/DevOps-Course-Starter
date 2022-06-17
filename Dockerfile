FROM python:3.10.3-slim-buster as base
COPY . /app/
WORKDIR /app
RUN pip install poetry
RUN poetry install

FROM base as production
EXPOSE 80
RUN chmod +x ./gunicorn.sh
ENTRYPOINT ["./gunicorn.sh"]

FROM base as development
EXPOSE 5000
ENTRYPOINT ["sh", "./flask.sh" ]

FROM base as test
ENV PATH = "${PATH}:/root/todo_app"
ENTRYPOINT ["poetry", "run", "pytest"]
CMD ["todo_app"]