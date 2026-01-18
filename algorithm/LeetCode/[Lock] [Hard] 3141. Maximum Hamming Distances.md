3141. Maximum Hamming Distances

Given an array `nums` and an integer `m`, with each element `nums[i]` satisfying `0 <= nums[i] < 2^m`, return an array `answer`. The `answer` array should be of the same length as `nums`, where each element `answer[i]` represents the **maximum Hamming distance** between `nums[i]` and any other element `nums[j]` in the array.

The **Hamming distance** between two binary integers is defined as the number of positions at which the corresponding bits differ (add leading zeroes if needed).

 

**Example 1:**
```
Input: nums = [9,12,9,11], m = 4

Output: [2,3,2,3]

Explanation:

The binary representation of nums = [1001,1100,1001,1011].

The maximum hamming distances for each index are:

nums[0]: 1001 and 1100 have a distance of 2.
nums[1]: 1100 and 1011 have a distance of 3.
nums[2]: 1001 and 1100 have a distance of 2.
nums[3]: 1011 and 1100 have a distance of 3.
```

**Example 2:**
```
Input: nums = [3,4,6,10], m = 4

Output: [3,3,2,3]

Explanation:

The binary representation of nums = [0011,0100,0110,1010].

The maximum hamming distances for each index are:

nums[0]: 0011 and 0100 have a distance of 3.
nums[1]: 0100 and 0011 have a distance of 3.
nums[2]: 0110 and 1010 have a distance of 2.
nums[3]: 1010 and 0100 have a distance of 3.
```

**Constraints:**

* `1 <= m <= 17`
* `2 <= nums.length <= 2^m`
* `0 <= nums[i] < 2^m`

# Submissions
---
**Solution 1: (BFS, max mamming distance = reverse min hamming distance)**

    nums = [   9,  12,   9,  11], m = 4
      x     1001 1100 1001 1011           d
     ~x     0110 0011 0110 0100           0
                  v         v
                 1011      1100           1           
                  v
                 1001                     2
    ans        2    3    2    3
            4-2   4-1  4-2  4-1
```
Runtime: 360 ms, Beats 75.00%
Memory: 150.75 MB, Beats 75.00%
```
```c++
class Solution {
public:
    vector<int> maxHammingDistances(vector<int>& nums, int m) {
        int i, rx, y;
        unordered_map<int, int> d;
        queue<int> q;
        for (auto &x: nums) { 
            rx = (~x) & ((1 << m) - 1);
            if (d.count(rx)) {
                continue;
            }
            d[rx] = 0;
            q.push(rx);
        }
        while (q.size()) {
            auto x = q.front();
            q.pop();
            for (i = 0; i < m; i++) {
                y = x ^ (1 << i);
                if (!d.count(y)) {
                    d[y] = d[x] + 1;
                    q.push(y);
                }
            }
        }
        vector<int> ans;
        for (int &x: nums) {
            ans.push_back(m - d[x]);
        }
        return ans;
    }
};
```
