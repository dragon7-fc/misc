1663. Smallest String With A Given Numeric Value

The **numeric value** of a **lowercase character** is defined as its position (`1-indexed`) in the alphabet, so the numeric value of `a` is `1`, the numeric value of `b` is `2`, the numeric value of `c` is `3`, and so on.

The **numeric value** of a **string** consisting of lowercase characters is defined as the sum of its characters' numeric values. For example, the numeric value of the string `"abe"` is equal to `1 + 2 + 5 = 8`.

You are given two integers `n` and `k`. Return the **lexicographically smallest string** with **length** equal to `n` and **numeric value** equal to `k`.

Note that a string `x` is lexicographically smaller than string `y` if `x` comes before `y` in dictionary order, that is, either `x` is a prefix of `y`, or if i is the first position such that `x[i]` != `y[i]`, then `x[i]` comes before `y[i]` in alphabetic order.

 

**Example 1:**
```
Input: n = 3, k = 27
Output: "aay"
Explanation: The numeric value of the string is 1 + 1 + 25 = 27, and it is the smallest string with such a value and length equal to 3.
```

**Example 2:**
```
Input: n = 5, k = 73
Output: "aaszz"
```

**Constraints:**

* 1 <= `n` <= 105
* n <= `k` <= 26 * n

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 376 ms
Memory Usage: 15.8 MB
```
```python
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = ''
        i = 0
        while i < n:
            if k > (n-i-1)*26:
                r = k - (n-i-1)*26
                ans += chr(96+r)
                ans += 'z'*(n-i-1)
                break
            else:
                k -= 1
                ans += 'a'
            i += 1
        return ans
```

**Solution 2: (Greedy)**
```
Runtime: 948 ms
Memory Usage: 17.3 MB
```
```python
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        arr = [97] * n
        k -= n
        
        i = n - 1
        while k > 0 and i > -1:
            arr[i] += min(k, 25)
            k -= min(k, 25)
            i -= 1
            
        return "".join([chr(i) for i in arr])
```