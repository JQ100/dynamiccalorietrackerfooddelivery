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
- `detail_id`: INT, Primary Key. A unique identifier for each personal detail record.
- `weight`: DECIMAL(5, 2). Records the weight of the individual.
- `Height`: DECIMAL(6, 1). Records the height of the individual.
- `date_of_birth`: DATE. Captures the birth date.
- `gender`: VARCHAR(25). Indicates the gender.
- `bmi`: DECIMAL(5, 2). Body Mass Index.
- `username`: VARCHAR(255). Chosen username for account identification.
- `password_hash`: VARCHAR(128). The hashed password for security.
- `password_salt`: VARCHAR(32). The salt used in conjunction with the hashed password.

#### PersonalData
- `data_id`: INT, Primary Key. Unique identifier for each personal data record.
- `detail_id`: INT, Foreign Key. Links to `PersonalDetails`.
- `daily_calorie_goal`: INT. The individual's target for daily caloric intake.
- `consumed_calorie`: INT. Total calories consumed on a given date.
- `today_date`: DATE. The date corresponding to the calorie data.

#### MealRecord
- `meal_id`: INT, Primary Key. Unique identifier for each meal record.
- `personal_data_id`: INT, Foreign Key. Links to `PersonalData`.
- `Recipes_id`: INT, Foreign Key. Links to `Recipes`.
- `date`: DATE. The date on which the meal was consumed.

#### Recipes
- `recipes_id`: INT, Primary Key. Unique identifier for each recipe.
- `name`: VARCHAR(64). Name of the recipe.
- `Ingredient`: INT. Presumed to be a foreign key to an ingredients table (if intended to store actual ingredients, this should be VARCHAR or TEXT).
- `recipes`: VARCHAR(4096). The recipe instructions.
- `nutritional_data`: VARCHAR(512). Nutritional information for the recipe.
- `link`: VARCHAR(512). A hyperlink to the recipe's source.

### Security Considerations
Sensitive details such as usernames and passwords are stored in a separate table (`PersonalDetails`) and are protected using hashing and salting techniques. This separation helps to safeguard the data against unauthorized access.

### Functional Operations
The database is set up to track and manage users' daily caloric intake efficiently. When a user logs a meal into the `MealRecord` table, it records their meal along with the corresponding date and recipe. The `consumed_calorie` field in the `PersonalData` table is then updated to reflect the daily total calorie intake.

### Scheme Of the table
#### `PersonalDetails`
| Field          | Type          | Description                                        |
|----------------|---------------|----------------------------------------------------|
| `detail_id`    | INT(10)       | Primary key. Unique identifier for personal details. |
| `weight`       | DECIMAL(5, 2) | Weight of the individual.                          |
| `Height`       | DECIMAL(6, 1) | Height of the individual.                          |
| `date_of_birth`| DATE          | Individual's birth date.                           |
| `gender`       | VARCHAR(25)   | Gender of the individual.                          |
| `bmi`          | DECIMAL(5, 2) | Body Mass Index of the individual.                 |
| `username`     | VARCHAR(255)  | Username for account login.                        |
| `password_hash`| VARCHAR(128)  | Hashed password for account security.              |
| `password_salt`| VARCHAR(32)   | Salt for the hashed password.                      |

#### `PersonalData`
| Field               | Type      | Description                                      |
|---------------------|-----------|--------------------------------------------------|
| `data_id`           | INT(10)   | Primary key. Unique identifier for personal data. |
| `detail_id`         | INT(10)   | Foreign key to `PersonalDetails`.               |
| `daily_calorie_goal`| INT(10)   | Target daily caloric intake.                     |
| `consumed_calorie`  | INT(10)   | Total calories consumed on a given date.         |
| `today_date`        | DATE      | The date for the calorie data.                   |

#### `MealRecord`
| Field              | Type    | Description                                     |
|--------------------|---------|-------------------------------------------------|
| `meal_id`          | INT(10) | Primary key. Unique identifier for meal records. |
| `personal_data_id` | INT(10) | Foreign key to `PersonalData`.                  |
| `Recipes_id`       | INT(10) | Foreign key to `Recipes`.                       |
| `date`             | DATE    | Date when the meal was consumed.                |

#### `Recipes`
| Field             | Type        | Description                                  |
|-------------------|-------------|----------------------------------------------|
| `recipes_id`      | INT(10)     | Primary key. Unique identifier for recipes.   |
| `name`            | VARCHAR(64) | Name of the recipe.                          |
| `Ingredient`      | INT(10)     | ID linking to an ingredients table.          |
| `recipes`         | VARCHAR(4096)| Recipe instructions.                        |
| `nutritional_data`| VARCHAR(512)| Nutritional information of the recipe.      |
| `link`            | VARCHAR(512)| Link to the recipe's source.   

### Script to generate the database
```sql
-- Create a new database (adjust the database name as needed) CREATE DATABASE IF NOT EXISTS FoodDelivery; USE FoodDelivery;

-- Table: Personal Details CREATE TABLE IF NOT EXISTS PersonalDetails (
  detail_id INT AUTO_INCREMENT PRIMARY KEY,
  weight DECIMAL(5, 2),
  height DECIMAL(6, 1),
  date_of_birth DATE,
  gender VARCHAR(25),
  bmi DECIMAL(5, 2),
  username VARCHAR(255),
  password_hash VARCHAR(128),
  password_salt VARCHAR(32)
);

-- Table: Personal Data CREATE TABLE IF NOT EXISTS PersonalData (
  data_id INT AUTO_INCREMENT PRIMARY KEY,
  detail_id INT,
  daily_calorie_goal INT,
  consumed_calorie INT DEFAULT 0,
  today_date DATE,
  FOREIGN KEY (detail_id) REFERENCES PersonalDetails(detail_id)
);

-- Table: Recipes CREATE TABLE IF NOT EXISTS Recipes (
  recipes_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(64),
  ingredient TEXT,
  recipes TEXT,
  nutritional_data varchar(512),
  link VARCHAR(512)
);

-- Table: Meal Record CREATE TABLE IF NOT EXISTS MealRecord (
  meal_id INT AUTO_INCREMENT PRIMARY KEY,
  personal_data_id INT,
  Recipes_id INT,
  date DATE,
  calories INT,
  FOREIGN KEY (personal_data_id) REFERENCES PersonalData(data_id),
  FOREIGN KEY (Recipes_id) REFERENCES Recipes(recipes_id)
);
```
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
