# helloworld-debug-flask

Simple helloworld python flask application configured for debugging with debugpy &amp; Docker

## Install virtual environment with project dependencies

```sh
    pyenv install 3.8.5
    pyenv virtualenv 3.8.5 helloworld-debug-flask
    pyenv activate helloworld-debug-flask
    pip install --upgrade pip
    pip install -r requirements-dev.txt
```

## Run automatic code linting in files

```sh
    black . -l 79 # maximum line length 80
```

## Upgrade project dependencies

```sh
    pip install -r requirements.in
    pip-compile --generate-hashes --allow-unsafe --output-file="requirements.txt" requirements.in
```

## Run project in docker

```sh
    docker build --rm --pull -f "./Dockerfile" -t "helloworlddebugflask:latest" "./"
```

## Test endpoint

```sh
    curl --insecure http://localhost:5000
```
