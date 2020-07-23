504. Base 7

Given an integer, return its base 7 string representation.

**Example 1:**
```
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
```
**Note:** The input will be in range of `[-1e7, 1e7]`.

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 52 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num >= 7:
            return self.convertToBase7(num // 7) + str(num % 7)
        elif num < 0:
            return '-' + self.convertToBase7(-num)
        elif num < 7:
            return str(num)
```

**Solution 2: (Math)**
```
Runtime: 40 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def convertToBase7(self, num: int) -> str:
        div, mod = divmod(abs(num), 7)
        ans = str(mod)
        while div > 0:
            div, mod = divmod(div, 7)
            ans = str(mod) + ans
        
        return ans if num > 0 else "-"+ans if num < 0 else "0"
```

**Solution 3: (Math)**
```
Runtime: 0 ms
Memory Usage: 6 MB
```
```c++
class Solution {
public:
    string convertToBase7(int num) {
        if(num == 0)
            return "0";
        bool isNegative = false;
        string result;
        if(num < 0){
            isNegative = true;
        }
        num = abs(num);
        while(num){
            int digit = num%7;
            num /= 7;
            result = to_string(digit) + result;
        }
        return isNegative ? "-"+result : result;
    }
};
```