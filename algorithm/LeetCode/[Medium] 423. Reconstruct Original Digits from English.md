423. Reconstruct Original Digits from English

Given a **non-empty** string containing an out-of-order English representation of digits `0-9`, output the digits in ascending order.

**Note:**

1. Input contains only lowercase English letters.
1. Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
1. Input length is less than 50,000.

**Example 1:**
```
Input: "owoztneoer"

Output: "012"
```

**Example 2:**
```
Input: "fviefuro"

Output: "45"
```

# Submissions
---
**Solution 1: (Hash Table)**
```
Runtime: 44 ms
Memory Usage: 14.6 MB
```
```python
class Solution:
    def originalDigits(self, s: str) -> str:
        names = [('zero','z','0'),('two','w','2'),('four','u','4'),('six','x','6'),('eight','g','8'),('one','o','1'),('three','t','3'),\
                 ('five','f','5'),('seven','s','7'),('nine','i','9')]
        result = []
        cnt = collections.Counter(s)
        for name in names:
            count = cnt[name[1]]
            if not count: continue
            for c in name[0]: cnt[c] -= count
            result.append(name[2]*count)
        return ''.join(sorted(result))
```