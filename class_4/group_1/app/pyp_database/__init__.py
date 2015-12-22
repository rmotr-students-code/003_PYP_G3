'''
You'll need to build a simple database system using files. That your database is using files 
underneath should be COMPLETELY hidden to your user. This is the database interface that we need:

import pyp_database
from datetime import date

pyp_database.create_database('imdb')
db = pyp_database.use('imdb')

db.create_table('actors', columns=['id', 'name', 'date_of_birth'])
db.actors.insert(1, 'Kevin Bacon', date(1958, 7, 8)) # Note 1
db.actors.query(name='Kevin Bacon') # Note 2

This database should be carefully packaged so it can be imported by some other program. WE DON'T WANT SCATTERED SCRIPTS ANYMORE. 
Improve your coding: more readable, documented, tested, self-packaged.

Note 1: Pay attention to the interface. We're doing db.actors, which is the name of the table. 
You'll have to work with dynamic attributes (__getattr__) or properties in order to solve that. 
Also, be careful on the type of data you're receiving. You should format dates, strings and numbers without issues.

Note 2: The attribute passed to query will also be dynamic and it'll depend on the columns present in the table.
----------------------------------------------------------------------------------
All these are improvements you can do:

Better queries

An improvement would be to provide a richer interface for queries. For example:

db.actors.query(name__like='Kevin%')
db.actors.query(name__ilike='%bacon%') # ilike means case insensitive
db.actors.query(date_of_birth__gt=date(1950, 1, 1)) # gt means "greater than"
db.actors.query(date_of_birth__gte=date(1958, 7, 8)) # gte means "greater than or or equals to"
------------------------------------------------------------------------------------
Indexes and unique values

Allow index creation on tables. Indexes might be also be used to check for unique values.

db.actors.index('name')  # Created an index in the name column
db.actors.index('id', unique=True)  # Created an index in the id column and it MUST be a unique value across the whole table.
--------------------------------------------------------------------------------------------------------------
Data validation and default values

Create tables indicating the data type for each column and if the value can be None or not:

db.create_table('actors', columns={
    'id': int,
    'name': str,
    'date_of_birth': date,
    'nationality': {
        'type': str,
        'allow_none': True,
    }
})

db.actors.insert('2', 'Julia Roberts', date(1958, 7, 8)) # This should fail because id is not an int
db.actors.insert(2, 'Julia Roberts', '1967') # This should fail because date is invalid
db.actors.insert(2, 'Julia Roberts', date(1967, 10,28)) # This succeeds and sets nationality to None
----------------------------------------------------------------------------------
CLI interface

It'd be really nice to have a Command Line Interface program to interact with databases:

$ python pyp_database create_database imdb
$ python pyp_database -d imdb create_table actors id,name,date_of_birth
$ python pyp_database -d imdb -t actors insert --id 1 --name "Kevin Bacon" --date_of_birth "1958-07-08"
$ python pyp_database -d imdb -t actors query --name "Kevin Bacon"
$ python pyp_database -d imdb -t actors query --name__like "Kevin%"
-------------------------------------------------------------------------------
Installable Package

Using setuptools publish your package to the cheeseshop (pypi.python.org) and make it installable to anyone. So I should be able to do:

$ pip install pyp_database

and use your database in my own project.
'''

