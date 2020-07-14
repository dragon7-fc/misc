330. Patching Array

Given a sorted positive integer array `nums` and an integer `n`, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.

**Example 1:**
```
Input: nums = [1,3], n = 6
Output: 1 
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.
```

**Example 2:**
```
Input: nums = [1,5,10], n = 20
Output: 2
Explanation: The two patches can be [2, 4].
```

**Example 3:**
```
Input: nums = [1,2,2], n = 5
Output: 0
```

# Submissions
---

Initialize an empty list, keep adding new numbers from provided nums into this list, keep updating the coverage range and ensure a continus coverage range. If you do so, you only need to care about whether the newly added number will break the coverage range or not.

Suppose 1~10 is already covered during this process, (by whatever combinations in the above list, doesn't matter), then for the next number added

1. If the next number is "11", you will have these new sums:
11, 11+1, 11+2, ..., 11+10, so your total coverage becomes 1~21, which is "2 x coverage + 1"
1. If the next numberis smaller than "11", for example "3", then the new coverage becomes: 10+3, 9+3, 8+3-> 1~13, which is "num + coverage"
1. If the next number is bigger than "11", for example "12", then number "11" is missing forever. There is no way to sum 11 by existing combinations. You have to manually patch "11" before being able to process the next number. Note that Patching number "1~10" can also cover the missing "11", but patching "11" is optimal because it maximizes the total coverage.

**Solution 1: (Greedy)**
```
Runtime: 16 ms
Memory Usage: 11.6 MB
```
```c++
class Solution {
public:
    int minPatches(vector<int>& nums, int n) {
        int ans = 0;
        long long max_reach = 0, i = 0;
        while(max_reach < n){
            if(i < nums.size() && nums[i] <= max_reach+1){
                max_reach = max_reach + nums[i];
                i++;
            }
            else{
                max_reach = max_reach + max_reach + 1;
                ans++;
            }
        }
        return ans;
    }
};
```

**Solution 2: (Greedy)**
```
Runtime: 84 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        covered, res, i= 0, 0, 0
        while covered < n:
            num = nums[i] if i<len(nums) else math.inf
            if num > covered + 1:
                covered = covered*2+1
                res += 1
            else:
                covered += num
                i += 1
        return res
```