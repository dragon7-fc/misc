41. First Missing Positive

Given an unsorted integer array, find the smallest missing positive integer.

**Example 1:**
```
Input: [1,2,0]
Output: 3
```

**Example 2:**
```
Input: [3,4,-1,1]
Output: 2
```

**Example 3:**
```
Input: [7,8,9,11,12]
Output: 1
```
**Note:**

* Your algorithm should run in O(n) time and uses constant extra space.

# Submissions
---
**Solution 1: (Sort)**

Just like swap and place the number to the correct index place.  
After placing them to the correct place, go through the array again to check if the number is right, if not then we have the missing index.
```
Runtime: 28 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        i = 0
        while i < N:
            if nums[i] <= 0 or nums[i] > N:
                i += 1
                continue
            j = nums[i]
            if nums[j-1] != nums[i]:
                nums[j-1], nums[i] = nums[i], nums[j-1]
            else:
                i += 1
        
        for i in range(N):
            if i + 1 != nums[i]:
                return i + 1
        return N + 1
```

**Solution 2: (Greedy)**
```
Runtime: 28 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 1
        while i in nums:
            i = i+1
        return i
```

**Solution 3: (Sort)**
```
Runtime: 40 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i]-1 in range(n) and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                
        return ([i == nums[i]-1 for i in range(n)] + [0]).index(False) + 1  
```

**Solution 4: (Index as a hash key)**
```
Runtime: 32 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Base case.
        if 1 not in nums:
            return 1
        
        # nums = [1]
        if n == 1:
            return 2
        
        # Replace negative numbers, zeros,
        # and numbers larger than n by 1s.
        # After this convertion nums will contain 
        # only positive numbers.
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        
        # Use index as a hash key and number sign as a presence detector.
        # For example, if nums[1] is negative that means that number `1`
        # is present in the array. 
        # If nums[2] is positive - number 2 is missing.
        for i in range(n): 
            a = abs(nums[i])
            # If you meet number a in the array - change the sign of a-th element.
            # Be careful with duplicates : do it only once.
            if a == n:
                nums[0] = - abs(nums[0])
            else:
                nums[a] = - abs(nums[a])
            
        # Now the index of the first positive number 
        # is equal to first missing positive.
        for i in range(1, n):
            if nums[i] > 0:
                return i
        
        if nums[0] > 0:
            return n
            
        return n + 1
```

**Solution 5: (value as index)**
```
Runtime: 116 ms
Memory Usage: 30.2 MB
```
```c


int firstMissingPositive(int* nums, int numsSize){
    int i = 0, j, tmp;
    while (i < numsSize) {
        if (nums[i] <= 0 || nums[i] > numsSize) {
            i += 1;
            continue;
        }
        j = nums[i];
        if (nums[j-1] != nums[i]) {
            tmp = nums[j-1];
            nums[j-1] = nums[i];
            nums[i] = tmp;
        } else
            i += 1;
    }
    for (i = 0; i < numsSize; i ++)
        if (i+1 != nums[i])
            return i+1;
    return numsSize+1;
}
```

**Solution 6: (value as index)**
```
Runtime: 47 ms
Memory: 43.49 MB
```
```c++
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int i = 0, j, n = nums.size();
        while (i < n) {
            if (nums[i] <= 0 || nums[i] > n) {
                i += 1;
                continue;
            }
            j = nums[i];
            if (nums[j-1] != nums[i]) {
                swap(nums[i], nums[j-1]);
            } else
                i += 1;
        }
        for (i = 0; i < n; i ++)
            if (i+1 != nums[i])
                return i+1;
        return nums.size()+1;
    }
};
```
