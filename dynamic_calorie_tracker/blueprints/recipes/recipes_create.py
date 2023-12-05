from sqlalchemy import create_engine, MetaData, Table, select


class Recipes:
    def __init__(self, name, ingredient,recipes,nutritional_data,link):
        self.name = name
        self.ingredient = ingredient
        self.recipes = recipes
        self.nutritional_data = nutritional_data
        self.link = link
    

username = 'root'
password = 'mJerrold1902'
host = '127.0.0.1'
database_name = 'recepiesFood'

# MySQL connection URL format: mysql+pymysql://username:password@host/database_name
db_url = f'mysql+pymysql://{username}:{password}@{host}/{database_name}'

# Create the engine
engine = create_engine(db_url)

# Test the connection by attempting to connect
try:
    with engine.connect() as connection:
        print("Connected to MySQL database!")
except Exception as e:
    print("Failed to connect to the database:", e)


metadata = MetaData()

# Define the 'recipes' table using SQLAlchemy's Table object
recipes = Table('recipes', metadata, autoload_with=engine)


# Selecting 'name' and 'calorie' columns from the 'recipes' table
query = select(recipes.c.name, recipes.c.calorie, recipes.c.link, recipes.c.recipes_id)

# with engine.connect() as connection:
#     result = connection.execute(query)
#     rows = result.fetchall()

#     for row in rows:
#         print(row[0], row[1], row[2], row[3])  # Accessing the first and second elements in the row for name and calorie respectively


def getMatching(a):
    list = []
    a = a.lower()
    with engine.connect() as connection:
        result = connection.execute(query)
        rows = result.fetchall()

        for row in rows:
            if (row[0].lower().find(a) != -1):
                list.append([row[0],row[3]])
    return list