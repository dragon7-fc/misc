1004. Max Consecutive Ones III

Given an array `A` of `0`s and `1`s, we may change up to `K` values from `0` to `1`.

Return the length of the longest (contiguous) subarray that contains only `1`s. 

 

**Example 1:**
```
Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
```

**Example 2:**
```
Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
```

**Note:**

* `1 <= A.length <= 20000`
* `0 <= K <= A.length`
* `A[i]` is `0` or `1`

# Submissions
---
**Solution 1: (Greedy, Two Pointers, Sliding Window)**
```
Runtime: 760 ms
Memory Usage: 13.3 MB
```
```python
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        zeroes = 0
        left, right = 0, 0
        ans = 0
        while right < len(A):
            if A[right] == 0:
                zeroes += 1
            while zeroes > K:
                if A[left] == 0:
                    zeroes -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        
        return ans
```

**Solution 2: (Sliding Window)**

    nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
                                ^j
                      ^i
    k             1 2 3          3
                      2          2

    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
                                  ^j
                ^i
        k   1 2     3 4
                      3        4
                               3
      ans                     10

```
Runtime: 0 ms, Beats 100.00%
Memory: 59.38 MB, Beats 25.44%
```
```c++
class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int n = nums.size(), i = 0, j, ck = 0, ans = 0;
        for (j = 0; j < n; j ++) {
            ck += nums[j] == 0;
            while (ck > k) {
                ck -= nums[i] == 0;
                i += 1;
            }
            ans = max(ans, j-i+1);
        }
        return ans;
    }
};
```

**Solution 3: (Sliding Window, non-shrinkable)**

            0 1 2 3 4 5 6 7 8 9 10
    nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
            i         j
              i       j
                i       j
                  i       j
                    i       j
                    i         j
                      i         j
                      i           j
ck                1 2 3 3 3 2 2 3

```
Runtime: 0 ms, Beats 100.00%
Memory: 69.66 MB, Beats 24.95%
```
```c++
class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int n = nums.size(), i = 0, j, ck = 0, ans = 0;
        for (j = 0; j < n; j ++) {
            ck += nums[j] == 0;
            if (ck > k) {
                ck -= nums[i] == 0;
                i += 1;
            }
        }
        return j - i;
    }
};
```
