167. Two Sum II - Input array is sorted

Given an array of integers that is already **sorted in ascending order**, find two numbers such that they add up to a specific target number.

The function `twoSum` should return indices of the two `numbers` such that they add up to the `target`, where index1 must be less than index2.

**Note:**
* Your returned answers (both index1 and index2) are not zero-based.
* You may assume that each input would have exactly one solution and you may not use the same element twice.

**Example:**
```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
```

# Submissions
---
**Solution 1: (Hash Table)**
```
Runtime: 64 ms
Memory Usage: 13.2 MB
```
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        memo = {}
        
        for i, n in enumerate(numbers):
            if target - n in memo:
                return [memo[target - n] + 1, i + 1]
            memo[n] = i        
```

**Solution 2: (DFS)**
```
Runtime: 72 ms
Memory Usage: 42 MB
```
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r, l = len(numbers) - 1, 0
        
        def dfs(l, r):
            if numbers[r] + numbers[l] == target:
                return [l+1, r+1]
            elif numbers[r] + numbers[l] > target:
                return dfs(l, r-1)
            else:
                return dfs(l+1, r)
        
        return dfs(l, r)
```

**Solution 3: (Two Pointers)**
```
Runtime: 60 ms
Memory Usage: 13.3 MB
```
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r, l = len(numbers)-1, 0
        
        while l < r:
            if numbers[r] + numbers[l] == target:
                return [l+1, r+1]
            elif numbers[r] + numbers[l] > target:
                r = r-1
            else:
                l = l+1
```

**Solution 4: (Two Pointers)**
```
Runtime: 4 ms
Memory Usage: 6.7 MB
```
```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize){
    int left = 0, right = numbersSize-1;
    while (left < right) {
        if (numbers[left] + numbers[right] < target)
            left += 1;
        else if (numbers[left] + numbers[right] > target)
            right -= 1;
        else
            break;
    }
    *returnSize = 2;
    int *ans = (int *)malloc(sizeof(int) * (*returnSize));
    ans[0] = left+1;
    ans[1] = right+1;
    return ans;
}
```
