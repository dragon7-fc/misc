81. Search in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., `[0,0,1,2,2,5,6]` might become `[2,5,6,0,0,1,2]`).

You are given a target value to search. If found in the array return true, otherwise return false.

**Example 1:**
```
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
```

**Example 2:**
```
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
```

**Follow up:**

* This is a follow up problem to Search in Rotated Sorted Array, where `nums` may contain duplicates.
* Would this affect the run-time complexity? How and why?

# Submissions
---
**Solution: (Binary Search)**
```
Runtime: 4 ms
Memory Usage: 14.1 MB
```
```c++
class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int n = nums.size();
        if (n == 0) return false;
        int end = n - 1;
        int start = 0;

        while (start <= end) {
            int mid = start + (end - start) / 2;

            if (nums[mid] == target) {
                return true;
            }

            if (!isBinarySearchHelpful(nums, start, nums[mid])) {
                start++;
                continue;
            }

            // which array does pivot belong to.
            bool pivotArray = existsInFirst(nums, start, nums[mid]);

            // which array does target belong to.
            bool targetArray = existsInFirst(nums, start, target);
            if (pivotArray ^ targetArray) { // If pivot and target exist in different sorted arrays, recall that xor is true only when both the operands are distinct
                if (pivotArray) {
                    start = mid + 1; // pivot in the first, target in the second
                } else {
                    end = mid - 1; // target in the first, pivot in the second
                }
            } else { // If pivot and target exist in same sorted array
                if (nums[mid] < target) {
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            }
        }
        return false;
    }

    // returns true if we can reduce the search space in current binary search space
    bool isBinarySearchHelpful(vector<int>& nums, int start, int element) {
        return nums[start] != element;
    }

    // returns true if element exists in first array, false if it exists in second
    bool existsInFirst(vector<int>& nums, int start, int element) {
        return nums[start] <= element;
    }
};
```

**Solution 1: (Binary Search)**
```
Runtime: 56 ms
Memory Usage: 15 MB
```
```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        N = len(nums)
        if N == 0: return False
        end = N - 1
        start = 0

        # returns true if we can reduce the search space in current binary search space
        def isBinarySearchHelpful(start, element):
            return nums[start] != element

        # returns true if element exists in first array, false if it exists in second
        def existsInFirst(start, element):
            return nums[start] <= element
        
        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return True

            if not isBinarySearchHelpful(start, nums[mid]):
                start += 1
                continue
            # which array does pivot belong to.
            pivotArray = existsInFirst(start, nums[mid])

            # which array does target belong to.
            targetArray = existsInFirst(start, target)
            if pivotArray ^ targetArray: # If pivot and target exist in different sorted arrays, recall that xor is true when both operands are distinct
                if pivotArray:
                    start = mid + 1 # pivot in the first, target in the second
                else:
                    end = mid - 1 # target in the first, pivot in the second
            else: # If pivot and target exist in same sorted array
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1

        return False
```

**Solution 2: (Set)**
```
Runtime: 60 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if target in set(nums): return True
```

**Solution 3: (DFS, Binary Search)**
```
Runtime: 52 ms
Memory Usage: 13.4 MB
```
```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums: return False

        def dfs(left, right):
            if left >= right: return False
            mid = left + (right - left) // 2
            if nums[mid] == target: return True
            if nums[mid] == nums[left] and nums[left] == nums[right - 1]:
                return dfs(left, mid) or dfs(mid + 1, right)
            if nums[mid] >= nums[left]:                
                return dfs(left, mid) if nums[left] <= target < nums[mid] else dfs(mid + 1, right)
            else:
                return dfs(mid + 1, right) if nums[mid] < target <= nums[right - 1] else dfs(left, mid)
        
        return dfs(0, len(nums))
```

**Solution 4: (DFS, Binary Search)**
```
Runtime: 56 ms
Memory Usage: 15 MB
```
```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def dfs(beg, end):
            if end - beg <= 1: return target in nums[beg: end+1]
            
            mid = (beg + end)//2
            if nums[mid] > nums[end]:   # eg. 3,4,5,6,7,1,2
                if nums[end] < target <= nums[mid]:
                    return dfs(beg, mid)
                else:
                    return dfs(mid + 1, end)
            elif nums[mid] < nums[end]: # eg. 6,7,1,2,3,4,5
                if nums[mid] < target <= nums[end]:
                    return dfs(mid + 1, end)
                else:
                    return dfs(beg, mid)
            else:
                return dfs(mid+1, end) or dfs(beg, mid)
    
        return dfs(0, len(nums)-1)
```

**Solution 5: (Binary Search)**
```
Runtime: 0 ms
Memory Usage: 6.1 MB
```
```c
// returns true if we can reduce the search space in current binary search space
bool isBinarySearchHelpful(int *nums, int start, int element) {
    return nums[start] != element;
}

// returns true if element exists in first array, false if it exists in second
bool existsInFirst(int *nums, int start, int element) {
    return nums[start] <= element;
}

bool search(int* nums, int numsSize, int target){
    if (numsSize == 0) return false;
    int end = numsSize - 1;
    int start = 0;

    while (start <= end) {
        int mid = start + (end - start) / 2;

        if (nums[mid] == target) {
            return true;
        }

        if (!isBinarySearchHelpful(nums, start, nums[mid])) {
            start++;
            continue;
        }

        // which array does pivot belong to.
        bool pivotArray = existsInFirst(nums, start, nums[mid]);

        // which array does target belong to.
        bool targetArray = existsInFirst(nums, start, target);
        if (pivotArray ^ targetArray) { // If pivot and target exist in different sorted arrays, recall that xor is true only when both the operands are distinct
            if (pivotArray) {
                start = mid + 1; // pivot in the first, target in the second
            } else {
                end = mid - 1; // target in the first, pivot in the second
            }
        } else { // If pivot and target exist in same sorted array
            if (nums[mid] < target) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
    }
    return false;
}
```

**Solution 6: (Binary Search)**

    nums = [2,5,6,0,0,1,2], target = 0
            ^l    ^m   ^r

    nums = [2,5,6,0,0,1,2], target = 3
            ^l    ^m    ^r
                    ^l^m^r
                        ^lmr

```
Runtime: 9 ms
Memory: 13.9 MB
```
```c++
class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;
        
        while(l <= r)
        {
            int mid = l + (r-l) / 2;
            if (nums[mid] == target)
                return true;
			// with duplicates we can have this contdition, just update left & right
            if((nums[l] == nums[mid]) && (nums[r] == nums[mid]))
            {
                l++;
                r--;
            }
            else if(nums[l] <= nums[mid])
            {
				// target is in first  half
                if((nums[l] <= target) && (nums[mid] > target))
                    r = mid - 1;
                else
                    l = mid + 1;
            }
            else
            {
                if((nums[mid] < target) && (nums[r]>= target))
                    l = mid + 1;
                else
                    r = mid - 1;
            }
        }
        return false;
    }
};
```
