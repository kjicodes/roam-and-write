from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

#Initialize db
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

