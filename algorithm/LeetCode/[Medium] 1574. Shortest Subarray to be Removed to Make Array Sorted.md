1574. Shortest Subarray to be Removed to Make Array Sorted

Given an integer array `arr`, remove a subarray (can be empty) from `arr` such that the remaining elements in `arr` are non-decreasing.

A subarray is a contiguous subsequence of the array.

Return the length of the shortest subarray to remove.

 

**Example 1:**
```
Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].
```

**Example 2:**
```
Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
```

**Example 3:**
```
Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.
```

**Example 4:**
```
Input: arr = [1]
Output: 0
```

**Constraints:**

* `1 <= arr.length <= 10^5`
* `0 <= arr[i] <= 10^9`

# Submissions
---
**Solution 1: (Two Pointers, remove front, tail or middle)**
```
Runtime: 636 ms
Memory Usage: 28.2 MB
```
```python
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        N = len(arr)
        left, right = 0, N - 1
        while left + 1 < N and arr[left] <= arr[left + 1]:
            left += 1
        if left == N - 1: 
            return 0
        while right > left and arr[right - 1] <= arr[right]:
            right -= 1
        ans = min(N - left - 1, right)
        i, j = 0, right
        while i <= left and j < N:
            if arr[j] >= arr[i]:
                ans = min(ans, j - i - 1)
                i += 1
            else:
                j += 1
        return ans
```

**Solution 2: (Two Pointers)**
```
Runtime: 0 ms
Memory: 69.54 MB
```
```c++
class Solution {
public:
    int findLengthOfShortestSubarray(vector<int>& arr) {
        int right = arr.size() - 1;
        while (right > 0 && arr[right] >= arr[right - 1]) {
            right--;
        }

        int ans = right;
        int left = 0;
        while (left < right && (left == 0 || arr[left - 1] <= arr[left])) {
            // find next valid number after arr[left]
            while (right < arr.size() && arr[left] > arr[right]) {
                right++;
            }
            // save length of removed subarray
            ans = min(ans, right - left - 1);
            left++;
        }
        return ans;
    }
};
```

**Solution 3: (Two Pointers)**

                    /
                  / 
                /  
       / 
     /
    ^i          ^j  ^n-1
        ^left   ^right
```
Runtime: 0 ms
Memory: 69.58 MB
```
```c++
class Solution {
public:
    int findLengthOfShortestSubarray(vector<int>& arr) {
        int n = arr.size(), left = 0, right = n-1, i, j, ans;

        // remove right or left area
        while (left+1 < n && arr[left+1] >= arr[left]) {
            left += 1;
        }
        if (left == n-1) {
            return 0;
        }
        while (right-1 >= 0 && arr[right-1] <= arr[right]) {
            right -= 1;
        }
        ans = min(n-left-1, right);

        // remove middle area
        i = 0, j = right;
        while (i <= left && j < n) {
            if (arr[i] <= arr[j]) {
                ans = min(ans, j-i-1);
                i += 1;
            } else {
                j += 1;
            }
        }
        return ans;
    }
};
```
