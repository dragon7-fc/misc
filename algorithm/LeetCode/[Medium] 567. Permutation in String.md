567. Permutation in String

Given two strings **s1** and **s2**, write a function to return `true` if **s2** contains the permutation of **s1**. In other words, one of the first string's permutations is the substring of the second string.

 

**Example 1:**
```
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
```

**Example 2:**
```
Input:s1= "ab" s2 = "eidboaoo"
Output: False
```

**Note:**

* The input strings only contain lower case letters.
* The length of both given strings is in range `[1, 10,000]`.

# Submissions
---
**Solution 1: (Two Pointers, Sliding Window)**
```
Runtime: 68 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        M, N = len(s1), len(s2)
        t = collections.Counter(s1)
        w = collections.Counter(s2[:M - 1])
        for i in range(M-1, N):
            w[s2[i]] += 1
            if w == t: 
                return True
            w[s2[i - M + 1]] -= 1
            if w[s2[i - M + 1]] == 0 : 
                del w[s2[i - M + 1]]

        return False
```