905. Sort Array By Parity

Given an array `A` of non-negative integers, return an array consisting of all the even elements of `A`, followed by all the odd elements of `A`.

You may return any answer array that satisfies this condition.

 

**Example 1:**
```
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
```

**Note:**

1. `1 <= A.length <= 5000`
1. `0 <= A[i] <= 5000`

# Solution
---

## Approach 1: Sort
**Intuition and Algorithm**

Use a custom comparator when sorting, to sort by parity.

```python
class Solution(object):
    def sortArrayByParity(self, A):
        A.sort(key = lambda x: x % 2)
        return A
```

**Complexity Analysis**

* Time Complexity: $O(N \log N)$, where $N$ is the length of `A`.

* Space Complexity: $O(N)$ for the sort, depending on the built-in implementation of sort.

## Approach 2: Two Pass
**Intuition and Algorithm**

Write all the even elements first, then write all the odd elements.

```python
class Solution(object):
    def sortArrayByParity(self, A):
        return ([x for x in A if x % 2 == 0] +
                [x for x in A if x % 2 == 1])
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of `A`.

* Space Complexity: $O(N)$ for the sort, depending on the built-in implementation of sort.

## Approach 3: In-Place
**Intuition**

If we want to do the sort in-place, we can use quicksort, a standard textbook algorithm.

**Algorithm**

We'll maintain two pointers `i` and `j`. The loop invariant is everything below i has parity 0 (ie. `A[k] % 2 == 0` when `k < i`), and everything above `j` has parity 1.

Then, there are 4 cases for ($A[i] % 2$):

*　If it is `(0, 1)`, then everything is correct: `i++` and `j--`.

* If it is `(1, 0)`, we swap them so they are correct, then continue.

* If it is `(0, 0)`, only the `i` place is correct, so we `i++` and continue.

* If it is `(1, 1)`, only the `j` place is correct, so we `j--` and continue.

Throughout all 4 cases, the loop invariant is maintained, and `j-i` is getting smaller. So eventually we will be done with the array sorted as desired.

```python
class Solution(object):
    def sortArrayByParity(self, A):
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0: i += 1
            if A[j] % 2 == 1: j -= 1

        return A
```

## Submissions
---
**Solution: (In-Place)**
```
Runtime: 92 ms
Memory Usage: 14.5 MB
```
```python
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0: i += 1
            if A[j] % 2 == 1: j -= 1

        return A
```

**Solution 1: (Two Pointers)**
```
Runtime: 80 ms
Memory Usage: 13.4 MB
```
```python
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1
        while True:
            while i < j and not A[i] & 1: i += 1
            while i < j and A[j] & 1: j -= 1
            if i < j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
            else:
                break
        return A
```

**Solution 2: (In-Place)**
```
Runtime: 23 ms
Memory Usage: 16.2 MB
```
```c++
class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        int i = 0, j = nums.size()-1;
        while (i < j) {
            if (nums[i] % 2 > nums[j] % 2) {
                int tmp = nums[i];
                nums[i] = nums[j];
                nums[j] = tmp;
            }

            if (nums[i] % 2 == 0) i++;
            if (nums[j] % 2 == 1) j--;
        }

        return nums;
    }
};
```
