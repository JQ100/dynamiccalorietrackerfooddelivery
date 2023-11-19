# Introduction

This is the repo for Dynamic Calorie Tracker project.

- The directory dynamic_calorie_tracker is the main module for the project. We implement code inside this module.
- The file requirements.txt defines the packages for running the service of the project.

# How To Run
1. Install `virtualenv` if it is not installed. It only needs to be installed once, so in most cases you can skip this step.
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ virtualenv env
```

3. Then run the command:
```
$ source ./env/bin/activate
```

4. Then install the dependencies:
```
$ (env) pip install -r requirements.txt
```

5. Create the database in "Create DB" section

6. Set the environment variable FLASK_APP. The following command is for the project dynamic_calorie_tracker.
```
$ (env) export FLASK_APP=dynamic_calorie_tracker
```

7. Finally start the web server:
```
$ (env) flask run
```

# DB

## Create DB
1. Open a terminal in the project root directory and run:
```
$ python
```
2. Run the following in python
```
>>> from dynamic_calorie_tracker import db
>>> from dynamic_calorie_tracker.extensions import db
>>> from dynamic_calorie_tracker import create_app
>>> from dynamic_calorie_tracker.models import *
>>> db.create_all(app=create_app())
```

## Query DB
1. Open a terminal in the project root directory and run:
```
$ sqlite3 dynamic_calorie_tracker/db.sqlite3
```
2. View the tables in DB
```
sqlite> .tables
```
3. View the schema in DB
```
sqlite> .schema
```
4. Run SQL queries
```
sqlite> select * from personal_info;
```

# Todo
- Hold knowledge sharing sessions. Record zoom videos.
    - How to start the server
    - How to use github
    - DB development
    - REST API
    - etc
- use snake format for file and variable names
- use db migrate to create and populate the db. Use "flask db init" to create db.
- May rename the repo

# Tutorials and Knowledge Sharing
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/) for writing README.md.
- [How to Use Flask-SQLAlchemy With Flask Blueprints](https://www.youtube.com/watch?v=WhwU1-DLeVw). A video about Flask code structure and database models.
- [Learn Flask for Python - Full Tutorial](https://youtu.be/Z1RJmh_OqeA?si=RZDIhkaCRJwQjdLJ&t=1182). A video about database models and REST API
