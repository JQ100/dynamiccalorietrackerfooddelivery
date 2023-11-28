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

### Security Considerations
Sensitive details such as usernames and passwords are stored in a separate table (`PersonalDetails`) and are protected using hashing and salting techniques. This separation helps to safeguard the data against unauthorized access.

### Functional Operations
The database is set up to track and manage users' daily caloric intake efficiently. When a user logs a meal into the `MealRecord` table, it records their meal along with the corresponding date and recipe. The `consumed_calorie` field in the `PersonalData` table is then updated to reflect the daily total calorie intake.

### Tables Description

#### `PersonalDetails`
| Field          | Type          | Description                                        |
|----------------|---------------|----------------------------------------------------|
| `detail_id`    | INT       | Primary key. Unique identifier for personal details. |
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
| `data_id`           | INT   | Primary key. Unique identifier for personal data. |
| `detail_id`         | INT   | Foreign key to `PersonalDetails`.               |
| `daily_calorie_goal`| INT   | Target daily caloric intake.                     |
| `consumed_calorie`  | INT   | Total calories consumed on a given date.         |
| `today_date`        | DATE      | The date for the calorie data.                   |

#### `MealRecord`
| Field              | Type    | Description                                     |
|--------------------|---------|-------------------------------------------------|
| `meal_id`          | INT | Primary key. Unique identifier for meal records. |
| `personal_data_id` | INT | Foreign key to `PersonalData`.                  |
| `Recipes_id`       | INT | Foreign key to `Recipes`.                       |
| `date`             | DATE    | Date when the meal was consumed.                |

#### `Recipes`
| Field             | Type        | Description                                  |
|-------------------|-------------|----------------------------------------------|
| `recipes_id`      | INT     | Primary key. Unique identifier for recipes.   |
| `name`            | VARCHAR(64) | Name of the recipe.                          |
| `Ingredient`      | INT     | ID linking to an ingredients table.          |
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

### DataBase for Food Delivery part, based on SQL Alchemy.

## Overview

This database is designed to store and manage data related to restaurant menu items and customer orders. It provides a structured way to keep track of what items are available on the menu, details about each restaurant, orders placed by customers, and the specifics of each order. The database schema facilitates the connection between different entities such as menu items, restaurants, orders, and customers, ensuring an integrated data management system.

## Database Schema

The database consists of the following tables:

### 1. `Restaurant`

This table stores information about the restaurants.

| Column Name    | Data Type | Description                           |
| -------------- | --------- | ------------------------------------- |
| id             | INT       | Primary key, auto-incremented         |
| name           | VARCHAR   | Name of the restaurant                |
| Phone_number   | VARCHAR   | Contact phone number for the restaurant |
| Email          | VARCHAR   | Contact email address for the restaurant |

### 2. `Menu_Item`

Contains details about the menu items available in a restaurant.

| Column Name      | Data Type | Description                                 |
| ---------------- | --------- | ------------------------------------------- |
| id               | INT       | Primary key, auto-incremented               |
| name             | VARCHAR   | Name of the menu item                       |
| price            | INT       | Price of the menu item                      |
| Calories         | INT       | Caloric content of the menu item            |
| Item_adding_date | DATE      | Date when the item was added to the menu    |
| Restaurant_id    | INT       | Foreign key to `Restaurant` table           |

### 3. `Order`

Records details of customer orders.

| Column Name    | Data Type | Description                        |
| -------------- | --------- | ---------------------------------- |
| order_id       | INT       | Primary key, auto-incremented      |
| date           | DATE      | The date when the order was placed |
| restaurant_id  | INT       | Foreign key to `Restaurant` table  |

### 4. `Order_Details`

This table holds the details for each order, linking what items were included.

| Column Name       | Data Type | Description                             |
| ----------------- | --------- | --------------------------------------- |
| order_details_id  | INT       | Primary key, auto-incremented           |
| order_id          | INT       | Foreign key to `Order` table            |
| menu_item_id      | INT       | Foreign key to `Menu_Item` table        |

### 5. `Customer_Orders`

Associates customer orders with restaurants and menu items.

| Column Name     | Data Type | Description                                 |
| --------------- | --------- | ------------------------------------------- |
| id              | INT       | Primary key, auto-incremented               |
| restaurant_id   | INT       | Foreign key to `Restaurant` table           |
| menu_item_id    | INT       | Foreign key to `Menu_Item` table            |

## Relationships

