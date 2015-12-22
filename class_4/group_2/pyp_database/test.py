#-- Imports
import pyp_database
from datetime import date

#pyp_database.create_database('imdb')
db = pyp_database.use('imdb')



#db.create_table('actors', columns=['id', 'name', 'date_of_birth'])


'''
db.actors.insert(1, 'Kevin Bacon', date(1958, 7, 8))
db.actors.insert(2, 'Kevin Martin', date(1953, 2, 9))
db.actors.insert(5, 'Jack Nickolson', date(1958, 7, 8))
db.actors.insert(6, 'Ralph Fiennes', date(1978, 7, 8))
db.actors.insert(3, 'Daniel Kevin', date(1958, 2, 1))
db.actors.insert(5, 'Daniel Day-Lewis', date(1953, 7, 8))
db.actors.insert(7, 'Robert De Niro', date(1952, 7, 8))
db.actors.insert(4, 'Kevin Pacino', date(1948, 7, 8))
db.actors.insert(8, 'Tom Hanks', date(1959, 7, 8))
db.actors.insert(9, 'Kevin Things', date(1958, 7, 8))
'''

'''
db.create_table('test_tab', columns=['id', 'name', 'date_of_birth'])
db.test_tab.insert(1, 'Kevin Bacon', date(1958, 7, 8))
db.test_tab.insert(2, 'Kevin Martin', date(1953, 2, 9))
db.test_tab.insert(3, 'Jack Nickolson', date(1958, 7, 8))
db.test_tab.index('id', unique=True) 
'''

#Query Testing

print(db.actors.query(name__like='Kevin%'))
exit()
print(db.actors.query(name__like='kevin%'))
print(db.actors.query(name__ilike='%Kevin%'))
print(db.actors.query(name__ilike='Kevin'))
print(db.actors.query(name__ilike='%Kevin'))
print(db.actors.query(name__like='%Bacon'))

