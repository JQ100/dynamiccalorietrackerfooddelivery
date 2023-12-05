from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

db = SQLAlchemy()

engine = create_engine(
    'sqlite:///db.sqlite3', echo=True)
db_session = Session(engine)
