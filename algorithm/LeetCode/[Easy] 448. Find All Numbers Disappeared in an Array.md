Find All Numbers Disappeared in an Array

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

**Example:**
```
Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
```

# Submissions
---
**Solution**
```
Runtime: 160 ms
Memory Usage: N/A
```
```python
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ret = list(range(n))
        for i in range(n):
            ret[nums[i] - 1] = None
        ret = [x+1 for x in ret if x != None]
        return ret
```

**Solution 1: (value as index)**

             0  1  2  3  4  5  6  7
    nums = [ 4, 3, 2, 7, 8, 2, 3, 1]
                                  ^
            -4 -3 -2 -7       -3 -1

```
Runtime: 0 ms, Beats 100.00%
Memory: 52.95 MB, Beats 89.42%
```
```c++
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int n = nums.size(), i, j;
        for (i = 0; i < n; i ++) {
            j = abs(nums[i]) - 1;
            if (nums[j] > 0) {
                nums[j] *= -1;
            }
        }
        vector<int> ans;
        for (i = 0; i < n; i ++) {
            if (nums[i] > 0) {
                ans.push_back(i + 1);
            }
        }
        return ans;
    }
};
```
