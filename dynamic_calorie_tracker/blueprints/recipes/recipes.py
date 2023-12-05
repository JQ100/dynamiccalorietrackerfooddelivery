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
password = '1234'
host = '127.0.0.1'
database_name = 'recipelol'

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

query = select(recipes.c.name, recipes.c.calorie, recipes.c.link, recipes.c.recipes_id)

########################################################################################################################


# function returns list of [recipe name, recipes_id] that find(a) has
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


#-----------------------------------------------------------------------------------------------------
app = Flask(__name__)
sample_list = ['String 1', 'String 2', 'String 3', 'String 4', 'String 5']


@app.route('/generate_divs')
def generate_divs():
    # Fetching the first 5 entries from the sample_list
    first_five_entries = sample_list[:5]
    return render_template('recipe.html', strings=first_five_entries)


if __name__ == '__main__':
    app.run(debug=True)

# python -m flask -app