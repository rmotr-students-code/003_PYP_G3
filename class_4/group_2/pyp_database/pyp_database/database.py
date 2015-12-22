#-- Imports
import os
from table import Table

#-- Constants
FILE_EXTENSION = '.data'

class Database(object):

    def __init__(self, db_name):
        """Initialise the object and create a dict of table objects."""
        self.db_name = db_name
        
        #Create a dict of Table objects based on the name of directories in the databases\db_name folder
        self.db = {}
        for elem in os.listdir(os.path.join('databases', self.db_name)):
            self.db[elem.replace(FILE_EXTENSION, "")] = Table(self.db_name, elem.replace(FILE_EXTENSION, ""))

    def __getattr__(self, table_name):
        """Return a table object from self.db."""
        self.table_name = table_name
        return self.db[table_name]

    def create_table(self, table_name, columns=[]):
        """Create the table file and adding a table object into db."""
        if os.path.exists(os.path.join('databases', self.db_name, table_name + FILE_EXTENSION)):
            print ("A table already has this name")
        else:
            #Writing the name of the column in the first line of the table file
            current_table = open(os.path.join('databases', self.db_name, table_name + FILE_EXTENSION), 'w')
            
            for i, column in enumerate(columns):
                current_table.write(column)
                if i < len(columns) - 1:
                    current_table.write(', ')
            current_table.write('\n')
            current_table.close()
    
            self.db[table_name] = Table(self.db_name, table_name) # Adding the new Table to our db dict
