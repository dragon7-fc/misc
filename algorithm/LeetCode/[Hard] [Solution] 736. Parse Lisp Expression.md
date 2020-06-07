736. Parse Lisp Expression

You are given a string `expression` representing a Lisp-like expression to return the integer value of.

The syntax for these expressions is given as follows.

* An expression is either an integer, a let-expression, an add-expression, a mult-expression, or an assigned variable. Expressions always evaluate to a single integer.
* (An integer could be positive or negative.)
* A let-expression takes the form `(let v1 e1 v2 e2 ... vn en expr)`, where `let` is always the string `"let"`, then there are 1 or more pairs of alternating variables and expressions, meaning that the first variable `v1` is assigned the value of the expression `e1`, the second variable `v2` is assigned the value of the expression `e2`, and so on **sequentially**; and then the value of this let-expression is the value of the expression expr.
* An add-expression takes the form `(add e1 e2)` where `add` is always the string `"add"`, there are always two expressions `e1`, `e2`, and this expression evaluates to the addition of the evaluation of `e1` and the evaluation of `e2`.
* A mult-expression takes the form `(mult e1 e2)` where `mult` is always the string `"mult"`, there are always two expressions `e1`, `e2`, and this expression evaluates to the multiplication of the evaluation of `e1` and the evaluation of `e2`.
* For the purposes of this question, we will use a smaller subset of variable names. A variable starts with a lowercase letter, then zero or more lowercase letters or digits. Additionally for your convenience, the names "add", "let", or "mult" are protected and will never be used as variable names.
* Finally, there is the concept of scope. When an expression of a variable name is evaluated, **within the context of that evaluation**, the innermost scope (in terms of parentheses) is checked first for the value of that variable, and then outer scopes are checked sequentially. It is guaranteed that every expression is legal. Please see the examples for more details on scope.

**Evaluation Examples:**
```
Input: (add 1 2)
Output: 3

Input: (mult 3 (add 2 3))
Output: 15

Input: (let x 2 (mult x 5))
Output: 10

Input: (let x 2 (mult x (let x 3 y 4 (add x y))))
Output: 14
Explanation: In the expression (add x y), when checking for the value of the variable x,
we check from the innermost scope to the outermost in the context of the variable we are trying to evaluate.
Since x = 3 is found first, the value of x is 3.

Input: (let x 3 x 2 x)
Output: 2
Explanation: Assignment in let statements is processed sequentially.

Input: (let x 1 y 2 x (add x y) (add x y))
Output: 5
Explanation: The first (add x y) evaluates as 3, and is assigned to x.
The second (add x y) evaluates as 3+2 = 5.

Input: (let x 2 (add (let x 3 (let x 4 x)) x))
Output: 6
Explanation: Even though (let x 4 x) has a deeper scope, it is outside the context
of the final x in the add-expression.  That final x will equal 2.

Input: (let a1 3 b2 (add a1 1) b2) 
Output 4
Explanation: Variable names can contain digits after the first character.
```

**Note:**

* The given string `expression` is well formatted: There are no leading or trailing spaces, there is only a single space separating different components of the string, and no space between adjacent parentheses. The expression is guaranteed to be legal and evaluate to an integer.
* The length of `expression` is at most 2000. (It is also non-empty, as that would not be a legal expression.)
* The answer and all intermediate calculations of that answer are guaranteed to fit in a 32-bit integer.

# Solution
---
## Approach #1: Recursive Parsing [Accepted]
**Intuition and Algorithm**

This question is relatively straightforward in terms of the idea of the solution, but presents substantial difficulties in the implementation.

Expressions may involve the evaluation of other expressions, which motivates a recursive approach.

One difficulty is managing the correct scope of the variables. We can use a stack of hashmaps. As we enter an inner scope defined by parentheses, we need to add that scope to our stack, and when we exit, we need to pop that scope off.

Our main `evaluate` function will go through each case of what form the `expression` could take.

* If the expression starts with a digit or '-', it's an integer: return it.

* If the expression starts with a letter, it's a variable. Recall it by checking the current scope in reverse order.

* Otherwise, group the tokens (variables or expressions) within this expression by counting the "balance" `bal` of the occurrences of `'('` minus the number of occurrences of `')'`. When the balance is zero, we have ended a token. For example, `(add 1 (add 2 3))`s should have tokens `'1'` and `'(add 2 3)'`.

* For add and mult expressions, evaluate each token and return the addition or multiplication of them.

* For let expressions, evaluate each expression sequentially and assign it to the variable in the current scope, then return the evaluation of the final expression.

```python
def implicit_scope(func):
    def wrapper(*args):
        args[0].scope.append({})
        ans = func(*args)
        args[0].scope.pop()
        return ans
    return wrapper

class Solution(object):
    def __init__(self):
        self.scope = [{}]

    @implicit_scope
    def evaluate(self, expression):
        if not expression.startswith('('):
            if expression[0].isdigit() or expression[0] == '-':
                return int(expression)
            for local in reversed(self.scope):
                if expression in local: return local[expression]

        tokens = list(self.parse(expression[5 + (expression[1] == 'm'): -1]))
        if expression.startswith('(add'):
            return self.evaluate(tokens[0]) + self.evaluate(tokens[1])
        elif expression.startswith('(mult'):
            return self.evaluate(tokens[0]) * self.evaluate(tokens[1])
        else:
            for j in xrange(1, len(tokens), 2):
                self.scope[-1][tokens[j-1]] = self.evaluate(tokens[j])
            return self.evaluate(tokens[-1])

    def parse(self, expression):
        bal = 0
        buf = []
        for token in expression.split():
            bal += token.count('(') - token.count(')')
            buf.append(token)
            if bal == 0:
                yield " ".join(buf)
                buf = []
        if buf:
            yield " ".join(buf)
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the length of expression. Each expression is evaluated once, but within that evaluation we may search the entire scope.

* Space Complexity: $O(N^2)$. We may pass $O(N)$ new strings to our evaluate function when making intermediate evaluations, each of length $O(N)$. With effort, we could reduce the total space complexity to $O(N)$ with interning or passing pointers.

# Submissions
---
**Solution 1: (Recursive Parsing)**
```
Runtime: 44 ms
Memory Usage: 13.7 MB
```
```python
def implicit_scope(func):
    def wrapper(*args):
        args[0].scope.append({})
        ans = func(*args)
        args[0].scope.pop()
        return ans
    return wrapper

class Solution:
    def __init__(self):
        self.scope = [{}]

    @implicit_scope
    def evaluate(self, expression: str) -> int:
        if not expression.startswith('('):
            if expression[0].isdigit() or expression[0] == '-':
                return int(expression)
            for local in reversed(self.scope):
                if expression in local: return local[expression]

        tokens = list(self.parse(expression[5 + (expression[1] == 'm'): -1]))
        if expression.startswith('(add'):
            return self.evaluate(tokens[0]) + self.evaluate(tokens[1])
        elif expression.startswith('(mult'):
            return self.evaluate(tokens[0]) * self.evaluate(tokens[1])
        else:
            for j in range(1, len(tokens), 2):
                self.scope[-1][tokens[j-1]] = self.evaluate(tokens[j])
            return self.evaluate(tokens[-1])

    def parse(self, expression):
        bal = 0
        buf = []
        for token in expression.split():
            bal += token.count('(') - token.count(')')
            buf.append(token)
            if bal == 0:
                yield " ".join(buf)
                buf = []
        if buf:
            yield " ".join(buf)
```