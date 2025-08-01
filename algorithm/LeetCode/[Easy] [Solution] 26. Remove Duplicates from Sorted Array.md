26. Remove Duplicates from Sorted Array

Given a sorted array `nums`, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

**Example 1:**
```
Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
```

**Example 2:**
```
Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
```

**Clarification:**

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by **reference**, which means modification to the input array will be known to the caller as well.

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

# Solution
---
## Approach 1: Two Pointers
**Algorithm**

Since the array is already sorted, we can keep two pointers $i$ and $j$, where $i$ is the slow-runner while $j$ is the fast-runner. As long as $nums[i] = nums[j]$, we increment $j$ to skip the duplicate.

When we encounter $nums[j] \neq nums[i]$, the duplicate run has ended so we must copy its value to $nums[i + 1]$. $i$ is then incremented and we repeat the same process again until $j$ reaches the end of array.

```java
public int removeDuplicates(int[] nums) {
    if (nums.length == 0) return 0;
    int i = 0;
    for (int j = 1; j < nums.length; j++) {
        if (nums[j] != nums[i]) {
            i++;
            nums[i] = nums[j];
        }
    }
    return i + 1;
}
```

**Complexity analysis**

* Time complextiy : $O(n)$. Assume that $n$ is the length of array. Each of $i$ and $j$ traverses at most $n$ steps.

* Space complexity : $O(1)$.

# Submissions
---
**Soluation: (Two Pointers)**
```
Runtime: 92 ms
Memory Usage: 15.5 MB
```
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1
```

**Solution 2: (Two Pointers)**
```
Runtime: 12 ms
Memory Usage: 7.5 MB
```
```c
int removeDuplicates(int* nums, int numsSize){
    if (numsSize < 2)
        return numsSize;
    int left = 1;
    for (int right = 1; right < numsSize; right++) {
        if (nums[right] != nums[right-1]) {
            nums[left] = nums[right];
            left += 1;
        }
    }
    return left;
}
```

**Solution 3: (Two Pointers)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 22.64, MB Beats 50.48%
```
```c++
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size(), i = 0, j = 1;
        while (j < n) {
            while (j < n && nums[i] == nums[j]) {
                j += 1;
            }
            if (j < n) {
                nums[++i] = nums[j];
            }
            j += 1;
        }
        return i+1;
    }
};
```

**Solution 4: (Two Pointers)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 22.64 MB, Beats 51.15%
```
```c++
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size(), i = 0, j = 0;
        while (j < n) {
            while (j+1 < n && nums[j] == nums[j+1]) {
                j += 1;
            }
            nums[i] = nums[j];
            i += 1;
            j += 1;
        }
        return i;
    }
};
```
