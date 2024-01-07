1404. Number of Steps to Reduce a Number in Binary Representation to One

Given a number `s` in their binary representation. Return the number of steps to reduce it to 1 under the following rules:

* If the current number is even, you have to divide it by 2.

* If the current number is odd, you have to add 1 to it.

It's guaranteed that you can always reach to one for all testcases.


**Example 1:**
```
Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14. 
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.  
Step 5) 4 is even, divide by 2 and obtain 2. 
Step 6) 2 is even, divide by 2 and obtain 1.  
```

**Example 2:**
```
Input: s = "10"
Output: 1
Explanation: "10" corressponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.  
```

**Example 3:**
```
Input: s = "1"
Output: 0
```

**Constraints:**

* `1 <= s.length <= 500`
* `s` consists of characters `'0'` or `'1'`
* `s[0] == '1'`

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 32 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def numSteps(self, s: str) -> int:
        n = int(s, 2)
        step = 0
        while n != 1:
            if n%2:
                n += 1
            else:
                n //= 2
            step += 1
            
        return step
```

**Solution 2: (Math)**
```
Runtime: 7 ms
Memory: 6.6 MB
```
```c++
class Solution {
public:
    int numSteps(string s) {
        int res = 0, carry = 0;
        for (int i = s.size() - 1; i > 0; --i) {
            ++res;
            if (s[i] - '0' + carry == 1) {
                carry = 1;
                ++res;
            }
        }
        return res + carry;
    }
};
```

**Solution 3: (DFS)**
```
Runtime: 6 ms
Memory: 6.7 MB
```
```c++
class Solution {
    int dfs(int i, int carry, string &s) {
        if (i == 0) {
            if (s[i] - '0' + carry == 1) {
                return 0;
            }
            return 1;
        }
        if (s[i] - '0' + carry == 1) {
            return dfs(i-1, 1, s) + 2;
        } else {
            return dfs(i-1, (s[i]-'0'+carry)/2, s) + 1;
        }
    }
public:
    int numSteps(string s) {
        return dfs(s.size()-1, 0, s);
    }
};
```
