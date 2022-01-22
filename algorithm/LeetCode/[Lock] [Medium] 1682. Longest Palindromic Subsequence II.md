1682. Longest Palindromic Subsequence II

A subsequence of a string `s` is considered a **good palindromic subsequence** if:

* It is a subsequence of `s`.
* It is a palindrome (has the same value if reversed).
* It has an **even** length.
* No two consecutive characters are equal, except the two middle ones.

For example, if `s = "abcabcabb"`, then `"abba"` is considered a **good palindromic subsequence**, while `"bcb"` (not even length) and `"bbbb"` (has equal consecutive characters) are not.

Given a string `s`, return the **length** of the **longest good palindromic subsequence** in `s`.

 

**Example 1:**
```
Input: s = "bbabab"
Output: 4
Explanation: The longest good palindromic subsequence of s is "baab".
```

**Example 2:**
```
Input: s = "dcbccacdb"
Output: 4
Explanation: The longest good palindromic subsequence of s is "dccd".
```

**Constraints:**

* `1 <= s.length <= 250`
* `s` consists of lowercase English letters.

# Submissions
---
**Solution 1: (DP Top-Down)**
```
Runtime: 1079 ms
Memory Usage: 15 MB
```
```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        char_to_indices = defaultdict(list)
        for index, char in enumerate(s):
            char_to_indices[char].append(index)
        import bisect

        @lru_cache(None)
        def longest(last_char, start, end):
            if start >= end - 1: return 0
            max_length = 0
            for begin in range(start, end):
                if (char := s[begin]) == last_char: continue
                end_i = bisect.bisect_left(char_to_indices[char], end) - 1
                if end_i >= 0 and begin < (last := char_to_indices[char][end_i]):
                    max_length = max(max_length, 2 + longest(char, begin + 1, last))
            return max_length

        return longest('', 0, len(s))
```
