1228. Missing Number In Arithmetic Progression

In some array `arr`, the values were in arithmetic progression: the values `arr[i+1] - arr[i]` are all equal for every `0 <= i < arr.length - 1`.

Then, a value from `arr` was removed that **was not the first or last value in the array**.

Return the removed value.

 

**Example 1:**
```
Input: arr = [5,7,11,13]
Output: 9
Explanation: The previous array was [5,7,9,11,13].
```

**Example 2:**
```
Input: arr = [15,13,12]
Output: 14
Explanation: The previous array was [15,14,13,12].
```

**Constraints:**

* `3 <= arr.length <= 1000`
* `0 <= arr[i] <= 10^5`

# Submissions
---
**Solution 1: (Arithmetic Sequence Sum)**

1. `arithmetic sequence sum = (first + last) * n / 2`
1. In this problem, the first and last value are not removed.
1. `first = min(A), last = max(A)`
1. We can calulate the `sum` of arithmetic sequence.
1. The difference between `sum - sum(A)` is the missing number.


```
Runtime: 68 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        return (min(arr) + max(arr)) * (len(arr) + 1) // 2 - sum(arr)
```

**Solution 2: (Binary Search)**
```
Runtime: 64 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        N = len(arr)
        d = (arr[-1] - arr[0]) // N
        left, right = 0, N
        while left < right:
            mid = (left + right) // 2
            if arr[mid] == arr[0] + d * mid:
                left = mid + 1
            else:
                right = mid
        return arr[0] + d * left
```