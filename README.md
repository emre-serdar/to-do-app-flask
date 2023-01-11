# to-do-app-flask
A simple to do web app with Flask and SqlAlchemy.

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/emre-serdar/to-do-app-flask.git
$ cd to-do-app-flask
```

Then install the dependencies:

```sh
$ pip install flask
$ pip install Flask-SqlAlchemy
```
Once `pip` has finished downloading the dependencies. Go to Flask shell to create a table in the database:
```sh
$ flask shell
>>> from app import db
>>> db.create_all()
```
To run:
```sh
$ export FLASK_APP=app
$ export FLASK_ENV=development
$ flask run
```
And navigate to `http://localhost:5000/`.

<img src="https://github.com/emre-serdar/to-do-app-flask/blob/main/flask-to-do.png" />
