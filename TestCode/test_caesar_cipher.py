import unittest
from ProductCode.caesar_cipher import caesar_cipher


class CaesarCipherTest(unittest.TestCase):
    def test_give_middle_Outz_k2_should_be_okffng_Qwvb(self):
        s, k = "middle-Outz", 2
        result = caesar_cipher(s, k)

        self.assertEqual(result, "okffng-Qwvb")

    def test_give_k0_should_not_change(self):
        self.assertEqual(caesar_cipher("Hello-World", 0), "Hello-World")

    def test_give_symbols_should_not_change(self):
        self.assertEqual(caesar_cipher("123 !@#", 10), "123 !@#")

    def test_give_large_k_52_should_be_same(self):
        self.assertEqual(caesar_cipher("abc", 52), "abc")

    def test_give_full_alphabet_shift(self):
        self.assertEqual(caesar_cipher("Always", 5), "Fqbfdx")
