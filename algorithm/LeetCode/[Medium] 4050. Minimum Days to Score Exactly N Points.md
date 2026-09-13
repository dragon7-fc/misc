4050. Minimum Days to Score Exactly N Points

You are given an integer `n` representing a target score.

Your score starts at 0, and each day you either **earn** points or **skip**.

Points are earned during a streak. On the first day of a streak you earn 1 point, on the second day 2 points, on the third day 3 points, and so on. Skipping a day earns **nothing** and **resets** the streak, so the next time you earn points, you start from 1 again.

Return the **minimum** number of days, including any skipped days, needed to reach a score of exactly `n`.

 

**Example 1:**
```
Input: n = 2

Output: 3

Explanation:

Day 1: earn 1 point. Score is 1.
Day 2: skip, which resets the streak. Earning here would add 2 points and take the score past n = 2.
Day 3: the streak has reset, so earning gives 1 point. Score is exactly n = 2 in 3 days.
```

**Example 2:**
```
Input: n = 9

Output: 6

Explanation:

Days 1 to 3: earn 1, 2, and 3 points. Score is 1 + 2 + 3 = 6.
Day 4: skip, which resets the streak.
Days 5 and 6: earn 1 and 2 points. Score is exactly 6 + 1 + 2 = 9 in 6 days.
```

**Example 3:**
```
Input: n = 12

Output: 7

Explanation:

Days 1 to 3: earn 1, 2, and 3 points. Score is 1 + 2 + 3 = 6.
Day 4: skip, which resets the streak.
Days 5 to 7: earn 1, 2, and 3 points. Score is exactly 6 + 1 + 2 + 3 = 12 in 7 days.
```

**Constraints:**

* `1 <= n <= 10^5`

# Submissions
---
**Solution 1: (DP Bottom-Up, for every score try all streak length)**
```
Runtime: 411 ms, Beats -%
Memory: 16.19 MB, Beats 40.00%
```
```c++
class Solution {
public:
    int minDays(int n) {
        vector<int> dp(n + 1, 1e9);
        dp[0] = 0;

        // Precompute triangular numbers T_k = k * (k + 1) / 2
        vector<int> T;
        for (int k = 1; ; ++k) {
            int pts = k * (k + 1) / 2;
            if (pts > n) break;
            T.push_back(pts);
        }

        for (int i = 1; i <= n; ++i) {
            for (int k = 1; k <= (int)T.size(); ++k) {
                int pts = T[k - 1]; // Points earned by a streak of length k
                if (pts > i) break;

                if (i == pts) {
                    // Single streak with no previous skip day
                    dp[i] = min(dp[i], k);
                } else if (dp[i - pts] != 1e9) {
                    // Previous score + 1 skip day + k active days
                    dp[i] = min(dp[i], dp[i - pts] + 1 + k);
                }
            }
        }

        return dp[n];
    }
};
```

**Solution 2: (DP Bottom-Up, for every score gradually increase streak length and try all solution)**

__Intuition__
DP

__Explanation__
The dp[n] stores the minimum days to reach score n.

For each valid streak length,
we calculate its resulting score.
We can achieve this exact score using exactly k days.

For scores slightly larger than the current streak score,
we update the array by combining previous optimal results.

Adding a new streak costs k days plus one day for the reset.
We continue increasing the streak length until it exceeds n.

return dp[n] as the final answer.

Complexity
Time O(n^1.5)
Space O(n)

    n = 2
point      1     2
score      1     3
        0  1  2
dp      0  1  3
----------------------
    n = 9
point      1     2        3
score      1     3        6
        0  1  2  3  4  5  6  7  8  9
dp      0  1  3  2  4  6  5  5  7  6 < ans
                          3


```
Runtime: 54 ms, Beats 100.00%
Memory: 15.46 MB, Beats 40.00%
```
```c++
class Solution {
public:
    int minDays(int n) {
        vector<int> dp(n + 1, INT_MAX);
        dp[0] = 0;
        int score = 1;
        int point = 1;
        while (score <= n) {
            dp[score] = point;
            for (int i = score + 1; i <= min(n, score + score); i ++) {
                
                // Previous score + 1 skip day + point active days
                dp[i] = min(dp[i], dp[i - score] + point + 1);
            }
            point += 1;
            score += point;
        }
        return dp[n];
    }
};
```
