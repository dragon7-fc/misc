2168. Unique Substrings With Equal Digit Frequency

Given a digit string `s`, return the number of **unique substrings** of `s` where every digit appears the same number of times.
 

**Example 1:**
```
Input: s = "1212"
Output: 5
Explanation: The substrings that meet the requirements are "1", "2", "12", "21", "1212".
Note that although the substring "12" appears twice, it is only counted once.
```

**Example 2:**
```
Input: s = "12321"
Output: 9
Explanation: The substrings that meet the requirements are "1", "2", "3", "12", "23", "32", "21", "123", "321".
```

**Constraints:**

* `1 <= s.length <= 1000`
* `s` consists of digits.

# Submissions
---
**Solution 1: (check all substring, rolling hash, O(N^2))**
```
Runtime: 6326 ms
Memory: 14.7 MB
```
```python
class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        res = set()

        def expand_from(i):
            cnt = collections.defaultdict(int)
            j = i + 1
            for c in s[i:]:
                cnt[c] += 1
                if s[i:j] not in res and len(set(cnt.values())) == 1:
                    res.add(s[i:j])
                j += 1
        for i in range(len(s)):
            expand_from(i)
        
        return len(res)
```
