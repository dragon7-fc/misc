2256. Minimum Average Difference

You are given a **0-indexed** integer array `nums` of length `n`.

The **average difference** of the index `i` is the **absolute difference** between the average of the **first** `i + 1` elements of nums and the average of the **last** `n - i - 1` elements. Both averages should be rounded down to the nearest integer.

Return the index with the **minimum average difference**. If there are multiple such indices, return the **smallest** one.

**Note:**

* The **absolute difference** of two numbers is the absolute value of their difference.
* The **average** of `n` elements is the sum of the `n` elements divided (**integer division**) by `n`.
* The average of `0` elements is considered to be `0`.
 

**Example 1:**
```
Input: nums = [2,5,3,9,5,3]
Output: 3
Explanation:
- The average difference of index 0 is: |2 / 1 - (5 + 3 + 9 + 5 + 3) / 5| = |2 / 1 - 25 / 5| = |2 - 5| = 3.
- The average difference of index 1 is: |(2 + 5) / 2 - (3 + 9 + 5 + 3) / 4| = |7 / 2 - 20 / 4| = |3 - 5| = 2.
- The average difference of index 2 is: |(2 + 5 + 3) / 3 - (9 + 5 + 3) / 3| = |10 / 3 - 17 / 3| = |3 - 5| = 2.
- The average difference of index 3 is: |(2 + 5 + 3 + 9) / 4 - (5 + 3) / 2| = |19 / 4 - 8 / 2| = |4 - 4| = 0.
- The average difference of index 4 is: |(2 + 5 + 3 + 9 + 5) / 5 - 3 / 1| = |24 / 5 - 3 / 1| = |4 - 3| = 1.
- The average difference of index 5 is: |(2 + 5 + 3 + 9 + 5 + 3) / 6 - 0| = |27 / 6 - 0| = |4 - 0| = 4.
The average difference of index 3 is the minimum average difference so return 3.
```

**Example 2:**
```
Input: nums = [0]
Output: 0
Explanation:
The only index is 0 so return 0.
The average difference of index 0 is: |0 / 1 - 0| = |0 - 0| = 0.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `0 <= nums[i] <= 10^5`

# Submissions
---
**Solution 1: (Two Pointers)**
```
Runtime: 1083 ms
Memory Usage: 24.9 MB
```
```python
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        N = len(nums)
        mn = float('inf')
        left = ans = 0
        right = sum(nums)
        for i in range(N):
            left += nums[i]
            right -= nums[i]
            cur = abs(left//(i+1) - (right//(N-1-i) if i != N-1 else right))
            if cur < mn:
                mn = cur
                ans = i
        return ans
```

**Solution 2: (Two Pointers)**
```
Runtime: 123 ms
Memory Usage: 78.4 MB
```
```c++
class Solution {
public:
    int minimumAverageDifference(vector<int>& nums) {
        int n(size(nums)), minAverageDifference(INT_MAX), index;
        
        long long sumFromFront(0), sumFromEnd(0);
        for (auto& num : nums) sumFromEnd += num;
        
        for (int i=0; i<n; i++) {
            sumFromFront += nums[i];
            sumFromEnd -= nums[i];
            int a = sumFromFront / (i+1); // average of the first i + 1 elements.
            int b = (i == n-1) ? 0 : sumFromEnd / (n-i-1); // average of the last n - i - 1 elements.
            
            if (abs(a-b) < minAverageDifference) {
                minAverageDifference = abs(a-b);
                index = i;
            }
        }
        return index;
    }
};
```
