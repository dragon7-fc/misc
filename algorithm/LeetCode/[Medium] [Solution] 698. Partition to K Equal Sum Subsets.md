698. Partition to K Equal Sum Subsets

Given an array of integers `nums` and a positive integer `k`, find whether it's possible to divide this array into `k` non-empty subsets whose sums are all equal.

 

**Example 1:**

```
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
```

**Note:**

* `1 <= k <= len(nums) <= 16`.
* `0 < nums[i] < 10000`.

# Solution
---
## Approach #1: Search by Constructing Subset Sums [Accepted]
**Intuition**

As even when `k = 2`, the problem is a "Subset Sum" problem which is known to be NP-hard, (and because the given input limits are low,) our solution will focus on exhaustive search.

A natural approach is to simulate the `k` groups (disjoint subsets of nums). For each number in `nums`, we'll check whether putting it in the `i`-th group solves the problem. We can check those possibilities by recursively searching.

**Algorithm**

Firstly, we know that each of the `k` group-sums must be equal to `target = sum(nums) / k`. (If this quantity is not an integer, the task is impossible.)

For each number in `nums`, we could add it into one of `k` group-sums, as long as the group's sum would not exceed the target. For each of these choices, we recursively search with one less number to consider in `nums`. If we placed every number successfully, then our search was successful.

One important speedup is that we can ensure all the 0 values of each group occur at the end of the array groups, by enforcing if `(groups[i] == 0) break;.` This greatly reduces repeated work - for example, in the first run of search, we will make only 1 recursive call, instead of `k`. Actually, we could do better by skipping any repeated values of `groups[i]`, but it isn't necessary.

Another speedup is we could sort the array `nums`, so that we try to place the largest elements first. When the answer is true and involves subsets with a low size, this method of placing elements will consider these lower size subsets sooner. We can also handle elements `nums[i] >= target` appropriately. These tricks are not necessary to solve the problem, but they are presented in the solutions below.

```python
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        target, rem = divmod(sum(nums), k)
        if rem: return False

        def search(groups):
            if not nums: return True
            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if search(groups): return True
                    groups[i] -= v
                if not group: break
            nums.append(v)
            return False

        nums.sort()
        if nums[-1] > target: return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        return search([0] * k)
```

**Complexity Analysis**

* Time Complexity: $O(k^{N-k} k!)$, where $N$ is the length of nums, and $k$ is as given. As we skip additional zeroes in groups, naively we will make $O(k!)$ calls to search, then an additional $O(k^{N-k})$ calls after every element of groups is nonzero.

* Space Complexity: $O(N)$, the space used by recursive calls to search in our call stack.

## Approach #2: Dynamic Programming on Subsets of Input [Accepted]
**Intuition and Algorithm**

As in Approach #1, we investigate methods of exhaustive search, and find `target = sum(nums) / k` in the same way.

Let `used` have the `i`-th bit set if and only if `nums[i]` has already been used. Our goal is to use `nums` in some order so that placing them into groups in that order will be valid. `search(used, ...)` will answer the question: can we partition `unused` elements of `nums[i]` appropriately?

This will depend on `todo`, the sum of the remaining `unused` elements, not crossing multiples of `target` within one number. If for example our `target` is `10`, and our elements to be placed in order are `[6, 5, 5, 4]`, this would not work as `6 + 5` "crosses" `10` prematurely.

If we could choose the order, then after placing `5`, our unused elements are `[4, 5, 6]`. Using `6` would make `todo` go from `15` to `9`, which crosses `10` - something unwanted. However, we could use `5` since `todo` goes from `15` to `10`; then later we could use `4` and `6` as those placements do not cross.

It turns out the maximum value that can be chosen so as to not cross a multiple of `target`, is `targ = (todo - 1) % target + 1.` This is essentially `todo % target`, `plus` `target` if that would be zero.

Now for each `unused` number that doesn't cross, we'll search on that state, and we'll return `true` if any of those searches are `true`.

Notice that the state `todo` depends only on the state `used`, so when memoizing our search, we only need to make lookups by `used`.

In the solutions below, we present both a top-down dynamic programming solution, and a bottom-up one. The bottom-up solution uses a different notion of state.

```python
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        target, rem = divmod(sum(nums), k)
        if rem or max(nums) > target: return False

        memo = [None] * (1 << len(nums))
        memo[-1] = True
        def search(used, todo):
            if memo[used] is None:
                targ = (todo - 1) % target + 1
                memo[used] = any(search(used | (1<<i), todo - num)
                                 for i, num in enumerate(nums)
                                 if (used >> i) & 1 == 0 and num <= targ)
            return memo[used]

        return search(0, target * k)
```

Bottom-Up Variation

```python
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        nums.sort()
        target, rem = divmod(sum(nums), k)
        if rem or nums[-1] > target: return False

        dp = [False] * (1 << len(nums))
        dp[0] = True
        total = [0] * (1 << len(nums))

        for state in xrange(1 << len(nums)):
            if not dp[state]: continue
            for i, num in enumerate(nums):
                future = state | (1 << i)
                if state != future and not dp[future]:
                    if (num <= target - (total[state] % target)):
                        dp[future] = True
                        total[future] = total[state] + num
                    else:
                        break
        return dp[-1]
```

**Complexity Analysis**

* Time Complexity: $O(N * 2^N)$, where $N$ is the length of `nums`. There are $2^N$ states of used (or state in our bottom-up variant), and each state performs $O(N)$ work searching through nums.

* Space Complexity: $O(2^N)$, the space used by `memo` (or `dp`, total in our bottom-up variant).

# Submissions
**Solution 1:**
```
Runtime: 44 ms
Memory Usage: 13.6 MB
```
```python
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, rem = divmod(sum(nums), k)
        if rem: return False

        def search(groups):
            if not nums: return True
            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if search(groups): return True
                    groups[i] -= v
                if not group: break
            nums.append(v)
            return False

        nums.sort()
        if nums[-1] > target: return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        return search([0] * k)
```

**Solution 2:**
```
Runtime: 176 ms
Memory Usage: 25.9 MB
```
```python
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:  
        target, rem = divmod(sum(nums), k)
        if rem or max(nums) > target: return False

        memo = [None] * (1 << len(nums))
        memo[-1] = True
        def search(used, todo):
            if memo[used] is None:
                targ = (todo - 1) % target + 1
                memo[used] = any(search(used | (1<<i), todo - num)
                                 for i, num in enumerate(nums)
                                 if (used >> i) & 1 == 0 and num <= targ)
            return memo[used]

        return search(0, target * k)
```