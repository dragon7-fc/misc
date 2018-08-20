""" 
Excel Sheet Column Number

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
"""


""" Solution: 60 ms """
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        base = 1
        for i in range(len(s)-1, -1, -1):
            result += base*(ord(s[i])-ord('A')+1)
            base *= 26
        return result


""" Solution2: 56 ms """
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for index, char in enumerate(s[::-1]):
            pos = ord(char) - ord('A')
            result += pow(26, index) * (pos+1)
        return result