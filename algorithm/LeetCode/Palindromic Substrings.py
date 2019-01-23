''' 
Palindromic Substrings

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.

'''


''' Solution1: 284 ms '''
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        palindrom = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            palindrom[i][i] = 1
        for i in range(n-1):
            if (s[i] == s[i+1]):
                palindrom[i][i+1] = 1
        for cur_len in range(3, n+1):
            for i in range(n-cur_len + 1):
                j = i+cur_len - 1
                if s[i] == s[j] and palindrom[i+1][j-1] == 1:
                    palindrom[i][j] = 1
        return sum([sum(row) for row in palindrom])


''' Solution2: 352 ms '''
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '': return 0
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)): dp[i][i] = 1
        for r in range(len(s)-1, -1, -1):
            for c in range(r+1, len(s)):
                if c == r+1:
                    dp[r][c] = 1 if s[r]==s[c] else 0
                else:
                    dp[r][c] = 1 if s[r]==s[c] and dp[r+1][c-1]==1 else 0
        return sum([sum(row) for row in dp])
        