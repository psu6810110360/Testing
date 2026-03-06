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

    def test_give_BBBBB_should_delete_4(self):
        self.assertEqual(alternating_characters("BBBBB"), 4)

    def test_give_single_char_should_delete_0(self):
        self.assertEqual(alternating_characters("A"), 0)

    def test_give_AABBCC_should_delete_3(self):
        self.assertEqual(alternating_characters("AABBCC"), 3)
