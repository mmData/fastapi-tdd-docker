# About this application
It is entirely based on the course https://testdriven.io/courses/tdd-fastapi/getting-started/ with changelog 1.2.0

## Running the Docker container
First we have to make the file project/entrypoint.sh executable:
- `chmod +x project/entrypoint.sh`
Then we build:
- `docker-compose build`
Run the container (erase the d to not be in detached mode):
- `docker-compose up -d`  
check:
- `http://localhost:5004/ping`

To do the build and run in one commands:
- `docker-compose up -d --build`

To bring down the container and volume:
- `docker-compose down -v`

## Checking the logs
- `docker-compose logs web`

## Access Database with psql
- `docker-compose exec web-db psql -U postgres`
Then:
- `\c web_dev`
- `\q`

## Running the tests
With the container up and running execute:
- `docker-compose exec web python -m pytest`

## Running the app without Docker
- `uvicorn app.main:app --port 5000`
To enable autoreload:
- `uvicorn app.main:app --port 5000 --reload`
Or:
- `python3 app/main.py`

## Heroku

Log in to Heroku Container Registry:
- `heroku container:login`
Provision a new Postgres database with the hobby-dev plan:
- `heroku addons:create heroku-postgresql:hobby-dev --app <app-name>`

# To Do
- Create cli.sh
- add proper logging
- add prometheus endpoints