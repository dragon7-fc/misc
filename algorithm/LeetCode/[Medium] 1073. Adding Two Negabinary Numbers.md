1073. Adding Two Negabinary Numbers

Given two numbers `arr1` and `arr2` in base `-2`, return the result of adding them together.

Each number is given in array format:  as an array of `0`s and `1`s, from most significant bit to least significant bit.  For example, `arr = [1,1,0,1]` represents the number `(-2)^3 + (-2)^2 + (-2)^0 = -3`.  A number `arr` in array format is also guaranteed to have no leading zeros: either `arr == [0]` or `arr[0] == 1`.

Return the result of adding `arr1` and `arr2` in the same format: as an array of `0`s and `1`s with no leading zeros.

 

**Example 1:**
```
Input: arr1 = [1,1,1,1,1], arr2 = [1,0,1]
Output: [1,0,0,0,0]
Explanation: arr1 represents 11, arr2 represents 5, the output represents 16.
```

**Note:**

1. `1 <= arr1.length <= 1000`
1. `1 <= arr2.length <= 1000`
1. `arr1` and `arr2` have no leading zeros
1. `arr1[i]` is `0` or `1`
1. `arr2[i]` is `0` or `1`

# Submissions
---
**Solution 1:**
```
Runtime: 72 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        num1 = sum([num*(-2)**i for i, num in enumerate(reversed(arr1))])
        num2 = sum([num*(-2)**i for i, num in enumerate(reversed(arr2))])
        target = num1+num2
        
        if target==0: return '0'
        
        answer = ''
        i = 0
        while target != 0:
            answer += "1" if target&1 else "0"
            target = -(target>>1)
            
        return answer[::-1]
        
```