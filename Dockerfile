FROM python:3 AS base
RUN curl -sSL https://install.python-poetry.org | python3 -
#Optimized version of the dockerfile
ENV PATH=$PATH:/root/.local/bin/
WORKDIR /app
COPY pyproject.toml poetry.toml /app/
RUN poetry install
#COPY . /app
COPY todo_app /app/todo_app

# Configure for production
FROM base AS production
ENV FLASK_DEBUG=false
ENTRYPOINT poetry run flask run --host 0.0.0.0

# Configure for local development
FROM base AS development
ENV FLASK_DEBUG=true
ENTRYPOINT poetry run flask run --host 0.0.0.0

# Setting up test container
FROM base as test
ENTRYPOINT poetry run pytest