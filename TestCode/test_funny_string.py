import unittest
from ProductCode.funny_string import funny_string

class FunnyStringTest(unittest.TestCase):
    def test_give_acxz_should_be_funny(self):
        # Arrange
        s = "acxz"
        # Act
        result = funny_string(s)
        # Assert
        self.assertEqual(result, "Funny") # [cite: 31]