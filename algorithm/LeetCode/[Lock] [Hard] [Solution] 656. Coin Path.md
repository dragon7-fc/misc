656. Coin Path

Given an array `A` (index starts at `1`) consisting of N integers: `A1, A2, ..., AN` and an integer `B`. The integer `B` denotes that from any place (suppose the index is `i`) in the array `A`, you can jump to any one of the place in the array `A` indexed `i+1`, `i+2`, …, `i+B` if this place can be jumped to. Also, if you step on the index `i`, you have to pay `Ai` coins. If `Ai` is `-1`, it means you can’t jump to the place indexed `i` in the array.

Now, you start from the place indexed `1` in the array `A`, and your aim is to reach the place indexed `N` using the minimum coins. You need to return the path of indexes (starting from `1` to `N`) in the array you should take to get to the place indexed `N` using minimum coins.

If there are multiple paths with the same cost, return the lexicographically smallest such path.

If it's not possible to reach the place indexed `N` then you need to return an empty array.

**Example 1:**
```
Input: [1,2,4,-1,2], 2
Output: [1,3,5]
```

**Example 2:**
```
Input: [1,2,4,-1,2], 1
Output: []
```

**Note:**

* Path `Pa1, Pa2, ..., Pan` is lexicographically smaller than `Pb1, Pb2, ..., Pbm`, if and only if at the first `i` where `Pai` and `Pbi` differ, `Pai < Pbi`; when no such `i` exists, then `n < m`.
* `A1 >= 0. A2, ..., AN` (if exist) will in the range of `[-1, 100]`.
* Length of `A` is in the range of `[1, 1000]`.
* `B` is in the range of `[1, 100]`.

# Solution
---
## Approach #1 Brute Force[Time Limit Exceeded]
In this approach, we make use of a $next$ array of size $n$. Here, $n$ refers to the size of the given $A$ array. The array $nums$ is used such that $nums[i]$ is used to store the minimum number of coins needed to jump till the end of the array $A$, starting from the index $i$.

We start by filling the $next$ array with all -1's. Then, in order to fill this $next$ array, we make use of a recursive function `jump(A, B, i, next)` which fills the $next$ array starting from the index $i$ onwards, given $A$ as the coins array and $B$ as the largest jump value.

With $i$ as the current index, we can consider every possible index from $i+1$ to $i+B$ as the next place to be jumped to. For every such next index, $j$, if this place can be jumped to, we determine the cost of reaching the end of the array starting from the index $i$, and with $j$ as the next index jumped from $i$, as $A[i] + jump(A, B, j, next)$. If this cost is lesser than the minimum cost required till now, for the same starting index, we can update the minimum cost and the value of $next[i]$ as well.

For every such function call, we also need to return this minimum cost.

At the end, we traverse over the $next$ array starting from the index 1. At every step, we add the current index to the resres list to be returned and also jump/move to the index pointed by $next[i]$, since this refers to the next index for the minimum cost. We continue in the same manner till we reach the end of the array $A$.

```java
public class Solution {
    public List < Integer > cheapestJump(int[] A, int B) {
        int[] next = new int[A.length];
        Arrays.fill(next, -1);
        jump(A, B, 0, next);
        List < Integer > res = new ArrayList();
        int i;
        for (i = 0; i < A.length && next[i] > 0; i = next[i])
            res.add(i + 1);
        if (i == A.length - 1 && A[i]>= 0)
            res.add(A.length);
        else
            return new ArrayList < Integer > ();
        return res;
    }
    public long jump(int[] A, int B, int i, int[] next) {
        if (i == A.length - 1 && A[i] >= 0)
            return A[i];
        long min_cost = Integer.MAX_VALUE;
        for (int j = i + 1; j <= i + B && j < A.length; j++) {
            if (A[j] >= 0) {
                long cost = A[i] + jump(A, B, j, next);
                if (cost < min_cost) {
                    min_cost = cost;
                    next[i] = j;
                }
            }
        }
        return min_cost;
    }
}
```

**Complexity Analysis**

* Time complexity : $O(B^n)$. The size of the recursive tree can grow upto $O(b^n)$ in the worst case. This is because, we have $B$ possible branches at every step. Here, $B$ refers to the limit of the largest jump and $n$ refers to the size of the given $A$ array.

* Space complexity : $O(n)$. The depth of the recursive tree can grow upto nn. nextnext array of size nn is used.

## Approach #2 Using Memoization [Accepted]
**Algorithm**

In the recursive solution just discussed, a lot of duplicate function calls are made, since we are considering the same index through multiple paths. To remove this redundancy, we can make use of memoization.

We keep a memomemo array, such that $memo[i]$ is used to store the minimum cost of jumps to reach the end of the array $A$. Whenever the value for any index is calculated once, it is stored in its appropriate location. Thus, next time whenever the same function call is made, we can return the result directly from this $memo$ array, pruning the search space to a great extent.

