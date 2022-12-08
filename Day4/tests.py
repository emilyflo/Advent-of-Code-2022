import unittest

from camp_cleanup import *

class cleanup(unittest.TestCase):
    def test_cleanup(self):
        answer = camp_cleanup('part1_example.txt')
        self.assertEqual(answer, 2)

if __name__ == "__main__":
    unittest.main()