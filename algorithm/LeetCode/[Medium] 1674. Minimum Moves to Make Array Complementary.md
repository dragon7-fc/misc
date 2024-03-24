1674. Minimum Moves to Make Array Complementary

You are given an integer array `nums` of even length `n` and an integer `limit`. In one move, you can replace any integer from `nums` with another integer between 1 and `limit`, inclusive.

The array `nums` is **complementary** if for all indices `i` (**0-indexed**), `nums[i] + nums[n - 1 - i]` equals the same number. For example, the array `[1,2,3,4]` is **complementary** because for all indices `i`, `nums[i] + nums[n - 1 - i] = 5`.

Return the minimum number of moves required to make `nums` **complementary**.

 

**Example 1:**
```
Input: nums = [1,2,4,3], limit = 4
Output: 1
Explanation: In 1 move, you can change nums to [1,2,2,3] (underlined elements are changed).
nums[0] + nums[3] = 1 + 3 = 4.
nums[1] + nums[2] = 2 + 2 = 4.
nums[2] + nums[1] = 2 + 2 = 4.
nums[3] + nums[0] = 3 + 1 = 4.
Therefore, nums[i] + nums[n-1-i] = 4 for every i, so nums is complementary.
```

**Example 2:**
```
Input: nums = [1,2,2,1], limit = 2
Output: 2
Explanation: In 2 moves, you can change nums to [2,2,2,2]. You cannot change any number to 3 since 3 > limit.
```

**Example 3:**
```
Input: nums = [1,2,1,2], limit = 2
Output: 0
Explanation: nums is already complementary.
```

**Constraints:**

* `n == nums.length`
* `2 <= n <= 10^5`
* `1 <= nums[i] <= limit <= 10^5`
* `n` is even.

# Submissions
---
**Solution 1: (O(max(n, k)) method)**

**Idea**

If we want to make the nums complementary, having all the pairs A = nums[i], B = nums[n - 1 - i] with A + B = T. Considering a pair A = nums[i], B = nums[n - 1 - i], there are 5 different situation for every such pair (A, B), given different target T.

* 2 <= T < min(A, B) + 1, we need 2 operations to make both A, B smaller
* min(A, B) + 1 <= T < A + B, we need 1 operation to make the larger one out of A and B smaller
* T = A + B, we need 0 operation
* A + B < T < max(A, B) + limit, we need 1 operation to make the smaller one out of A and B larger
* max(A, B) + limit < T <= 2 * limit, we need 2 operation to make both A, B larger

We calculate the boundary for each pair (A, B) and note down the corresponding operation changes as delta. delta[i] = x means we need x more operations when target T change from i - 1 to i.

**Complexity**

* Time: O(max(n, k))
* Space: O(k)

```
Runtime: 1732 ms
Memory Usage: 36.3 MB
```
```python
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        delta = collections.Counter()
        n = len(nums)
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            delta[2] += 2
            delta[min(a, b) + 1] -= 1
            delta[a + b] -= 1
            delta[a + b + 1] += 1
            delta[max(a, b) + limit + 1] += 1
            
        curr = 0            
        res = math.inf
        for i in range(2, 2 * limit + 1):
            curr += delta[i]
            res = min(res, curr)
        return res   
```
