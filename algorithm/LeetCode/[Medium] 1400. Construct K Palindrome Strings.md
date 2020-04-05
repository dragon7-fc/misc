1400. Construct K Palindrome Strings

Given a string `s` and an integer k. You should construct `k` non-empty palindrome strings using all the characters in `s`.

Return `True` if you can use all the characters in s to construct `k` palindrome strings or `False` otherwise.

 

**Example 1:**
```
Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
```

**Example 2:**
```
Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.
```

**Example 3:**
```
Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.
```

**Example 4:**
```
Input: s = "yzyzyzyzyzyzyzy", k = 2
Output: true
Explanation: Simply you can put all z's in one string and all y's in the other string. Both strings will be palindrome.
```

**Example 5:**
```
Input: s = "cr", k = 7
Output: false
Explanation: We don't have enough characters in s to construct 7 palindromes.
```

**Constraints:**

* `1 <= s.length <= 10^5`
* All characters in `s` are lower-case English letters.
* `1 <= k <= 10^5`

# Submissions
---
**Solution 1: (Math)**

**Explanation**

* Condition 1. `odd characters <= k`

Count the occurrences of all characters.  
If one character has odd times occurrences,  
there must be at least one palindrome,  
with odd length and this character in the middle.  
So we count the characters that appear odd times,  
the number of odd character should not be bigger than k.

* Condition 2. `k <= s.length()`

Also, if we have one character in each palindrome,  
we will have at most `s.length()` palindromes,  
so we need `k <= s.length()`.

The above two condition are necessary and sufficient conditions for this problem.  
So we return `odd <= k <= n`

```
Runtime: 76 ms
Memory Usage: 14.6 MB
```
```python
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return sum(i & 1 for i in collections.Counter(s).values()) <= k <= len(s)
```