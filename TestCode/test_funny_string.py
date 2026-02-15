import unittest
from ProductCode.funny_string import funny_string

class FunnyStringTest(unittest.TestCase):
    def test_give_acxz_should_be_funny(self):
        
        s = "acxz"
        
        result = funny_string(s)
        
        self.assertEqual(result, "Funny")
    def test_give_bcxz_should_be_not_funny(self):
        s = "bcxz"
        result = funny_string(s)
        self.assertEqual(result, "Not Funny")
    def test_give_aaaaa_should_be_funny(self):
        self.assertEqual(funny_string("aaaaa"), "Funny")