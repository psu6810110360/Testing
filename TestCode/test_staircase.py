import unittest
from ProductCode.staircase import staircase

class StaircaseTest(unittest.TestCase): 
    def test_give_n_2_should_be_staircase_2_layers(self):
        n = 2
        pattern = '#'
        expected_output = " #\n##"
        
      
        result = staircase(n, pattern)
        
        
        self.assertEqual(result, expected_output) 