- Each `Menu_Item` is associated with a `Restaurant`.
- Each `Order` is associated with a `Restaurant`.
- `Order_Details` link `Orders` to the `Menu_Items` included in them.
- `Customer_Orders` provide a direct association between `Restaurants` and `Menu_Items` ordered by customers.

## Usage

The database can be utilized by restaurant management systems to keep track of menu items, process customer orders, and maintain records of what items are being ordered from which restaurant, along with the necessary details of each transaction.

For implementation and interaction with the database, SQLAlchemy ORM classes can be used, providing a Pythonic way to manage the underlying SQL database.


### Script to generate it on the SQL

```
CREATE TABLE IF NOT EXISTS `Menu_Item` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(64) NOT NULL,
  `price` INT NOT NULL,
  `Calories` INT NOT NULL,
  `Item_adding_date` DATE NOT NULL,
  `Restaurant_id` INT NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Restaurant` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(64) NOT NULL,
  `Phone_number` VARCHAR(12) NOT NULL,
  `Email` VARCHAR(64) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Order` (
  `order_id` INT NOT NULL AUTO_INCREMENT,
  `date` DATE NOT NULL,
  `restaurant_id` INT NOT NULL,
  PRIMARY KEY (`order_id`)
);

CREATE TABLE IF NOT EXISTS `Order_Details` (
  `order_details_id` INT NOT NULL AUTO_INCREMENT,
  `order_id` INT NOT NULL,
  `menu_item_id` INT NOT NULL,
  PRIMARY KEY (`order_details_id`)
);

CREATE TABLE IF NOT EXISTS `customer_orders` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `restaurant_id` INT NOT NULL,
  `menu_item_id` INT NOT NULL,
  PRIMARY KEY (`id`)
);

-- Add Foreign Keys
ALTER TABLE `Menu_Item` ADD CONSTRAINT `fk_Menu_Item_Restaurant` FOREIGN KEY (`Restaurant_id`) REFERENCES `Restaurant` (`id`);
ALTER TABLE `Order` ADD CONSTRAINT `fk_Order_Restaurant` FOREIGN KEY (`restaurant_id`) REFERENCES `Restaurant` (`id`);
ALTER TABLE `Order_Details` ADD CONSTRAINT `fk_Order_Details_Order` FOREIGN KEY (`order_id`) REFERENCES `Order` (`order_id`);
ALTER TABLE `Order_Details` ADD CONSTRAINT `fk_Order_Details_Menu_Item` FOREIGN KEY (`menu_item_id`) REFERENCES `Menu_Item` (`id`);
ALTER TABLE `customer_orders` ADD CONSTRAINT `fk_customer_orders_Restaurant` FOREIGN KEY (`restaurant_id`) REFERENCES `Restaurant` (`id`);
ALTER TABLE `customer_orders` ADD CONSTRAINT `fk_customer_orders_Menu_Item` FOREIGN KEY (`menu_item_id`) REFERENCES `Menu_Item` (`id`);

```

### The script to generate The database on SQL Alchemy

```
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class MenuItem(Base):
    __tablename__ = 'Menu_Item'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    price = Column(Integer, nullable=False)
    Calories = Column(Integer, nullable=False)
    Item_adding_date = Column(Date, nullable=False)
    Restaurant_id = Column(Integer, ForeignKey('Restaurant.id'))
    restaurant = relationship("Restaurant", back_populates="menu_items")

class Restaurant(Base):
    __tablename__ = 'Restaurant'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    Phone_number = Column(String(12), nullable=False)
    Email = Column(String(64), nullable=False)
    menu_items = relationship("MenuItem", order_by=MenuItem.id, back_populates="restaurant")
    orders = relationship("Order", back_populates="restaurant")

class Order(Base):
    __tablename__ = 'Order'
    order_id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    restaurant_id = Column(Integer, ForeignKey('Restaurant.id'))
    restaurant = relationship("Restaurant", back_populates="orders")
    order_details = relationship("OrderDetails", back_populates="order")

class OrderDetails(Base):
    __tablename__ = 'Order_Details'
    order_details_id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('Order.order_id'))
    menu_item_id = Column(Integer, ForeignKey('Menu_Item.id'))
    order = relationship("Order", back_populates="order_details")
    menu_item = relationship("MenuItem")

class CustomerOrders(Base):
    __tablename__ = 'customer_orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    restaurant_id = Column(Integer, ForeignKey('Restaurant.id'))
    menu_item_id = Column(Integer, ForeignKey('Menu_Item.id'))
    restaurant = relationship("Restaurant")
    menu_item = relationship("MenuItem")

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///sqlalchemy_example.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)

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
