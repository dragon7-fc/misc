1641. Count Sorted Vowel Strings

Given an integer `n`, return the number of strings of length `n` that consist only of vowels (`a`, `e`, `i`, `o`, `u`) and are **lexicographically sorted**.

A string `s` is **lexicographically sorted** if for all valid `i`, `s[i]` is the same as or comes before `s[i+1]` in the alphabet.

 

**Example 1:**
```
Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
```

**Example 2:**
```
Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
```

**Example 3:**
```
Input: n = 33
Output: 66045
```

**Constraints:**

* `1 <= n <= 50`

# Submissions
---
**Solution 1: (DP TOP-Down)**
```
Runtime: 32 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        @lru_cache(None)
        def dp(n, i):
            if n == 0: return 1  # Found a valid answer
            if i == 5:  return 0  # Reach to length of vowels [a, e, i, o, u]
            ans = dp(n, i + 1)  # Skip vowels[i]
            ans += dp(n - 1, i)  # Include vowels[i]
            return ans

        return dp(n, 0)
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 32 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [0] + [1] * 5
        for i in range(1, n + 1):
            for k in range(1, 6):
                dp[k] += dp[k - 1]
        return dp[5]
```