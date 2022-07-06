# Python Flask Backend

This is the application Flask application, which is containerized with tests.

- Built in Python version 3.9.7
- Uses [Uses Flask](https://flask.palletsprojects.com/en/2.1.x/) as the server backend.
- Uses [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/) for UI development.
- Uses [Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/) for handling migrations.
- Uses [Flask WTForms](https://flask.palletsprojects.com/en/2.1.x/patterns/wtforms//) for the web forms.
- Uses [PyTest](https://docs.pytest.org/en/7.1.x/) for our testing framework.
- Uses [Makefile](https://makefiletutorial.com/) to execute commands

# Structure

## src
- The `src` folder contains the source code of project and the technical test.

## tests
- The `tests` folder contains the tests for the system.

## Dockerfile and docker-compose.yaml
- The `Dockerfile` and `docker-compose.yaml` are the files which containerizes the application.

## Running the project
- Create a virtual environment, then install the package dependencies using command `pip install -r requirements.txt`
- After creating the virtaul environment and installing the packages start a `postgres` and `pgadmin4` docker images using `make up` command. This will start the `postgres database` used as the database for the application.
- To run the `application` run the command `make server`. This will start the flask app on port `5000` which can be accessed on the browser through `http://127.0.0.1:8000`.
- After accessing the website, create an account and run the scipts in `data.sql` to populate the database with data from `PGAdmin 4` web browser.
- To access the `PGAdmin 4` on the browser access the URL `http://localhost:5050/browser/` then create a server with the database credentials in `.env` file.
  
## Running the tests
- To run tests, first create a variable on `.env` `TESTING` and set its value to `1`, then execute the command `make test`. When the value of testing is `0` then we are under development.