923. 3Sum With Multiplicity

Given an integer array `A`, and an integer target, return the number of tuples `i, j, k`  such that `i < j < k` and `A[i] + A[j] + A[k] == target`.

As the answer can be very large, return it modulo `10^9 + 7`.

 

**Example 1:**
```
Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (A[i], A[j], A[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
```

**Example 2:**
```
Input: A = [1,1,2,2,2,2], target = 5
Output: 12
Explanation: 
A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.
``` 

**Note:**

* `3 <= A.length <= 3000`
* `0 <= A[i] <= 100`
* `0 <= target <= 300`

# Solutions
---
## Approach Notes
The approaches described below assume some familiarity with the two pointer technique that can be used to solve the LeetCode problem "Two Sum".

In the problem, we have a sorted array A of unique elements, and want to know how many `i < j` with `A[i] + A[j] == target`.

The idea that does it in linear time, is that for each `i` in increasing order, the `j`'s that satisfy the equation `A[i] + A[j] == target` are decreasing.

```python
def solve(A, target):
    # Assume A already sorted
    i, j = 0, len(A) - 1
    ans = 0
    while i < j:
        if A[i] + A[j] < target:
            i += 1
        elif A[i] + A[j] > target:
            j -= 1
        else:
            ans += 1
            i += 1
            j -= 1
    return ans
```

This is not a complete explanation. For more on this problem, please review the LeetCode problem "Two Sum".

## Approach 1: Three Pointer
**Intuition and Algorithm**

Sort the array. For each `i`, set `T = target - A[i]`, the remaining target. We can try using a two-pointer technique to find `A[j] + A[k] == T`. This approach is the natural continuation of trying to make the two-pointer technique we know from previous problems, work on this problem.

Because some elements are duplicated, we have to be careful. In a typical case, the target is say, `8`, and we have a remaining array `(A[i+1:])` of `[2,2,2,2,3,3,4,4,4,5,5,5,6,6]`. We can analyze this situation with cases.

Whenever `A[j] + A[k] == T`, we should count the multiplicity of `A[j]` and `A[k]`. In this example, if `A[j] == 2` and `A[k] == 6`, the multiplicities are `4` and `2`, and the total number of pairs is `4 * 2 = 8`. We then move to the remaining window `A[j:k+1]` of `[3,3,4,4,4,5,5,5]`.

As a special case, if `A[j] == A[k]`, then our manner of counting would be incorrect. If for example the remaining window is `[4,4,4]`, there are only `3` such pairs. In general, when `A[j] == A[k]`, we have $\binom{M}{2} = \frac{M*(M-1)}{2}$ pairs `(j,k)` (with `j < k`) that satisfy `A[j] + A[k] == T`, where $M$ is the multiplicity of `A[j]` (in this case $M=3$).

For more details, please see the inline comments.

```python
class Solution(object):
    def threeSumMulti(self, A, target):
        MOD = 10**9 + 7
        ans = 0
        A.sort()

        for i, x in enumerate(A):
            # We'll try to find the number of i < j < k
            # with A[j] + A[k] == T, where T = target - A[i].

            # The below is a "two sum with multiplicity".
            T = target - A[i]
            j, k = i+1, len(A) - 1

            while j < k:
                # These steps proceed as in a typical two-sum.
                if A[j] + A[k] < T:
                    j += 1
                elif A[j] + A[k] > T:
                    k -= 1
                # These steps differ:
                elif A[j] != A[k]: # We have A[j] + A[k] == T.
                    # Let's count "left": the number of A[j] == A[j+1] == A[j+2] == ...
                    # And similarly for "right".
                    left = right = 1
                    while j + 1 < k and A[j] == A[j+1]:
                        left += 1
                        j += 1
                    while k - 1 > j and A[k] == A[k-1]:
                        right += 1
                        k -= 1

                    # We contributed left * right many pairs.
                    ans += left * right
                    ans %= MOD
                    j += 1
                    k -= 1

                else:
                    # M = k - j + 1
                    # We contributed M * (M-1) / 2 pairs.
                    ans += (k-j+1) * (k-j) / 2
                    ans %= MOD
                    break

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the length of `A`.

* Space Complexity: $O(1)$.

## Approach 2: Counting with Cases
**Intuition and Algorithm**

Let count[x] be the number of times that `x` occurs in `A`. For every `x+y+z == target`, we can try to count the correct contribution to the answer. There are a few cases:

* If `x`, `y`, and `z` are all different, then the contribution is `count[x] * count[y] * count[z]`.

* If `x == y != z`, the contribution is $\binom{\text{count[x]}}{2} * \text{count[z]}$.

* If `x != y == z`, the contribution is $\text{count[x]} * \binom{\text{count[y]}}{2}$.

* If `x == y == z`, the contribution is $\binom{\text{count[x]}}{3}$.

(Here, $\binom{n}{k}$ denotes the binomial coefficient $\frac{n!}{(n-k)!k!}$.)

Each case is commented in the implementations below.

```python
class Solution(object):
    def threeSumMulti(self, A, target):
        MOD = 10**9 + 7
        count = [0] * 101
        for x in A:
            count[x] += 1

        ans = 0

        # All different
        for x in xrange(101):
            for y in xrange(x+1, 101):
                z = target - x - y
                if y < z <= 100:
                    ans += count[x] * count[y] * count[z]
                    ans %= MOD

        # x == y
        for x in xrange(101):
            z = target - 2*x
            if x < z <= 100:
                ans += count[x] * (count[x] - 1) / 2 * count[z]
                ans %= MOD

        # y == z
        for x in xrange(101):
            if (target - x) % 2 == 0:
                y = (target - x) / 2
                if x < y <= 100:
                    ans += count[x] * count[y] * (count[y] - 1) / 2
                    ans %= MOD

        # x == y == z
        if target % 3 == 0:
            x = target / 3
            if 0 <= x <= 100:
                ans += count[x] * (count[x] - 1) * (count[x] - 2) / 6
                ans %= MOD

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N + W^2)$, where $N$ is the length of `A`, and $W$ is the maximum possible value of `A[i]`. (Note that this solution can be adapted to be $O(N^2)$ even in the case that $W$ is very large.)

