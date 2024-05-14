FROM python:3
RUN curl -sSL https://install.python-poetry.org | python3 -
COPY . /app
WORKDIR /app
ENV PATH=$PATH:/root/.local/bin/
RUN pip install poetry
RUN poetry install
ENTRYPOINT poetry run flask run --host 0.0.0.0