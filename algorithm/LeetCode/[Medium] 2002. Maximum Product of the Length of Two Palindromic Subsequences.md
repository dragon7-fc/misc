2002. Maximum Product of the Length of Two Palindromic Subsequences

Given a string `s`, find two **disjoint palindromic subsequences** of `s` such that the **product** of their lengths is **maximized**. The two subsequences are **disjoint** if they do not both pick a character at the same index.

Return the **maximum** possible **product** of the lengths of the two palindromic subsequences.

A **subsequence** is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters. A string is **palindromic** if it reads the same forward and backward.

 

**Example 1:**

![two-palindromic-subsequences](img/2002_two-palindromic-subsequences.png)
```
example-1
Input: s = "leetcodecom"
Output: 9
Explanation: An optimal solution is to choose "ete" for the 1st subsequence and "cdc" for the 2nd subsequence.
The product of their lengths is: 3 * 3 = 9.
```

**Example 2:**
```
Input: s = "bb"
Output: 1
Explanation: An optimal solution is to choose "b" (the first character) for the 1st subsequence and "b" (the second character) for the 2nd subsequence.
The product of their lengths is: 1 * 1 = 1.
```

**Example 3:**
```
Input: s = "accbcaxxcxx"
Output: 25
Explanation: An optimal solution is to choose "accca" for the 1st subsequence and "xxcxx" for the 2nd subsequence.
The product of their lengths is: 5 * 5 = 25.
```

**Constraints:**

* `2 <= s.length <= 12`
* `s` consists of lowercase English letters only.

# Submissions
---
**Solution 1: (Bitmask, Brute Force)**
```
Runtime: 3422 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def maxProduct(self, s: str) -> int:
        mem = {}
        n = len(s)
        for i in range(1,1<<n):
            tmp = ""
            for j in range(n):
                if i>>j & 1 == 1:
                    tmp += s[j]
            if tmp == tmp[::-1]:
                mem[i] = len(tmp)
        res = 0
        for i,x in mem.items():
            for j,y in mem.items():
                if i&j == 0:
                    res = max(res,x*y)
        return res
```
