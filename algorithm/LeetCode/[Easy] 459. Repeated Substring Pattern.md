459. Repeated Substring Pattern

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

**Example 1:**
```
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
```

**Example 2:**
```
Input: "aba"
Output: False
```

**Example 3:**
```
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
```

# Submissions
---
**Solution 1:**

**Example:**

To find if the string has a repeatable substring inside, we can create a new string by duplicating the original string.
Ex. "abcabc" => "abcabcabcabc"
By removing the first and last character of the new string we create the string "bcabcabcabcab"
If the original string "abcabc" is in "bcabcabcab", we return true.

**Why it works:**

If the original string has a repeating substring, the repeating substring can be no larger than 1/2 the length of the original string. I.e "xyxy" would be "xy"
By repeating the string and removing the first and last character of the new string, I.e "xyxyxyxy" => "yxyxyx", if the original string "xyxy" can be found in "yxyxyx", it means that "xyxy" has a repeating substring.

However, this solution doesn't tell us what the repeating substring is, but does solve the question if it exists.

```
Runtime: 28 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]
```

**Solution 2:**
```
Runtime: 60 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        
        for i in range(1,n//2+1):
            if n%i == 0:
                for j in range(i,n,i):
                    if s[0:i] != s[j:j+i]:
                        break
                    elif j==n-i:
                        return True
        return False
```