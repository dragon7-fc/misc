35. Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

**Example 1:**
```
Input: [1,3,5,6], 5
Output: 2
```

**Example 2:**
```
Input: [1,3,5,6], 2
Output: 1
```

**Example 3:**
```
Input: [1,3,5,6], 7
Output: 4
```

**Example 4:**
```
Input: [1,3,5,6], 0
Output: 0
```

# Submissions
---
**Solution 1: (Linear Scan)**
```
Runtime: 56 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
            
        return len(nums)
```

**Solution 2: (Linear Scan)**
```
Runtime: 36 ms
Memory Usage: N/A
```
```python
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return len([x for x in nums if x<target])
```

**Solution 3: (Binary Search)**
```
Runtime: 48 ms
Memory Usage: 13.5 MB
```
```python
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return bisect.bisect_left(nums, target)
```

**Solution 4: (Binary Search)**
```
Runtime: 4 ms
Memory Usage: 6.2 MB
```
```c


int searchInsert(int* nums, int numsSize, int target){
    int low,high,mid;
	low=0;
	high=numsSize-1;
	while(low<=high)
	{
		mid=(low+high)/2;
		if(target==nums[mid])
			return mid;
		else if (target<nums[mid])
			high = mid-1;
		else
			low=mid+1;
	}

	return low;
}
```
