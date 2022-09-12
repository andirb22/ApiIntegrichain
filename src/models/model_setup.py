from models import configDB
from models import models_entity




def create_tables():
     configDB.db.create_all()