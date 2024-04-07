713. Subarray Product Less Than K

Your are given an array of positive integers `nums`.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than `k`.

**Example 1:**
```
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
```

**Note:**

* `0 < nums.length <= 50000`.
* `0 < nums[i] < 1000`.
* `0 <= k < $10^6$`.

# Solution
---
## Approach #1: Binary Search on Logarithms [Accepted]
**Intuition**

Because $\log(\prod_i x_i) = \sum_i \log x_i$, we can reduce the problem to subarray sums instead of subarray products. The motivation for this is that the product of some arbitrary subarray may be way too large (potentially 1000^50000), and also dealing with sums gives us some more familiarity as it becomes similar to other problems we may have solved before.

**Algorithm**

After this transformation where every value `x` becomes `log(x)`, let us take prefix sums `prefix[i+1] = nums[0] + nums[1] + ... + nums[i]`. Now we are left with the problem of finding, for each `i`, the largest `j` so that `nums[i] + ... + nums[j] = prefix[j] - prefix[i] < k`.

Because prefix is a monotone increasing array, this can be solved with binary search. We add the width of the interval `[i, j]` to our answer, which counts all subarrays `[i, k]` with `k <= j`.

```Python
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k == 0: return 0
        k = math.log(k)

        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + math.log(x))

        ans = 0
        for i, x in enumerate(prefix):
            j = bisect.bisect(prefix, x + k - 1e-9, i+1)
            ans += j - i - 1
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N\log N)$, where $N$ is the length of nums. Inside our for loop, each binary search operation takes $O(\log N)$ time.

* Space Complexity: $O(N)$, the space used by prefix.

## Approach #2: Sliding Window [Accepted]
**Intuition**

For each `right`, call `opt(right)` the smallest left so that the product of the subarray `nums[left] * nums[left + 1] * ... * nums[right]` is less than `k`. `opt` is a monotone increasing function, so we can use a sliding window.

**Algorithm**

Our loop invariant is that `left` is the smallest value so that the product in the window `prod = nums[left] * nums[left + 1] * ... * nums[right]` is less than `k`.

For every `right`, we update `left` and `prod` to maintain this invariant. Then, the number of intervals with subarray product less than `k` and with right-most coordinate `right`, is `right - left + 1`. We'll count all of these for each value of `right`.

```python
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of nums. left can only be incremented at most N times.

* Space Complexity: $O(1)$, the space used by prod, left, and ans.

# Submissions
---
**Solution: (Sliding window)**
```
Runtime: 1280 ms
Memory Usage: 18.2 MB
```
```python
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans             
```

**Solution 2: (Sliding window)**
```
untime: 66 ms
Memory: 63.67 MB
```
```c++
class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        if (k <= 1) {
            return 0;
        }
        int n = nums.size(), i = 0, cur = 1, ans = 0;
        for (int j = 0; j < n; j ++) {
            cur *= nums[j];
            while (cur >= k) {
                cur /= nums[i];
                i += 1;
            }
            ans += j-i+1;
        }
        return ans;
    }
};
```