* Space Complexity: $O(W)$.

## Approach 3: Adapt from Three Sum
**Intuition and Algorithm**

As in Approach 2, let `count[x]` be the number of times that `x` occurs in `A`. Also, let `keys` be a sorted list of unique values of `A`. We will try to adapt a 3Sum algorithm to work on keys, but add the correct answer contributions.

For example, if `A = [1,1,2,2,3,3,4,4,5,5]` and `target = 8`, then `keys = [1,2,3,4,5]`. When doing 3Sum on keys (with `i <= j <= k`), we will encounter some tuples that sum to the target, like `(x,y,z) = (1,2,5), (1,3,4), (2,2,4), (2,3,3)`. We can then use count to calculate how many such tuples there are in each case.

This approach assumes familiarity with 3Sum. For more, please visit the associated LeetCode problem here https://leetcode.com/problems/3sum.

```python
class Solution(object):
    def threeSumMulti(self, A, target):
        MOD = 10**9 + 7
        count = collections.Counter(A)
        keys = sorted(count)

        ans = 0

        # Now, let's do a 3sum on "keys", for i <= j <= k.
        # We will use count to add the correct contribution to ans.
        for i, x in enumerate(keys):
            T = target - x
            j, k = i, len(keys) - 1
            while j <= k:
                y, z = keys[j], keys[k]
                if y + z < T:
                    j += 1
                elif y + z > T:
                    k -= 1
                else: # x+y+z == T, now calculate the size of the contribution
                    if i < j < k:
                        ans += count[x] * count[y] * count[z]
                    elif i == j < k:
                        ans += count[x] * (count[x] - 1) / 2 * count[z]
                    elif i < j == k:
                        ans += count[x] * count[y] * (count[y] - 1) / 2
                    else:  # i == j == k
                        ans += count[x] * (count[x] - 1) * (count[x] - 2) / 6

                    j += 1
                    k -= 1

        return ans % MOD
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the length of `A`.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution: (Two pointer)**
```
Runtime: 76 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        MOD = 10**9 + 7
        count = collections.Counter(A)
        keys = sorted(count)

        ans = 0

        # Now, let's do a 3sum on "keys", for i <= j <= k.
        # We will use count to add the correct contribution to ans.
        for i, x in enumerate(keys):
            T = target - x
            j, k = i, len(keys) - 1
            while j <= k:
                y, z = keys[j], keys[k]
                if y + z < T:
                    j += 1
                elif y + z > T:
                    k -= 1
                else: # x+y+z == T, now calculate the size of the contribution
                    if i < j < k:
                        ans += count[x] * count[y] * count[z]
                    elif i == j < k:
                        ans += count[x] * (count[x] - 1) // 2 * count[z]
                    elif i < j == k:
                        ans += count[x] * count[y] * (count[y] - 1) // 2
                    else:  # i == j == k
                        ans += count[x] * (count[x] - 1) * (count[x] - 2) // 6

                    j += 1
                    k -= 1

        return ans % MOD
```