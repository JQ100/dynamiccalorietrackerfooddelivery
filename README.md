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
## Database Documentation

### Overview
This database is structured to hold and manage personal information, dietary details, meal records, and a comprehensive collection of recipes. The design incorporates a separation of personal details from other personal data for enhanced security. The system is capable of tracking daily caloric intake by documenting meal consumption and aggregating total calories consumed per day.

### Tables Description

#### PersonalDetails
- `detail_id`: INT(10), Primary Key. A unique identifier for each personal detail record.
- `weight`: DECIMAL(5, 2). Records the weight of the individual.
- `Height`: DECIMAL(6, 1). Records the height of the individual.
- `date_of_birth`: DATE. Captures the birth date.
- `gender`: VARCHAR(25). Indicates the gender.
- `bmi`: DECIMAL(5, 2). Body Mass Index.
- `username`: VARCHAR(255). Chosen username for account identification.
- `password_hash`: VARCHAR(128). The hashed password for security.
- `password_salt`: VARCHAR(32). The salt used in conjunction with the hashed password.

#### PersonalData
- `data_id`: INT(10), Primary Key. Unique identifier for each personal data record.
- `detail_id`: INT(10), Foreign Key. Links to `PersonalDetails`.
- `daily_calorie_goal`: INT(10). The individual's target for daily caloric intake.
- `consumed_calorie`: INT(10). Total calories consumed on a given date.
- `today_date`: DATE. The date corresponding to the calorie data.

#### MealRecord
- `meal_id`: INT(10), Primary Key. Unique identifier for each meal record.
- `personal_data_id`: INT(10), Foreign Key. Links to `PersonalData`.
- `Recipes_id`: INT(10), Foreign Key. Links to `Recipes`.
- `date`: DATE. The date on which the meal was consumed.

#### Recipes
- `recipes_id`: INT(10), Primary Key. Unique identifier for each recipe.
- `name`: VARCHAR(64). Name of the recipe.
- `Ingredient`: INT(10). Presumed to be a foreign key to an ingredients table (if intended to store actual ingredients, this should be VARCHAR or TEXT).
- `recipes`: VARCHAR(4096). The recipe instructions.
- `nutritional_data`: VARCHAR(512). Nutritional information for the recipe.
- `link`: VARCHAR(512). A hyperlink to the recipe's source.

### Security Considerations
Sensitive details such as usernames and passwords are stored in a separate table (`PersonalDetails`) and are protected using hashing and salting techniques. This separation helps to safeguard the data against unauthorized access.

### Functional Operations
The database is set up to track and manage users' daily caloric intake efficiently. When a user logs a meal into the `MealRecord` table, it records their meal along with the corresponding date and recipe. The `consumed_calorie` field in the `PersonalData` table is then updated to reflect the daily total calorie intake.

### SQL Trigger for Consumed Calories

The following SQL trigger is designed to update the `consumed_calorie` field in the `PersonalData` table whenever a new entry is added to the `MealRecord` table:

```sql
DELIMITER $$

CREATE TRIGGER UpdateConsumedCalories
AFTER INSERT ON MealRecord
FOR EACH ROW
BEGIN
    DECLARE total_calories INT;

    SELECT SUM(r.nutritional_data) INTO total_calories
    FROM MealRecord AS m
    JOIN Recipes AS r ON m.Recipes_id = r.recipes_id
    WHERE m.date = NEW.date AND m.personal_data_id = NEW.personal_data_id;

    UPDATE PersonalData
    SET consumed_calorie = total_calories
    WHERE data_id = NEW.personal_data_id AND today_date = NEW.date;
END$$

DELIMITER ;

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
- [Learn Flask for Python - Full Tutorial](https://youtu.be/Z1RJmh_OqeA?si=RZDIhkaCRJwQjdLJ&t=1182). A video about database models and REST API.
- [Modular Applications with Blueprints](https://flask.palletsprojects.com/en/2.0.x/blueprints/). Check out the section "Blueprint Resources".
