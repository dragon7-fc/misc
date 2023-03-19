2592. Maximize Greatness of an Array

You are given a **0-indexed** integer array `nums`. You are allowed to permute `nums` into a new array perm of your choosing.

We define the **greatness** of nums be the number of indices `0 <= i < nums.length` for which `perm[i] > nums[i]`.

Return the **maximum** possible greatness you can achieve after permuting `nums`.

 

**Example 1:**
```
Input: nums = [1,3,5,2,1,3,1]
Output: 4
Explanation: One of the optimal rearrangements is perm = [2,5,1,3,3,1,1].
At indices = 0, 1, 3, and 4, perm[i] > nums[i]. Hence, we return 4.
```

**Example 2:**
```
Input: nums = [1,2,3,4]
Output: 3
Explanation: We can prove the optimal perm is [2,3,4,1].
At indices = 0, 1, and 2, perm[i] > nums[i]. Hence, we return 3.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `0 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Sort, Two Pointers)**
```
Runtime: 575 ms
Memory: 28.2 MB
```
```python
class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1: return 0
        a = sorted(nums)
        b = a[:]
        i = j = 0
        while i < N and j < N:
            while j < N and a[i] >= b[j]:
                j += 1
            if j == N:
                break
            i += 1
            j += 1
        return i
```

**Solution 2: (Sort, Two Pointers)**
```
Runtime: 135 ms
Memory: 75.8 MB
```
```c++
class Solution {
public:
    int maximizeGreatness(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int i=0,j=1,ans=0;
        while(i<nums.size() && j<nums.size()){
            if(nums[i]<nums[j]){
                i++;j++;
                ans++;
            }
            else{
                j++;
            }
        }
        return ans;
    }
};
```
