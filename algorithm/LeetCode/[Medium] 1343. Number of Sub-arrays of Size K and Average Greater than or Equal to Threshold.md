1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

Given an array of integers `arr` and two integers `k` and `threshold`.

Return the number of sub-arrays of size `k` and average greater than or equal to `threshold`.

 

**Example 1:**
```
Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
```

**Example 2:**
```
Input: arr = [1,1,1,1,1], k = 1, threshold = 0
Output: 5
```

**Example 3:**
```
Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.
```

**Example 4:**
```
Input: arr = [7,7,7,7,7,7,7], k = 7, threshold = 7
Output: 1
```

**Example 5:**
```
Input: arr = [4,4,4,4], k = 4, threshold = 1
Output: 1
``` 

**Constraints:**

* `1 <= arr.length <= 10^5`
* `1 <= arr[i] <= 10^4`
* `1 <= k <= arr.length`
* `0 <= threshold <= 10^4`

# Submissions
---
**Solution 1: (Prefix Sum)**

* Time: O(n), where n = a.length.
* space: O(1),

```
Runtime: 700 ms
Memory Usage: 25.7 MB
```
```python
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        prefixSum = [0]
        for i in arr:
            prefixSum.append(i + prefixSum[-1])
        return sum(prefixSum[i + k] - prefixSum[i] >= k * threshold for i in range(len(arr) - k + 1))
```

**Solution 2: (Two Pointer)**
```
Runtime: 764 ms
Memory Usage: 25.5 MB
```
```python
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        i = 0
        
        # Initial sum will be of arr[0:k], i.e s = sum(arr[0:k])
        s = sum(arr[:k])
        avg = s / k
        
        # Total no of required subarrays
        res = 0
        
        while (True):            
             # If current avg satisfies the condition
            if avg >= threshold:
                res += 1
            i += 1
            if i+k-1>n-1:
                break
                
             # Remove the starting value and add one more value
            s = s - arr[i-1] + arr[i+k-1]
            avg = s/k            
        return res
```