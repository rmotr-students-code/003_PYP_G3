# -- Imports
import database
import os

def use(db_name):
    if os.path.exists(os.path.join('databases', db_name)):
        return database.Database(db_name)
    else:
        print ("There isn't any database with this name")
        return False

def create_database(db_name):
    if os.path.exists(os.path.join('databases', db_name)):
        print ("A database already has this name")
    else:
        os.makedirs(os.path.join('databases', db_name))