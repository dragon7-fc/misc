2516. Take K of Each Character From Left and Right

You are given a string `s` consisting of the characters `'a'`, `'b'`, and `'c'` and a non-negative integer `k`. Each minute, you may take either the **leftmost** character of `s`, or the **rightmost** character of `s`.

Return the **minimum** number of minutes needed for you to take **at least** `k` of each character, or return `-1` if it is not possible to take `k` of each character.

 

**Example 1:**
```
Input: s = "aabaaaacaabc", k = 2
Output: 8
Explanation: 
Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.
```

**Example 2:**

Input: s = "a", k = 1
Output: -1
Explanation: It is not possible to take one 'b' or 'c' so return -1.
 

**Constraints:**

* `1 <= s.length <= 10^5`
* `s` consists of only the letters `'a'`, `'b'`, and `'c'`.
* `0 <= k <= s.length`

# Submissions
---
**Solution 1: (inverse Sliding Window)**
```
Runtime: 657 ms
Memory: 14.8 MB
```
```python
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        N = len(s)
        ta, tb, tc = s.count('a'), s.count('b'), s.count('c')
        cur = [0, 0, 0]
        ans = float('inf')
        i = 0
        for j in range(N):
            cur[ord(s[j]) - ord('a')] += 1
            while i <= j and (ta-cur[0] < k or tb - cur[1] < k or tc - cur[2] < k):
                cur[ord(s[i]) - ord('a')] -= 1
                i += 1 
            if ta - cur[0] >= k and tb - cur[1] >= k and tc - cur[2] >= k:
                ans = min(ans, N - (j-i+1))
            j += 1
        if ans == float('inf'):
            return -1
        return ans
```
