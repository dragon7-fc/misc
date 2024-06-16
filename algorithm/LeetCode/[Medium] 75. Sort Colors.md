75. Sort Colors

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

**Example:**
```
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

**Follow up:**

* A rather straight forward solution is a two-pass algorithm using counting sort.
* First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
* Could you come up with a one-pass algorithm using only constant space?

# Submissions
---
**Solution 1: (Two Pointers)**
```
Runtime: 32 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left,right = 0 , 0
        
        # move all 0's to the left
        while right < len(nums):
            if nums[right] != 0:
                right += 1
                continue
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right += 1
        
        right = left
        # move all 1' to the left
        while right < len(nums):
            if nums[right] != 1:
                right += 1
                continue
            nums[left],nums[right] = nums[right], nums[left]
            left += 1
            right += 1
```

**Solution 2: (Two Pointers)**
```
Runtime: 0 ms
Memory Usage: 6.2 MB
```
```c


void sortColors(int* nums, int numsSize){
    int i = 0, j = 0;
    int tmp;
    while (j < numsSize) {
        if (nums[j] != 0) {
            j += 1;
            continue;
        }
        tmp = nums[j];
        nums[j] = nums[i];
        nums[i] = tmp;
        i += 1;
        j += 1;
    }
    j = i;
    while (j < numsSize) {
        if (nums[j] != 1) {
            j += 1;
            continue;
        }
        tmp = nums[j];
        nums[j] = nums[i];
        nums[i] = tmp;
        i += 1;
        j += 1;
    }
}
```
**Solution 3: (Two Pointers)**
```
Runtime: 0 ms
Memory: 9.72 MB
```
```c++
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n = nums.size(), i = 0, j = 0;
        while (j < n) {
            if (nums[j] == 0) {
                swap(nums[i], nums[j]);
                i += 1;
            }
            j += 1;
        }
        j = i;
        while (j < n) {
            if (nums[j] == 1) {
                swap(nums[i], nums[j]);
                i += 1;
            }
            j += 1;
        }
    }
};
```
