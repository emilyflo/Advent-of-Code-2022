import unittest
from rucksack import rucksack_organization

class test_problems(unittest.TestCase):
    def test_rucksack(self):
        answer = rucksack_organization()

        self.assertEqual(answer, 157)

if __name__ == "__main__":
    unittest.main()