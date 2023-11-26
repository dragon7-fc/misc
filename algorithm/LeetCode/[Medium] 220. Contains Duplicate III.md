220. Contains Duplicate III

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the **absolute** difference between **nums[i]** and **nums[j]** is at most t and the **absolute** difference between i and j is at most k.

**Example 1:**
```
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
```

**Example 2:**
```
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
```

**Example 3:**
```
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
```

# Submissions
---
**Solution 1: (Two Pointer)**
```
Runtime: 48 ms
Memory Usage: 16.4 MB
```
```'
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        N = len(nums)
        if t == 0 and len(nums) == len(set(nums)):
            # Quick response for special case on t = 0
            # t = 0 requires at last one pair of duplicate elements
            return False
        for i, cur_val in enumerate(nums):
            for j in range(i+1, i+k+1):
                if j >= N:
                    # avoid index out of boundary
                    break
                if abs(cur_val - nums[j]) <= t:
                    # hit: 
                    # i != j, | i-j | <= k
                    # | nums[i] - nums[j] | <= t
                    return True
                
        return False
```

**Solution 2: (Sliding Window, set)**
```
Runtime: 259 ms
Memory: 114.9 MB
```
```c++
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int indexDiff, int valueDiff) {
        int n = nums.size();
        multiset<int> ms;     //to store window elements in sorted order
		int i = 0, j = 0;
        while (j < n)
        {
            auto up = ms.upper_bound(nums[j]);
            if ((up != ms.end() && *up-nums[j] <= valueDiff) || (up != ms.begin() && nums[j] - *(--up) <= valueDiff)) {
                return true;
            }
            ms.insert(nums[j]);
            if (ms.size() == indexDiff+1) {
                ms.erase(nums[i]);
                i ++;
            }
            j ++;
        }
        return false;
    }
};
```
