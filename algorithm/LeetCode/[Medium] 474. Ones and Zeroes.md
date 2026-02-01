474. Ones and Zeroes

In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of **m** 0s and **n** 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given **m** `0s` and **n** `1s`. Each `0` and `1` can be used at most **once**.

**Note:**

* The given numbers of 0s and 1s will both not exceed 100
* The size of given string array won't exceed 600.
 

**Example 1:**
```
Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”
```

**Example 2:**
```
Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".
```

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 2864 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            zeros, ones = s.count("0"), s.count("1")
            for i in range(m, zeros-1, -1):
                for j in range(n , ones-1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - zeros][j - ones])
        return dp[-1][-1]
```

**Solution 2: (DP Top-Town)**
```
Runtime: 2100 ms
Memory Usage: 264.5 MB
```
```python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        N = len(strs)
        
        @functools.lru_cache(None)
        def dp(index, m_zeroes, n_ones):
            if index >= N:
                return 0
            else:
                s = strs[index]
                ones, zeroes = s.count('1'), s.count('0')
                if m_zeroes - zeroes >= 0 and n_ones - ones >= 0:
                    return max(1 + dp(index + 1, m_zeroes - zeroes, n_ones - ones), dp(index + 1, m_zeroes, n_ones))
                else:
                    return dp(index + 1, m_zeroes, n_ones)
        
        return dp(0, m, n)
```

**Solution 3: (DP Top-Town)**
```
Runtime: 474 ms
Memory Usage: 102.2 MB
```
```c++
class Solution {
    int explore(vector<pair<int,int>>& count,vector<vector<vector<int>>> &dp,int m,int n,int i)
    {
        if(m<0||n<0)
            return -1;
        if(i==count.size()||(m==0&&n==0))
        {
            return 0;
        }
    
        if(dp[i][m][n]!=-1)
            return dp[i][m][n];
        int ans=0;
        //We have Two option 
        
        //1) Take current one
            ans=max(ans,1+explore(count,dp,m-count[i].first,n-count[i].second,i+1));
        
        //2)Don't take the current one 
        
            ans=max(ans,explore(count,dp,m,n,i+1));
        
        
        return dp[i][m][n]=ans;
    }
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        vector<pair<int,int>> count;
        vector<vector<vector<int>>> dp(strs.size(),vector<vector<int>>(m+1,vector<int>(n+1,-1)));
        for(int i=0;i<strs.size();i++)
        {
            int count0=0;
            int count1=0;
            for(int j=0;j<strs[i].size();j++)
            {
                if(strs[i][j]=='0')
                {
                    count0++;
                }
                else
                {
                    count1++;
                }
            }
            count.push_back({count0,count1});
        }
        
        return explore(count,dp,m,n,0);
    }
};
```

**Solution 4: (DP Bottom-Up)**

    strs = ["10","0001","111001","1"      ,"0"], m = 5, n = 3
cm (#0)      1    3      2        0         1
cn (#1)      1    1      4        1         0

dp[i + cm][j + cn] = max(dp[i + cm][j + cn], dp[i][j] + 1)

        i
    <-------
dp  0  1  2  3n   ^
0   0  1          |
1   1  1  2       |
2      2  3       |j
3      1  2       |
4      2  2  3
5         3  4 < ans
m



```
Runtime: 39 ms, Beats 96.59%
Memory: 13.73 MB, Beats 84.01%
```
```c++
class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        int i, j, cm, cn, ans = 0;
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, -1));
        dp[0][0] = 0;
        for (auto &str: strs) {
            cm = count(str.begin(), str.end(), '0');
            cn = str.length() - cm;
            for (i = m - cm; i >= 0; i --) {
                for (j = n - cn; j >= 0; j --) {
                    if (dp[i][j] >= 0) {
                        dp[i + cm][j + cn] = max(dp[i + cm][j + cn], dp[i][j] + 1);
                        ans = max(ans, dp[i + cm][j + cn]);
                    }
                }
            }
        }
        return ans;
    }
};
```
