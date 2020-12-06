1679. Max Number of K-Sum Pairs

You are given an integer array `nums` and an integer `k`.

In one operation, you can pick two numbers from the array whose sum equals `k` and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

**Example 1:**
```
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
```

**Example 2:**
```
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`
* `1 <= k <= 10^9`

# Submissions
---
**Solution 1: (Two Pointers)**
```
Runtime: 652 ms
Memory Usage: 26.7 MB
```
```python
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0, len(nums)-1
        res = 0
        while i < j :
            summ = nums[i]+nums[j]
            if summ == k:
                i += 1
                j -= 1
                res += 1
            elif summ < k:
                i += 1
            else:
                j -= 1
        return res
```

**Solution 2: (Counter)**
```
Runtime: 644 ms
Memory Usage: 27.3 MB
```
```python
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = Counter(nums)
        ans = 0
        for key in d.keys():
            if key * 2 == k:
                ans += d[key] // 2
            elif d[k - key] > 0:
                mi = min(d[key], d[k - key])
                d[key] -= mi     
                d[k - key] -= mi
                ans += mi
        return ans
```