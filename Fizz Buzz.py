import unittest

class unitest(unittest.TestCase):
    def testInputZero(self):
        Input = 0
        Output = []
        self.assertEqual(Solution().fizzBuzz(Input),Output);

class Solution():
    def fizzBuzz(self, n):
        Ans = []
        return Ans

if __name__ == '__main__':
    unittest.main()
