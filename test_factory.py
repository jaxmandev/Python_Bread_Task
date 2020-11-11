# import after "pip download unittest"
from factory import NaanFactory
import unittest

class TestNaanFactory(unittest.TestCase):
    factory = NaanFactory()

    # test that make_dough returns 'dough' if 'water' and 'flour' passed as arguments
    def test_make_dough(self):
        self.assertEqual(self.factory.make_dough('water', 'flour'), 'dough')
        self.assertNotEqual(self.factory.make_dough('sugar', 'flour'), 'dough')


    # test that bake_naan returns 'bread' if 'dough' passed as argument
    def test_bake_naan(self):
        self.assertEqual(self.factory.bake_naan('dough'), 'bread')
    
    # test that run_factory returns True if 'water' and 'flour' are arguments
    def test_run_factory(self):
        self.assertTrue(self.factory.run_factory('water', 'flour'))