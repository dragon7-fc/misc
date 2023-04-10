2616. Minimize the Maximum Difference of Pairs

You are given a **0-indexed** integer array `nums` and an integer `p`. Find `p` pairs of indices of `nums` such that the **maximum** difference amongst all the pairs is **minimized**. Also, ensure no index appears more than once amongst the `p` pairs.

Note that for a pair of elements at the index `i` and `j`, the difference of this pair is `|nums[i] - nums[j]|`, where `|x|` represents the **absolute value** of `x`.

Return the **minimum maximum difference** among all `p` pairs.

 

**Example 1:**
```
Input: nums = [10,1,2,7,1,3], p = 2
Output: 1
Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5. 
The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.
```

**Example 2:**
```
Input: nums = [4,2,1,2], p = 1
Output: 0
Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, which is the minimum we can attain.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `0 <= nums[i] <= 10^9`
* `0 <= p <= (nums.length)/2`

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 189 ms
Memory: 81.2 MB
```
```c++
class Solution {
public:
    int minimizeMax(vector<int>& nums, int p) {
        sort(begin(nums), end(nums));
        int l = 0, r = nums.back() - nums.front();
        while (l < r) {
            int m = (l + r) / 2, cnt = 0;
            for (int i = 0; i + 1 < nums.size(); ++i)
                if (m >= (nums[i + 1] - nums[i])) {
                    ++cnt;
                    ++i;
                }
            if (cnt >= p)
                r = m;
            else
                l = m + 1;
        }
        return l;
    }
};
```
