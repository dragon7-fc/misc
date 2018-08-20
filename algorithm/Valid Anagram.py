""" 
Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

"""


""" Solution1: 52 ms """
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        m = len(t)
        s_counter = collections.Counter(s)
        t_counter = collections.Counter(t)
        if s_counter == t_counter:
            return True
        return False


""" Solution2: 76 ms """
return True if s is None or t is None else sorted(s) == sorted(t)