import unittest

import part1, part2

def importData():
    with open('test_input.txt') as input_file:
        inputDataArray = input_file.readlines()
    cleanInputDataArray = []
    for line in inputDataArray:
        cleanInputDataArray.append(line.replace("\n", ""))
    return cleanInputDataArray

class Test_TestPart1(unittest.TestCase):
    def test_part1(self):

        self.assertEqual(part1.calculateScratchcards(importData()), 13)

class Test_TestPart2(unittest.TestCase):
    def test_part2(self):

        self.assertEqual(part2.calculateScratchcards(importData()), 30)

if __name__ == '__main__':
    unittest.main()
