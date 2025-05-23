1726. Tuple with Same Product

Given an array `nums` of distinct positive integers, return the number of tuples `(a, b, c, d)` such that `a * b = c * d` where `a`, `b`, `c`, and `d` are elements of nums, and `a != b` != `c != d`.

 

**Example 1:**
```
Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
```

**Example 2:**
```
Input: nums = [1,2,4,5,10]
Output: 16
Explanation: There are 16 valids tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,4,5)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
```

**Example 3:**
```
Input: nums = [2,3,4,6,8,12]
Output: 40
```

**Example 4:**
```
Input: nums = [2,3,5,7]
Output: 0
```

**Constraints:**

* `1 <= nums.length <= 1000`
* `1 <= nums[i] <= 104`
* All elements in `nums` are **distinct**.

# Submissions
---
**Solution 1: (Greedy, Hash Table)**
```
Runtime: 664 ms
Memory Usage: 43.1 MB
```
```python
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        ans = 0
        freq = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)): 
                key = nums[i] * nums[j]
                ans += freq.get(key, 0)
                freq[key] = 1 + freq.get(key, 0)
        return 8*ans
```

**Solution 2: (Hash Table)**
```
Runtime: 369 ms, Beats 21.63%
Memory: 85.11 MB, Beats 23.20%
```
```c++
class Solution {
public:
    int tupleSameProduct(vector<int>& nums) {
        int n = nums.size(), i, j, ans = 0;
        unordered_map<int, int> cnt;
        for (i = 1; i < n; i ++) {
            for (j = 0; j < i; j ++) {
                ans += cnt[nums[i]*nums[j]] * 8;
                cnt[nums[i]*nums[j]] += 1;
            }
        }
        return ans;
    }
};
```
