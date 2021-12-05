941. Valid Mountain Array

Given an array `A` of integers, return `true` if and only if it is a valid mountain array.

Recall that `A` is a mountain array if and only if:

* `A.length >= 3`
* There exists some `i` with `0 < i < A.length - 1` such that:
    * `A[0] < A[1] < ... A[i-1] < A[i]`
    * `A[i] > A[i+1] > ... > A[A.length - 1]`

![941_hint_valid_mountain_array.png](img/941_hint_valid_mountain_array.png)
 

**Example 1:**
```
Input: [2,1]
Output: false
```

**Example 2:**
```
Input: [3,5,5]
Output: false
```

**Example 3:**
```
Input: [0,3,2,1]
Output: true
```

**Note:**

* `0 <= A.length <= 10000`
* `0 <= A[i] <= 10000`

# Solution
---
## Approach 1: One Pass
**Intuition**

If we walk along the mountain from left to right, we have to move strictly up, then strictly down.

Algorithm

Let's walk up from left to right until we can't: that has to be the peak. We should ensure the peak is not the first or last element. Then, we walk down. If we reach the end, the array is valid, otherwise its not.

```python
class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of `A`.

* Space Complexity: $O(1)$.

# Submissions
---
**Solution 1: (One Pass)**
```
Runtime: 204 ms
Memory Usage: 15.7 MB
```
```python
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        N = len(arr)
        i = 0

        # walk up
        while i+1 < N and arr[i] < arr[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and arr[i] > arr[i+1]:
            i += 1

        return i == N-1
```

**Solution 2: (One Pass)**
```
Runtime: 236 ms
Memory Usage: 15.1 MB
```
```python
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        slope = 0
        for i in range(1, len(A)):
            if (slope == 0 or slope == 1) and A[i]-A[i-1] > 0:
                slope = 1
            elif (slope == 1 or slope == 2) and A[i]-A[i-1] < 0:
                slope = 2
            else:
                return False
            
        return slope == 2
```

**Solution 3: (Array)**
```
Runtime: 20 ms
Memory Usage: 7.1 MB
```
```c
bool validMountainArray(int* arr, int arrSize){
    int i = 0;
    while (i + 1 < arrSize && arr[i] < arr[i+1])
        i += 1;
    if (i == 0 || i == arrSize-1)
        return false;
    while (i+1 < arrSize && arr[i] > arr[i+1])
        i += 1;
    
    return i == arrSize-1;
}
```
