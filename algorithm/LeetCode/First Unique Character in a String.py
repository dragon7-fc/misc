""" 
First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

"""


""" Solution1: 192 ms """
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """            
        n = len(s)
        dic = {}
        for i in range(n):
            if s[i] not in dic.keys():
                dic[s[i]] = i
            else:
                dic[s[i]] = -1
        result = list(filter(lambda x: x>=0, dic.values()))
        return min(result) if result else -1


""" Solution2: 192 ms """
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """            
        count = {}
        for ch in s:
            count[ch] = count.get(ch,0)+1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1
