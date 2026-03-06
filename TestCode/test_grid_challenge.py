import unittest
from ProductCode import grid_challenge


class GridChallengeTest(unittest.TestCase):
    def test_give_sorted_columns_should_be_YES(self):
        grid = ["abc", "hjk", "mpq"]
        self.assertEqual(grid_challenge(grid), "YES")

    def test_give_unsorted_columns_should_be_NO(self):
        grid = ["ebg", "afe", "hig"]
        self.assertEqual(grid_challenge(grid), "NO")
