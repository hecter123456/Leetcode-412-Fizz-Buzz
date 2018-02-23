import unittest

class unitest(unittest.TestCase):
    def testInputZero(self):
        Input = 0
        Output = []
        self.assertEqual(Solution().fizzBuzz(Input),Output);
    def testSample(self):
        Input = 15
        Output = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
        self.assertEqual(Solution().fizzBuzz(Input),Output);

class Solution():
    def fizzBuzz(self, n):
        Ans = []
        for i in range(1,n+1):
            if i % 15 == 0:
                Ans.append("FizzBuzz")
            elif i % 5 == 0:
                Ans.append("Buzz")
            elif i % 3 == 0:
                Ans.append("Fizz")
            else:
                Ans.append(str(i))
        return Ans

if __name__ == '__main__':
    unittest.main()
