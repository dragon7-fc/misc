945. Minimum Increment to Make Array Unique

Given an array of integers `A`, a move consists of choosing any `A[i]`, and incrementing it by `1`.

Return the least number of moves to make every value in `A` unique.

 

**Example 1:**
```
Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].
```

**Example 2:**
```
Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
``` 

**Note:**

1. `0 <= A.length <= 40000`
1. `0 <= A[i] < 40000`

# Solution
---
## Approach 1: Counting
**Intuition**

Let's count the quantity of each element. Clearly, we want to increment duplicated values.

For each duplicate value, we could do a "brute force" solution of incrementing it repeatedly until it is not unique. However, we might do a lot of work - consider the work done by an array of all ones. We should think of how to amend our solution to solve this case as well.

What we can do instead is lazily evaluate our increments. If for example we have `[1, 1, 1, 1, 3, 5]`, we don't need to process all the increments of duplicated `1`s. We could take three ones (`taken = [1, 1, 1]`) and continue processing. When we find an empty place like `2`, `4`, or `6`, we can then recover that our increment will be `2-1`, `4-1`, and `6-1`.

**Algorithm**

Count the values. For each possible value `x`:

* If there are `2 or more` values `x` in `A`, save the extra duplicated values to increment later.
* If there are `0` values `x` in `A`, then a saved value `v` gets incremented to `x`.

In Java, the code is less verbose with a slight optimization: we record only the number of saved values, and we subtract from the answer in advance. In the `[1, 1, 1, 1, 3, 5]` example, we do `taken = 3` and `ans -= 3` in advance, and later we do `ans += 2`; `ans += 4`; `ans += 6`. This optimization is also used in Approach 2.

```python
class Solution(object):
    def minIncrementForUnique(self, A):
        count = collections.Counter(A)
        taken = []

        ans = 0
        for x in xrange(100000):
            if count[x] >= 2:
                taken.extend([x] * (count[x] - 1))
            elif taken and count[x] == 0:
                ans += x - taken.pop()
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of `A`.

* Space Complexity: $O(N)$.

## Approach 2: Maintain Duplicate Info
**Intuition**

Let's imagine the array is sorted and we are moving from left to right. As in Approach 1, we want to take duplicate values to release later.

**Algorithm**

There are two cases.

* If `A[i-1] == A[i]`, we have a duplicate to take.

* If `A[i-1] < A[i]`, we might be able to place our taken values into those free positions. Specifically, we have `give = min(taken, A[i] - A[i-1] - 1)` possible values to release, and they will have final values `A[i-1] + 1, A[i-1] + 2, ..., A[i-1] + give`. This has a sum of $A[i-1] * \text{give} + (\sum_{k=1}^{give})$.

```python
class Solution(object):
    def minIncrementForUnique(self, A):
        A.sort()
        A.append(100000)
        ans = taken = 0

        for i in xrange(1, len(A)):
            if A[i-1] == A[i]:
                taken += 1
                ans -= A[i]
            else:
                give = min(taken, A[i] - A[i-1] - 1)
                ans += give * (give + 1) / 2 + give * A[i-1]
                taken -= give

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N\log N)$, where $N$ is the length of `A`.

* Space Complexity: $O(N)$ in additional space complexity, depending on the specific implementation of the built in sort.

# Submissions
---
**Solution: (Counting, bucket sort)**
```
Runtime: 1772 ms
Memory Usage: 20.8 MB
```
```python
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        count = collections.Counter(A)
        taken = []

        ans = 0
        for x in range(100000):
            if count[x] >= 2:
                taken.extend([x] * (count[x] - 1))
            elif taken and count[x] == 0:
                ans += x - taken.pop()
        return ans
```

**Solution: (Maintain Duplicate Info)**
```
Runtime: 424 ms
Memory Usage: 19 MB
```
```python
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        A.append(100000)
        ans = taken = 0

        for i in range(1, len(A)):
            if A[i-1] == A[i]:
                taken += 1
                ans -= A[i]
            else:
                give = min(taken, A[i] - A[i-1] - 1)
                ans += give * (give + 1) // 2 + give * A[i-1]
##                     ----------------------   -------------
##                      $\sum_(k=1}^{give}$ 
##                             
##                /|           /|
##               ---          ---                   ---
##               | |     =                    +     | |
##               ---                                ---
                taken -= give

        return ans
```
