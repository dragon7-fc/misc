992. Subarrays with K Different Integers

Given an array `A` of positive integers, call a (contiguous, not necessarily distinct) subarray of `A` good if the number of different integers in that subarray is exactly `K`.

(For example, `[1,2,3,1,2]` has `3` different integers: `1`, `2`, and `3`.)

Return the number of good subarrays of `A`.

 

**Example 1:**
```
Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
```

**Example 2:**
```
Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
``` 

**Note:**

* `1 <= A.length <= 20000`
* `1 <= A[i] <= A.length`
* `1 <= K <= A.length`

# Solution
---
## Approach 1: Sliding Window
**Intuition**

For convenience, let's denote subarrays by tuples: `(i,j) = [A[i], A[i+1], ..., A[j]]`, and call a subarray valid if it has `K` different integers.

For each `j`, let's consider the set $S_j$ of all `i` such that the subarray `(i, j)` is valid.

Firstly, $S_j$ must be a contiguous interval. If `i1 < i2 < i3`,` (i1,j)` and `(i3,j)` are valid, but `(i2,j)` is not valid, this is a contradiction because `(i2,j)` must contain more than `K` different elements [as `(i3,j)` contains `K`], but `(i1,j)` [which is a superset of `(i2,j)`] only contains `K` different integers.

So now let's write $S_j$ as intervals: $S_j = [\text{left1}_j, \text{left2}_j]$.

The second observation is that the endpoints of these intervals must be monotone increeasing - namely, $\text{left1}_j$ and $\text{left2}_j$ are monotone increasing. With similar logic to the above, we could construct a proof of this fact, but the intuition is that after adding an extra element to our subarrays, they are already valid, or we need to shrink them a bit to keep them valid.

**Algorithm**

We'll maintain two sliding windows, corresponding to $\text{left1}_j$ and $\text{left2}_j$. Each sliding window will be able to count how many different elements there are in the window, and add and remove elements in a queue-like fashion.

```python
class Window:
    def __init__(self):
        self.count = collections.Counter()
        self.nonzero = 0

    def add(self, x):
        self.count[x] += 1
        if self.count[x] == 1:
            self.nonzero += 1

    def remove(self, x):
        self.count[x] -= 1
        if self.count[x] == 0:
            self.nonzero -= 1

class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        window1 = Window()
        window2 = Window()
        ans = left1 = left2 = 0

        for right, x in enumerate(A):
            window1.add(x)
            window2.add(x)

            while window1.nonzero > K:
                window1.remove(A[left1])
                left1 += 1

            while window2.nonzero >= K:
                window2.remove(A[left2])
                left2 += 1

            ans += left2 - left1

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of `A`.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution 1: (Sliding Window, exactly k = (at most k) - (at most k-1))**
```
Runtime: 780 ms
Memory Usage: 15.9 MB
```
```python
class Window:
    def __init__(self):
        self.count = collections.Counter()
        self.nonzero = 0

    def add(self, x):
        self.count[x] += 1
        if self.count[x] == 1:
            self.nonzero += 1

    def remove(self, x):
        self.count[x] -= 1
        if self.count[x] == 0:
            self.nonzero -= 1
            
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        window1 = Window()
        window2 = Window()
        ans = left1 = left2 = 0

        for right, x in enumerate(A):
            window1.add(x)
            window2.add(x)

            while window1.nonzero > K:
                window1.remove(A[left1])
                left1 += 1

            while window2.nonzero >= K:
                window2.remove(A[left2])
                left2 += 1

            ans += left2 - left1

        return ans
```

**Solution 1: (Sliding Window, exactly k = (at most k) - (at most k-1))**
```
Runtime: 83 ms
Memory: 48.76 MB
```
```c++
class Solution {
    int atMostK(vector<int>& A, int K) {
        int i = 0, res = 0;
        unordered_map<int, int> count;
        for (int j = 0; j < A.size(); ++j) {
            if (!count[A[j]]++) K--;
            while (K < 0) {
                if (!--count[A[i]]) K++;
                i++;
            }
            res += j - i + 1;
        }
        return res;
    }
public:
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        return atMostK(nums, k) - atMostK(nums, k - 1);
    }
};
```
