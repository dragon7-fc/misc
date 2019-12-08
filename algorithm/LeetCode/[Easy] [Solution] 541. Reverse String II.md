541. Reverse String II

Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

**Example:**
```
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
```

**Restrictions:**

* The string consists of lower English letters only.
* Length of the given string and k will in the range `[1, 10000]`

# Solution
---
## Approach #1: Direct [Accepted]
**Intuition and Algorithm**

We will reverse each block of `2k` characters directly.

Each block starts at a multiple of `2k`: for example, `0`, `2k`, `4k`, `6k`, .... One thing to be careful about is we may not reverse each block if there aren't enough characters.

To reverse a block of characters from `i` to `j`, we can swap characters in positions `i++` and `j--``.

```python
class Solution(object):
    def reverseStr(self, s, k):
        a = list(s)
        for i in xrange(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the size of `s`. We build a helper array, plus reverse about half the characters in `s`.

* Space Complexity: $O(N)$, the size of `a`.

# Submissions
---
**Solution:**
```
Runtime: 32 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)
```