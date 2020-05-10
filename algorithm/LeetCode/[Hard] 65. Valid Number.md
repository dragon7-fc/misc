65. Valid Number

Validate if a given string can be interpreted as a decimal number.

Some examples:
```
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false
```

**Note:** It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

* Numbers 0-9
* Exponent - "e"
* Positive/negative sign - "+"/"-"
* Decimal point - "."

Of course, the context of these characters also matters in the input.

**Update (2015-02-10):**

The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.

# Submissions
---
**Solution 1: (Math, String)**
```
Runtime: 32 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s.strip())
            return True
        except:
            return False
```

**Solution 2: (Math, Regular Expression)**
```
Runtime: 36 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def isNumber(self, s: str) -> bool:
        return re.match(r'[ ]*[\+-]{0,1}([0-9]+|([0-9]*\.[0-9]{1,}|[0-9]+\.[0-9]{0,}))(e[+-]{0,1}[0-9]+){0,1}[ ]*$',s)
```

**Solution 3: (Math, Greedy)**
```
Runtime: 32 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def isNumber(self, s: str) -> bool:
        decimalFound = False
        started = False
        negposfound = False
        eFound = False
        spaceFoundAfterStart = False
        for i in range(0, len(s)):
            if s[i] >= '0' and s[i] <= '9':
                if spaceFoundAfterStart:
                    return False
                if not started:
                    started = True
            elif s[i] == '.':
                if decimalFound or eFound or spaceFoundAfterStart:
                    return False
                decimalFound = True
            elif s[i] == '+' or s[i] == '-':
                if eFound and (started or negposFound or spaceFoundAfterStart):
                    return False
                if not eFound and (started or negposfound or decimalFound or spaceFoundAfterStart):
                    return False
                negposfound = True
            elif s[i] == 'e':
                if not started or eFound or spaceFoundAfterStart:
                    return False
                if i+1 == len(s) or (s[i+1] != '-' and s[i+1] != '+' and  (s[i+1] < '0' or s[i+1] > '9')):
                    return False
                eFound = True
                started = False
                negposFound = False
            elif s[i] == ' ':
                if started or decimalFound or negposfound or eFound:
                    spaceFoundAfterStart = True
            else:
                return False
            
        return started
```