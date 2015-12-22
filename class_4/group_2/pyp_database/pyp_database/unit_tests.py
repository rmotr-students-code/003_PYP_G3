import os
import unittest
from database import Database
from api import use, create_database
from table import Table

class Test(unittest.TestCase):
	
	def test_create_db(self):
		self.assertEqual(create_database('imdb'),None)
		#create_database('unit_test_db')
		self.assertTrue(os.path.exists(os.path.join('databases','unit_test_db')))
	
	def test_use_db(self):
		self.assertFalse(use('godzilla'))
		#self.assertTrue(isinstance(use('imbd'), Database))
	
	def test_table(self):
		pass
		#self.assertTrue(os.path.exists(os.path.join('pyp_database','databases', 'imdb', 'actors.data')))
		#use('imbd').create_table('empty_unit_test_table')
		#self.assertTrue(len(use('imbd').empty_unit_test_table.dict_representation.keys())==0)
	
	def test_insertion(self):
		pass
	
	def test_query_like(self):
		pass
	
	def test_query_ilike(self):
		pass
	
	def test_query_gt(self):
		pass
	
	def test_query_lte(self):
		pass
	
	def test_validation(self):
		pass

if __name__ == "__main__":
    unittest.main()