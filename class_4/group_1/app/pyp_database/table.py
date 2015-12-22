import os

COL_SEP = "|"

class Table(object):
    def __init__(self, db_path, table_name, columns):
        self.name = table_name
        self.full_path = os.path.join(db_path, table_name)
        self.__columns_file_path = os.path.join(self.full_path, "columns.dat")
        self.__table_file_path = os.path.join(self.full_path, "table.dat")
        if not os.path.exists(self.full_path):
            self.columns = columns
            os.makedirs(self.full_path)
            file = open(self.__columns_file_path, "w")
            file.write(COL_SEP.join(self.columns))
            file.close()
            file = open(self.__table_file_path, "w")
            file.close()
        else:
            with open(self.__columns_file_path, "r") as f:
                self.columns = f.readline().split(COL_SEP)

    def __read_table(self):
        '''
        Reads the entire table into memory
        '''
        file = open(self.__table_file_path, "r")
        db = file.read().splitlines()
        file.close()
        return [row.split(COL_SEP) for row in db]

    def __read_columns(self):
        '''
        Reads the column header into memory
        '''
        file = open(self.__columns_file_path, "r")
        columns = file.read().splitlines()[0].split(COL_SEP)
        file.close()
        return columns


    def insert(self, *args):
        '''
        Inserts into table
        
        :param *args: The arguments to insert into the table
        '''
        # Add checking to make sure that the number of args match the number of columns
        if len(list(*args)) != len(self.__read_columns()):
            raise Exception("Number of items being inserted doesn't match number of columns")
        row = COL_SEP.join(map(str, list(*args))) + '\n'

        file = open(self.__table_file_path, "a")
        file.write(row)
        file.close


    def query(self, **kwargs):
        '''
        '''
        columns = self.__read_columns() # you already have the columns in self.columns
        table = self.__read_table()
        return_list = []
        
        #for i in kwargs.keys():
        #    if i not in columns:
        #        raise Exception("Column %s doesn't exist" % i)
        #
        #    index = columns.index(i)
        #
        #    for t in table:
        #        if t[index] == kwargs[i]:
        #            return_list.append(t)
        #return return_list
