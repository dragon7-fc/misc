1291. Sequential Digits

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a **sorted** list of all the integers in the range `[low, high]` inclusive that have sequential digits.

 

**Example 1:**
```
Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
```

**Constraints:**

* `10 <= low <= high <= 10^9`

# Submissions
---
**Solution 1: (Sliding Window)**
```
Runtime: 35 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample = "123456789"
        n = 10
        nums = []

        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(n - length):
                num = int(sample[start: start + length])
                if num >= low and num <= high:
                    nums.append(num)
        
        return nums
```

**Solution 2: (Precomputation)**
```
Runtime: 59 ms
Memory Usage: 14.3 MB
```
```python
class Seqs:
    def __init__(self):
        sample = "123456789"
        n = 10
        self.nums = nums = []

        for length in range(2, n):
            for start in range(n - length):
                nums.append(int(sample[start: start + length]))

class Solution:
    s = Seqs()
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        return [x for x in self.s.nums if x >= low and x <= high]
```
