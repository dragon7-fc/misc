80. Remove Duplicates from Sorted Array II

Given a sorted array `nums`, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by **modifying the input array** in-place with O(1) extra memory.

**Example 1:**
```
Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
```

**Example 1:**
```
Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
```

**Clarification:**

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:
```
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

# Submissions
---
**Solution 1: (Two Pointers)**
```
Runtime: 64 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        i = 1
        for j in range(2, len(nums)):
            if (nums[i-1] != nums[j]) or (nums[i] != nums[j]):
                i += 1        
            nums[i] = nums[j]   
        return i+1
```

**Solution 2: (Two Pointers)**
```
Runtime: 8 ms
Memory Usage: 6.4 MB
```
```c
int removeDuplicates(int* nums, int numsSize){
    int i = 0, left = 0, right = 0;
    int ans = 0;
    while (left < numsSize) {
        while (right < numsSize && nums[right] == nums[left]) {
            right += 1;
        }
        if (right-left == 1) {
            nums[i] = nums[left];
            i += 1;
            ans += 1;
        } else {
            nums[i] = nums[left];
            nums[i+1] = nums[left];
            i += 2;
            ans += 2;
        }
        left = right;
    }
    return ans;
}
```

**Solution 3: (Greedy)**
```
Runtime: 7 ms
Memory Usage: 10.9 MB
```
```c++
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        if (n < 3)
            return n;
        int i = 1;
        for (int j = 2; j < n; j ++) {
            // before copy, check already have 2 same value
            if (nums[i-1] != nums[j] || nums[i] != nums[j])
                i += 1;
            nums[i] = nums[j];
        }
        return i+1;
    }
};
```

**Solution 4: (Two Pointers)**
```
Runtime: 4 ms, Beats 84.33%
Memory: 19.54 MB, Beats 56.77%
```
```c++
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size(), i = 0, j = 0, k;
        while (j < n) {
            nums[i] = nums[j];
            i += 1;
            j += 1;
            k = 1;
            while (j < n && nums[j] == nums[j-1]) {
                j += 1;
                k += 1;
                if (k == 2) {
                    nums[i] = nums[i-1];
                    i += 1;
                }
            }
        }
        return i;
    }
};
```

**Solution 5: (Two Pointers)**
```
Runtime: 15 ms, Beats 14.57%
Memory: 19.54 MB, Beats 56.40%
```
```c++
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size(), i = 0, j = 0;
        while (j < n) {
            nums[i] = nums[j];
            i += 1;
            j += 1;
            if (j < n && nums[j] == nums[j-1]) {
                nums[i] = nums[j];
                i += 1;
                j += 1;
                while (j < n && nums[j] == nums[j-1]) {
                    j += 1;
                }
            }
        }
        return i;
    }
};
```
