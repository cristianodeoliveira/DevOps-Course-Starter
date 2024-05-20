FROM python:3 AS base
RUN curl -sSL https://install.python-poetry.org | python3 -
COPY . /app
WORKDIR /app
ENV PATH=$PATH:/root/.local/bin/
RUN poetry install
ENTRYPOINT poetry run flask run --host 0.0.0.0


# Configure for production
FROM base AS production
ENV FLASK_DEBUG=false
ENTRYPOINT poetry run flask run --host 0.0.0.0


# Configure for local development
FROM base AS development
ENV FLASK_DEBUG=true
ENTRYPOINT poetry run flask run --host 0.0.0.0

