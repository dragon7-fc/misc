3301. Maximize the Total Height of Unique Towers

You are given an array `maximumHeight`, where `maximumHeight[i]` denotes the **maximum** height the ith tower can be assigned.

Your task is to assign a height to each tower so that:

1. The height of the `i`th tower is a positive integer and does not exceed `maximumHeight[i]`.
1. No two towers have the same height.

Return the **maximum** possible total sum of the tower heights. If it's not possible to assign heights, return `-1`.

 

**Example 1:**
```
Input: maximumHeight = [2,3,4,3]

Output: 10

Explanation:

We can assign heights in the following way: [1, 2, 4, 3].
```

**Example 2:**
```
Input: maximumHeight = [15,10]

Output: 25

Explanation:

We can assign heights in the following way: [15, 10].
```

**Example 3:**
```
Input: maximumHeight = [2,2,1]

Output: -1

Explanation:

It's impossible to assign positive heights to each index so that no two towers have the same height.
```
 

**Constraints:**

* `1 <= maximumHeight.length <= 10^5`
* `1 <= maximumHeight[i] <= 10^9`

# Submissions
---
**Solution 1: (Sort)**
```
Runtime: 206 ms
Memory: 119.92 MB
```
```c++
class Solution {
public:
    long long maximumTotalSum(vector<int>& maximumHeight) {
        sort(maximumHeight.begin(), maximumHeight.end());
        int cur = INT_MAX;
        long long ans = 0;
        for (int i = maximumHeight.size()-1; i >= 0; i --) {
            cur = min(cur, maximumHeight[i]);
            if (cur <= 0) {
                return -1;
            }
            ans += cur;
            cur -= 1;
        }
        return ans;
    }
};
```
