2165. Smallest Value of the Rearranged Number

You are given an integer `num`. **Rearrange** the digits of `num` such that its value is **minimized** and it does not contain **any** leading zeros.

Return the rearranged number with minimal value.

Note that the sign of the number does not change after rearranging the digits.

 

**Example 1:**
```
Input: num = 310
Output: 103
Explanation: The possible arrangements for the digits of 310 are 013, 031, 103, 130, 301, 310. 
The arrangement with the smallest value that does not contain any leading zeros is 103.
```

**Example 2:**
```
Input: num = -7605
Output: -7650
Explanation: Some possible arrangements for the digits of -7605 are -7650, -6705, -5076, -0567.
The arrangement with the smallest value that does not contain any leading zeros is -7650.
```

**Constraints:**

* `-1015 <= num <= 1015`

# Submissions
---
**Solution 1: (String)**
```
Runtime: 32 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def smallestNumber(self, num: int) -> int:
        s = sorted(str(abs(num)))
        if num <= 0:
            return -int(''.join(s[::-1]))
        i = next(i for i,a in enumerate(s) if a > '0')
        s[i], s[0] = s[0], s[i]
        return int(''.join(s))
```

**Solution 2: (String)**
```
Runtime: 0 ms
Memory Usage: 5.9 MB
```
```c++
class Solution {
public:
    long long smallestNumber(long long num) {
        auto s = std::to_string(abs(num));
        std::sort(s.begin(), s.end(), [&](int a, int b){ return num < 0 ? a > b : a < b; });
        if (num > 0)
            std::swap(s[0], s[s.find_first_not_of('0')]);
        return std::stoll(s) * (num < 0 ? -1 : 1);
    }
};
```
