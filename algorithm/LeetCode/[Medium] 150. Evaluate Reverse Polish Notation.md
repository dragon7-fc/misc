150. Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are `+`, `-`, `*`, `/`. Each operand may be an integer or another expression.

**Note:**

* Division between two integers should truncate toward zero.
* The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.

**Example 1:**
```
Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

**Example 2:**
```
Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

**Example 3:**
```
Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```

# Submissions
---
**Solution 1: (Stack)**
```
Runtime: 68 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': operator.add, 
            '-': operator.sub, 
            '*': operator.mul, 
            '/': operator.truediv
        }
        stack = []
        for token in tokens:
            if token in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(int(ops[token](a, b)))
            else:
                stack.append(int(token))
        
        return stack.pop()
```

**Solution 22 (Stack)**
```
Runtime: 8 ms
Memory Usage: 7.5 MB
```
```c


int evalRPN(char ** tokens, int tokensSize){
    int stack[10000];
    int size = 0;
    for (int i = 0; i < tokensSize; i ++) {
        if (strcmp(tokens[i], "+") && strcmp(tokens[i], "-") && strcmp(tokens[i], "*") && strcmp(tokens[i], "/")) {
            stack[size] = atoi(tokens[i]);
            size += 1;
        } else {
            if (strcmp(tokens[i], "+") == 0)
                stack[size-2] += stack[size-1];
            else if (strcmp(tokens[i], "-") == 0)
                stack[size-2] -= stack[size-1];
            else if (strcmp(tokens[i], "*") == 0)
                stack[size-2] *= stack[size-1];
            else
                stack[size-2] /= stack[size-1];
            size -= 1;
        }
    }
    return stack[0];
}
```
