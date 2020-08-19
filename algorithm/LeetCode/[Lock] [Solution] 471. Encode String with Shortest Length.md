471. Encode String with Shortest Length

Given a **non-empty** string, encode the string such that its encoded length is the shortest.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly k times.

**Note:**

* k will be a positive integer and encoded string will not be empty or have extra space.
* You may assume that the input string contains only lowercase English letters. The string's length is at most 160.
* If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return any of them is fine.
 

**Example 1:**
```
Input: "aaa"
Output: "aaa"
Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.
```

**Example 2:**
```
Input: "aaaaa"
Output: "5[a]"
Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
```

**Example 3:**
```
Input: "aaaaaaaaaa"
Output: "10[a]"
Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5, which is the same as "10[a]".
```

**Example 4:**
```
Input: "aabcaabcd"
Output: "2[aabc]d"
Explanation: "aabc" occurs twice, so one answer can be "2[aabc]d".
```

**Example 5:**
```
Input: "abbbabbbcabbbabbbc"
Output: "2[2[abbb]c]"
Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to "2[abbb]c", so one answer can be "2[2[abbb]c]".
```

# Submissions
---
**Solution 1: (DP Top-Down)**

For any s, you can either

1. Do not encode it
1. Or encode it to one string if possible
1. Or, split it into two, encode the two substring to their shortest possible length, and combine them

Pick up the shortest result from 1~3.
During this process, you should remember the best encoding result for all substrings so that it can be reused.

For #2, you can use LeetCode 459: Repeated Substring Pattern to find out whether the "s" is repeated or not, and how many times it is repeated:
"i=(s+s).find(s,1)"
"i" is the length of repeating pattern. If i>=len(s), then s is not repeated.

```
Runtime: 264 ms
Memory Usage: 16.1 MB
```
```python
class Solution:
    @functools.lru_cache(None)
    def encode(self, s: str) -> str:
        i = (s+s).find(s,1)
        encoded = str(len(s)//i) + '[' + self.encode(s[:i])+ ']' if i < len(s) else s
        splitEncoded = [self.encode(s[:i]) + self.encode(s[i:]) for i in range(1,len(s))]
        return min(splitEncoded + [encoded], key=len)
```