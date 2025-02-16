2698. Find the Punishment Number of an Integer


Given a positive integer `n`, return the **punishment number** of `n`.

The **punishment number** of `n` is defined as the sum of the squares of all integers `i` such that:

* `1 <= i <= n`
* The decimal representation of `i * i` can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals `i`.
 

**Example 1:**
```
Input: n = 10
Output: 182
Explanation: There are exactly 3 integers i that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 + 1.
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 + 0.
Hence, the punishment number of 10 is 1 + 81 + 100 = 182
```

**Example 2:**
```
Input: n = 37
Output: 1478
Explanation: There are exactly 4 integers i that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1. 
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 + 1. 
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 + 0. 
- 36 since 36 * 36 = 1296 and 1296 can be partitioned into 1 + 29 + 6.
Hence, the punishment number of 37 is 1 + 81 + 100 + 1296 = 1478
```

**Constraints:**

* `1 <= n <= 1000`

 # Submissions
---
**Solution 1: (Backtracking)**
```
Runtime: 1516 ms
Memory: 16.4 MB
```
```python
class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0
        def bt(i, cur, s, t):
            if i == len(s):
                if cur == t:
                    return True
                return False
            j = i+1
            while j <= len(s):
                ncur = cur + int(s[i:j])
                if cur > t:
                    break
                if bt(j, ncur, s, t):
                    return True
                j += 1
            return False
                
        for i in range(1, n+1):
            if bt(0, 0, str(i*i), i):
                ans += i*i
                
        return ans
```

**Solution 2: (DP Bottom-Up)**

cur 1 2 9 6
    - --- -
ncur  296
left  ncur/10**k
right ncur%(10**k)
j     ^
k         ^
left   29
right     6
1 <= k <= j
          [6]
        [96, 15]
      [296, 35, 17, 98]
    [1296, 135, 108, 27, ]

dp[i][j] = cur/(10**k) + dp[cur%(10**k)] 

```
Runtime: 1029 ms, Beats 5.04%
Memory: 431.86 MB, Beats 10.58%
```
```c++
class Solution {
public:
    int punishmentNumber(int n) {
        int i, j, k, cur, ncur, left, right;
        vector<vector<unordered_set<int>>> dp(1001, vector<unordered_set<int>>(8));
        int ans = 0;
        for (i = 1; i <= n; i ++) {
            cur = i*i;
            for (j = 1; pow(10, j-1) <= cur; j ++) {
                ncur = cur%(int)pow(10, j);
                for (k = 0; k < j; k ++) {
                    left = ncur/(int)pow(10, k);
                    for (auto right: dp[i][k]) {
                        dp[i][j].insert(left + right);
                    }
                }
                dp[i][j].insert(ncur);
            }
            if (dp[i][j-1].count(i)) {
                ans += cur;
            }
        }
        return ans;
    }
};
```


**Solution 3: (Backtracking)**
```
Runtime: 145 ms
Memory: 5.9 MB
```
```c++
class Solution {
    bool check(string s,int n,int idx = 0,int sum = 0)
    {
        if (idx >= s.size())
        {
            // cout<<n<<" "<<sum<<endl;
            if (sum == n) return true;
            return false;
        }
        int num = 0;
        for (int i = idx; i < s.size(); i++)
        {
            num = num*10 + (s[i]-'0');
            if (num > n) return false;
            if(check(s, n, i+1, sum+num)) return true;
        }
        return false;
    }
public:
    int punishmentNumber(int n) {
        int ans = 0;
        for (int i = 1; i <= n; i ++)
        {
            int x = i*i;
            string s = to_string(x);
            if (check(s, i))
            {
                ans += x;
            }
        }
        return ans;
    }
};
```

**Solution 4: (Recursion of Integers, Time: O(n * 2^(log_10 (n))), Space: O(log_10 (n)))**
```
Runtime: 0 ms, Beats 100.00%
Memory: 7.86 MB, Beats 95.72%
```
```c++
class Solution {
     bool dfs(int num, int target) {
        if (target < 0 || num < target) {
            return false;
        }
        if (num == target) {
            return true;
        }
        return dfs(num / 10, target - num % 10) ||
               dfs(num / 100, target - num % 100) ||
               dfs(num / 1000, target - num % 1000);
    }

public:
    int punishmentNumber(int n) {
        int i, cur, ans = 0;
        for (i = 1; i <= n; i++) {
            cur = i*i;
            if (dfs(cur, i)) {
                ans += cur;
            }
        }
        return ans;
    }
};
```
