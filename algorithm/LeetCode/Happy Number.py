""" 
Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

"""


""" Solution1: 60 ms """
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n != 1:
            sum = 0
            while n > 0:
                last_digit = n%10
                sum += last_digit**2
                n //= 10
            if sum == 11 or sum == 20:
                return False
            n = sum
            
        return True


""" Solution2: 48 ms """
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = {}
        v = n
        while True:
            v = sum([int(i)**2 for i in str(v)])
            if v == 1:
                return True
            elif v in seen:
                return False
            else:
                seen[v] = 1