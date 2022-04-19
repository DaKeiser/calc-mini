<h1 align="center">Calculator using Devops pipeline</h1>

> Developed as a part of CS 816 - Software Production Engineering course.

## Install

```sh
git clone git@github.com:DaKeiser/calc-mini.git
cd calc-mini
pip install pipenv
```

## Demo

```sh
nc 40.81.233.44 6969
```

## Build Code

```sh
pipenv run build
```

## Run the server

```sh
pipenv run start
```

## Connect to server

```sh
nc <server_ip> 6969
```

## Run Tests

```sh
pipenv run test
```

## Docker Development

```sh
docker build -t keiserdocker:calc_pip:latest .
docker run -p "6969:6969" -it keiserdocker:calc_pip:latest
```

## Pipeline

Find the docker image on https://hub.docker.com/r/keiserdocker/minicalc

## App Demo

Demo video with simultaneous 2 client setup

<a href="https://asciinema.org/a/ZUSgiPsAlateIn7KEEBPRbjxn" target="_blank"><img src="https://asciinema.org/a/ZUSgiPsAlateIn7KEEBPRbjxn.svg" /></a>