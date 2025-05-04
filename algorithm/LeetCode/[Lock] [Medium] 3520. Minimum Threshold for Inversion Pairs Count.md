3520. Minimum Threshold for Inversion Pairs Count

You are given an array of integers `nums` and an integer `k`.

An inversion pair with a **threshold** `x` is defined as a pair of indices `(i, j)` such that:

* `i < j`
* `nums[i] > nums[j]`
* The difference between the two numbers is at most `x` (i.e. `nums[i] - nums[j] <= x`).

Your task is to determine the **minimum** integer `min_threshold` such that there are **at least** `k` inversion pairs with threshold `min_threshold`.

If no such integer exists, return `-1`.

 

**Example 1:**
```
Input: nums = [1,2,3,4,3,2,1], k = 7

Output: 2

Explanation:

For threshold x = 2, the pairs are:

(3, 4) where nums[3] == 4 and nums[4] == 3.
(2, 5) where nums[2] == 3 and nums[5] == 2.
(3, 5) where nums[3] == 4 and nums[5] == 2.
(4, 5) where nums[4] == 3 and nums[5] == 2.
(1, 6) where nums[1] == 2 and nums[6] == 1.
(2, 6) where nums[2] == 3 and nums[6] == 1.
(4, 6) where nums[4] == 3 and nums[6] == 1.
(5, 6) where nums[5] == 2 and nums[6] == 1.
There are less than k inversion pairs if we choose any integer less than 2 as threshold.
```

**Example 2:**
```
Input: nums = [10,9,9,9,1], k = 4

Output: 8

Explanation:

For threshold x = 8, the pairs are:

(0, 1) where nums[0] == 10 and nums[1] == 9.
(0, 2) where nums[0] == 10 and nums[2] == 9.
(0, 3) where nums[0] == 10 and nums[3] == 9.
(1, 4) where nums[1] == 9 and nums[4] == 1.
(2, 4) where nums[2] == 9 and nums[4] == 1.
(3, 4) where nums[3] == 9 and nums[4] == 1.
There are less than k inversion pairs if we choose any integer less than 8 as threshold.
```
 

**Constraints:**

* `1 <= nums.length <= 10^4`
* `1 <= nums[i] <= 10^9`
* `1 <= k <= 10^9`

# Submissions
---
**Solution 1: (BIT)**
```
Runtime: 347 ms, Beats 70.49%
Memory: 46.09 MB, Beats 72.13%
```
```c++
class Solution {
    int query(vector<int> &bitree, int i) {
        int res = 0;
        for(int j = i; j > 0; j -= -j & j)
            res += bitree[j];
        
        return res;
    }

    void update(vector<int> &bitree, int i) {
        for(int j = i + 1; j < bitree.size(); j += -j & j) 
            bitree[j] += 1;
    }
public:
    int minThreshold(vector<int>& nums, int k) {
        int N = nums.size();

        vector<int> sortArr = nums;
        sort(sortArr.begin(), sortArr.end());
        
        int l = 0,
            r = 1e9 + 1;
        while(l < r) {
            int m = l + (r - l) / 2,
                cnt = 0;
            vector<int> bitree(N + 1);

            for(int i = 0; i < N; i++) {
                int  low = lower_bound(sortArr.begin(), sortArr.end(), nums[i] + 1) - sortArr.begin(),
                     upp = upper_bound(sortArr.begin(), sortArr.end(), nums[i] + m) - sortArr.begin(),
                     idx = lower_bound(sortArr.begin(), sortArr.end(), nums[i]) - sortArr.begin();

                cnt += query(bitree, upp) - query(bitree, low);

                update(bitree, idx);
            }

            if(cnt >= k) 
                r = m;
            
            else
                l = m + 1;

        }

        return l == 0 || l == 1e9 + 1 ? -1 : l;
    }
};
```
