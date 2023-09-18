# fastapi-example

Example of a simple FastAPI application, with a Postgres DB in a Docker Container.
Based on: https://fastapi.tiangolo.com/tutorial/sql-databases/#sql-relational-databases

## Prerequisites

Before running the application it is recommended to set up a virtual environment.

1. In PyCharm, press `CTRL + ALT + S`.
2. Navigate to `Project > Python Interpreter`.
3. Click on `Add interpreter` and configure Python 3.11 or higher.

## Running the application locally

To start a local database, run the following commands:

1. Run `docker run -p 5432:5432 --name postgres -e POSTGRES_USER=user -e POSTGRES_PASSWORD=mysecretpassword -d postgres`
   to start a container.

Then, to run the application:

1. First install dependencies by running `pip install -r requirements.txt`.
2. Then, from the root folder, start the application by running `python .\main.py`.
3. Go to `localhost:8000`.

The uvicorn server will start automatically.

## Nox usage

Nox is a command-line tool that automates testing in Python environments. In this project it is
used to evaluate code quality and complexity, check typing, run tests, and format code.

### Running all Nox sessions

To run all Nox sessions, simply run `nox` in the project directory.

### Formatting project code

To perform formatting using isort and autoflake, run `nox --sessions format`.
This will only run the formatting session.

### Running tests and coverage

To run all unit tests and check code coverage, run `nox --sessions test`.

### Evaluating code complexity

To evaluate code complexity, run `nox --sessions complexity`.
