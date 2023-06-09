import unittest

from TreeOfLife import TreeOfLife

class TestTreeOfLife(unittest.TestCase):
    def test_tree(self):
        self.assertEqual(
            TreeOfLife(3, 4, 12, ['.+..', '..+.', '.+..']),
            ['.+..', '..+.', '.+..']
        )


if __name__ == '__main__':
    unittest.main()