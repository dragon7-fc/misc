1433. Check If a String Can Break Another String

Given two strings: `s1` and `s2` with the same size, check if some permutation of string `s1` can break some permutation of string `s2` or vice-versa (in other words `s2` can break `s1`).

A string `x` can break string `y` (both of size `n`) if `x[i] >= y[i]` (in alphabetical order) for all `i` between `0` and `n-1`.

 

**Example 1:**
```
Input: s1 = "abc", s2 = "xya"
Output: true
Explanation: "ayx" is a permutation of s2="xya" which can break to string "abc" which is a permutation of s1="abc".
```

**Example 2:**
```
Input: s1 = "abe", s2 = "acd"
Output: false 
Explanation: All permutations for s1="abe" are: "abe", "aeb", "bae", "bea", "eab" and "eba" and all permutation for s2="acd" are: "acd", "adc", "cad", "cda", "dac" and "dca". However, there is not any permutation from s1 which can break some permutation from s2 and vice-versa.
```

**Example 3:**
```
Input: s1 = "leetcodee", s2 = "interview"
Output: true
```

**Constraints:**

* `s1.length == n`
* `s2.length == n`
* `1 <= n <= 10^5`
* All strings consist of lowercase English letters.

# Submissions
---
**Solution 1: (Greedy)**

Check if `sorted(s1) >= sorted(s2)` or `sorted(s1) <= sorted(s2)` one by one.
```
Runtime: 196 ms
Memory Usage: 16.2 MB
```
```python
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        N = len(s1)
        sorted_s1 = sorted(s1)
        sorted_s2 = sorted(s2)
        return all(sorted_s1[i] >= sorted_s2[i] for i in range(N)) or all(sorted_s2[i] >= sorted_s1[i] for i in range(N))
```