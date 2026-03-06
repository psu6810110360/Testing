import unittest
from ProductCode.caesar_cipher import caesar_cipher


class CaesarCipherTest(unittest.TestCase):
    def test_give_middle_Outz_k2_should_be_okffng_Qwvb(self):
        s, k = "middle-Outz", 2
        result = caesar_cipher(s, k)

        self.assertEqual(result, "okffng-Qwvb")

    def test_give_k_more_than_26(self):
        self.assertEqual(caesar_cipher("abc", 27), "bcd")
