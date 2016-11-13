import unittest

from minesweeper import Minesweeper

class TestMinesweeper(unittest.TestCase):
    def test_create_grid(self):
        grid1 = Minesweeper(3, 2)
        self.assertIsInstance(grid1.grid, list, msg="Minesweeper.grid didn't return a list")
        self.assertEqual(len(grid1.grid), 2, msg="Minesweeper.grid need to have a size of Y")
        self.assertEqual(len(grid1.grid[0]), 3, msg="Minesweeper.grid need to have a size of X")
        self.assertEqual([
            ['.', '.', '.'],
            ['.', '.', '.'],
        ], grid1.grid, msg="Minesweeper.grid need to be empty")

    def test_can_add_mine(self):
        grid2 = Minesweeper(4, 4)
        self.assertEqual([
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
        ], grid2.grid, msg="Minesweeper.grid need to be empty with different")

        grid2.add_mine(1, 1)
        self.assertEqual([
            ['.', '.', '.', '.'],
            ['.', '*', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
        ], grid2.grid)

        grid2.add_mine(3, 2)
        self.assertEqual([
            ['.', '.', '.', '.'],
            ['.', '*', '.', '.'],
            ['.', '.', '.', '*'],
            ['.', '.', '.', '.'],
        ], grid2.grid)


    def test_can_compute_grid(self):
        grid2 = Minesweeper(4, 4)
        grid2.add_mine(0, 0)
        grid2.add_mine(1, 2)
        grid2.compute()

        self.assertEqual([
            ['*', 1, 0, 0],
            [2, 2, 1, 0],
            [1, '*', 1, 0],
            [1, 1, 1, 0],
        ], grid2.grid)
