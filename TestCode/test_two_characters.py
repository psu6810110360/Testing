import unittest

from ProductCode.two_characters import two_characters


class TwoCharactersTest(unittest.TestCase):
    def test_give_beabeefeab_should_be_5(self):
        self.assertEqual(two_characters("beabeefeab"), 5)

    def test_give_aaaaa_should_be_0(self):
        self.assertEqual(two_characters("aaaaa"), 0)

    def test_give_aabb_should_be_0(self):
        self.assertEqual(two_characters("aabb"), 0)

    def test_give_empty_string_should_be_0(self):
        self.assertEqual(two_characters(""), 0)

    def test_give_aba_should_be_3(self):
        self.assertEqual(two_characters("aba"), 3)
