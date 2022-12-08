import unittest

from rucksack import *
from badges import *

class test_problems(unittest.TestCase):
    def test_rucksack(self):
        answer = rucksack_organization('test.txt')
        self.assertEqual(answer, 157)

class badges(unittest.TestCase):
    def test_badges(self):
        answer = elf_badges('test2.txt')
        self.assertEqual(answer, 70)

if __name__ == "__main__":
    unittest.main()