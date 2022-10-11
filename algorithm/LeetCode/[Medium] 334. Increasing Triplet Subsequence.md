334. Increasing Triplet Subsequence

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

>>Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.

**Note:** Your algorithm should run in O(n) time complexity and O(1) space complexity.

**Example 1:**
```
Input: [1,2,3,4,5]
Output: true
```

**Example 2:**
```
Input: [5,4,3,2,1]
Output: false
```

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 52 ms
Memory Usage: 14.5 MB
```
```python
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums: return False
        mi, mi2 = nums[0], float('inf')
        for num in nums[1:]:
            if num <= mi:
                mi = num
            elif num <= mi2:
                mi2 = num
            else:
                return True
        return False
```

**Solution 2: (Greedy)**
```
Runtime: 98 ms
Memory: 61.6 MB
```
```c++
class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        long long a = 1e10, b = 1e10;
        for (int num : nums) {
            if (num > b) return true;
            if (num > a) b = min((long long) num, b);
            a = min((long long) num, a);
        }
        return false;
    }
};
```
