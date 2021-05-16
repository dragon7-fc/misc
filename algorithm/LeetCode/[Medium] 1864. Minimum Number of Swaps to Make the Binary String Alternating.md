1864. Minimum Number of Swaps to Make the Binary String Alternating

Given a binary string `s`, return the minimum number of character swaps to make it alternating, or `-1` if it is impossible.

The string is called **alternating** if no two adjacent characters are equal. For example, the strings `"010"` and `"1010"` are alternating, while the string `"0100"` is not.

Any two characters may be swapped, even if they are not adjacent.

 

**Example 1:**
```
Input: s = "111000"
Output: 1
Explanation: Swap positions 1 and 4: "111000" -> "101010"
The string is now alternating.
```

**Example 2:**
```
Input: s = "010"
Output: 0
Explanation: The string is already alternating, no swaps are needed.
```

**Example 3:**
```
Input: s = "1110"
Output: -1
```

**Constraints:**

* `1 <= s.length <= 1000`
* `s[i]` is either `'0'` or `'1'`

# Submissions
---
**Solution 1: (Case Study)**
```
Runtime: 36 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def minSwaps(self, s: str) -> int:
        count = Counter(s)
        if abs(count["0"] - count["1"]) > 1:
            return -1
        
        def calc(alternate):
            res = 0
            for c in s:
                if c != alternate:
                    res += 1
                alternate = "1" if alternate == "0" else "0"
            return res // 2
        
        if count["0"] > count["1"]:
            return calc("0")
        elif count["0"] < count["1"]:
            return calc("1")
        else:
            return min(calc("1"), calc("0"))
```