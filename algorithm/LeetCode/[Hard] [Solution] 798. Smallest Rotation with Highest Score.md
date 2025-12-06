798. Smallest Rotation with Highest Score

Given an array `A`, we may rotate it by a non-negative integer `K` so that the array becomes `A[K], A[K+1], A{K+2], ... A[A.length - 1], A[0], A[1], ..., A[K-1]`.  Afterward, any entries that are less than or equal to their index are worth 1 point. 

For example, if we have `[2, 4, 1, 3, 0]`, and we rotate by `K = 2`, it becomes `[1, 3, 0, 2, 4]`.  This is worth 3 points because 1 > 0 [no points], 3 > 1 [no points], 0 <= 2 [one point], 2 <= 3 [one point], 4 <= 4 [one point].

Over all possible rotations, return the rotation index K that corresponds to the highest score we could receive.  If there are multiple answers, return the smallest such index K.

**Example 1:**
```
Input: [2, 3, 1, 4, 0]
Output: 3
Explanation:  
Scores for each K are listed below: 
K = 0,  A = [2,3,1,4,0],    score 2
K = 1,  A = [3,1,4,0,2],    score 3
K = 2,  A = [1,4,0,2,3],    score 3
K = 3,  A = [4,0,2,3,1],    score 4
K = 4,  A = [0,2,3,1,4],    score 3
So we should choose K = 3, which has the highest score.
``` 

**Example 2:**
```
Input: [1, 3, 0, 2, 4]
Output: 0
Explanation:  A will always have 3 points no matter how it shifts.
So we will choose the smallest K, which is 0.
```

**Note:**

* `A` will have length at most `20000`.
* `A[i]` will be in the range `[0, A.length]`.

# Solution
---
## Approach #1: Interval Stabbing [Accepted]
**Intuition**

Say `N = 10` and `A[2] = 5`. Then there are `5` rotations that are bad for this number: rotation indexes `0, 1, 2, 8, 9` - these rotations will cause this number to not get 1 point later.

In general, for each number in the array, we can map out what rotation indexes will be bad for this number. It will always be a region of one interval, possibly two if the interval wraps around (eg. `8, 9, 0, 1, 2` wraps around, to become `[8, 9]` and `[0, 1, 2]`.)

At the end of plotting these intervals, we need to know which rotation index has the least intervals overlapping it - this one is the answer.

**Algorithm**

First, an element like `A[2] = 5` will not get score in (up to) 5 posiitons: when the 5 is at final index 0, 1, 2, 3, or 4. When we shift by 2, we'll get final index 0. If we shift `5-1 = 4` before this, this element will end up at final index 4. In general (modulo N), a shift of `i - A[i] + 1` to `i` will be the rotation indexes that will make `A[i]` not score a point.

If we are trying to plot an interval like `[2, 3, 4]`, then instead of doing `bad[2]--; bad[3]--; bad[4]--;`, what we will do instead is keep track of the cumulative total: `bad[2]--; bad[5]++`. For "wrap-around" intervals like `[8, 9, 0, 1, 2]`, we will keep track of this as two separate intervals: `bad[8]--, bad[10]++, bad[0]--, bad[3]++`. (Actually, because of our implementation, we don't need to remember the `bad[10]++` part.)

At the end, we want to find a rotation index with the least intervals overlapping. We'll maintain a cumulative total `cur` representing how many intervals are currently overlapping our current rotation index, then update it as we step through each rotation index.

```python
class Solution(object):
    def bestRotation(self, A):
        N = len(A)
        bad = [0] * N
        for i, x in enumerate(A):
            left, right = (i - x + 1) % N, (i + 1) % N
            bad[left] -= 1
            bad[right] += 1
            if left > right:
                bad[0] -= 1

        best = -N
        ans = cur = 0
        for i, score in enumerate(bad):
            cur += score
            if cur > best:
                best = cur
                ans = i

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where NN is the length of `A`.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution 1: (Interval Stabbing)**
```
Runtime: 208 ms
Memory Usage: 16.2 MB
```
```python
class Solution:
    def bestRotation(self, A: List[int]) -> int:
        N = len(A)
        bad = [0] * N
        for i, x in enumerate(A):
            left, right = (i - x + 1) % N, (i + 1) % N
            bad[left] -= 1
            bad[right] += 1
            if left > right:
                bad[0] -= 1

        best = -N
        ans = cur = 0
        for i, score in enumerate(bad):
            cur += score
            if cur > best:
                best = cur
                ans = i

        return ans
```

**Solution 2: (Counter)**


 0 1 2 3 4 5 6 7 8 9
     5
 x x x           x x invalid

              v
nums = [2,3,1,4,0]

        2
          -----  
          3
            ---  
            1
        ---   ---
              4
                -
                0
        ---------
```
Runtime: 0 ms, Beats 100.00%
Memory: 78.54 MB, Beats 19.62%
```
```c++
class Solution {
public:
    int bestRotation(vector<int>& nums) {
        int n = nums.size();
        vector<int> cnt(n);
        for (int i = 0; i < n; i ++) {
            cnt[(i + 1) % n] += 1;             // interval start
            cnt[(i + 1 - nums[i] + n) % n] -= 1;  // interval end
        }
        int count = 0;
        int maxCount = -1;
        int ans = 0;
        for (int i = 0; i < n; i ++) {  // find most overlap interval
            count += cnt[i];
            if (count > maxCount) {
                ans = i;
                maxCount = count;
            }
        }
        return ans;
    }
};
```
