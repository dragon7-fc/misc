772. Basic Calculator III

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open `(` and closing parentheses `)`, the plus `+` or minus sign `-`, **non-negative** integers and empty spaces ` `.

The expression string contains only non-negative integers, `+`, `-`, `*`, `/` operators , open `(` and closing parentheses `)` and empty spaces ` `. The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of `[-2147483648, 2147483647]`.

Some examples:
```
"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12
```

**Note:** **Do not** use the `eval` built-in library function.

# Submissions
---
**Solution 1: (Two Stack, operator stack + operation stack)**
```
Runtime: 40 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return None
        
        def higher(o1, o2):
            if o1 == '/' or o1 == '*':
                return (o2 == '+' or o2 == '-' or o2 =='(' )
            else: 
                return o2 == '('
        
        stN = []
        stO = []
        num = 0
        dictO = {'+' : lambda a, b: a+b,
                '-': lambda a, b: b-a,
                 '/': lambda a, b: b //a,
                "*": lambda a, b: a*b,}
        have_num = False
        for i, val in enumerate(s):
            if val.isnumeric():
                num  = num * 10 + int(val)
                have_num = True
            if (not val.isnumeric() and val != ' '):
                if have_num:
                    stN.append(num)
                    num = 0
                    have_num = False
                if val == '(':
                    stO.append(val)
                elif val == ')':
                    while stO[-1] != '(':
                        stN.append(dictO[stO.pop(-1)](stN.pop(-1), stN.pop(-1)))
                    stO.pop()
                else:
                    while stO and not higher(val, stO[-1]):
                        stN.append(dictO[stO.pop(-1)](stN.pop(-1), stN.pop(-1)))
                    stO.append(val)
            
        if have_num:
            stN.append(num)
        while stO:
            stN.append(dictO[stO.pop(-1)](stN.pop(-1), stN.pop(-1)))
        return stN.pop()
```

**Solution 2: (DFS)**
```
Runtime: 40 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def calculate(self, s: str) -> int:
        s = s + "+"
        
        def doUpdate(stack, v, op):
            if op == "+" or op == "-":
                if op == "-":
                    v *= -1
                stack.append(v)
            elif op == "*":
                stack[-1] = stack[-1]*v
            else:
                stack[-1] = int(stack[-1]/v)
        
        def dfs(i, s):
            st = []
            v = 0
            sign = "+"
            while i < len(s):
                if s[i] == ' ':
                    i += 1
                elif s[i].isdigit():
                    v = v * 10 + int(s[i])
                    i += 1
                elif s[i] == '(':
                    v,j = dfs(i+1, s)
                    i = j
                elif s[i] == ')':
                    doUpdate(st, v, sign)
                    i += 1
                    break
                else:
                    doUpdate(st, v, sign)
                    v = 0
                    sign = s[i]
                    i += 1
            
            return sum(st), i
                    
        res,_ = dfs(0, s)        
        return res
```