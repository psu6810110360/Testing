import unittest
from ProductCode.grid_challenge import grid_challenge


class GridChallengeTest(unittest.TestCase):
    def test_give_sorted_columns_should_be_YES(self):
        grid = ["abc", "hjk", "mpq"]
        self.assertEqual(grid_challenge(grid), "YES")

    def test_give_unsorted_columns_should_be_NO(self):
        grid = ["ebg", "afe", "hig"]
        self.assertEqual(grid_challenge(grid), "NO")

    def test_give_single_row_YES(self):
        self.assertEqual(grid_challenge(["z"]), "YES")

    def test_give_identical_rows_YES(self):
        self.assertEqual(grid_challenge(["abc", "abc", "abc"]), "YES")

    def test_give_reverse_rows_that_need_sort_YES(self):
        self.assertEqual(grid_challenge(["cba", "fed"]), "YES")
