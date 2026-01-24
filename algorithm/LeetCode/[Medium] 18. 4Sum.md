18. 4Sum

Given an array nums of `n` integers, return an array of all the unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:

* `0 <= a, b, c, d < n`
* `a`, `b`, `c`, and `d` are distinct.
* `nums[a] + nums[b] + nums[c] + nums[d] == target`

You may return the answer in any order.

 

**Example 1:**
```
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```

**Example 2:**
```
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
```

**Constraints:**

* `1 <= nums.length <= 200`
* `-10^9 <= nums[i] <= 10^9`
* `-10^9 <= target <= 10^9`

# Submissions
---
**Solution 1: (Two Pointers)**

* Time: O(N^3)
* Space: O(N)

```
Runtime: 84 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return res
            if k == 2:
                return twoSum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for _, set in enumerate(kSum(nums[i + 1:], target - nums[i], k - 1)):
                        res.append([nums[i]] + set)
            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            lo, hi = 0, len(nums) - 1
            while (lo < hi):
                sum = nums[lo] + nums[hi]
                if sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
            return res

        nums.sort()
        return kSum(nums, target, 4)
```

**Solution 2: (Hash Set)**

* Time: O(N^3)
* Space: O(N)

```
Runtime: 92 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return []
            if k == 2:
                return twoSum(nums, target)
            res = []
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for _, set in enumerate(kSum(nums[i + 1:], target - nums[i], k - 1)):
                        res.append([nums[i]] + set)
            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            s = set()
            for i in range(len(nums)):
                if len(res) == 0 or res[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        res.append([target - nums[i], nums[i]])
                s.add(nums[i])
            return res

        nums.sort()
        return kSum(nums, target, 4)
```

**Solution 3: (Two Pointers)**
```
Runtime: 120 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if nums == None or len(nums) == 0:
            return nums
        N = len(nums)
        nums.sort()
        ans = []
        for i in range(N-3):
            for j in range(i+1, N-2):
                t = target - nums[i] -  nums[j]
                min_sum = nums[j+1] + nums[j+2]
                max_sum = nums[-1] + nums[-2]
                if t < min_sum or t > max_sum:
                    continue
                left = j+1
                right = N-1
                while left < right:
                    cur = nums[left] + nums[right]
                    if cur == t:
                        ans += [[nums[i], nums[j], nums[left], nums[right]]]
                        left += 1
                        right -= 1
                    elif cur < t:
                        left += 1
                    else:
                        right -= 1
        ans = set([tuple(x) for x in ans])
        return ans
```

**Solution 4: (Two Pointers, O(n^3))**

             0  1  2  3  4  5
    nums = [ 1, 0,-1, 0,-2, 2], target = 0
            -2 -1  0  0  1  2
             i  ->
                j ->
                   k ->      
                         <- l

```
Runtime: 24 ms, Beats 40.20%
Memory: 17.48 MB, Beats 59.00%
```
```c++
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        int n = nums.size(), i, j, k, l;
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        for (i = 0; i < n-3; i ++) {
            if (i && nums[i] == nums[i-1]) {
                continue;
            }
            j = i+1;
            while (j < n-2) {
                k = j+1, l = n-1;
                while (k < l) {
                    if ((long long)nums[i] + nums[j] + nums[k] + nums[l] == target) {
                        ans.push_back({nums[i], nums[j], nums[k], nums[l]});
                        while (k < l && nums[k] == nums[k+1]) {
                            k += 1;
                        }
                        k += 1;
                        l -= 1;
                    } else if ((long long)nums[i] + nums[j] + nums[k] + nums[l] > target) {
                        l -= 1;
                    } else {
                        k += 1;
                    }
                }
                while (j < n-2 && nums[j+1] == nums[j]) {
                    j += 1;
                }
                j += 1;
            }
        }
        return ans;
    }
};
```
