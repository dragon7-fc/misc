932. Beautiful Array

For some fixed `N`, an array `A` is beautiful if it is a permutation of the integers `1, 2, ..., N`, such that:

For every `i < j`, there is **no** `k` with `i < k < j` such that `A[k] * 2 = A[i] + A[j]`.

Given `N`, return **any** beautiful array `A`.  (It is guaranteed that one exists.)

 

**Example 1:**
```
Input: 4
Output: [2,1,4,3]
```

**Example 2:**
```
Input: 5
Output: [3,1,2,5,4]
```

**Note:**

* `1 <= N <= 1000`

# Submissions
---
**Solution 1: (Divide and Conquer)**

Example:
1,2,3,4,5,6,7,8,9
-->
1,3,5,7,9,2,4,6,8
-->
1,5,9,3,7,2,6,4,8
-->
1,9,5,3,7,2,6,4,8

**Approach 1: Divide and Conquer**

**Intuition**

First, notice that the condition is equivalent to saying that `A` has no arithmetic subsequence. We'll use the term "arithmetic-free" interchangeably with "beautiful".

One way is to guess that we should divide and conquer. One reason for this is that the condition is linear, so if the condition is satisfied by variables taking on values `(1, 2, ..., n)`, it is satisfied by those variables taking on values `(a + b, a + 2*b, a + 3*b, ..., a + (n-1)*b)` instead.

If we perform a divide and conquer, then we have two parts left and right, such that each part is arithmetic-free, and we only want that a triple from both parts is not arithmetic. Looking at the conditions:

* `2*A[k] = A[i] + A[j]`
* `(i < k < j)`, `i` from `left`, `j` from `right`

we can guess that because the `left` hand side `2*A[k]` is even, we can choose `left` to have all odd elements, and `right` to have all even elements.

Another way we could arrive at this is to try to place a number in the middle, like `5`. We will have `4` and `6` say, to the `left` of `5`, and `7` to the `right` of `6`, etc. We see that in general, odd numbers move towards one direction and even numbers towards another direction.

One final way we could arrive at this is to inspect possible answers arrived at by brute force. On experimentation, we see that many answers have all the odd elements to one side, and all the even elements to the other side, with only minor variation.

**Algorithm**

Looking at the elements `1, 2, ..., N`, there are `(N+1) / 2` odd numbers and `N / 2` even numbers.

We solve for elements `1, 2, ..., (N+1) / 2` and map these numbers onto `1, 3, 5, ....` Similarly, we solve for elements `1, 2, ..., N/2` and map these numbers onto `2, 4, 6, ....`

We can compose these solutions by concatenating them, since an arithmetic sequence never starts and ends with elements of different parity.

We memoize the result to arrive at the answer quicker.

**Complexity Analysis**

* **Time Complexity**: $O(N \log N)$. The function f is called only $O(\log N)$ times, and each time does $O(N)$ work.

* **Space Complexity**: $O(N \log N)$.

```
Runtime: 36 ms
Memory Usage: 12.6 MB
```
```python
class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        def dfs(lst):
            if len(lst) <= 2:
                return lst
            return dfs(lst[::2]) + dfs(lst[1::2])
        
        return dfs([_ for _ in range(1,N+1)])
```
