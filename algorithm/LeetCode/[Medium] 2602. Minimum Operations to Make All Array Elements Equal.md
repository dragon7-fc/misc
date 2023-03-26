2602. Minimum Operations to Make All Array Elements Equal

You are given an array `nums` consisting of positive integers.

You are also given an integer array `queries` of size `m`. For the `i`th query, you want to make all of the elements of nums equal to `queries[i]`. You can perform the following operation on the array **any** number of times:

* **Increase** or **decrease** an element of the array by `1`.

Return an array `answer` of size `m` where `answer[i]` is the **minimum** number of operations to make all elements of nums equal to `queries[i]`.

**Note** that after each query the array is reset to its original state.

 

**Example 1:**
```
Input: nums = [3,1,6,8], queries = [1,5]
Output: [14,10]
Explanation: For the first query we can do the following operations:
- Decrease nums[0] 2 times, so that nums = [1,1,6,8].
- Decrease nums[2] 5 times, so that nums = [1,1,1,8].
- Decrease nums[3] 7 times, so that nums = [1,1,1,1].
So the total number of operations for the first query is 2 + 5 + 7 = 14.
For the second query we can do the following operations:
- Increase nums[0] 2 times, so that nums = [5,1,6,8].
- Increase nums[1] 4 times, so that nums = [5,5,6,8].
- Decrease nums[2] 1 time, so that nums = [5,5,5,8].
- Decrease nums[3] 3 times, so that nums = [5,5,5,5].
So the total number of operations for the second query is 2 + 4 + 1 + 3 = 10.
```

**Example 2:**
```
Input: nums = [2,9,6,3], queries = [10]
Output: [20]
Explanation: We can increase each value in the array to 10. The total number of operations will be 8 + 1 + 4 + 7 = 20.
```

**Constraints:**

* `n == nums.length`
* `m == queries.length`
* `1 <= n, m <= 10^5`
* `1 <= nums[i], queries[i] <= 10^9`

# Submissions
---
**Solution 1: (Prefix sum, Binary Search, Math)**
```
Runtime: 1009 ms
Memory: 41.7 MB
```
```python
class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sum, n = [0], len(nums)
        for num in nums:
            prefix_sum.append(num + prefix_sum[-1])
        ans = []
        for q in queries:
            idx = bisect.bisect(nums, q) # There are idx numbers in nums less than q.
            ans.append((q * idx - prefix_sum[idx]) + (prefix_sum[-1] - prefix_sum[idx] - q * (n - idx)))   
        return ans
```

**Solution 2: (Prefix sum, Binary Search, Math)**
```
Runtime: 283 ms
Memory: 78.1 MB
```
```c++
class Solution {
public:
    vector<long long> minOperations(vector<int>& nums, vector<int>& queries) {
        sort(nums.begin(), nums.end());    
        int n = nums.size();
        vector<long long> prefix(n), ans(queries.size());
        for (int i = 0; i < n; ++i)
            prefix[i] = nums[i] + (i > 0 ? prefix[i - 1] : 0);
        for (int k = 0; k < queries.size(); ++k) {
            auto &q = queries[k];
            int i = lower_bound(nums.begin(), nums.end(), q) - nums.begin();
            long long leftCnt = i, rightCnt = n - i;
            long long left = leftCnt * q - (i > 0 ? prefix[i - 1] : 0);
            long long right = rightCnt <= 0 
                ? 0 
                : prefix.back() - (i > 0 ? prefix[i - 1] : 0) - rightCnt * q;
            ans[k] = left + right;
        }
        return ans;
    }
};
```
