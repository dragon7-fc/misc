132. Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

**Example:**
```
Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
```

# Submissions
---
**Solution 1: (DP Top-Down)**
```
Runtime: 2352 ms
Memory Usage: 18.9 MB
```
```python
class Solution:
    def minCut(self, s: str) -> int:
        
        @functools.lru_cache(None)
        def dp(cur):
            if cur == cur[::-1]: return 0
            for i in range(1, len(cur)):
                if cur[:i] == cur[:i][::-1] and cur[i:] == cur[i:][::-1]:
                    return 1
            rst = len(s) - 1
            for i in range(1, len(cur)):
                if cur[:i] == cur[:i][::-1]:
                    rst = min(dp(cur[i:]), rst)
            return rst + 1

        return dp(s)
```

        return dfs(0, len(s))
```
**Solution 1: (DP Top-Down)**
```
Runtime: 2440 ms
Memory Usage: 16.9 MB
```
```python
class Solution:
    def minCut(self, s: str) -> int:
        
        @functools.lru_cache(None)
        def dp(i, j):
            if s[i:j] == s[i:j][::-1]: return 0
            for k in range(i + 1, j):
                if s[i:k] == s[i:k][::-1] and s[k:j] == s[k:j][::-1]:
                    return 1
            rst = float('inf')
            for k in range(i + 1, j):
                if s[i:k] == s[i:k][::-1]:
                    rst = min(rst, dp(k, j) + 1)
            return rst

        return dp(0, len(s))
```

**Solution 3: (DP Top-Down)**
```
Runtime: 1544 ms
Memory Usage: 487.2 MB
```
```python
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        @lru_cache(None)
        def isPalindrome(l, r):  # l, r inclusive
            if l >= r: return True
            if s[l] != s[r]: return False
            return isPalindrome(l+1, r-1)
        
        @lru_cache(None)
        def dp(i):  # s[i..n-1]
            if i == n:
                return 0
            ans = math.inf
            for j in range(i, n):
                if (isPalindrome(i, j)):
                    ans = min(ans, dp(j+1) + 1)
            return ans
        
        return dp(0) - 1
```

**Solution 4: (DP Top-Down)**
```
Runtime: 1578 ms
Memory: 7 MB
```
```c++
class Solution {
    bool isPalindrome(string &s,int i,int j){
        while(j>=i){
            if(s[i]!=s[j]) return false;
            i++;
            j--;
        }
        return true;
    }
    int solve(string &s,int i, vector<int> &dp){
        if(i>=s.size() || isPalindrome(s,i,s.size()))
            return 0;
        if(dp[i]!=-1) return dp[i];
        int res=INT_MAX;
        for(int j=i;j<s.size();j++){
            if(isPalindrome(s, i, j))
            {
                int cost=1+solve(s, j+1, dp);
                res = min(res, cost);
            }
        }
        return dp[i]=res;
    }
public:
    int minCut(string s) {
        vector<int> dp(s.size(), -1);
        return solve(s, 0, dp)-1;
    }
};
```

**Solution 5: (DP Bottom-Up)**
```
Runtime: 1504 ms
Memory: 6.8 MB
```
```c++
class Solution {
    bool isPalindrome(string& s, int l, int r) {
        while (l < r) {
            if(s[l++] != s[r--]) {
                return false;
            }
        }
        return true;
    }
public:
    int minCut(string s) {
        int n = s.size();
        vector<int> dp(n+1, 0);
        for(int i = n-1; i >= 0; i--) {
            int minSteps = INT_MAX;
            for (int j = i; j < n; j++) {
                if (isPalindrome(s, i, j)) {
                    int steps = 1 + dp[j+1];
                    minSteps = min(minSteps, steps);
                }
            }
            dp[i] = minSteps;
        }
        return dp[0] - 1;
    }
};
```

**Solution 6: (DP Bottom-Up, Two Layers of DP, DP + palindrome precomputation)**
```
Runtime: 56 ms, Beats 60.60%
Memory: 12.12 MB, Beats 31.70%
```
```c++
class Solution {
public:
    int minCut(string s) {
        int n = s.length();
        vector<vector<bool>> isPal(n, vector<bool>(n));
        for (int k = 1; k <= n; k ++) {
            for (int i = 0; i + k - 1 < n; i ++) {
                int j = i + k - 1;
                if (k == 1) {
                    isPal[i][j] = true;
                } else if (k == 2) {
                    isPal[i][j] = s[i] == s[j];
                } else {
                    isPal[i][j] = (s[i] == s[j]) && isPal[i + 1][j - 1];
                }
            }
        }
        vector<int> dp(n);
        for (int j = 0; j < n; j ++) {
            if (isPal[0][j]) {
                dp[j] = 0;
            } else {
                dp[j] = j;
                for (int i = 0; i < j; i ++) {
                    if (isPal[i + 1][j]) {
                        dp[j] = min(dp[j], dp[i] + 1);
                    }
                }
            }
        }
        return dp[n - 1];
    }
};
```
