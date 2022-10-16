976. Largest Perimeter Triangle

Given an array `A` of positive lengths, return the largest perimeter of a triangle with **non-zero area**, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return `0`.

 

**Example 1:**
```
Input: [2,1,2]
Output: 5
```

**Example 2:**
```
Input: [1,2,1]
Output: 0
```

**Example 3:**
```
Input: [3,2,3,4]
Output: 10
```

**Example 4:**
```
Input: [3,6,2,3]
Output: 8
```

**Note:**

1.`3 <= A.length <= 10000`
1. `1 <= A[i] <= 10^6`

# Solution
---
## Approach 1: Sort
**Intuition**

Without loss of generality, say the sidelengths of the triangle are $a \leq b \leq c$. The necessary and sufficient condition for these lengths to form a triangle of non-zero area is $a + b > c$.

Say we knew $c$ already. There is no reason not to choose the largest possible $a$ and $b$ from the array. If $a + b > c$, then it forms a triangle, otherwise it doesn't.

**Algorithm**

This leads to a simple algorithm: Sort the array. For any $c$ in the array, we choose the largest possible $a \leq b \leq c$: these are just the two values adjacent to $c$. If this forms a triangle, we return the answer.

```python
class Solution(object):
    def largestPerimeter(self, A):
        A.sort()
        for i in xrange(len(A) - 3, -1, -1):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0
```

**Complexity Analysis**

* Time Complexity: $O(N \log N)$, where $N$ is the length of `A`.

* Space Complexity: $O(1)$.

# Submissions
---
**Solution 1: (Sort)**
```
Runtime: 208 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        for i in range(len(A) - 3, -1, -1):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0
```

**Solution 2: (Sort)**
```
Runtime: 63 ms
Memory: 21.8 MB
```
```c++
class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (int i = nums.size()-3; i >= 0; i --) {
            if (nums[i] + nums[i+1] > nums[i+2])
                return nums[i] + nums[i+1] + nums[i+2];
        }
        return 0;
    }
};
```
