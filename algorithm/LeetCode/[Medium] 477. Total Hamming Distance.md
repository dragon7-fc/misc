477. Total Hamming Distance

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

**Example:**
```
Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
```

**Note:**

* Elements of the given array are in the range of `0` to `10^9`
* Length of the array will not exceed `10^4`.

# Submissions
---
**Solution 1: (Bit Manipulation)**
```
Runtime: 388 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        N = len(nums)
        if (N == 0):
            return 0
        current_bit = 1
        ret = 0
        max_ = max(nums)
        while (current_bit <= max_):
            counter = 0
            for number in nums:
                if (number & current_bit):
                    counter += 1
            ret += counter * (N - counter)
            current_bit <<= 1
            
        return ret
```