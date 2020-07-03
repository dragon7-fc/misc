679. 24 Game

You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through `*`, `/`, `+`, `-`, `(`, `)` to get the value of 24.

**Example 1:**
```
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24
```

**Example 2:**
```
Input: [1, 2, 1, 2]
Output: False
```

**Note:**

* The division operator `/` represents real division, not integer division. For example, `4 / (1 - 2/3) = 12`.
* Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with `[1, 1, 1, 1]` as input, the expression `-1 - 1 - 1 - 1` is not allowed.
* You cannot concatenate numbers together. For example, if the input is `[1, 2, 1, 2]`, we cannot write this as `12 + 12`.

# Solution
---
## Approach #1: Backtracking [Accepted]
**Intuition and Algorithm**

There are only 4 cards and only 4 operations that can be performed. Even when all operations do not commute, that gives us an upper bound of $12 * 6 * 2 * 4 * 4 * 4 = 9216$ possibilities, which makes it feasible to just try them all. Specifically, we choose two numbers (with order) in 12 ways and perform one of 4 operations (12 * 4). Then, with 3 remaining numbers, we choose 2 of them and perform one of 4 operations (6 * 4). Finally we have two numbers left and make a final choice of 2 * 4 possibilities.

We will perform 3 binary operations (`+, -, *, /` are the operations) on either our numbers or resulting numbers. Because `-` and `/` do not commute, we must be careful to consider both `a / b` and `b / a`.

For every way to remove two numbers `a`, `b` in our list, and for each possible result they can make, like `a+b`, `a/b`, etc., we will recursively solve the problem on this smaller list of numbers.

```python
from operator import truediv, mul, add, sub

class Solution(object):
    def judgePoint24(self, A):
        if not A: return False
        if len(A) == 1: return abs(A[0] - 24) < 1e-6

        for i in xrange(len(A)):
            for j in xrange(len(A)):
                if i != j:
                    B = [A[k] for k in xrange(len(A)) if i != k != j]
                    for op in (truediv, mul, add, sub):
                        if (op is add or op is mul) and j > i: continue
                        if op is not truediv or A[j]:
                            B.append(op(A[i], A[j]))
                            if self.judgePoint24(B): return True
                            B.pop()
        return False
```

**Complexity Analysis**

* Time Complexity: $O(1)$. There is a hard limit of 9216 possibilities, and we do $O(1)$ work for each of them.

* Space Complexity: $O(1)$. Our intermediate arrays are at most 4 elements, and the number made is bounded by an $O(1)$ factor.

# Submissions
---
**Solution 1: (Backtracking)**
```
Runtime: 152 ms
Memory Usage: 13.9 MB
```
```python
from operator import truediv, mul, add, sub

class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if not nums: return False
        if len(nums) == 1: return abs(nums[0] - 24) < 1e-6

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    B = [nums[k] for k in range(len(nums)) if i != k != j]
                    for op in (truediv, mul, add, sub):
                        if (op is add or op is mul) and j > i: continue
                        if op is not truediv or nums[j]:
                            B.append(op(nums[i], nums[j]))
                            if self.judgePoint24(B): return True
                            B.pop()
        return False
```