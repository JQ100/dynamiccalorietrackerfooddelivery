# Introduction

This is the repo for Dynamic Calorie Tracker project

# How To Run
1. Install `virtualenv`:
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

5. go to the project directory or your blue print directory. Do nothing if you are already in the directory.
```
$ (env) cd my_project
```

6. Set the environment variable FLASK_APP. The following command is for the project DynamicCalorieTracker.
```
$ (env) export FLASK_APP=DynamicCalorieTracker.py
```

7. Finally start the web server:
```
$ (env) flask run
```

This server will start on port 5000 by default. You can change this in `app.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```
