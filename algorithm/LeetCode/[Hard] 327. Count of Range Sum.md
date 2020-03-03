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

**Solution 3: (Prefix Sum, Binary Search)**
```
Runtime: 156 ms
Memory Usage: 13.2 MB
```
```python
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix=[0]
        for num in nums:
            prefix.append(prefix[-1]+num)
        prefix.pop(0)
        cur,res = [0],0
        for val in prefix:
            idx1 = bisect.bisect_right(cur,val-lower)
            idx2 = bisect.bisect_left(cur,val-upper)
            res+=idx1-idx2
            bisect.insort(cur,val)
            
        return res
```

**Solution 4: (Binary Indexed Tree)**
```
Runtime: 252 ms
Memory Usage: 13.2 MB
```
```python
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        preSums = [0] 
        for num in nums:
            preSums.append(preSums[-1] + num)
        
        sorted_preSums = sorted(preSums)
        count = 0
        
        self.len = len(preSums) + 1
        self.BIT = [0] * self.len
        
        for preSum in preSums:
            right = bisect.bisect_right(sorted_preSums, preSum - lower)
            left = bisect.bisect_left(sorted_preSums, preSum - upper) 
            count += self.getCount(right) - self.getCount(left)
            self.update(bisect.bisect_right(sorted_preSums, preSum))
        return count
    
    def getCount(self, i):
        count = 0
        while i > 0:
            count += self.BIT[i]
            i -= i & -i
        return count
    
    def update(self, i):
        while i < self.len:
            self.BIT[i] += 1
            i += i & -i
```