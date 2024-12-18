# Making queries

## Reference

- https://docs.djangoproject.com/en/5.1/topics/db/queries/

## pyenv

```sh
pyenv install 3.12.3
pyenv global 3.12.3
```

## poetry

```sh
python -m pip install poetry
```

## Activate virtual environment

```sh
poetry shell
source .venv/bin/activate
```

## Install packages

```sh
poetry install
```

## Run migrations

```sh
python manage.pr migrate
```

## Run server

```sh
python manage.py runserver
```

## ruff

```sh
python -m ruff format
python -m ruff check --fix
```
