96. Unique Binary Search Trees

Given n, how many structurally unique **BST**'s (binary search trees) that store values 1 ... n?

**Example:**
```
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 40 ms
Memory Usage: N/A
```
```python
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        arr = [0]*(n+1)
        arr[0] = 1
        arr[1] = 1
        arr[2] = 2
        for i in range(3,n+1):
            for j in range(i):
                arr[i] += arr[j]*arr[i-1-j]
        return arr[-1]
```

**Solution 2: (DP Top-Down)**
```
Runtime: 24 ms
Memory Usage: 12.9 MB
```
```python
import functools
class Solution:
    
    @functools.lru_cache(None)
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        elif n == 2:
            return 2
        rst = 0
        for i in range(n):
            rst += self.numTrees(i) * self.numTrees(n - i - 1)
        return rst
```

**Solution 3: (DP Bottom-Up)**
```
Runtime: 0 ms
Memory Usage: 6 MB
```
```c++
class Solution {
public:
    int numTrees(int n) {
        vector<int> dp(n+1,0);
        dp[0]=1;  
        for(int i=1;i<=n;i++){
            int sum=0;
            for(int j=1;j<=i;j++){
                sum+=(dp[j-1]*dp[i-j]);    
            }
            dp[i]=sum;
        }
        return dp[n];
    }
};
```

**Solution 4: (DP Top-Down)**
```
Runtime: 0 ms
Memory Usage: 6.1 MB
```
```c++
class Solution {
public:
    int rec(int n, map<int,int> &dp){
        if(n==0){
            dp[0] = 1;
            return 1;
        }
        if(dp.find(n)!=dp.end())
            return dp[n];
        int sum = 0;
        for(int k=1;k<=n;k++)
            sum += rec(n-k,dp)*rec(k-1,dp);
        dp[n] = sum;
        return sum;
    }
    int numTrees(int n) {
        map<int,int> dp;
        return rec(n,dp);
    }
};
```

**Solution 5: (DP Bottom-Up)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 8.07 MB, Beats 38.66%
```
```c++
class Solution {
public:
    int numTrees(int n) {
        if (n <= 2) {
            return n;
        }
        int i, j;
        vector<int> dp(n+1);
        dp[0] = 1;
        dp[1] = 1;
        dp[2] = 2;
        for (i = 3; i <= n; i ++) {
            for (j = 0; j < i; j ++) {
                dp[i] += dp[j]*dp[i-j-1];
            }
        }
        return dp[n];
    }
};
```
