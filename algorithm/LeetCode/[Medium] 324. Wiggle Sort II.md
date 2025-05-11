324. Wiggle Sort II

Given an unsorted array `nums`, reorder it such that `nums[0] < nums[1] > nums[2] < nums[3]....`

**Example 1:**
```
Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
```

**Example 2:**
```
Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
```

**Note:**
* You may assume all input has valid answer.

**Follow Up:**
* Can you do it in O(n) time and/or in-place with O(1) extra space?

# Submissions
---
**Solution 1: (Sort)**
```
Runtime: 172 ms
Memory Usage: 15.7 MB
```
```python
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse=True)
        mid=len(nums)//2
        nums[::2], nums[1::2] = nums[mid:], nums[:mid]
        
        return nums
```

**Solution 2: (Sort)**
```
Runtime: 3 ms, Beats 49.84%
Memory: 21.85 MB, Beats 67.95%
```
```c++
class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        int n = nums.size(), i = 1, j = n-1;
        vector<int> dp = nums;
        sort(dp.begin(), dp.end());
        while (i < n) {
            nums[i] = dp[j];
            i += 2;
            j -= 1;
        }
        i = 0;
        while (j >= 0) {
            nums[i] = dp[j];
            i += 2;
            j -= 1;
        }
    }
};
```

**Solution 3: (median --- Virtual Indexing)**

index:     0  1  2  3   4   5  6  7  8  9
number:   18 17 19 16  15  11 14 10 13 12

index:     5  0  6  1  7  2  8  3  9  4
number:   11 18 14 17 10 19 13 16 12 15

A(0) = nums[1)
A(1) = nums[3)
A(2) = nums[5)
A(3) = nums[7)
A(4) = nums[9)
A(5) = nums[0)
A(6) = nums[2)
A(7) = nums[4)
A(8) = nums[6)
A(9) = nums[8)


```
Runtime: 0 ms, Beats 100.00%
Memory: 21.39 MB, Beats 94.38%
```
```c++
class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        int n = nums.size();
    
        // Find a median.
        auto midptr = nums.begin() + n / 2;
        nth_element(nums.begin(), midptr, nums.end());
        int mid = *midptr;
        
        // Index-rewiring.
        #define A(i) nums[(1+2*(i)) % (n|1)]

        // 3-way-partition-to-wiggly in O(n) time with O(1) space.
        int i = 0, j = 0, k = n - 1;
        while (j <= k) {
            if (A(j) > mid)
                swap(A(i++), A(j++));
            else if (A(j) < mid)
                swap(A(j), A(k--));
            else
                j++;
        }
    }
};
```
