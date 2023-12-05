from flask import Blueprint, render_template, redirect, Flask
from sqlalchemy import create_engine, MetaData, Table, select


# flask stuff

recipes_bp = Blueprint("recipe", __name__, template_folder="templates")

@recipes_bp.route("/recipes")
def recipes():
    return render_template('recipe.html')

#######################################################################################################
# sqlalchemy stuff VVVV
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

query = select(recipes.c.name, recipes.c.calories, recipes.c.link, recipes.c.recipes_id)

#######################################################################################################################


# function returns list of [recipe name, recipes_id] that find(a) has
def getMatching(a):
    print("starting running")
    list = []
    a = a.lower()
    with engine.connect() as connection:
        result = connection.execute(query)
        rows = result.fetchall()

        for row in rows:
            if (row[0].lower().find(a) != -1):
                list.append([row[0],row[3]])
    return list

recipes_bp = Blueprint("restaurant_bp", __name__, template_folder="templates")

# @app.route('/generate_divs', methods=['GET'])
# def generate_divs():
#     query = request.args.get('q', '')  # Retrieve the search query
#     filtered_list = [s for s in sample_list if query.lower() in s.lower()]

#     # If query is empty or no match found, show all strings, else show filtered results
#     strings_to_display = filtered_list if filtered_list else sample_list[:5]
#     return render_template('recipe.html', strings=strings_to_display)

from flask import request

@recipes_bp.route('/recipes', methods=['GET'])
def search():
    search_query = request.args.get('q', '')  # Retrieve the search query from the form
    matching_recipes = getMatching(search_query)  # Use your function to get matching recipes
    print (matching_recipes)
    return render_template('recipe.html', recipes=matching_recipes)
     



# python -m flask -app