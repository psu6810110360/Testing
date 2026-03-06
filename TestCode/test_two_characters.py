import unittest

from ProductCode import two_characters


class TwoCharactersTest(unittest.TestCase):
    def test_give_beabeefeab_should_be_5(self):
        self.assertEqual(two_characters("beabeefeab"), 5)
