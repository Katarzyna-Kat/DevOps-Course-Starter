FROM python:3.10.3-slim-buster as base
COPY . /app/
WORKDIR /app
RUN pip install poetry
RUN poetry install

FROM base as production
EXPOSE 80
RUN chmod +x /opt/gunicorn.sh
ENTRYPOINT ["/home/runner/work/DevOps-Course-Starter/DevOps-Course-Starter/gunicorn.sh"]

FROM base as development
EXPOSE 5000
ENTRYPOINT ["sh", "/opt/flask.sh" ]

FROM base as test
ENV PATH = "${PATH}:/root/todo_app"
ENTRYPOINT ["poetry", "run", "pytest"]
CMD ["todo_app"]