```java
public class Solution {
    public List < Integer > cheapestJump(int[] A, int B) {
        int[] next = new int[A.length];
        Arrays.fill(next, -1);
        long[] memo = new long[A.length];
        jump(A, B, 0, next, memo);
        List < Integer > res = new ArrayList();
        int i;
        for (i = 0; i < A.length && next[i] > 0; i = next[i])
            res.add(i + 1);
        if (i == A.length - 1 && A[i] >= 0)
            res.add(A.length);
        else
            return new ArrayList < Integer > ();
        return res;
    }
    public long jump(int[] A, int B, int i, int[] next, long[] memo) {
        if (memo[i] > 0)
            return memo[i];
        if (i == A.length - 1 && A[i] >= 0)
            return A[i];
        long min_cost = Integer.MAX_VALUE;
        for (int j = i + 1; j <= i + B && j < A.length; j++) {
            if (A[j] >= 0) {
                long cost = A[i] + jump(A, B, j, next, memo);
                if (cost < min_cost) {
                    min_cost = cost;
                    next[i] = j;
                }
            }
        }
        memo[i] = min_cost;
        return min_cost;
    }
}
```

**Complexity Analysis**

* Time complexity : $O(nB)$. $memo$ array of size $n$ is filled only once. We also do a traversal over the nextnext array, which will go upto $B$ steps. Here, nn refers to the number of nodes in the given tree.

* Space complexity : $O(n)$. The depth of the recursive tree can grow upto $n$. nextnext array of size nn is used.


## Approach #3 Using Dynamic Programming [Accepted]
**Algorithm**

From the solutions discussed above, we can observe that the cost of jumping till the end of the array AA starting from the index $i$ is only dependent on the elements following the index $i$ and not the ones before it. This inspires us to make use of Dynamic Programming to solve the current problem.

We again make use of a $next$ array to store the next jump locations. We also make use of a $dp$ with the same size as that of the given $A$ array. $dp[i]$ is used to store the minimum cost of jumping till the end of the array $A$, starting from the index $i$. We start with the last index as the current index and proceed backwards for filling the nextnext and $dp$ array.

With $i$ as the current index, we consider all the next possible positions from $i+1$, $i+2$,..., $i+B$, and determine the position, $j$, which leads to a minimum cost of reaching the end of AA, which is given by $A[i]+dp[j]$. We update $next[i]$ with this corresponding index. We also update $dp[i]$ with the minimum cost, to be used by the previous indices' cost calculations.

At the end, we again jump over the indices as per the nextnext array and put these indices in the $res$ array to be returned.

```java
public class Solution {
    public List < Integer > cheapestJump(int[] A, int B) {
        int[] next = new int[A.length];
        long[] dp = new long[A.length];
        Arrays.fill(next, -1);
        List < Integer > res = new ArrayList();
        for (int i = A.length - 2; i >= 0; i--) {
            long min_cost = Integer.MAX_VALUE;
            for (int j = i + 1; j <= i + B && j < A.length; j++) {
                if (A[j] >= 0) {
                    long cost = A[i] + dp[j];
                    if (cost < min_cost) {
                        min_cost = cost;
                        next[i] = j;
                    }
                }
            }
            dp[i] = min_cost;
        }
        int i;
        for (i = 0; i < A.length && next[i] > 0; i = next[i])
            res.add(i + 1);
        if (i == A.length - 1 && A[i] >= 0)
            res.add(A.length);
        else
            return new ArrayList < Integer > ();
        return res;
    }
}
```

**Complexity Analysis**

* Time complexity : $O(nB)$. We need to consider all the possible $B$ positions for every current index considered in the $A$ array. Here, $A$ refers to the number of elements in $A$.

* Space complexity : $O(n)$. $dp$ and $next$ array of size $n$ are used.

# Submissions
---
**Solution 1: (DP Top-Down)**
```
Runtime: 200 ms
Memory Usage: 15.6 MB
```
```python
class Solution:
    def cheapestJump(self, A: List[int], B: int) -> List[int]:
        N = len(A)
        rst = [-1]*N
        ans = []
        
        @functools.lru_cache(None)
        def dp(i):
            nonlocal rst
            if i == N - 1 and A[i] >= 0:
                return A[i]
            min_cost = float('inf')
            for j in range(i + 1, min(i + B+1, N)):
                if A[j] >= 0:
                    cost = A[i] + dp(j)
                    if cost < min_cost:
                        min_cost = cost
                        rst[i] = j
            return min_cost
        
        dp(0)
        i = 0
        while i < N and rst[i] > 0:
            ans += [i+1]
            i = rst[i]
        if i == N - 1 and A[i]>= 0:
            ans += [N]
        else:
            return [];
        return ans
        return ans
```

**Solution 2; (DP Bottom-Up)**
```
Runtime: 120 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def cheapestJump(self, A: List[int], B: int) -> List[int]:
        N = len(A)
        rst = [-1]*N
        ans = []
        dp = [0]*N
        for i in range(N - 2, -1, -1):
            min_cost = float('inf')
            for j in range(i + 1, min(i + B+1, N)):
                if A[j] >= 0:
                    cost = A[i] + dp[j]
                    if cost < min_cost:
                        min_cost = cost
                        rst[i] = j
            dp[i] = min_cost
        i = 0
        while i < N and rst[i] > 0:
            ans += [i+1]
            i = rst[i]
        if i == N - 1 and A[i]>= 0:
            ans += [N]
        else:
            return [];
        return ans
```