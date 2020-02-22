327. Count of Range Sum

Given an integer array `nums`, return the number of range sums that lie in `[lower, upper]` inclusive.
Range sum `S(i, j)` is defined as the sum of the elements in nums between indices `i` and `j` `(i ≤ j)`, inclusive.

**Note:**

* A naive algorithm of O(n2) is trivial. You MUST do better than that.

**Example:**
```
Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3 
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.
```

# Submissions
---
**Solution 1: (Prefix Sum, Hash Table)**
```
Runtime: 268 ms
Memory Usage: 13.3 MB
```
```python
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        N = len(nums)
        cumSum = [0]
        ans = 0
        for i in range(N):
            cumSum.append(cumSum[-1] + nums[i])
        record = collections.defaultdict(int)
        for csum in cumSum:
            for target in range(lower, upper+1):
                if csum - target in record:
                    ans += record[csum - target]
            record[csum] +=1
        return ans
```

**Solution 2: (Prefix Sum, Divide and Conquer, Merge Sort)**
```
Runtime: 216 ms
Memory Usage: 14.6 MB
```
```python
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        N = len(nums)
        cumSum = [0]
        for i in range(N):
            cumSum.append(cumSum[-1]+nums[i])
        ans = 0
        # inclusive
        def mergesort(l, r):
            if l == r:
                return 0
            mid = (l+r) // 2
            cnt = mergesort(l, mid) + mergesort(mid+1, r)

            i = j = mid+1
            # O(n)
            for left in cumSum[l:mid+1]:
                while i <= r and cumSum[i] - left < lower:
                    i += 1
                while j <= r and cumSum[j] - left <= upper:
                    j += 1
                cnt += j-i
                
            cumSum[l:r+1] = sorted(cumSum[l:r+1])
            return cnt

        return mergesort(0, N)
```