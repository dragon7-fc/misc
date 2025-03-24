3494. Find the Minimum Amount of Time to Brew Potions

You are given two integer arrays, `skill` and `mana`, of length `n` and `m`, respectively.

In a laboratory, `n` wizards must brew m potions in order. Each potion has a mana capacity `mana[j]` and must pass through all the wizards sequentially to be brewed properly. The time taken by the `i`th wizard on the `j`th potion is `timeij = skill[i] * mana[j]`.

Since the brewing process is delicate, a potion **must** be passed to the next wizard immediately after the current wizard completes their work. This means the timing must be synchronized so that each wizard begins working on a potion **exactly** when it arrives. ​

Return the **minimum** amount of time required for the potions to be brewed properly.

 

**Example 1:**
```
Input: skill = [1,5,2,4], mana = [5,1,4,2]

Output: 110

Explanation:

Potion Number	Start time	Wizard 0 done by	Wizard 1 done by	Wizard 2 done by	Wizard 3 done by
0	            0	        5	                30	                40	                60
1	            52	        53	                58	                60	                64
2	            54	        58	                78	                86	                102
3	            86	        88	                98	                102	                110
As an example for why wizard 0 cannot start working on the 1st potion before time t = 52, consider the case where the wizards started preparing the 1st potion at time t = 50. At time t = 58, wizard 2 is done with the 1st potion, but wizard 3 will still be working on the 0th potion till time t = 60.
```

**Example 2:**
```
Input: skill = [1,1,1], mana = [1,1,1]

Output: 5

Explanation:

Preparation of the 0th potion begins at time t = 0, and is completed by time t = 3.
Preparation of the 1st potion begins at time t = 1, and is completed by time t = 4.
Preparation of the 2nd potion begins at time t = 2, and is completed by time t = 5.
```

**Example 3:**
```
Input: skill = [1,2,3,4], mana = [1,2]

Output: 21
```
 

**Constraints:**

* `n == skill.length`
* `m == mana.length`
* `1 <= n, m <= 5000`
* `1 <= mana[i], skill[i] <= 5000`

# Submissions
---
**Solution 1: (DP Bottom-Up)**

   skill =    [1,    5,    2,    4]
    mana =    [5,    1,    4,    2]
                
    dp   0 ->  5    30    40    60
                             /      
        52    53    58    60 <- 64  pre = max(pre - mana[j]*skill[i],  dp[n+1])
    dp  52 -> 53    58    60    64
                             /
        54    58    60    64 <- 80  pre
    dp  54 -> 58    78    86    102
        86    88    98    102   110 pre
    dp  86    88    98    102   110

```
Runtime: 219 ms, Beats 84.55%
Memory: 45.46 MB, Beats 84.55%
```
```c++
class Solution {
public:
    long long minTime(vector<int>& skill, vector<int>& mana) {
        int n = skill.size(), m = mana.size(), i, j;
        long long pre;
        vector<long long> dp(n+1);
        for (i = 0; i < n; i ++) {
            dp[i+1] = dp[i] + skill[i]*mana[0];
        }
        for (i = 1; i < m; i ++) {
            pre = dp[n] + skill[n-1]*mana[i];
            for (j = n-1; j >= 0; j --) {
                pre = max(dp[j+1], pre - mana[i]*skill[j]);
            }
            dp[0] = pre;
            for (j = 0; j < n; j ++) {
                dp[j+1] = dp[j] + mana[i]*skill[j];
            }
        }
        return dp[n];
    }
};
```
