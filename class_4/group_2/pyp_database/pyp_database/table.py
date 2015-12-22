#-- Imports
import os
import re
from collections import Counter

#-- Constants
FILE_EXTENSION = '.data'

class Table(object):
    
    #A dictionary containing the table's info. Mirrors the file.

    def __init__(self, db_name, table_name):
        """ """
        self.db_name = db_name
        self.table_name = table_name
        #self.dict_representation = table_dictionary
        self.index = None
        
    def index(self,column,unique=True):
        pass
        """
        if unique == True:
            if set(Counter(self.dict_representation[column]).values())==set([1]):
                self.index = column
            else:
                return 'Values in this columns are not unique. Please edit the column or use another.'
        else:
            self.index = column
        """

    def insert(self, *args):
        """Add a line to the table file"""
        #Writing the new data in the next line of the file
        current_table = open(os.path.join('databases', self.db_name, self.table_name + FILE_EXTENSION), 'a')
        for i, column in enumerate(args):
            current_table.write(str(column))
            if i < len(args) - 1:
                current_table.write(', ')
        current_table.write('\n')
        current_table.close()

    def query(self, **kwarg):
        """Return a list of the first match for column == query"""
        # Extracting query from **kwarg, may be there is an easier way
        print (kwarg)
        column = str(list(kwarg.keys())[0])
        query = kwarg[list(kwarg.keys())[0]]
        
        column, filt = column.split("__")
        
        # Formatting the content of the file into list of list
        table_file = open(os.path.join('databases', self.db_name, self.table_name + FILE_EXTENSION))
        table = table_file.readlines()
        table = [line.replace("\n", "").split(", ") for line in table]
        # Get the index of the column
        index = table[0].index(column)
        results_list = []
        
        
        for row in table[1:]:
            if self.match(row[index], query, filt):
                results_list.append(row)

        return results_list

    def match(self, value, query, filt):
        """ """
        if filt == None:
            if query == value:
                return True
        if not query.startswith('%'):
            query = '^' + query
        if not query.endswith('%'):
            query = query + '$'
            
        query = query.replace('%','.*')
            
        if filt == 'like':
            if re.match(query, value):
                return True
        if filt == 'ilike':
            if re.match(query, value, re.I):
                return True
        if filt == 'gt':
            if value > query:
                return True
        if filt == 'gte':
            if value >= query:
                return True
        if filt == 'lt':
            if value < query:
                return True
        if filt == 'lte':
            if value <= query:
                return True
                
        return False
        
    
        
          