1999. Smallest Greater Multiple Made of Two Digits

Given three integers, `k`, `digit1`, and `digit2`, you want to find the **smallest** integer that is:

* **Larger** than `k`,
* A **multiple** of `k`, and
* Comprised of **only** the digits `digit1` and/or `digit2`.

Return the **smallest** such integer. If no such integer exists or the integer exceeds the limit of a signed 32-bit integer `(2^31 - 1)`, return `-1`.

 

**Example 1:**
```
Input: k = 2, digit1 = 0, digit2 = 2
Output: 20
Explanation:
20 is the first integer larger than 2, a multiple of 2, and comprised of only the digits 0 and/or 2.
```

**Example 2:**
```
Input: k = 3, digit1 = 4, digit2 = 2
Output: 24
Explanation:
24 is the first integer larger than 3, a multiple of 3, and comprised of only the digits 4 and/or 2.
```

**Example 3:**
```
Input: k = 2, digit1 = 0, digit2 = 0
Output: -1
Explanation:
No integer meets the requirements so return -1.
```

**Constraints:**

* `1 <= k <= 1000`
* `0 <= digit1 <= 9`
* `0 <= digit2 <= 9`

# Submissions
---
**Solution 1: (BFS)**
```
Runtime: 38 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        if digit1 == digit2 == 0:
            return -1
        
        isValid = lambda n: n > k and not n % k  
		
		# handle duplicate and find the sorted order of digits
        digits = sorted({digit1, digit2})
        
        # init queue and avoid leading zeros
        queue = collections.deque()
        for d in digits:
            if isValid(d): 
                return d
            if d > 0: 
                queue.append(d)
                
        MAX = (2 ** 31 - max(digits)) / 10
        num = queue.popleft()
        while num < MAX:
            for d in digits:
                queue.append(num * 10 + d)
                if isValid(queue[-1]): 
                    return queue[-1]
            num = queue.popleft()
        return -1
```
