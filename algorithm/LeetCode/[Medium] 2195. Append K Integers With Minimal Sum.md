2195. Append K Integers With Minimal Sum

You are given an integer array `nums` and an integer `k`. Append `k` unique positive integers that do not appear in `nums` to `nums` such that the resulting total sum is **minimum**.

Return the sum of the `k` integers appended to `nums`.

 

**Example 1:**
```
Input: nums = [1,4,25,10,25], k = 2
Output: 5
Explanation: The two unique positive integers that do not appear in nums which we append are 2 and 3.
The resulting sum of nums is 1 + 4 + 25 + 10 + 25 + 2 + 3 = 70, which is the minimum.
The sum of the two integers appended is 2 + 3 = 5, so we return 5.
```

**Example 2:**
```
Input: nums = [5,6], k = 6
Output: 25
Explanation: The six unique positive integers that do not appear in nums which we append are 1, 2, 3, 4, 7, and 8.
The resulting sum of nums is 5 + 6 + 1 + 2 + 3 + 4 + 7 + 8 = 36, which is the minimum. 
The sum of the six integers appended is 1 + 2 + 3 + 4 + 7 + 8 = 25, so we return 25.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`
* `1 <= k <= 10^8`

# Submissions
---
**Solution 1: (Sort, Greedy)**
```
Runtime: 747 ms
Memory Usage: 28.8 MB
```
```python
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        ans, lo = 0, 1
        cnt = 0
        for num in sorted(nums):
            if num > lo:
                hi = min(num - 1, k - 1 + lo)
                cnt = hi - lo + 1
                ans += (lo + hi) * cnt // 2 
                k -= cnt
                if k == 0:
                    return ans
            lo = num + 1
        if k > 0:
            ans += (lo + lo + k - 1) * k // 2
        return ans
```

**Solution 2: (Sort, Greedy)**
```
Runtime: 223 ms
Memory Usage: 66.2 MB
```
```c++
class Solution {
public:
    long long minimalKSum(vector<int>& nums, int k) {
        sort(begin(nums), end(nums));
        long ans = 0, N = nums.size();
        for (int i = 0; i < N && k; ++i) {
            long prev = i == 0 ? 0 : nums[i - 1]; // the previous number
            long cnt = min((long)k, max((long)0, nums[i] - prev - 1)); // the count of missing numbers between `prev` and `A[i]`
            k -= cnt; // use these `cnt` missing numbers
            ans += (long)(prev + 1 + prev + cnt) * cnt / 2; // sum of these `cnt` missing numbers `[prev+1, prev+cnt]`.
        }
        if (k > 0) ans += ((long)nums.back() + 1 + nums.back() + k) * k / 2; // If there are still missing numbers, add the sum of numbers`[nums.back()+1, nums.back()+k]` to answer
        return ans;
    }
};
```
