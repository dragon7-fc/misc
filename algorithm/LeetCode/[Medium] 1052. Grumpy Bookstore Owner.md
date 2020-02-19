1052. Grumpy Bookstore Owner

Today, the bookstore owner has a store open for `customers.length` minutes.  Every minute, some number of customers (`customers[i]`) enter the store, and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the `i`-th minute, `grumpy[i] = 1`, otherwise `grumpy[i] = 0`.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for `X` minutes straight, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

 

**Example 1:**
```
Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
``` 

**Note:**

1. `1 <= X <= customers.length == grumpy.length <= 20000`
1. `0 <= customers[i] <= 1000`
1. `0 <= grumpy[i] <= 1`

# Submissions
---
**Solution 1: (Sliding Window)**
```
Runtime: 344 ms
Memory Usage: 16.1 MB
```
```python
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        N = len(customers)
        satisfy = 0
        ans, tmp_ans = 0, 0
        for i in range(N):
            if not grumpy[i]:
                satisfy += customers[i]
        j = 0
        tmp_ans = satisfy
        while j < X:
            if grumpy[j]:
                tmp_ans += customers[j]
            j += 1
        ans = tmp_ans
        for i in range(1, N):
            if j < N and grumpy[j]:
                tmp_ans += customers[j]
            if grumpy[i-1]:
                tmp_ans -= customers[i-1]
            ans = max(ans, tmp_ans)
            j += 1
        return ans
```