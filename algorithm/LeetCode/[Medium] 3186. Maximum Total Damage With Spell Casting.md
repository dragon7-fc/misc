3186. Maximum Total Damage With Spell Casting

A magician has various spells.

You are given an array `power`, where each element represents the damage of a spell. Multiple spells can have the same damage value.

It is a known fact that if a magician decides to cast a spell with a damage of `power[i]`, they **cannot** cast any spell with a damage of `power[i] - 2`, `power[i] - 1`, `power[i] + 1`, or `power[i] + 2`.

Each spell can be cast **only once**.

Return the **maximum** possible total damage that a magician can cast.

 

**Example 1:**
```
Input: power = [1,1,3,4]

Output: 6

Explanation:

The maximum possible damage of 6 is produced by casting spells 0, 1, 3 with damage 1, 1, 4.
```

**Example 2:**
```
Input: power = [7,1,6,6]

Output: 13

Explanation:

The maximum possible damage of 13 is produced by casting spells 1, 2, 3 with damage 1, 6, 6.
```
 

**Constraints:**

* `1 <= power.length <= 10^5`
* `1 <= power[i] <= 10^9`

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 532 ms
Memory: 225.07 MB
```
```c++
class Solution {
public:
    long long maximumTotalDamage(vector<int>& power) {
        map<int, long long> cnt;
        for (auto p: power) {
            cnt[p] += 1;
        }
        vector<pair<int, long long>> dp;
        long long pre, ans = 0;
        int i = -1, j;
        for (auto [p, c]: cnt) {
            pre = 0;
            j = i;
            while (j >= 0 && (dp[j].first == p-1 || dp[j].first == p-2)) {
                j -= 1;
            }
            if (j >= 0) {
                pre = dp[j].second;
            }
            dp.push_back({p, max(dp.size() ? dp.back().second : 0, p*c + pre)});
            ans = max(ans, dp.back().second);
            i += 1;
        }
        return ans;
    }
};
```
