4007. Widest Possible Fence

You are given an integer array `planks`, where `planks[i]` represents the height of the `i`th wooden plank. Each plank has a width of 1 unit.

You want to build a fence consisting of planks that all have the same height.

You may either use a plank as is, or combine **exactly** two distinct original planks into a single plank whose height equals the sum of their heights. Each original plank can be used **at most** once, and not all original planks need to be used.

Return the **maximum** possible width of the fence that can be built.

 

**Example 1:**
```
Input: planks = [1,3,2,5,7,5,4,2,1]

Output: 4

Explanation:

We can have four planks of height 5.

planks[3] = 5
planks[5] = 5
planks[0] + planks[6] = 1 + 4 = 5
planks[1] + planks[2] = 3 + 2 = 5
Hence, the maximum width is 4.
```

**Example 2:**
```
Input: planks = [2,3,7]

Output: 1

Explanation:

It is impossible to form two planks of the same height, even after combining two distinct original planks.
Since not all original planks need to be used, we can choose any one plank as the fence.
Therefore, the maximum possible width is 1.
```

**Constraints:**

* `1 <= planks.length <= 1000`
* `1 <= planks[i] <= 109`

# Submissions
---
**Solution 1: (Counter)**
```
Runtime: 1114 ms, Beats 100.00%
Memory: 330.86 MB, Beats 88.89%
```
```c++
class Solution {
public:
    int maximumWidth(vector<int>& planks) {
        int n = planks.size();
        unordered_map<int, int> cnt;
        unordered_map<int, int> cnt2;
        for (const auto &p: planks) {
            cnt[p] += 1;
            cnt2[p] += 1;
        }
        for (auto it = cnt.begin(); it != cnt.end(); it++) {
            auto &[h, k] = *it;
            for (auto nit = it; nit != cnt.end(); nit++) {
                auto &[h2, k2] = *nit;
                if (nit != it) {
                    cnt2[h + h2] += min(k, k2);
                } else {
                    // 2 same height plank can still form another plank
                    cnt2[h + h2] += k / 2;
                }
            }
        }
        int ans = 0;
        for (auto &[_, k]: cnt2) {
            ans = max(ans, k);
        }
        return ans;
    }
};
```
