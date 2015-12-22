import sys
import os
import shutil
import string
import pytest
sys.path.append("/home/ubuntu/workspace/class_4/group_1/app/pyp_database")
import database
import table
import random

created_dirs = []
columns = ["col1", "col2", "col3"]

def random_string(size=6, chars=string.ascii_letters + string.digits):
    temp = ''.join(random.choice(chars) for _ in range(size))
    if temp in created_dirs:
        return random_string(size=size+1)
    else:
        return temp

class TestDatabase:
    def test_creation_of_db(self):
        db_name = random_string()
        created_dirs.append(db_name)
        database.Database.create_database(db_name)
        assert os.path.exists(db_name)
    
    def test_creation_of_multiple_db(self):
        db_names = [random_string() for _ in range(5)]
        assert len(db_names) == 5
        for db_name in db_names:
            database.Database.create_database(db_name)
            created_dirs.append(db_name)
        for db_name in db_names:
            assert os.path.exists(db_name)
            
    def test_use_preexisting_db(self):
        db_name = "test_empty_db"
        created_dirs.append(db_name)
        os.makedirs(db_name)
        db = database.Database.use(db_name)
        assert db != None
        assert isinstance(db, database.Database)
        assert hasattr(db, "__tables")
    
    def test_use_nonexisting_db(self):
        db_name = "NON_EXISTING_DB"
        db = database.Database.use(db_name)
        assert db == None
    
    def test_create_and_use(self):
        db_name = random_string()
        created_dirs.append(db_name)
        database.Database.create_database(db_name)
        assert os.path.exists(db_name)
        db = database.Database.use(db_name)
        assert isinstance(db, database.Database)
        assert db != None
        assert hasattr(db, "__tables")

    def test_create_table(self):
        db_name = random_string()
        created_dirs.append(db_name)
        database.Database.create_database(db_name)
        db = database.Database.use(db_name)
        db.create_table("table1", columns)
        assert "table1" in getattr(db, "__tables")
        my_table = db.table1
        assert my_table != None
        assert isinstance(my_table, table.Table)
        
    def test_create_table_with_preexisting(self):
        db_name = random_string()
        created_dirs.append(db_name)
        table_name = "table1"
        os.makedirs(db_name)
        db = database.Database.use(db_name)
        db.create_table(table_name, columns)
        with pytest.raises(Exception):
            db.create_table(table_name, columns)
        
    def test_use_preexisting_db_with_preexisting_tables(self):
        db_name = random_string()
        created_dirs.append(db_name)
        table_name1 = "table1"
        table_name2 = "table2"
        my_table1 = table.Table(db_name, table_name1, columns)
        my_table2 = table.Table(db_name, table_name2, columns[::-1])
        db = database.Database.use(db_name)
        assert getattr(db, table_name1).columns == columns
        assert getattr(db, table_name2).columns == columns[::-1]

class TestTable:
    def test_creating_a_table_object(self):
        db_name = "tabledb_test1"
        table_name = "table1"
        created_dirs.append(db_name)
        os.makedirs(db_name)
        my_table = table.Table(db_name, table_name, columns)
        assert os.path.exists(os.path.join(db_name, table_name))
        columns_file_path = os.path.join(db_name, table_name, "columns.dat")
        assert os.path.exists(columns_file_path)
        assert os.path.isfile(columns_file_path)
        with open(columns_file_path, "r") as f:
            line = f.readline()
            assert line == table.COL_SEP.join(columns)
        table_file_path = os.path.join(db_name, table_name, "table.dat")
        assert os.path.exists(table_file_path)
        assert os.path.isfile(table_file_path)
        assert isinstance(my_table, table.Table)
        assert hasattr(my_table, "columns")
        assert hasattr(my_table, "name")
        assert hasattr(my_table, "full_path")

    def test_preexisting_table(self):
        db_name = "tabledb_test2"
        created_dirs.append(db_name)
        table_name = "table1"
        table_path = os.path.join(db_name, table_name)
        columns_file_path = os.path.join(db_name, table_name, "columns.dat")
        table_file_path = os.path.join(db_name, table_name, "table.dat")
        os.makedirs(db_name)
        os.makedirs(table_path)
        with open(columns_file_path, "w") as f:
            f.write(table.COL_SEP.join(columns))
        with open(table_file_path, "w") as f:
            for _ in range(5):
                f.write(table.COL_SEP.join([random_string() for _ in range(len(columns))]) + "\n")
        my_table = table.Table(db_name, table_name, ["1", "2"])
        with open(os.path.join(my_table.full_path,"columns.dat"), "r") as f:
            assert f.readline() == table.COL_SEP.join(columns)
        with open(os.path.join(my_table.full_path,"table.dat"), "r") as f:
            assert f.readline() != ""
        assert my_table.columns == columns

def test_cleanup():
    '''
    Remove all the created dirs
    '''
    for db_name in created_dirs:
        if os.path.exists(db_name):
            shutil.rmtree(db_name)
            