1215. Stepping Numbers

A Stepping Number is an integer such that all of its adjacent digits have an absolute difference of exactly `1`. For example, `321` is a Stepping Number while `421` is not.

Given two integers `low` and `high`, find and return a sorted list of all the Stepping Numbers in the range `[low, high]` inclusive.

**Example 1:**
```
Input: low = 0, high = 21
Output: [0,1,2,3,4,5,6,7,8,9,10,12,21]
```

**Constraints:**

* `0 <= low <= high <= 2 * 10^9`

# Solution
---
**Solution 1:**
```
Runtime: 348 ms
Memory Usage: 37.6 MB
```
```python
class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        def dfs(n):
            if n > high: 
                return 
            q.add(n)
            d = n % 10
            if d == 0:
                dfs(n * 10 + 1)
            elif d == 9:
                dfs(n * 10 + 8)
            else:
                dfs(n * 10 + d + 1) 
                dfs(n * 10 + d - 1)
        q = set()
        for i in range(10):
            dfs(i)
        return sorted(v for v in q if v >= low)
```

**Solution 2:**
```
Runtime: 292 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        q1, q2 = set(), collections.deque(range(10))
        while q2:
            n = q2.popleft()
            if low <= n <= high:
                q1.add(n)
            if n < high:
                d = n % 10
                if d == 0:
                    q2.append(n * 10 + 1)
                elif d == 9:
                    q2.append(n * 10 + 8)
                else:
                    q2.append(n * 10 + d + 1)
                    q2.append(n * 10 + d - 1)
        return sorted(q1)
```
