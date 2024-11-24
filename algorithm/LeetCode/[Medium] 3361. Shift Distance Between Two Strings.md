3361. Shift Distance Between Two Strings

You are given two strings `s` and `t` of the same length, and two integer arrays `nextCost` and `previousCost`.

In one operation, you can pick any index i of s, and perform either one of the following actions:

* Shift `s[i]` to the next letter in the alphabet. If `s[i] == 'z'`, you should replace it with `'a'`. This operation costs `nextCost[j]` where `j` is the index of `s[i]` in the alphabet.
* Shift `s[i]` to the previous letter in the alphabet. If `s[i] == 'a'`, you should replace it with `'z'`. This operation costs `previousCost[j]` where `j` is the index of `s[i]` in the alphabet.

The **shift distance** is the **minimum** total cost of operations required to transform `s` into `t`.

Return the **shift distance** from `s` to `t`.

 

**Example 1:**
```
Input: s = "abab", t = "baba", nextCost = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], previousCost = [1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

Output: 2

Explanation:

We choose index i = 0 and shift s[0] 25 times to the previous character for a total cost of 1.
We choose index i = 1 and shift s[1] 25 times to the next character for a total cost of 0.
We choose index i = 2 and shift s[2] 25 times to the previous character for a total cost of 1.
We choose index i = 3 and shift s[3] 25 times to the next character for a total cost of 0.
```

**Example 2:**
```
Input: s = "leet", t = "code", nextCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], previousCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

Output: 31

Explanation:

We choose index i = 0 and shift s[0] 9 times to the previous character for a total cost of 9.
We choose index i = 1 and shift s[1] 10 times to the next character for a total cost of 10.
We choose index i = 2 and shift s[2] 1 time to the previous character for a total cost of 1.
We choose index i = 3 and shift s[3] 11 times to the next character for a total cost of 11.
```

**Constraints:**

`1 <= s.length == t.length <= 10^5`
`s` and `t` consist only of lowercase English letters.
`nextCost.length == previousCost.length == 26`
`0 <= nextCost[i], previousCost[i] <= 10^9`

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 177 ms
Memory: 53.12 MB
```
```c++
class Solution {
public:
    long long shiftDistance(string s, string t, vector<int>& nextCost, vector<int>& previousCost) {
        long long ans = 0;
        for (int i = 0; i < s.length(); ++i) {
            int ss = s[i] - 'a';
            int tt = t[i] - 'a';
            if (ss == tt) continue;

            long long next = 0, pre = 0;

            for (int j = ss; j != tt; j = (j + 1) % 26) {
                next += nextCost[j];
            }
            for (int j = ss; j != tt; j = (j - 1 + 26) % 26) {
                pre += previousCost[j];
            }
            ans += min(next, pre);
        }

        return ans;
    }
};
```

**Solution 2: (Prefix Sum)**
```
Runtime: 67 ms
Memory: 61.16 MB
```
```c++
class Solution {
public:
    long long shiftDistance(string s, string t, vector<int>& nextCost, vector<int>& previousCost) {
        vector<long long> pre(27), pre2(27);
        int i, j;
        long long ans = 0;
        for (i = 0; i < 26; i ++) {
            pre[i+1] = pre[i] + nextCost[i];
        }
        for (i = 25; i >= 0; i --) {
            pre2[i] = pre2[i+1] + previousCost[i];
        }
        vector<vector<long long>> dp(26, vector<long long>(26));
        for (i = 0; i < 26; i ++) {
            for (j = 0; j < 26; j ++) {
                if (i < j) {
                    dp[i][j] = min(pre[j]-pre[i], pre2[0]-(pre2[i+1]-pre2[j+1]));
                } else if (i > j) {
                    dp[i][j] = min(pre2[j+1]-pre2[i+1], pre[26]-(pre[i]-pre[j]));
                }
            }
        }
        for (i = 0; i < s.size(); i ++) {
            ans += dp[s[i]-'a'][t[i]-'a'];
        }
        return ans;
    }
};
```
