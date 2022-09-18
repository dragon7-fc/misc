2414. Length of the Longest Alphabetical Continuous Substring

An **alphabetical continuous** string is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string `"abcdefghijklmnopqrstuvwxyz"`.

* For example, `"abc"` is an alphabetical continuous string, while `"acb"` and `"za"` are not.

Given a string `s` consisting of lowercase letters only, return the length of the **longest** alphabetical continuous substring.

 

**Example 1:**
```
Input: s = "abacaba"
Output: 2
Explanation: There are 4 distinct continuous substrings: "a", "b", "c" and "ab".
"ab" is the longest continuous substring.
```

**Example 2:**
```
Input: s = "abcde"
Output: 5
Explanation: "abcde" is the longest continuous substring.
```

**Constraints:**

* `1 <= s.length <= 10^5`
* `s` consists of only English lowercase letters.

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 963 ms
Memory Usage: 14.9 MB
```
```python
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        cur = 1 ### We are currently at 0 position, so the length is 1.
        res = 1 ### At least the string should contain 1 letter.
        for i in range(1,len(s)):
        	### If the ith letter is continued from the previous letter, 
        	### update the curLength and store the maximum length to res
            if ord(s[i])-ord(s[i-1])==1:
                cur = cur+1
                res = max(cur,res)
            ### This is the start of a new substring with length 1.
            else:
                cur = 1
        return res
```

**Solution 2: (Greedy)**
```
Runtime: 141 ms
Memory Usage: 15.4 MB
```
```c++
class Solution {
public:
    int longestContinuousSubstring(string s) {
        int j = 0, res = 1;
        for (int i = 1; i < s.size(); ++i) {
            if (s[i] != s[j] + i - j)
                j = i;
            res = max(res, i - j + 1);
        }
        return res;
    }
};
```
