66. Plus One

Given a **non-empty** array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

**Example 1:**
```
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
```

**Example 2:**
```
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
```

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 36 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        stack = []
        for digit in digits[::-1]:
            sum_ = digit+carry
            if sum_ >= 10:
                sum_ -= 10
                carry = 1
            else:
                carry = 0
            stack.append(sum_)
        if carry:
            stack.append(carry)
        
        return stack[::-1]
```

**Solution 2: (String)**
```
Runtime: 20 ms
Memory Usage: N/A
```
```python
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if (len(digits) == 0):
            return 0
        num_str = ""
        for digit in digits:
            num_str += str(digit)
        num = int(num_str)+1
        return [int(dig) for dig in str(num)]
```

**Solution 3: (String)**
```
Runtime: 20 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int, str(int(''.join(map(str, digits))) + 1)))
```