137. Single Number II

Given a **non-empty** array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

**Note:**

* Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

**Example 1:**
```
Input: [2,2,3,2]
Output: 3
```

**Example 2:**
```
Input: [0,1,0,1,0,1,99]
Output: 99
```

# Submissions
---
**Solution 1: (Bit Manipulation)**
```
Runtime: 72 ms
Memory Usage: 14.6 MB
```
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        for num in nums:
            seen_once = ~seen_twice & (seen_once^num)
            seen_twice = ~seen_once & (seen_twice^num)
        return seen_once
```

**Solution 2: (Math)**
```
Runtime: 56 ms
Memory Usage: 14.5 MB
```
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return int((3*sum(set(nums)) - sum(nums)) // 2)
```

**Solution 3: (Bit Manipulation, count every bit)**
```
Runtime: 9 ms
Memory: 9.3 MB
```
```c++
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for (int i = 0; i < 32; ++i) {
            int sum = 0;
            for (const int num : nums)
                sum += num >> i & 1;
            sum %= 3;
            ans |= sum << i;
        }
        return ans;
    }
};
```
