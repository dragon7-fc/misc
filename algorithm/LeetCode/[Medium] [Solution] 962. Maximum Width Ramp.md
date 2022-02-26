962. Maximum Width Ramp

Given an array `A` of integers, a ramp is a tuple `(i, j)` for which `i` < `j` and `A[i] <= A[j]`.  The width of such a ramp is `j - i`.

Find the maximum width of a ramp in `A`.  If one doesn't exist, return `0`.

**Example 1:**
```
Input: [6,0,8,2,1,5]
Output: 4
Explanation: 
The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.
```

**Example 2:**
```
Input: [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: 
The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.
``` 

**Note:**

1. `2 <= A.length <= 50000`
1. `0 <= A[i] <= 50000`

# Solution
---
## Approach 1: Sort
**Intuition and Algorithm**

For all elements like `A[i] = v`, let's write the indices `i` in sorted order of their values `v`. For example with `A[0] = 7, A[1] = 2, A[2] = 5, A[3] = 4`, we can write the order of indices `i=1, i=3, i=2, i=0`.

Then, whenever we write an index `i`, we know there was a ramp of width `i - min(indexes_previously_written)` (if this quantity is positive). We can keep track of the minimum of all indexes previously written as `m`.
 
 ```python
class Solution(object):
    def maxWidthRamp(self, A):
        ans = 0
        m = float('inf')
        for i in sorted(range(len(A)), key = A.__getitem__):
            ans = max(ans, i - m)
            m = min(m, i)
        return ans
```

**Complexity Analysis**

*Time Complexity: $O(N \log N)$, where $N$ is the length of `A`.

* Space Complexity: $O(N)$, depending on the implementation of the sorting function.

## Approach 2: Binary Search Candidates
**Intuition**

Consider `i` in decreasing order. We want to find the largest `j` with `A[j] >= A[i]` if it exists.

Thus, the candidates for `j` are decreasing: if there is `j1 < j2` and `A[j1] <= A[j2]` then we strictly prefer `j2`.

**Algorithm**

Let's keep a list of these candidates `j`. For example, with `A = [0,8,2,7,5]`, the candidates for `i = 0` would be candidates = `[(v=5, i=4), (v=7, i=3), (v=8, i=1)]`. We keep the list of candidates in decreasing order of `i` and increasing order of `v`.

Now we can binary search to find the largest `j` with `A[j] >= A[i]`: it's the first one in this list of candidates with `v >= A[i]`.

```python
class Solution(object):
    def maxWidthRamp(self, A):
        N = len(A)

        ans = 0
        candidates = [(A[N-1], N-1)]
        # candidates: i's decreasing, by increasing value of A[i]
        for i in xrange(N-2, -1, -1):
            # Find largest j in candidates with A[j] >= A[i]
            jx = bisect.bisect(candidates, (A[i],))
            if jx < len(candidates):
                ans = max(ans, candidates[jx][1] - i)
            else:
                candidates.append((A[i], i))

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N \log N)$, where $N$ is the length of `A`.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution: (Sort)**
```
Runtime: 400 ms
Memory Usage: 21.2 MB
```
```python
class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        ans = 0
        m = float('inf')
        for i in sorted(range(len(A)), key = A.__getitem__):
            ans = max(ans, i - m)
            m = min(m, i)
        return ans
```

**Solution: (Binary Search Candidates, Insertion Sort)**
```
Runtime: 448 ms
Memory Usage: 20.7 MB
```
```python
class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        N = len(A)

        ans = 0
        candidates = [(A[N-1], N-1)]
        # candidates: i's decreasing, by increasing value of A[i]
        for i in range(N-2, -1, -1):
            # Find largest j in candidates with A[j] >= A[i]
            jx = bisect.bisect(candidates, (A[i],))
            if jx < len(candidates):
                ans = max(ans, candidates[jx][1] - i)
            else:
                candidates.append((A[i], i))

        return ans
```

**Solution 1: (Binary Search Candidates, Insertion Sort)**

* Time: Nlog(N)
* Space: O(N)

```
Runtime: 81 ms
Memory Usage: 29.6 MB
```
```c++
class Solution {
public:
    int maxWidthRamp(vector<int>& nums) {
        int out{0}, sz(size(nums));
        vector v{sz-1};
        for (int i{sz-2}; i >= 0; i--)
            if (nums[i] <= nums[v.back()])
                out = max(out, *lower_bound(begin(v), end(v), i, [&](const auto & i, const auto & j){ return nums[i] < nums[j]; }) -i);
            else
                v.push_back(i);
        return out;
    }
};
```

**Solution 2: (Stack)**

* Time: O(N) 
* Space: O(N)

```
Runtime: 57 ms
Memory Usage: 29.5 MB
```
```c++
class Solution {
public:
    int maxWidthRamp(vector<int>& nums) {
        int out{0}, sz(size(nums));
        stack<int> s({sz-1});
        for (int i{sz-2}; i >= 0; i--)
            if (nums[s.top()] < nums[i]) s.push(i);

        for (int i{0}; i < sz; )
            if (!empty(s) and nums[i] <= nums[s.top()])
                out = max(out, s.top()-i), s.pop();
            else
                ++i;
        return out;
    }
};
```
