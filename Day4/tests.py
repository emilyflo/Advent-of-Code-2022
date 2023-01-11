import unittest
from camp_cleanup import *
from camp_cleanup2 import *

class cleanup(unittest.TestCase):
    def test_cleanup(self):
        answer = camp_cleanup('part1_example.txt')
        self.assertEqual(answer, 2)

class cleanup2(unittest.TestCase):
    def test_cleanup2(self):
        answer = camp_cleanup2('part1_example.txt')
        self.assertEqual(answer, 4)

if __name__ == "__main__":
    unittest.main()