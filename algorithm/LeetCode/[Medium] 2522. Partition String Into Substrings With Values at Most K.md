2522. Partition String Into Substrings With Values at Most K

You are given a string `s` consisting of digits from `1` to `9` and an integer `k`.

A partition of a string `s` is called **good** if:

* Each digit of `s` is part of **exactly** one substring.
* The value of each substring is less than or equal to `k`.

Return the **minimum** number of substrings in a **good** partition of `s`. If no **good** partition of `s` exists, return `-1`.

**Note** that:

* The **value** of a string is its result when interpreted as an integer. For example, the value of `"123"` is `123` and the value of `"1"` is `1`.
* A **substring** is a contiguous sequence of characters within a string.
 

**Example 1:**
```
Input: s = "165462", k = 60
Output: 4
Explanation: We can partition the string into substrings "16", "54", "6", and "2". Each substring has a value less than or equal to k = 60.
It can be shown that we cannot partition the string into less than 4 substrings.
```

**Example 2:**
```
Input: s = "238182", k = 5
Output: -1
Explanation: There is no good partition for this string.
```

**Constraints:**

* `1 <= s.length <= 10^5`
* `s[i]` is a digit from `'1'` to `'9'`.
* `1 <= k <= 10^9`

# Submissions
---
**Solution 1: (DP Top-Down)**
```
Runtime: 1994 ms
Memory: 205.1 MB
```
```python
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        N = len(s)

        @functools.lru_cache(None)
        def dp(i):
            if i == N:
                return 0
            rst = float('inf')
            j = i+1
            while j < N+1:
                cur = int(s[i:j])
                if cur > k:
                    break
                rst = min(rst, 1 + dp(j))
                j += 1
            return rst
        
        ans = dp(0)
        return ans if ans != float('inf') else -1
```

> **Solution 1: (Greedy)**
```
Runtime: 199 ms
Memory: 14.5 MB
```
```python
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        curr, ans = 0, 1
        for d in s:
            if int(d) > k:
                return -1
            curr = 10 * curr + int(d)
            if curr > k:
                ans += 1
                curr = int(d)
        return ans
```
