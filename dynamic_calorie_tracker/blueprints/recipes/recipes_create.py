from sqlalchemy import create_engine, MetaData, Table


class Recipes:
    def __init__(self, name, ingredient,recipes,nutritional_data,link):
        self.name = name
        self.ingredient = ingredient
        self.recipes = recipes
        self.nutritional_data = nutritional_data
        self.link = link
    
from sqlalchemy import create_engine, MetaData, Table

# MySQL connection string format: 'mysql+mysqlconnector://username:password@host:port/database_name'
# Replace 'username', 'password', 'host', 'port', and 'database_name' with your MySQL credentials
connection_string = 'mysql+mysqlconnector://username:password@host:port/database_name'

# Create an SQLAlchemy engine
engine = create_engine(connection_string)

# Create a metadata object
metadata = MetaData()

# Example: Reflect an existing database table
# Replace 'your_table_name' with the name of the table you want to work with
your_table = Table('your_table_name', metadata, autoload=True, autoload_with=engine)

# Establish a connection
with engine.connect() as connection:
    # Example: Execute a SELECT query
    query = your_table.select()
    result = connection.execute(query)

    # Fetch and display data
    for row in result:
        print(row)

    result.close()