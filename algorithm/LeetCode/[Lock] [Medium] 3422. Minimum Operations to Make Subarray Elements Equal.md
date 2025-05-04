3422. Minimum Operations to Make Subarray Elements Equal

You are given an integer array `nums` and an integer `k`. You can perform the following operation any number of times:

* Increase or decrease any element of nums by 1.

Return the **minimum** number of operations required to ensure that **at least** one **subarray** of size `k` in `nums` has all elements equal.

 

**Example 1:**
```
Input: nums = [4,-3,2,1,-4,6], k = 3

Output: 5

Explanation:

Use 4 operations to add 4 to nums[1]. The resulting array is [4, 1, 2, 1, -4, 6].
Use 1 operation to subtract 1 from nums[2]. The resulting array is [4, 1, 1, 1, -4, 6].
The array now contains a subarray [1, 1, 1] of size k = 3 with all elements equal. Hence, the answer is 5.
```

**Example 2:**
```
Input: nums = [-2,-2,3,1,4], k = 2

Output: 0

Explanation:

The subarray [-2, -2] of size k = 2 already contains all equal elements, so no operations are needed. Hence, the answer is 0.
```
 

**Constraints:**

* `2 <= nums.length <= 10^5`
* `-10^6 <= nums[i] <= 10^6`
* `2 <= k <= nums.length`

# Submissions
---
**Solution 1: (multiset)**
```
Runtime: 765 ms, Beats 60.00%
Memory: 310.51 MB, Beats 73.33%
```
```c++
class Solution {
public:
    long long minOperations(vector<int>& nums, int k) {
        //Return the minimum number of operations required to ensure that at least one subarray of size k in nums has all elements equal.
        int n = nums.size();
        multiset<int> below_median; //multiset for sorted duplicates
        multiset<int> above_median;
        long long below_sum = 0;
        long long above_sum = 0;
        for(int i=0; i<k-1; i++) {
            below_median.insert(nums[i]);
            below_sum += nums[i];
        }
        int median_idx = k/2;
        bool odd = (k%2==1);
        long long min_cost = LLONG_MAX;
        for(int l = 0; l<=n-k; l++) {
            int r = l+k-1;
            int r_num = nums[r];
            below_median.insert(r_num);
            below_sum += r_num;
            // Rebalance: Move elements from below_median to above_median
            while(below_median.size()>median_idx) {
                auto it = prev(below_median.end());
                int r_of_below = *it;
                below_sum -= r_of_below;
                below_median.erase(it);
                above_median.insert(r_of_below);
                above_sum += r_of_below;
            }
            while(!above_median.empty() && *prev(below_median.end()) > *above_median.begin()) {
                int r_below_median = *prev(below_median.end());
                int l_above_median = *above_median.begin();
                below_median.erase(prev(below_median.end()));
                above_median.erase(above_median.begin());
                below_sum -= r_below_median;
                above_sum -= l_above_median;
                swap(r_below_median, l_above_median);
                below_median.insert(r_below_median);
                above_median.insert(l_above_median);
                below_sum += r_below_median;
                above_sum += l_above_median;
            };

            long long local_cost = above_sum - below_sum;  // m + x - (m - y) = x + y
            if(odd)
                local_cost -= *above_median.begin();
            min_cost = min(min_cost, local_cost);
            int removal_val = nums[l];
            if(below_median.find(removal_val)!=below_median.end()) {
                below_median.erase(below_median.find(removal_val));
                below_sum -= removal_val;
            } else {
                above_median.erase(above_median.find(removal_val));
                above_sum -= removal_val;                
            }
        }
        return min_cost;
    }
};
```
