import unittest
from problem1 import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_sortArray(self):
        # Test cases
        self.assertEqual(self.solution.sortArray([5, 2, 9, 1, 5, 6]), [1, 2, 5, 5, 6, 9])
        self.assertEqual(self.solution.sortArray([4, 2, 3, 1]), [1, 2, 3, 4])
        self.assertEqual(self.solution.sortArray([10, 7, 8, 9, 1, 5]), [1, 5, 7, 8, 9, 10])
        self.assertEqual(self.solution.sortArray([]), [])
        self.assertEqual(self.solution.sortArray([1]), [1])
        self.assertEqual(self.solution.sortArray([-2, -5, -45, -10]), [-45, -10, -5, -2])
        self.assertEqual(self.solution.sortArray([3, 3, 3]), [3, 3, 3])
    
    def test_sortArray_large_input(self):
        # Large input test case
        largeInput = list(range(10000, 0, -1))
        sortedOutput = list(range(1, 10001))
        self.assertEqual(self.solution.sortArray(largeInput), sortedOutput)

if __name__ == '__main__':
    unittest.main()