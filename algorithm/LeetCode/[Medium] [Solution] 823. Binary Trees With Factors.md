823. Binary Trees With Factors

Given an array of unique integers, each integer is strictly greater than 1.

We make a binary tree using these integers and each number may be used for any number of times.

Each non-leaf node's value should be equal to the product of the values of it's children.

How many binary trees can we make?  Return the answer modulo **10 ** 9 + 7**.

**Example 1:**
```
Input: A = [2, 4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]
```

**Example 2:**
```
Input: A = [2, 4, 5, 10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
```

**Note:**

* `1 <= A.length <= 1000`.
* `2 <= A[i] <= 10 ^ 9`.

# Submissions
---
## Approach #1: Dynamic Programming [Accepted]
**Intuition**

The largest value `v` used must be the root node in the tree. Say `dp(v)` is the number of ways to make a tree with root node `v`.

If the root node of the tree (with value `v`) has children with values `x` and `y` (and `x * y == v`), then there are `dp(x) * dp(y)` ways to make this tree.

In total, there are $\sum_{\substack{x * y = v}} \text{dp}(x) * \text{dp}(y)$ ways to make a tree with root node `v`.

**Algorithm**

Actually, let `dp[i]` be the number of ways to have a root node with value `A[i]`.

Since in the above example we always have `x < v` and `y < v`, we can calculate the values of `dp[i]` in increasing order using dynamic programming.

For some root value `A[i]`, let's try to find candidates for the children with values `A[j]` and `A[i] / A[j]` (so that evidently `A[j] * (A[i] / A[j]) = A[i]`). To do this quickly, we will need index which looks up this value: if `A[k] = A[i] / A[j]`, then `index[A[i] / A[j]] = k`.

After, we'll add all possible `dp[j] * dp[k]` (with `j < i, k < i`) to our answer `dp[i]`. In our Java implementation, we carefully used long so avoid overflow issues.

```python
class Solution(object):
    def numFactoredBinaryTrees(self, A):
        MOD = 10 ** 9 + 7
        N = len(A)
        A.sort()
        dp = [1] * N
        index = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for j in xrange(i):
                if x % A[j] == 0: #A[j] will be left child
                    right = x / A[j]
                    if right in index:
                        dp[i] += dp[j] * dp[index[right]]
                        dp[i] %= MOD

        return sum(dp) % MOD
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the length of `A`. This comes from the two for-loops iterating `i` and `j`.

* Space Complexity: $O(N)$, the space used by `dp` and `index`.

# Submissions
---
**Solution 1: (Dynamic Programming, Bottom-Up)**
```
Runtime: 388 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        N = len(arr)
        arr.sort()
        dp = [1] * N
        index = {x: i for i, x in enumerate(arr)}
        for i, x in enumerate(arr):
            for j in range(i):
                if x % arr[j] == 0: #arr[j] will be left child
                    right = x // arr[j]
                    if right in index:
                        dp[i] += dp[j] * dp[index[right]]
                        dp[i] %= MOD

        return sum(dp) % MOD
```

**Solution 2: (DP Top-Down)**
```
Runtime: 584 ms
Memory Usage: 15.2 MB
```
```python
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        s_arr, N = set(arr), 10**9 + 7
        
        @lru_cache(None)
        def dp(num):
            ans = 1
            for cand in s_arr:
                if num % cand == 0 and num//cand in s_arr:
                    ans += dp(cand)*dp(num//cand)
            return ans
        
        return sum(dp(num) for num in s_arr) % N
```

**Solution 3: (DP Bottom-Up)**
```
Runtime: 178 ms
Memory Usage: 16.5 MB
```
```c++
class Solution {
public:
    int numFactoredBinaryTrees(vector<int>& arr) {
        sort(arr.begin(),arr.end());
        int mod = 1e9 + 7;
        map<int, long long> mp;
        
        for(int j = 0; j < arr.size(); j++){
            mp[arr[j]] = 1;
            for(int i = 0; i < j; i++){
                if(arr[j] % arr[i] == 0){
                    mp[arr[j]] += (long long)(mp[arr[i]] * mp[arr[j] / arr[i]]) % mod;
                    mp[arr[j]] %= mod;
                }
            }
        }
        long long ans = 0;
        
        for(auto it = mp.begin(); it!=mp.end(); it++){
            ans = (ans + it->second)  % mod;
        }
        return ans;
    }
};
```
