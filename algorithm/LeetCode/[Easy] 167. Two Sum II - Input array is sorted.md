167. Two Sum II - Input array is sorted

Given an array of integers that is already **sorted in ascending order**, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

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
**Solution 1:**
```
Runtime: 76 ms
Memory Usage: 15 MB
```
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = collections.defaultdict(list)
        for i in range(len(numbers)):
            dic[numbers[i]].append(i+1)

        for i in range(len(numbers)):
            if target-numbers[i] in dic:
                return [i+1, dic[target-numbers[i]][-1]]
```

**Solution 2:**
```
Runtime: 80 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r, l = len(numbers)-1, 0
        while r>l:
            if numbers[r]+numbers[l]==target:
                return [l+1, r+1]
            elif numbers[r]+numbers[l]>target:
                r = r-1
            else:
                l = l+1
        return []
```

**Solution 2:**
```
Runtime: 72 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        memo = {}
        for i, n in enumerate(numbers):
            if target-n in memo:
                return [memo[target-n]+1, i+1]
            memo[n] = i
```
