16. 3Sum Closest

Given an array `nums` of n integers and an integer `target`, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

**Example:**
```
Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```

# Submissions
---
**Solution 1: (Two Pointers)**
```
Runtime: 120 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while (lo < hi):
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
        return target - diff
```

**Solution 2: (Binary Search)**
```
Runtime: 168 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                complement = target - nums[i] - nums[j]
                hi = bisect_right(nums, complement, j + 1)
                lo = hi - 1
                if hi < len(nums) and abs(complement - nums[hi]) < abs(diff):
                    diff = complement - nums[hi]
                if lo > j and abs(complement - nums[lo]) < abs(diff):
                    diff = complement - nums[lo]
            if diff == 0:
                break
        return target - diff
```

**Solution 3: (qsort, Two Pointers)**
```
Runtime: 4 ms
Memory Usage: 5.8 MB
```
```c
int cmp(int *a, int *b) {
    return *a - *b;
}

int threeSumClosest(int* nums, int numsSize, int target){
    int diff = INT_MAX, j, k, t;
    qsort(nums, numsSize, sizeof(int), cmp);
    for (int i = 0; i < numsSize; i ++) {
        j = i+1;
        k = numsSize-1;
        while (j < k) {
            t = nums[i] + nums[j] + nums[k];
            if (abs(target -t) < abs(diff))
                diff = target - t;
            if (t < target)
                j += 1;
            else
                k -= 1;
        }
        if (diff == 0)
            break;
    }
    return target - diff;
}
```

**Solution 3: (Sort, Two Pointers)**
```
Runtime: 652 ms
Memory: 16.4 MB
```
```c++
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        int res = nums[0]+nums[1]+nums[2];
        int n = nums.size();
        int curr = INT_MAX;
        for(int i =0;i<n;i++){
            int j = i+1, k = n-1;
            while(k>j){
                curr = nums[i] + nums[j] + nums[k];
                if (abs(curr-target) < abs(res-target))
                    res = curr;
                if (curr < target)
                    j++;
                else
                    k--;
            }
        }
        
        return res;
    }
};
```
