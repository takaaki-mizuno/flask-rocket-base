# How to setup project

This project uses `pyproject.toml` proposed on [PEP-0518](https://www.python.org/dev/peps/pep-0518/#specification) instead of `requirements.txt`. And you can use [Poetry](https://python-poetry.org/). 

## 1. Setup python 3.8.x environment with `pyenv` and install Poetry

- Install [pyenv](https://github.com/pyenv/pyenv)
- Install latest version of python 3.8.x and use it.

```
pyenv install 3.8.0
pyenv local 3.8.0
```

- Install [Poetry](https://python-poetry.org/)

```
pip3 install poetry
```

- Install dependency

```
poetry install
```

- Run server

```
poetry run python manage.py run
```
