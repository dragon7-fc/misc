248. Strobogrammatic Number III

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

**Example:**
```
Input: low = "50", high = "100"
Output: 3 
Explanation: 69, 88, and 96 are three strobogrammatic numbers.
```

**Note:**

* Because the range might be a large number, the low and high numbers are represented as string.

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 364 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        dic = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        mid_set = set(["0", "1", "8"])
        cnt = 0
        def dfs(cur, length):
            nonlocal cnt, dic, low, high
            if len(cur) == length:
                if len(cur) != 1 and cur[0] == '0': return
                if (length == len(low) and int(low) > int(cur)) or (length == len(high) and int(cur) > int(high)): return
                cnt += 1
                return
            for add in dic:
                if len(cur)+2 <= length:
                    dfs(add+cur+dic[add], length)

        for l in range(len(low), len(high) + 1):
            if not l%2:
                dfs("", l)
            else:
                for start in mid_set:
                    dfs(start, l)
        return cnt
```