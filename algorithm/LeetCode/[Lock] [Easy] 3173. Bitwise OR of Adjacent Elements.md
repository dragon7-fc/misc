3173. Bitwise OR of Adjacent Elements

Given an array `nums` of length `n`, return an array answer of length `n - 1` such that `answer[i] = nums[i] | nums[i + 1]` where `|` is the bitwise `OR` operation.

 

**Example 1:**
```
Input: nums = [1,3,7,15]

Output: [3,7,15]
```

**Example 2:**
```
Input: nums = [8,4,2]

Output: [12,6]
```

**Example 3:**
```
Input: nums = [5,4,9,11]

Output: [5,13,11]
```
 

**Constraints:**

`2 <= nums.length <= 100`
`0 <= nums[i] <= 100`

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 19 ms
Memory: 41.56 MB
```
```c++
class Solution {
public:
    vector<int> orArray(vector<int>& nums) {
        vector<int> ans;
        for (int i = 0; i < nums.size()-1; i ++) {
            ans.push_back(nums[i]|nums[i+1]);
        }
        return ans;
    }
};
```
