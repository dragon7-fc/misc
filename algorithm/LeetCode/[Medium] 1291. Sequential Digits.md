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
**Solution 1: (Sliding window)**
```
Runtime: 24 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        len_low = len(str(low))
        len_high = len(str(high))
        digits = '123456789'
        ans = []
        for win_len in range(len_low, len_high + 1):
            for i in range(10-win_len):
                if low <= int(digits[i:i + win_len]) <= high:
                    ans.append(int(digits[i:i + win_len]))
        return ans
        
```