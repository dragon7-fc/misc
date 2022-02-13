2170. Minimum Operations to Make the Array Alternating

You are given a **0-indexed** array `nums` consisting of `n` positive integers.

The array nums is called **alternating** if:

* `nums[i - 2] == nums[i]`, where `2 <= i <= n - 1`.
* `nums[i - 1] != nums[i]`, where `1 <= i <= n - 1`.
In one **operation**, you can **choose** an index `i` and change `nums[i]` into any positive integer.

Return the **minimum number of operations** required to make the array alternating.

 

**Example 1:**
```
Input: nums = [3,1,3,2,4,3]
Output: 3
Explanation:
One way to make the array alternating is by converting it to [3,1,3,1,3,1].
The number of operations required in this case is 3.
It can be proven that it is not possible to make the array alternating in less than 3 operations. 
```
**Example 2:**
```
Input: nums = [1,2,2,2,2]
Output: 2
Explanation:
One way to make the array alternating is by converting it to [1,2,1,2,1].
The number of operations required in this case is 2.
Note that the array cannot be converted to [2,2,2,2,2] because in this case nums[0] == nums[1] which violates the conditions of an alternating array.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^5`

# Submissions
---
**Solution 1: (Counter)**
```
Runtime: 1352 ms
Memory Usage: 33.3 MB
```
```python
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1: return 0 # edge case 
        odd, even = Counter(), Counter()
        for i, x in enumerate(nums): 
            if i&1: odd[x] += 1
            else: even[x] += 1
        most_odd = odd.most_common()
        most_even = even.most_common()
        if most_odd[0][0] != most_even[0][0]: return len(nums) - most_odd[0][1] - most_even[0][1]
        cand = N - most_odd[0][1] - (most_even[1][1] if len(most_even)>1 else 0)
        cand1 = N - most_even[0][1] - (most_odd[1][1] if len(most_odd)>1 else 0)
        return min(cand, cand1) 
```

**Solution 2: (Counter)**
```
Runtime: 340 ms
Memory Usage: 103.4 MB
```
```c++
class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int mark[100001][2] = {}, i, j, k, res = 0;
        for (i = 0; i < nums.size(); i++)
            mark[nums[i]][i & 1]++;
        for (i = 1, j = k = 0; i <= 100000; i++)
            res = max(res, max(mark[i][0] + k, mark[i][1] + j)), j = max(j, mark[i][0]), k = max(k, mark[i][1]);
        return nums.size() - res;
    }
};
```
