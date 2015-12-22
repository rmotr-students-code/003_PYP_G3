from table import Table
import os

class Database(object):
    def __init__(self, name):
        '''
        '''
        self.__tables = {}
        self.path = name
        for directory in [d for d in os.listdir(name) if not os.path.isfile(d)]:
            self.__tables[directory] = Table(self.path, directory, None)
    
    def create_table(self, table_name, columns):
        '''
        Creates a table
        
        :param str table_name: name of the table
        :param list columns: a list of columns to create
        '''
        if os.path.exists(os.path.join(self.path, table_name)):
            raise Exception()
        self.__tables[table_name] = Table(self.path, table_name, columns)
    
    def __getattr__(self, name):
        '''
        AH: Gets called when we do db.actors, so we
        simply return self.__tables[actors] 
        '''
        if name == "__tables":
            return self.__tables
        elif name in self.__tables:
            return self.__tables[name]
    
    @classmethod
    def create_database(cls, name):
        '''
        AM: Takes in db name to create and creates the relevant directories
        Also check if it already exists
        '''
        if not os.path.exists(name):
            os.makedirs(name)
            return True
        else:
            return False
    
    @classmethod
    def use(cls, name):
        '''
        '''
        if os.path.exists(name):
            return Database(name)
        else:
            return None