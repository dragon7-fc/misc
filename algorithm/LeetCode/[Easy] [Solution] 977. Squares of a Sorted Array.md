977. Squares of a Sorted Array

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

**Example 1:**
```
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
```

**Example 2:**
```
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```

**Note:**

1. 1 <= `A.length` <= 10000
1. -10000 <= `A[i]` <= 10000
1. `A` is sorted in non-decreasing order.

# Solution
---
## Approach 1: Sort
**Intuition and Algorithm**

Create an array of the squares of each element, and sort them.

```python
class Solution(object):
    def sortedSquares(self, A):
        return sorted(x*x for x in A)
```

**Complexity Analysis**

* Time Complexity: $O(N \log N)$, where $N$ is the length of `A`.

* Space Complexity: $O(N)$.

## Approach 2: Two Pointer
**Intuition**

Since the array `A` is sorted, loosely speaking it has some negative elements with squares in decreasing order, then some non-negative elements with squares in increasing order.

For example, with `[-3, -2, -1, 4, 5, 6]`, we have the negative part `[-3, -2, -1]` with squares [9, 4, 1], and the positive part `[4, 5, 6]` with squares `[16, 25, 36]`. Our strategy is to iterate over the negative part in reverse, and the positive part in the forward direction.

**Algorithm**

We can use two pointers to read the positive and negative parts of the array - one pointer `j` in the positive direction, and another `i` in the negative direction.

Now that we are reading two increasing arrays (the squares of the elements), we can merge these arrays together using a two-pointer technique.

```python
class Solution(object):
    def sortedSquares(self, A):
        N = len(A)
        # i, j: negative, positive parts
        j = 0
        while j < N and A[j] < 0:
            j += 1
        i = j - 1

        ans = []
        while 0 <= i and j < N:
            if A[i]**2 < A[j]**2:
                ans.append(A[i]**2)
                i -= 1
            else:
                ans.append(A[j]**2)
                j += 1

        while i >= 0:
            ans.append(A[i]**2)
            i -= 1
        while j < N:
            ans.append(A[j]**2)
            j += 1

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of `A`.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution 1: (Sort)**
```
Runtime: 252 ms
Memory Usage: 15.6 MB
```
```python
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(x*x for x in A)
```

**Solution 2: (Two Pointer)**
```
Runtime: 324 ms
Memory Usage: 15.8 MB
```
```python
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        N = len(A)
        # i, j: negative, positive parts
        j = 0
        while j < N and A[j] < 0:
            j += 1
        i = j - 1

        ans = []
        while 0 <= i and j < N:
            if A[i]**2 < A[j]**2:
                ans.append(A[i]**2)
                i -= 1
            else:
                ans.append(A[j]**2)
                j += 1

        while i >= 0:
            ans.append(A[i]**2)
            i -= 1
        while j < N:
            ans.append(A[j]**2)
            j += 1

        return ans
```

**Solution 3: (Two Pointer)**
```
Runtime: 19 ms
Memory: 29.40 MB
```
```c++
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n = nums.size(), i, j;
        vector<int> ans;
        j = lower_bound(nums.begin(), nums.end(), 0) - nums.begin();
        i = j-1;
        while (i >= 0 && j < n) {
            if (nums[i]*nums[i] <= nums[j]*nums[j]) {
                ans.push_back(nums[i]*nums[i]);
                i -= 1;
            } else {
                ans.push_back(nums[j]*nums[j]);
                j += 1;
            }
        }
        while (i >= 0) {
            ans.push_back(nums[i]*nums[i]);
            i -= 1;
        }
        while (j < n) {
            ans.push_back(nums[j]*nums[j]);
            j += 1;
        }
        return ans;
    }
};
```

**Solution 4: (Two Pointer)**

    nums = [ -4, -1,  0,  3, 10]
             16   1   0   9 100
              l               r
              l           r
                  l       r
                  l   r
                      lr
    ans       0   1   9  10 100

```
Runtime: 17 ms
Memory: 28.48 MB
```
```c++
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n);
        for (int i = 0; i < n; i++) {
            nums[i] *= nums[i];
        }
        int i=nums.size()-1;
        int l = 0, r = nums.size()-1;

        while (l <= r) {
            if (nums[l] > nums[r]) {
                ans[i--] = nums[l++];
            } else {
                ans[i--] = nums[r--];
            }
        }

        return ans;
    }
};
```
