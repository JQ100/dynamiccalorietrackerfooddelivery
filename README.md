# Introduction

This is the repo for Dynamic Calorie Tracker project

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

# How To Run
1. Install `virtualenv` if it is not installed:
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

5. Set the environment variable FLASK_APP. The following command is for the project dynamic_calorie_tracker.
```
$ (env) export FLASK_APP=dynamic_calorie_tracker
```

6. Finally start the web server:
```
$ (env) flask run
```

This server will start on port 5000 by default. You can change this in `app.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```

# Todo
* Hold knowledge sharing sessions. Record zoom videos.
* May rename the repo dynamic_calorie_tracker
* use camel format for file and variable names
* use db migrate to create and populate the db. Use "flask db init" to create db.

# Tutorials
* [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/) for writing README.md.
