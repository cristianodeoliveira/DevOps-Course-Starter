FROM python:3
RUN curl -sSL https://install.python-poetry.org | python3 -
COPY . /app
WORKDIR /app
ENV PATH=$PATH:/root/.local/share/pypoetry/venv/lib/python3.12/site-packages/poetry
RUN pip install poetry
ENTRYPOINT poetry run flask run