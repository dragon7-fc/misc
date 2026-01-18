13. Roman to Integer

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.
```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```
For example, two is written as `II` in Roman numeral, just two one's added together. Twelve is written as, `XII`, which is simply `X + II`. The number twenty seven is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

* I can be placed before `V` (5) and `X` (10) to make 4 and 9. 
* X can be placed before `L` (50) and `C` (100) to make 40 and 90. 
* C can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from `1` to `3999`.

**Example 1:**
```
Input: "III"
Output: 3
```

**Example 2:**
```
Input: "IV"
Output: 4
```

**Example 3:**
```
Input: "IX"
Output: 9
```

**Example 4:**
```
Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
```

**Example 5:**
```
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

# Submissions
---
**Solution 1: (Math, Hash Table)**
```
Runtime: 136 ms
Memory Usage: N/A
```
```python
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        result = 0    
        for i in range(0, len(s)):
            result +=  roman_dict[s[i]]
            if i>=1 and roman_dict[s[i]]>roman_dict[s[i-1]]:
                result -= 2*roman_dict[s[i-1]]
        return result
```

**Solution 2: (Math, Hash Table)**

            0     1     2     3     4     5     6
    s = "   M     C     M     X     C     I     V"
ans     +1000  -100 +1000   -10  +100    -1    +5
               ----------- ----------   ---------
mp
I: 1
V: 5
X: 10
L: 50
C: 100
D: 500
M: 1000


```
Runtime: 37 ms
Memory Usage: 8.9 MB
```
```c++
class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char,int> mp{
            {'I',1},
            {'V',5},
            {'X',10},
            {'L',50},
            {'C',100},
            {'D',500},
            {'M',1000},
        };
        int ans = 0;
        for(int i=0; i < s.size(); i++){
            if(mp[s[i]] < mp[s[i + 1]])
                ans -= mp[s[i]];
            else
                ans += mp[s[i]];
        }
        return ans;

    }
};
```
