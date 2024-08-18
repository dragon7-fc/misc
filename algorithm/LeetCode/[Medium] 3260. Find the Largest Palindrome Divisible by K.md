3260. Find the Largest Palindrome Divisible by K

You are given two positive integers `n` and `k`.

An integer `x` is called **k-palindromic** if:

* `x` is a **palindrome**.
* `x` is divisible by `k`.

Return the largest integer having `n` digits (as a string) that is **k-palindromic**.

**Note** that the integer must not have leading zeros.

 

**Example 1:**
```
Input: n = 3, k = 5

Output: "595"

Explanation:

595 is the largest k-palindromic integer with 3 digits.
```

**Example 2:**
```
Input: n = 1, k = 4

Output: "8"

Explanation:

4 and 8 are the only k-palindromic integers with 1 digit.
```

**Example 3:**
```
Input: n = 5, k = 6

Output: "89898"
```
 

**Constraints:**

* `1 <= n <= 10^5`
* `1 <= k <= 9`

# Submissions
---
**Solution 1: (DP Top-Down, Math)**

Time complexity: O(n∗10)
Space complexity: O(n∗10)

```
Runtime: 628 ms
Memory: 191.80 MB
```
```c++
class Solution {
    int dp[100005][11];
    int up[100005];
    int solve(int i, int n, int t, int mod, int k, vector<vector<int>>& kmod){
        if(i == n) return mod == 0;
        if(dp[i][mod] != -1) return dp[i][mod];
        int oi = t - i - 1;
        int no = 0;
        for(int dig=9; dig>=0; dig--){
            int val = solve(i+1, n, t, (mod + kmod[i][dig] + ((oi != i) ? kmod[oi][dig] : 0)) % k, k, kmod);
            // if(dig == 6 && i == n/2) cout << val << endl;
            if(val){
                up[i] = dig;
                break;
            }
        }
        return dp[i][mod] = (up[i] != -1);
    }
public:
    string largestPalindrome(int n, int k) {
        vector<vector<int>> kmod(n, vector<int>(10));
        int num = 1;
        for(int i=0; i<n; i++){
            for(int j=1; j<10; j++){
                kmod[i][j] = (num * j) % k;
            }
            num = (num * 10) % k;
        }
        memset(dp, -1, sizeof dp);
        memset(up, -1, sizeof up);
        string ans(n, '0');
        solve(0, (n+1)/2, n, 0, k, kmod);
        for(int i=0; i<(n+1)/2; i++){
            ans[i] = '0' + up[i];
            ans[n-i-1] = ans[i];
        }
        return ans;
    }
};
```
