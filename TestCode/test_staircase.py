import unittest
from ProductCode.staircase import staircase


class StaircaseTest(unittest.TestCase):
    def test_give_n_2_should_be_staircase_2_layers(self):
        n = 2
        pattern = "#"
        expected_output = " #\n##"

        result = staircase(n, pattern)

        self.assertEqual(result, expected_output)

    def test_give_n_0_should_return_error(self):

        self.assertEqual(staircase(0, "#"), "Out of range")

    def test_give_n_31_should_return_error(self):

        self.assertEqual(staircase(31, "#"), "Out of range")
