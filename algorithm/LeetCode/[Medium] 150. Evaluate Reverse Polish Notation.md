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

**Solution 3: (Stack)**
```
Runtime: 3 ms
Memory: 15.43 MB
```
```c++
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        int cur, pre;
        stack<int> dp;
        for (auto token: tokens) {
            if (token == "+" || token == "-" || token == "*" || token == "/") {
                cur = dp.top();
                dp.pop();
                pre = dp.top();
                dp.pop();
                if (token == "+") {
                    dp.push(pre + cur);
                } else if (token == "-") {
                    dp.push(pre - cur);
                } else if (token == "*") {
                    dp.push(pre * cur);
                } else if (token == "/") {
                    dp.push(pre / cur);
                }
            } else {
                cur = stoi(token);
                dp.push(cur);
            }
        }
        return dp.top();
    }
};
```

**Solution 4: (Stack)**
```
Runtime: 73 ms
Memory: 14.4 MB
```
```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b
        }
        
        stack = []
        for token in tokens:
            if token in operations:
                number_2 = stack.pop()
                number_1 = stack.pop()
                operation = operations[token]
                stack.append(operation(number_1, number_2))
            else:
                stack.append(int(token))
        return stack.pop()
```

**Solution 5: (Stack)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 17.08 MB, Beats 61.73%
```
```c++
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stk;
        for (auto token: tokens) {
            if (token == "+" || token == "-" || token == "*" || token == "/") {
                auto b = stk.top();
                stk.pop();
                auto a = stk.top();
                stk.pop();
                if (token == "+") {
                    stk.push(a+b);
                } else if (token == "-") {
                    stk.push(a-b);
                } else if (token == "*") {
                    stk.push(a*b);
                } else {
                    stk.push(a/b);
                }
            } else {
                stk.push(stoi(token));
            }
        }
        return stk.top();
    }
};
```
