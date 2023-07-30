852. Peak Index in a Mountain Array

Let's call an array `A` a mountain if the following properties hold:

* `A.length >= 3`
* There exists some `0 < i < A.length - 1` such that `A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]`

Given an array that is definitely a mountain, return any `i` such that `A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]`.

**Example 1:**
```
Input: [0,1,0]
Output: 1
```

**Example 2:**
```
Input: [0,2,1,0]
Output: 1
```

**Note:**

* `3 <= A.length <= 10000`
* `0 <= A[i] <= 10^6`
* `A` is a mountain, as defined above.

# Solution
---
## Approach 1: Linear Scan
**Intuition and Algorithm**

The mountain increases until it doesn't. The point at which it stops increasing is the peak.

```python
class Solution(object):
    def peakIndexInMountainArray(self, A):
        for i in xrange(len(A)):
            if A[i] > A[i+1]:
                return i
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of `A`.

* Space Complexity: $O(1)$.

## Approach 2: Binary Search
**Intuition and Algorithm**

The comparison `A[i] < A[i+1]` in a mountain array looks like `[True, True, True, ..., True, False, False, ..., False]`: 1 or more boolean Trues, followed by 1 or more boolean False. For example, in the mountain array `[1, 2, 3, 4, 1]`, the comparisons `A[i] < A[i+1]` would be `True, True, True, False`.

We can binary search over this array of comparisons, to find the largest index `i` such that `A[i] < A[i+1]`. For more on binary search, see the [LeetCode explore topic here](https://leetcode.com/explore/learn/card/binary-search/).

```python
class Solution(object):
    def peakIndexInMountainArray(self, A):
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mi = (lo + hi) / 2
            if A[mi] < A[mi + 1]:
                lo = mi + 1
            else:
                hi = mi
        return lo
```

**Complexity Analysis**

* Time Complexity: $O(\log N)$, where $N$ is the length of `A`.

* Space Complexity: $O(1)$.

# Submissions
---
**Solution:**
```
Runtime: 80 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if A[mi] < A[mi + 1]:
                lo = mi + 1
            else:
                hi = mi
        return lo
```

**Solution 2: (Binary Search)**
```
Runtime: 15 ms
Memory Usage: 6.5 MB
```
```c


int peakIndexInMountainArray(int* arr, int arrSize){
    int left = 0, right = arrSize-1, mid;
    while (left < right) {
        mid = (left+right)/2;
        if (arr[mid] < arr[mid+1])
            left = mid+1;
        else
            right = mid;
    }
    return right;
}
```

**Solution 3: (Binary Search)**
```
Runtime: 11 ms
Memory Usage: 6.5 MB
```
```c


int peakIndexInMountainArray(int* arr, int arrSize){
    int low = 1, high = arrSize-2;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid - 1] < arr[mid] && arr[mid] > arr[mid + 1])
            return mid;
        else if(arr[mid - 1] < arr[mid] && arr[mid] < arr[mid + 1])
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}
```

**Solution 4: (Binary Search)**
```
Runtime: 119 ms
Memory: 59.7 MB
```
```c++
class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int mid, left = 1, right = arr.size()-2;
        while (left <= right) {
            mid = left + (right-left)/2;
            if (arr[mid-1] < arr[mid] && arr[mid] > arr[mid+1]) {
                return mid;
            } else if (arr[mid-1] < arr[mid] && arr[mid] < arr[mid+1]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }
};
```
