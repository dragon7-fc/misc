2597. The Number of Beautiful Subsets

You are given an array `nums` of positive integers and a positive integer `k`.

A subset of `nums` is **beautiful** if it does not contain two integers with an absolute difference equal to `k`.

Return the number of **non-empty beautiful** subsets of the array `nums`.

A **subset** of `nums` is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

 

**Example 1:**
```
Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].
```

**Example 2:**
```
Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].
```

**Constraints:**

* `1 <= nums.length <= 20`
* `1 <= nums[i], k <= 1000`

# Submissions
---
**Solution 1: (Hash Table, Backtracking)**
```
Runtime: 9112 ms
Memory: 14 MB
```
```python
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        N = len(nums)
        ans = 0
        
        def bt(i, cnt):
            nonlocal ans
            if i == N:
                if cnt:
                    ans += 1
                return
            
            if nums[i] - k not in cnt and nums[i] + k not in cnt:
                cnt[nums[i]] += 1
                bt(i + 1, cnt)
                cnt[nums[i]] -= 1
                if not cnt[nums[i]]:
                    del cnt[nums[i]]
            bt(i + 1, cnt)
        
        bt(0, Counter())
        return ans
```

**Solution 2: (Binary Search, Backtracking)**
```
Runtime: 537 ms
Memory: 33.7 MB
```
```c++
class Solution {
    int solve(int i, int k, int n, vector<int> &nums, vector<int> &dp) {
        if (i == n) {
            return 0;
        }
        int o1 = 0, o2 = 0;
        o1 = solve(i + 1, k, n, nums, dp);
        if (binary_search(dp.begin(), dp.end(), nums[i] - k) == 0)
        {
            dp.push_back(nums[i]);
            o2 = 1 + solve(i + 1, k, n, nums, dp);
            dp.pop_back();
        }
        return o1 + o2;
    }
public:
    int beautifulSubsets(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<int> dp;
        return solve(0, k, n, nums, dp);
    }
};
```
