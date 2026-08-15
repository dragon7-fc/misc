334. Increasing Triplet Subsequence

Given an integer array `nums`, return `true` if there exists a triple of indices `(i, j, k)` such that `i < j < k` and `nums[i] < nums[j] < nums[k]`. If no such indices exists, return `false`.

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

**Example 3:**
```
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: One of the valid triplet is (1, 4, 5), because nums[1] == 1 < nums[4] == 4 < nums[5] == 6.
```

**Constraints:**

* `1 <= nums.length <= 5 * 10^5`
* `-2^31 <= nums[i] <= 2^31 - 1`
 

**Follow up**: Could you implement a solution that runs in `O(n)` time complexity and `O(1)` space complexity?

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

**Solution 2: (Greedy, Two-Barriers, LIS, sequencially check current value greater than second smallest b then try to update second smallest b by larger than smallest a and smallest a, try to maintain a < b < current value structure)**

  
  ~  a  b  num

--------------------------
     -------------->
          
b       x       |update
           x <  |            
a       x       v        
      small

     -------------->
          
b           |update
         x  |            
a      x    v        
     small

-----------------------------------
6                     x < true
5               b      
4                   b  
3                      
2           a          
1             a        
0                 a    
    nums = [2,1,5,0,4,6]
a       ~   2 1   0   x < true
b       ~       5   4

```
Runtime: 98 ms
Memory: 61.6 MB
```
```c++
class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        long long a = 1e10, b = 1e10;
        for (auto &num : nums) {
            if (num > b) {
                return true;
            }

            // if current value > smallest a then update second smallest b to preserve a < b structure
            if (num > a) {
                b = min((long long)num, b);
            }

            a = min((long long)num, a);
        }
        return false;

    }
};
```

**Solution 3: (Greedy, try to maintain min1 < min2 < current value structure)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 115.81 MB, Beats 12.05%
```
```c++
class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int n = nums.size();
        if (n < 3) {
            return false;
        }
        int min1 = INT_MAX;
        int min2 = INT_MAX;
        for (const auto &num: nums) {
            if (num <= min1) {
                min1 = num;
            } else if (num <= min2) {
                min2 = num;
            } else {
                return true;
            }
        }
        return false;
    }
};
```
