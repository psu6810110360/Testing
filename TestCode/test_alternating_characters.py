import unittest
from ProductCode.alternating_characters import alternating_characters


class AlternatingCharactersTest(unittest.TestCase):
    def test_give_AAAA_should_delete_3(self):
        s = "AAAA"
        result = alternating_characters(s)
        self.assertEqual(result, 3)

    def test_give_ABABAB_should_delete_0(self):
        s = "ABABAB"
        result = alternating_characters(s)
        self.assertEqual(result, 0)

    def test_give_AABBAA_should_delete_3(self):
        s = "AABBAA"
        result = alternating_characters(s)
        self.assertEqual(result, 3)

    def test_give_CCCC_should_delete_3(self):
        s = "CCCC"
        result = alternating_characters(s)
        self.assertEqual(result, 3)

    def test_give_BABABA_should_delete_0(self):
        s = "BABABA"
        result = alternating_characters(s)
        self.assertEqual(result, 0)
