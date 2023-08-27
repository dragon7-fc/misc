646. Maximum Length of Pair Chain

You are given `n` pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair `(c, d)` can follow another pair `(a, b)` if and only if `b < c`. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

**Example 1:**
```
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
```

**Note:**

* The number of given pairs will be in the range [1, 1000].

# Solution
---
## Approach #1: Dynamic Programming [Accepted]
**Intuition**

If a chain of length k ends at some `pairs[i]`, and `pairs[i][1] < pairs[j][0]`, we can extend this chain to a chain of length k+1.

Algorithm

Sort the pairs by first coordinate, and let `dp[i]` be the length of the longest chain ending at `pairs[i]`. When `i < j` and `pairs[i][1] < pairs[j][0]`, we can extend the chain, and so we have the candidate answer `dp[j] = max(dp[j], dp[i] + 1)`.

```python
class Solution(object): #Time Limit Exceeded
    def findLongestChain(self, pairs):
        pairs.sort()
        dp = [1] * len(pairs)

        for j in xrange(len(pairs)):
            for i in xrange(j):
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$ where $N$ is the length of pairs. There are two for loops, and $N^2$ dominates the sorting step.

* Space Complexity: $O(N)$ for sorting and to store dp.

## Approach #2: Greedy [Accepted]
**Intuition**

We can greedily add to our chain. Choosing the next addition to be the one with the lowest second coordinate is at least better than a choice with a larger second coordinate.

**Algorithm**

Consider the pairs in increasing order of their second coordinate. We'll try to add them to our chain. If we can, by the above argument we know that it is correct to do so.

```python
class Solution(object):
    def findLongestChain(self, pairs):
        cur, ans = float('-inf'), 0
        for x, y in sorted(pairs, key = operator.itemgetter(1)):
            if cur < x:
                cur = y
                ans += 1
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N \log N)$ where $N$ is the length of S. The complexity comes from the sorting step, but the rest of the solution does linear work.

* Space Complexity: $O(N)$. The additional space complexity of storing `cur` and `ans`, but sorting uses `O(N)O(N)` space. Depending on the implementation of the language used, sorting can sometimes use less space.

# Submissions
---
**Solution 1: (Dynamic Programming Bottom-Up)**
```
Runtime: 2676 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        dp = [1] * len(pairs)

        for j in range(len(pairs)):
            for i in range(j):
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)
```

**Solution 2: (Greedy)**
```
Runtime: 236 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        cur, ans = float('-inf'), 0
        for x, y in sorted(pairs, key=lambda v: v[1]):
            if cur < x:
                cur = y
                ans += 1
        return ans
```

**Solution 3: (DP Top-Down)**
```
Runtime: 1088 ms
Memory Usage: 14.5 MB
```
```python
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        N = len(pairs)
        pairs.sort()
        
        @functools.lru_cache(None)
        def dfs(i):
            if i == N-1:
                return 1
            j, rst = i+1, 0
            while j < N:
                if pairs[i][1] < pairs[j][0]:
                    rst = 1 + dfs(j)
                    break
                j += 1
            rst = max(rst, dfs(i+1))
            return rst
            
        return dfs(0)
```

**Solution 4: (DP Bottom-Up)**
```
Runtime: 212 ms
Memory: 22.8 MB
```
```c++
class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        int n = pairs.size();
        sort(pairs.begin(), pairs.end());
        vector<int> dp(n, 1);
        int ans = 1;
        for (int j = 1; j < n; j ++) {
            for (int i = 0; i < j; i ++) {
                if (pairs[i][1] < pairs[j][0]) {
                    dp[j] = max(dp[j], dp[i]+1);
                    ans = max(ans, dp[j]);
                }
            }
        }
        return ans;
    }
};
```

**Solution 5: (Greedy, sort by end point)**
```
Runtime: 39 ms
Memory: 22.4 MB
```
```c++
class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        int n = pairs.size();
        sort(pairs.begin(), pairs.end(), [](vector<int> &pa, vector<int> &pb){
            return pa[1] < pb[1];
        });
        int cur = INT_MIN, ans = 0;
        for (int i = 0; i < n; i ++) {
            if (cur < pairs[i][0]) {
                cur = pairs[i][1];
                ans += 1;
            }
        }
        return ans;
    }
};
```
