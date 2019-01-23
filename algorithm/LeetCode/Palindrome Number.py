""" 
Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
 """
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        return True if x==x[::-1] else False

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        palindrome = []
        while x:
            y = x%10
            palindrome.append(y)
            x = int(x/10)
        match = 0
        for i in range(int(len(palindrome)/2)):
            if palindrome[i] == palindrome[len(palindrome)-1 -i]:
                match +=1
        if match == int(len(palindrome)/2):
            return True
        else:
            return False