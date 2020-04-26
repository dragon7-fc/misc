1191. K-Concatenation Maximum Sum

Given an integer array `arr` and an integer `k`, modify the array by repeating it `k` times.

For example, if `arr = [1, 2]` and `k = 3` then the modified array will be `[1, 2, 1, 2, 1, 2]`.

Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be `0` and its sum in that case is `0`.

As the answer can be very large, return the answer **modulo** `10^9 + 7`.

**Example 1:**

```
Input: arr = [1,2], k = 3
Output: 9
```

**Example 2:**

```
Input: arr = [1,-2,1], k = 5
Output: 2
```

**Example 3:**

```
Input: arr = [-1,-2], k = 7
Output: 0
```

**Constraints:**

* `1 <= arr.length <= 10^5`
* `1 <= k <= 10^5`
* `-10^4 <= arr[i] <= 10^4`

# Submissions
---
**Solution 1: (Case Study)**
```
Runtime: 412 ms
Memory Usage: 26 MB
```
```python
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        '''
        0.默认最小值是0，一个元素也不取
        1.一个array组成:arr[i->j] 一段array的最大值；
        2.两个array:arr[i->len(arr)](后缀和)+arr[0->j](前缀和最大值)
        3.多个array:arr[i->len(arr)](后缀和)+(k-2)*sum(中间)+arr[0->j](前缀和最大值)
        ''' 
        
        s = dp = prefix_max_sum = prefix_min_sum = 0
        max_dp = 0
        
        for i in range(len(arr)):
            s += arr[i]
            dp = max(arr[i], dp+arr[i]) #最大连续和
            max_dp = max(max_dp, dp)
            #最小前缀和与最大前缀和
            prefix_max_sum = max(prefix_max_sum, s)
            prefix_min_sum = min(prefix_min_sum, s)
        
        suffix_max_sum = s - prefix_min_sum
        
        if k==1:
            res = max_dp
        elif k==2:
            res = max(0, max_dp, prefix_max_sum+suffix_max_sum)
        else:
            if s<=0:
                res = max(0, max_dp, prefix_max_sum+suffix_max_sum)
            else:
                res = max(0, max_dp, prefix_max_sum+suffix_max_sum+(k-2)*s)
        return res%(10**9+7)         
```

**Solution 2: (Kanane's Algorithm, DP Bottom-Up)**
```
Runtime: 356 ms
Memory Usage: 26.9 MB
```
```python
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        total = sum(arr)
        
        def maxSubArraySum(a):
            size = len(a)
            max_so_far = float('-inf')
            max_ending_here = 0

            for i in a:
                max_ending_here += i
                if max_ending_here < 0: max_ending_here=0
                max_so_far = max(max_so_far, max_ending_here)

            return max_so_far
        
        kadanes = maxSubArraySum(arr)
        if (k < 2): return kadanes%(10**9+7)
        if (total > 0): return (kadanes + (k-1)*total)%(10**9+7)
        stitchedKadanes = maxSubArraySum(arr*2)
        return stitchedKadanes%(10**9+7)
```

**Solution 3: (Kanane's Algorithm, DP Bottom-Up)**
```
Runtime: 444 ms
Memory Usage: 27.1 MB
```
```python
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        N = len(arr)
        if arr == None or N == 0: return 0
        maxOfEnd = arr[0] if arr[0] > 0 else 0
        maxSoFar, total = maxOfEnd, arr[0]
        for i in range(1, min(k, 2)*N):
            maxOfEnd = max(maxOfEnd + arr[i % N], arr[i % N])
            maxSoFar = max(maxOfEnd, maxSoFar)
            if i < N:
                total += arr[i]
        k -= 1
        while total > 0 and k >= 2:
            maxSoFar = (maxSoFar + total) % 1000000007
            k -= 1
            
        return maxSoFar
```