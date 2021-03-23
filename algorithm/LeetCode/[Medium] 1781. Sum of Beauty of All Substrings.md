1781. Sum of Beauty of All Substrings

The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

* For example, the beauty of `"abaacc"` is `3 - 1 = 2`.

Given a string `s`, return the sum of beauty of all of its substrings.

 

**Example 1:**
```
Input: s = "aabcb"
Output: 5
Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
```

**Example 2:**
```
Input: s = "aabcbaa"
Output: 17
```

**Constraints:**

* `1 <= s.length <= 500`
* `s` consists of only lowercase English letters.

# Solutiobn 1: (Brute Force, Hash Table)
```
Runtime: 1932 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def beautySum(self, s: str) -> int:
        N = len(s)
        ans = 0
        for i in range(N):
            cnt = collections.defaultdict(int)
            for j in range(i, N):
                cnt[s[j]] += 1
                ans += max(cnt.values()) - min(cnt.values())
        return ans
```