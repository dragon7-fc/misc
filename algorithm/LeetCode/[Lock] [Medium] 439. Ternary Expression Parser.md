439. Ternary Expression Parser

Given a string **expression** representing arbitrarily nested ternary expressions, evaluate the expression, and return the result of it.

You can always assume that the given expression is valid and only contains digits, `'?'`, `':'`, `'T'`, and `'F'` where `'T'` is `true` and `'F'` is `false`. All the numbers in the expression are **one-digit** numbers (i.e., in the range `[0, 9]`).

The conditional expressions group right-to-left (as usual in most languages), and the result of the expression will always evaluate to either a digit, `'T'` or `'F'`.

 

**Example 1:**
```
Input: expression = "T?2:3"
Output: "2"
Explanation: If true, then result is 2; otherwise result is 3.
```

**Example 2:**
```
Input: expression = "F?1:T?4:5"
Output: "4"
Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:
"(F ? 1 : (T ? 4 : 5))" --> "(F ? 1 : 4)" --> "4"
or "(F ? 1 : (T ? 4 : 5))" --> "(T ? 4 : 5)" --> "4"
```

**Example 3:**
```
Input: expression = "T?T?F:5:3"
Output: "F"
Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:
"(T ? (T ? F : 5) : 3)" --> "(T ? F : 3)" --> "F"
"(T ? (T ? F : 5) : 3)" --> "(T ? F : 5)" --> "F"
```

**Constraints:**

* `5 <= expression.length <= 10^4`
* `expression` consists of digits, `'T'`, `'F'`, `'?'`, and `':'`.
* It is **guaranteed** that `expression` is a valid ternary expression and that each number is a **one-digit number**.

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 67 ms
Memory Usage: 17 MB
```
```python
class Solution:
    def parseTernary(self, expression: str) -> str:
        n = len(expression)
        
        def helper(i):
            nonlocal n
            if (i+1 >= n) or (i+1 < n and expression[i+1] == ':'):
                return expression[i], i+2
            exp = expression[i]
            l, i = helper(i+2)
            r, i = helper(i)
            if exp == 'T':
                return l, i
            return r, i
        
        ans, _ = helper(0)
        return ans
```

**Solution 2: (Stack)**
```
Runtime: 70 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def parseTernary(self, expression: str) -> str:
        stackmark=[]
        stacknumalpha=[]
        for i in expression[::-1]:
            if i.isalpha() and len(stackmark)>1 and stackmark[-1]=="?":
                first=stacknumalpha.pop()
                second=stacknumalpha.pop()
                stackmark.pop()
                stackmark.pop()
                if i == "T":
                    stacknumalpha.append(first)
                elif i == "F":
                    stacknumalpha.append(second)
            elif i.isalpha() or i.isdigit():
                stacknumalpha.append(i)
            elif i in ":?":
                stackmark.append(i)
        return stacknumalpha[0]
```

**Solution 3: (DFS)**
```
Runtime: 3 ms
Memory: 8.3 MB
```
```c++
class Solution {
    pair<string, int> dfs(int i, string &expression) {
        if (i+1 >= expression.size() || expression[i+1] == ':') {
            return {string(1, expression[i]), i+2};
        }
        auto [left, k] = dfs(i+2, expression);
        auto [right, j] = dfs(k, expression);
        if (expression[i] == 'T') {
            return {left, j};
        }
        return {right, j};
    }
public:
    string parseTernary(string expression) {
        return dfs(0, expression).first;
    }
};
```

**Solution 4: (Stack)**
```
Runtime: 3 ms
Memory: 7.2 MB
```
```c++
class Solution {
public:
    string parseTernary(string expression) {
        // Initialize a stack
        stack<char> stack;
        int i = expression.size() - 1;

        // Traverse the expression from right to left
        while (i >= 0) {

            // Current character
            char curr = expression[i];
            
            // Push every T, F, and digit on the stack
            if (curr >= '0' && curr <= '9' || curr == 'T' || curr == 'F') {
                stack.push(curr);
            }
            
            // As soon as we encounter ?, 
            // replace top two elements of the stack with one
            else if (curr == '?') {
                char onTrue = stack.top();
                stack.pop();
                char onFalse = stack.top();
                stack.pop();
                stack.push(expression[i - 1] == 'T' ? onTrue : onFalse);
                
                // Decrement i by 1 as we have already used
                // Previous Boolean character
                i--;
            }
            
            // Go to the previous character
            i--;
        }
        
        // Return the final character
        return string(1, stack.top());
    }
};
```

**Solution 5: (DFS)**
```
Runtime: 6 ms
Memory: 7.4 MB
```
```c++
class Solution {
public:
    string parseTernary(string expression) {
        std::function<char(int&)> rec = [&](int& index) {
            if(index == expression.size() - 1) return expression[index];

            if(expression[index+1] == '?') {
                int tempIndex = index;
                char expr1 = rec(index += 2);
                char expr2 = rec(++index);

                if(expression[tempIndex] == 'T') return expr1;
                return expr2;
            }

            return expression[index++];
        };

        int index = 0;
        return std::string{rec(index)};
    }
};
```

**Solution 6: (DFS, post order)**

                  0 1 2 3 4 5 6 7 8
    expression = "F ? 1 : T ? 4 : 5"
                          ---------
                  -----------------

                F <0
              /   \
         2> 1       T <4
         ("1",4)  /   \
              6> 4      5 <8
               ("4",8) ("5",10)
                 ^

                  0 1 2 3 4 5 6 7 8
    expression = "T ? T ? F : 5 : 3"
                      ---------
                  -----------------

                 T <0
               /   \
              T <2  3 <8
            /  \   ("3",10)
        4> F    5 <6
       ("F",6) ("5",8)
         ^
```
Runtime: 3 ms, Beats 36.07%
Memory: 10.30 MB, Beats 11.48%
```
```c++
class Solution {
    pair<string, int> dfs(int i, string &expression) {
        if (i + 1 >= expression.size() || expression[i + 1] == ':') {
            return {string(1, expression[i]), i + 2};
        }
        auto &&[left, k] = dfs(i + 2, expression);
        auto &&[right, j] = dfs(k, expression);
        if (expression[i] == 'T') {
            return {left, j};
        }
        return {right, j};
    }
public:
    string parseTernary(string expression) {
        return dfs(0, expression).first;
    }
};
```

**Solution 7: (DFS, post order)**

                  0 1 2 3 4 5 6 7 8
    expression = "F ? 1 : T ? 4 : 5"
                          ---------
                  -----------------

                F <0
              /   \
         2> 1       T <4
           "1"     /   \
              6> 4      5 <8
                "4"     "5"    
                 ^

                  0 1 2 3 4 5 6 7 8
    expression = "T ? T ? F : 5 : 3"
                      ---------
                  -----------------

                 T <0
               /   \
              T <2  3 <8
            /  \   "3"
        4> F    5 <6
          "F"  "5"
           ^

```
Runtime: 0 ms, Beats 100.00%
Memory: 9.06 MB, Beats 37.70%
```
```c++
class Solution {
    char dfs(int &i, string &expression) {
        if (i == expression.size() - 1) {
            return expression[i];
        }
        if (expression[i + 1] == '?') {
            int j = i;
            i += 2;
            char expr1 = dfs(i, expression);
            i += 1;
            char expr2 = dfs(i, expression);
            if (expression[j] == 'T') {
                return expr1;
            }
            return expr2;
        }
        return expression[i++];
    };
public:
    string parseTernary(string expression) {
        int i = 0;
        return string{dfs(i, expression)};
    }
};
```
