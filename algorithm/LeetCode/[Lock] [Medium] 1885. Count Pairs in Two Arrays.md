1885. Count Pairs in Two Arrays

Given two integer arrays `nums1` and `nums2` of length `n`, count the pairs of indices `(i, j)` such that `i < j` and `nums1[i] + nums1[j] > nums2[i] + nums2[j]`.

Return the number of pairs satisfying the condition.

 

**Example 1:**
```
Input: nums1 = [2,1,2,1], nums2 = [1,2,1,2]
Output: 1
Explanation: The pairs satisfying the condition are:
- (0, 2) where 2 + 2 > 1 + 1.
```

**Example 2:**
```
Input: nums1 = [1,10,6,2], nums2 = [1,4,1,5]
Output: 5
Explanation: The pairs satisfying the condition are:
- (0, 1) where 1 + 10 > 1 + 4.
- (0, 2) where 1 + 6 > 1 + 1.
- (1, 2) where 10 + 6 > 4 + 1.
- (1, 3) where 10 + 2 > 4 + 5.
- (2, 3) where 6 + 2 > 1 + 5.
```

**Constraints:**

* `n == nums1.length == nums2.length`
* `1 <= n <= 10^5`
* `1 <= nums1[i], nums2[i] <= 10^5`

# Submissions
---
**Solution 1: (Sort, Two Pointers)**
```
Runtime: 1798 ms
Memory Usage: 32.5 MB
```
```python
class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        arr = sorted([x-y for x,y in zip(nums1, nums2)])
        res = 0
        left, right = 0, len(arr)-1
        while left < right:
            if arr[left]+arr[right] > 0:
                res += right - left
                right -= 1
            else:
                left += 1
        return res
```

**Solution 2: (Sort and Two Pointer)**
```
Runtime: 137 ms
Memory: 98.72 MB
```
```c++
class Solution {
public:
    long long countPairs(vector<int>& nums1, vector<int>& nums2) {
        int N = nums1.size(); // nums2 is the same length

        // Difference[i] stores nums1[i] - nums2[i]
        vector<int> difference(N);
        for (int i = 0; i < N; i++) {
            difference[i] = nums1[i] - nums2[i];
        }
        sort(begin(difference), end(difference));

        // Count the number of valid pairs
        long long result = 0;
        int left = 0;
        int right = N - 1;
        while (left < right) {
            // Left makes a valid pair with right
            // Right also makes a valid pair with the indices between the pointers
            if (difference[left] + difference[right] > 0) {
                result += right - left;
                right--;
            // Left and right are not a valid pair
            } else {
                left++;
            }
        }
        return result;
    }
};
```

