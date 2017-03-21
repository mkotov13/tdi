# Grading Web app

This prototype application allows users to submit answers to questions online and receive instant feedback. A few facts:
 - questions AND answers are stored in a database
 - feedback is available upon submission
 - adding new questions is very easy

# Architecture

The app runs on Flask, a framework for creating web applications using Python. I chose Flask because of a few factors: it's simple to install, simple to use (given basic knowledge of Python), and it's exteremely flexible.

The data is stored using SQLite.

# Installation

## Setting up

##### Clone the repo

```
$ git clone https://github.com/hack4impact/flask-base.git
$ cd flask-base
```

##### Initialize a virtualenv

```
$ pip install virtualenv
$ python -m virtualenv install
```

If the commands above do not get the job done, try the following:

```
$ pip install virtualenv
$ virtualenv -p /path/to/python3.x/installation env
$ source env/bin/activate
```

For mac users it will most likely be
```
$ pip install virtualenv
$ virtualenv -p python3 env
$ source env/bin/activate
```
Note: if you are using a python2.x version, point the -p value towards your python2.x

If you're still not having any luck, please consult the [Flask installation guide](http://flask.pocoo.org/docs/0.12/installation/)

##### (If you're on a mac) Make sure xcode tools are installed

```
$ xcode-select --install
```

#### Flask extensions

If you are on Linux, OS X or Cygwin, install flask and extensions by entering the following commands, one after another:

```
$ flask/bin/pip install flask
$ flask/bin/pip install flask-login
$ flask/bin/pip install flask-openid
$ flask/bin/pip install flask-sqlalchemy
$ flask/bin/pip install sqlalchemy-migrate
$ flask/bin/pip install flask-whooshalchemy
$ flask/bin/pip install flask-wtf
```

These commands will download and install all the packages that will be used by this application.

to create a new database, run the `db_create.py` script, then use `db_upgrade.py` to upgrade the database to the latest version

# Interacting with the app

To boot the app, run the following on the command line:

```
python run.py
```

## Beginning

Once the app is up and running, please navigate to `localhost:5000`

If for some reason you are getting the 401 Unauthorized error, please navigate to `localhost:5000/login`. For more info on logging in, please see below.

## Logging in

Current implementation only supports login via OpenID. The simplest way to obtain an OpenID is by signing up for Yahoo mail (at this point in time, Yahoo is one of the few big websites that supports OpenID).

## Adding questions

Any user is able to add questions. To do so, please navigate to the home page and submit your question via the form.

# Extending current framework

## Making edits to the model - Database Migration

If you have made any edits to any of the models, you must update the database. To do so, please run

```
$ python db_migrate.py
```

This script will save the updated schema while preserving everything that was there before. This way, there is no need to dump and recreate the database with every edit.

# Future directions

## Scoring functions with parameters vs. numbers in a web form

While not currently implemented, the ability to grade functions with parameters can be added on by collecting the code of the function in a web form. Submitting the form would trigger a script that would send the code to a remote server where the function can be executed. Once the script receives the result of the function from the remote server, it would compare it against the right answer stored in the database and produce feedback.

Also, currently the right answer to a question is stored as a field in the Question table in the database. To store multiple pairs of inputs with expected outputs, a separate table could be created. One of the fields in that table would be question_id, a foreign key from the Question table.

## Additional features

Given current architecture, the following extensions/improvements are quite easy to implement

 - categorize students into groups
 - add questions only for a specific group of students
