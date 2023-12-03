import unittest

import part1, part2

def importData():
    with open('test_input.txt') as input_file:
        inputDataArray = input_file.readlines()
    return inputDataArray

class Test_TestPart1(unittest.TestCase):
    def test_part1(self):

        self.assertEqual(part1.calculateEngine(importData()), 4361)

class Test_TestPart2(unittest.TestCase):
    def test_part2(self):

        self.assertEqual(part2.calculateEngine(importData()), 467835)

if __name__ == '__main__':
    unittest.main()
