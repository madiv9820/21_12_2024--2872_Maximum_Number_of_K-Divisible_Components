from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testcases = {1: (7, [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], [3,0,6,1,5,2,1], 3, 3),
                            2: (5, [[0,2],[1,2],[1,3],[2,4]], [1,8,1,4,4], 6, 2)}
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_case_1(self):
        n, edges, values, k, output = self.__testcases[1]
        result = self.__obj.maxKDivisibleComponents(n = n, edges = edges, values = values, k = k)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_case_2(self):
        n, edges, values, k, output = self.__testcases[2]
        result = self.__obj.maxKDivisibleComponents(n = n, edges = edges, values = values, k = k)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()