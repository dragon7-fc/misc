392. Is Subsequence

Given a string **s** and a string **t**, check if **s** is subsequence of **t**.

You may assume that there is only lower case English letters in both **s** and **t**. **t** is potentially a very long (length ~= 500,000) string, and **s** is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

**Example 1:**
```
s = "abc", t = "ahbgdc"

Return true.
```

**Example 2:**
```
s = "axc", t = "ahbgdc"

Return false.
```

**Follow up:**

* If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

**Credits:**

* Special thanks to @pbrother for adding this problem and creating all test cases.

# Submissions
---
**Solution 1: (Two Pointers)**
```
Runtime: 224 ms
Memory Usage: 18.4 MB
```
```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        j = 0
        for i in range(len(t)):
            if t[i] == s[j]:
                j += 1
            if j == len(s):
                return True
        return False
```

**Solution 2: (Two Pointers)**
```
Rntime: 0 ms
Memory Usage: 6.4 MB
```
```c++
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i = 0, j = 0;
        while(j < t.size() and i < s.size()) {
            if(s[i] == t[j])
                i++, j++;
            else 
                j++;
        }
        
        return i == s.size();
    }
};
```
