65. Valid Number

A **valid number** can be split up into these components (in order):

1. A **decimal number** or an integer.
1. (Optional) An `'e'` or `'E'`, followed by an **integer**.

A **decimal number** can be split up into these components (in order):

1. (Optional) A sign character (either `'+'` or '`-'`).
1. One of the following formats:
    1. At least one digit, followed by a dot `'.'`.
    1. At least one digit, followed by a dot `'.'`, followed by at least one digit.
    1. A dot `'.'`, followed by at least one digit.

An **integer** can be split up into these components (in order):

1. (Optional) A sign character (either `'+'` or `'-'`).
1. At least one digit.

For example, all the following are valid numbers: `["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]`, while the following are not valid numbers: `["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]`.

Given a string `s`, return `true` if `s` is a **valid number**.

 

**Example 1:**
```
Input: s = "0"
Output: true
```

**Example 2:**
```
Input: s = "e"
Output: false
```

**Example 3:**
```
Input: s = "."
Output: false
```

**Example 4:**
```
Input: s = ".1"
Output: true
```

**Constraints:**

* `1 <= s.length <= 20`
* `s` consists of only English letters (both uppercase and lowercase), digits (`0-9`), plus `'+'`, minus `'-'`, or dot `'.'`.

# Submissions
---
**Solution 1: (Math, Regular Expression)**
```
Runtime: 28 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def isNumber(self, s: str) -> bool:
        return re.match(r'[ ]*[\+-]{0,1}([0-9]+|([0-9]*\.[0-9]{1,}|[0-9]+\.[0-9]{0,}))(eE[+-]{0,1}[0-9]+){0,1}[ ]*$',s)
```

**Solution 2: (Math, String)**
```
Runtime: 28 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def isNumber(self, s: str) -> bool:
        def is_integer(s):
            return s.isdigit() or len(s) > 0 and s[0] in "+-" and s[1:].isdigit()
        
        def is_decimal(s):
            parts = s.split(".")
            if len(parts) != 2: return False
            if is_integer(parts[0]) and parts[1].isdigit(): return True
            if parts[0] in ["","+","-"] and parts[1].isdigit(): return True
            if is_integer(parts[0]) and not parts[1]: return True
            return False
        
        s = s.lower()
        parts = s.split("e")
        if len(parts) > 2: return False
        if not is_integer(parts[0]) and not is_decimal(parts[0]): return False
        return True if len(parts) == 1 else is_integer(parts[1])
```

**Solution 3: (String, Greedy)**
```
Runtime: 0 ms
Memory: 6.3 MB
```
```c++
class Solution {
public:
    bool isNumber(string s) {
        if (s.empty()) return false;

        size_t i = 0;
        if (s[i] == '+' || s[i] == '-') i++;

        bool has_integer_part = false;
        while (i < s.size() && isdigit(s[i])) {
            has_integer_part = true;
            i++;
        }

        bool has_decimal_part = false;
        if (i < s.size() && s[i] == '.') {
            i++;
            while (i < s.size() && isdigit(s[i])) {
                has_decimal_part = true;
                i++;
            }
        }

        if (i < s.size() && (s[i] == 'e' || s[i] == 'E')) {
            i++;

            if (i < s.size() && (s[i] == '+' || s[i] == '-')) i++;

            if (i == s.size() || !isdigit(s[i])) {
                return false;
            }
            while (i < s.size() && isdigit(s[i])) {
                i++;
            }
        }
        return i == s.size() && (has_integer_part || has_decimal_part);
    }
};
```
