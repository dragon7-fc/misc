266. Palindrome Permutation

Given a string `s`, return `true` if a permutation of the string could form a palindrome.

 

**Example 1:**
```
Input: s = "code"
Output: false
```

**Example 2:**
```
Input: s = "aab"
Output: true
```

**Example 3:**
```
Input: s = "carerac"
Output: true
```

**Constraints:**

* `1 <= s.length <= 5000`
* `s` consists of only lowercase English letters.

# Submissions
---
**Solution 1: (Counter)**
```
Runtime: 32 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        cnt = collections.Counter(s)
        odd, even = 0, 0
        for val in cnt.values():
            if val%2:
                odd += 1
            else:
                even += 1
        return False if odd > 1 else True
```

**Solution 2: (Single Pass)**
```
Runtime: 28 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        d = collections.defaultdict(int)
        count = 0
        for i in range(len(s)):
            d[s[i]] += 1
            if d[s[i]] % 2 == 0:
                count -= 1
            else:
                count += 1
        return count <= 1
```

**Solution 3: (Set)**
```
Runtime: 32 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        a = set()
        for c in s:
            if c in a:
                a -= set(c)
            else:
                a |= set(c)
        return len(a) <= 1
```