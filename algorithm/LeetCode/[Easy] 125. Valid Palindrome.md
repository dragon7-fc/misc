125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

**Note:** For the purpose of this problem, we define empty string as valid palindrome.

**Example 1:**
```
Input: "A man, a plan, a canal: Panama"
Output: true
```

**Example 2:**
```
Input: "race a car"
Output: false
```

# Submissions
---
**Solution 1: (String)**
```
Runtime: 52 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filter_str = [*filter(lambda c:c.isdigit() or c.isalpha(), s.lower())]  # list(filter(lambda c:c.isdigit() or c.isalpha(), s.lower()))
        return filter_str[::-1] == filter_str
```