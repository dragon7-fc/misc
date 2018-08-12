""" 
Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
 """
 class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        palindrom_begin_at = 0
        max_len = 0
        palindrom = [[0 for x in range(n)] for y in range(n)]

        # trivial case: single letter palindroms
        for i in range(n):
            palindrom[i][i] = True
            palindrom_begin_at = i
            max_len = 1

        # finding palindroms of 2 characters
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                palindrom[i][i + 1] = True
                palindrom_begin_at = i
                max_len = 2

        # finding palindroms of length 3 to n and saving the longest
        for cur_len in range(3, n+1):
            for i in range(n - cur_len+1):
                j = i + cur_len-1

                # the first last character should match
                # and rest of the substring should be a palindrom
                if s[i] == s[j] and palindrom[i + 1][j - 1] == True: 
                    palindrom[i][j] = True
                    palindrom_begin_at = i
                    max_len = cur_len

        if max_len >= 1:
            return s[palindrom_begin_at:palindrom_begin_at+max_len]
        else:
            return ""