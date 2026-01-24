1877. Minimize Maximum Pair Sum in Array

The **pair sum** of a pair `(a,b)` is equal to `a + b`. The **maximum pair sum** is the largest **pair sum** in a list of pairs.

For example, if we have pairs `(1,5)`, `(2,3)`, and `(4,4)`, the **maximum pair sum** would be `max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8`.
Given an array `nums` of **even** length n, pair up the elements of nums into `n / 2` pairs such that:

* Each element of `nums` is in **exactly** one pair, and
* The **maximum pair sum** is **minimized**.

Return the minimized maximum pair sum after optimally pairing up the elements.

 

**Example 1:**
```
Input: nums = [3,5,2,3]
Output: 7
Explanation: The elements can be paired up into pairs (3,3) and (5,2).
The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.
```

**Example 2:**
```
Input: nums = [3,5,4,2,4,6]
Output: 8
Explanation: The elements can be paired up into pairs (3,5), (4,4), and (6,2).
The maximum pair sum is max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8.
```

**Constraints:**

* `n == nums.length`
* `2 <= n <= 10^5`
* `n` is even.
* `1 <= nums[i] <= 10^5`

# Submissions
---
**Solution 1: (Sort)**
```
Runtime: 1188 ms
Memory Usage: 27.9 MB
```
```python
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        i, j = 0, N-1
        ans = 0
        while i < j:
            ans = max(ans, nums[i] + nums[j])
            i += 1
            j -= 1
        return ans
```

**Solution 2: (Sort)**
```
Runtime: 413 ms
Memory Usage: 17.5 MB
```
```c
int cmp(void *a, void *b) {
    return *(int *)a - *(int *)b;
}
#define max(a, b) (a > b ? a : b) 

int minPairSum(int* nums, int numsSize){
    int i = 0, j = numsSize-1, ans = 0;
    qsort(nums, numsSize, sizeof(int), cmp);
    while (i < j) {
        ans = max(ans, nums[i] + nums[j]);
        i += 1;
        j -= 1;
    }
    return ans;
}
```

**Solution 3: (Sort)**
```
Runtime: 166 ms, Beats 76.78%
Memory: 100.04 MB, Beats 30.18%
```
```c++
class Solution {
public:
    int minPairSum(vector<int>& nums) {
        int n = nums.size(), i, ans = 0;
        sort(begin(nums), end(nums));
        for (i = 0; i < n / 2; i ++) {
            ans = max(ans, nums[i] + nums[n - 1 - i]);
        }
        return ans;
    }
};
```
