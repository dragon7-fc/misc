246. Strobogrammatic Number

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

 

**Example 1:**
```
Input: num = "69"
Output: true
```

**Example 2:**
```
Input: num = "88"
Output: true
```

**Example 3:**
```
Input: num = "962"
Output: false
```

**Example 4:**
```
Input: num = "1"
Output: true
```

# Submissions
---
**Solution 1: (Two Pointers, Hash Table)**
```
Runtime: 24 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        s = {}
        s['6'] = '9'
        s['1'] = '1'
        s['0'] = '0'
        s['9'] = '6'
        s['8'] = '8'
        s['2'] = s['3'] = s['4'] = s['5'] = s['7'] = ''
        if len(num) == 0:
            return False
        
        l = 0
        r = len(num) - 1
        
        while l <= r:
            if s[num[l]] != num[r]:
                return False
            l += 1
            r -= 1
        return True
```

**Solution 2: (Hash Table)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 8.09 MB, Beats 37.95%
```
```c++
class Solution {
public:
    bool isStrobogrammatic(string num) {
        int n = num.size(), i;
        string dp;
        unordered_map<char,char> m = {
            {'0','0'},
            {'1','1'},
            {'6','9'},
            {'8','8'},
            {'9','6'}
        };
        for (i = n-1; i >= 0; i --) {
            if (!m.count(num[i])) {
                return false;
            }
            dp += m[num[i]];
        }
        return dp == num;
    }
};
```
