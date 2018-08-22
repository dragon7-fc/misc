""" 
Power of Three

Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?

"""

""" Solution1: 708 ms """
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        while n%3 == 0:
            n //= 3
        return n == 1


""" Solution2: 492 ms """
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 0:
            return (math.log10(n)/math.log10(3))%1 == 0
        else:
            return False


""" Solution3: 452 ms """
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1: return False
        if n == 1: return True
        
        while n > 1:
            if n % 3 != 0:
                return False
            n /= 3
        
        return True
            