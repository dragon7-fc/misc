523. Continuous Subarray Sum

Given a list of **non-negative numbers** and a target **integer** k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of **k**, that is, sums up to n\*k where n is also an **integer**.

 

**Example 1:**
```
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
```

**Example 2:**
```
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
```

**Note:**

* The length of the array won't exceed 10,000.
* You may assume the sum of all the numbers is in the range of a signed 32-bit integer.

# Submissions
---
**Solution 1: (DP Top Down, Line 13: RecursionError: maximum recursion depth exceeded
Last executed i)**
```python
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        if N < 2: return 0
        
        @functools.lru_cache(None)
        def dp(i, j ,target):
            if j >= N:
                return False
            target += nums[j]
            if j - i >= 1 and (k and target%k == 0 or k == 0 and target == 0):
                return True
            return dp(i, j+1, target) or dp(i+1, i+1, 0)
            
        return dp(0, 0, 0)
```

**Solution 1: (Greedy, Prefix Sum, Math)**

At first, we calculate prefix_sum cumsum
d = b - a( b is on the right of a).
what we want is that d is multiple of k, so we just need d % k = 0.
Because d = b - a, so d % k = 0 -> (b - a) %k. = 0.
So (b-a)%k=0 --> b%k - a%k = 0, then b%k = a%k.

```
Runtime: 276 ms
Memory Usage: 14.6 MB
```
```python
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cumsum = [0]
        for n in nums:
            cumsum.append(cumsum[-1]+n)
        record = {}
        for a,b in zip(cumsum[:-1],cumsum[1:]):  # subarry need at least 2 elements
            b = b%k if k else b
            a = a%k if k else a
            if b in record:
                return True
            record[a] = 1 
        return False
```

**Solution 2: (Hash Table, Greedy, Prefix Sum, (a+b) % c = a%c + b %c)**
```
Runtime: 568 ms
Memory: 113.8 MB
```
```c++
class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        int cur = 0;
        // Only store the first index for a ps.
        unordered_map<int, int> m;
        for (int i = 0; i < n; ++i) {
            cur = (cur + nums[i]) % k;
            // Sum from the start is a multiple of k.
            if (cur == 0 && i > 0) return true;
            // If ps doesn't exist before, insert it.
            if (m.count(cur) == 0) m[cur] = i;
            // Otherwise return true, only if the index diff is > 1.
            else if (i - m[cur] > 1) return true;
        }
        return false;
    }
};
```
