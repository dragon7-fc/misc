152. Maximum Product Subarray

Given an integer array `nums`, find the contiguous subarray within an array (containing at least one number) which has the largest product.

**Example 1:**
```
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```

**Example 2:**
```
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

# Submissions
---
**Solution 1: (DP, Bottom-Up, 1-D)**
```
Runtime: 60 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max_so_far = min_so_far = nums[0]
        for i in range(1, len(nums)):
            candidates = (nums[i], max_so_far*nums[i], min_so_far*nums[i])
            max_so_far = max(candidates)
            min_so_far = min(candidates)
            ans = max(ans, max_so_far)
        
        return ans           
```

**Solution 2: (DP, Bottom-Up)**
```
Runtime: 52 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res1 = [0 for i in range(len(nums))]
        res2 = [0 for i in range(len(nums))]
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if i == 0:
                res1[i] = nums[i]
                res2[i] = nums[i]
            else:
                res1[i] = max(nums[i], nums[i]*res1[i-1], nums[i]*res2[i-1])
                res2[i] = min(nums[i], nums[i]*res1[i-1], nums[i]*res2[i-1])
        
        return max(max(res1), max(res2))
```

**Solution 3: (DP Dottom-Up, block min max)**

                  v
    nums = [  2,  3, -2,  4]
dp_max        2   6  -2   4
dp_min        2   3 -12 -48
tmp_dp_max        6  -2   4
ans           2   6

                  v
    nums = [ -2,  0, -1]
dp_max       -2   0   0
dp_min       -2   0  -1
tmp_dp_max        0   0
ans          -2   0

```
Runtime: 4 ms
Memory Usage: 6.5 MB
```
```c

#define max(_a, _b) ((_a) > (_b) ? (_a) : (_b))
#define min(_a, _b) ((_a) < (_b) ? (_a) : (_b))

int maxProduct(int* nums, int numsSize){
    int dp_max = nums[0];
    int dp_min = nums[0];
    int tmp_dp_max;
    int ans = nums[0];
    for (int i = 1; i < numsSize; i ++) {
        tmp_dp_max = max(max(nums[i], dp_max*nums[i]), dp_min*nums[i]);
        dp_min = min(min(nums[i], dp_max*nums[i]), dp_min*nums[i]);
        dp_max = tmp_dp_max;
        if (ans < dp_max)
            ans = dp_max;
    }
    return ans;
}
```

**Solution 4: (DP Dottom-Up, block min max)**

    nums = [  2,    3,       -2,       4]
candidates    2 3,6,6 -2,-12,-4 4,-8,-48
max           2     6        -2        4
min           2     2       -12      -48
ans           2     6

    nums = [ -2,    0,    -1]
candidates   -2 0,0,0 -1,0,0
max          -2     0      0
min          -2     0     -1
ans          -2     0
```
Runtime: 0 ms, Beats 100.00%
Memory: 17.88 MB, Beats 23.73%
```
```c++
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size(), i, ans, max_so_far, min_so_far;
        array<int, 3> candidates;
        ans = max_so_far = min_so_far = nums[0];
        for (i = 1; i < n; i ++) {
            candidates = {nums[i], max_so_far * nums[i], min_so_far * nums[i]};
            max_so_far = *max_element(begin(candidates), end(candidates));
            min_so_far = *min_element(begin(candidates), end(candidates));
            ans = max(ans, max_so_far);
        }
        return ans;
    }
};
```
