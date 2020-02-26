726. Number of Atoms

Given a chemical `formula` (given as a string), return the count of each atom.

An atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

1 or more digits representing the count of that element may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, output the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

**Example 1:**
```
Input: 
formula = "H2O"
Output: "H2O"
Explanation: 
The count of elements are {'H': 2, 'O': 1}.
```

**Example 2:**
```
Input: 
formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: 
The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
```

**Example 3:**
```
Input: 
formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: 
The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
```

**Note:**

* All atom names consist of lowercase letters, except for the first character which is uppercase.
* The length of formula will be in the range `[1, 1000]`.
* formula will only consist of letters, digits, and round parentheses, and is a valid formula as defined in the problem.

# Solution
---
## Approach #1: Recursion [Accepted]
**Intuition and Algorithm**

Write a function `parse` that parses the formula from index `i`, returning a map `count` from names to multiplicities (the number of times that name is recorded).

We will put `i` in global state: our `parse` function increments `i` throughout any future calls to `parse`.

* When we see a `'('`, we will parse whatever is inside the brackets (up to the closing ending bracket) and add it to our count.

* Otherwise, we should see an uppercase character: we will parse the rest of the letters to get the name, and add that (plus the multiplicity if there is one.)

* At the end, if there is a final multiplicity (representing the multiplicity of a bracketed sequence), we'll multiply our answer by this.

```python
class Solution(object):
    def countOfAtoms(self, formula):
        def parse():
            N = len(formula)
            count = collections.Counter()
            while (self.i < N and formula[self.i] != ')'):
                if (formula[self.i] == '('):
                    self.i += 1
                    for name, v in parse().items():
                        count[name] += v
                else:
                    i_start = self.i
                    self.i += 1
                    while (self.i < N and formula[self.i].islower()):
                        self.i += 1
                    name = formula[i_start: self.i]
                    i_start = self.i
                    while (self.i < N and formula[self.i].isdigit()):
                        self.i += 1
                    count[name] += int(formula[i_start: self.i] or 1)
            self.i += 1
            i_start = self.i
            while (self.i < N and formula[self.i].isdigit()):
                self.i += 1
            if (i_start < self.i):
                multiplicity = int(formula[i_start: self.i])
                for name in count:
                    count[name] *= multiplicity

            return count

        self.i = 0
        ans = []
        count = parse()
        for name in sorted(count):
            ans.append(name)
            multiplicity = count[name]
            if multiplicity > 1:
                ans.append(str(multiplicity))
        return "".join(ans)
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the length of the formula. It is $O(N)$ to parse through the formula, but each of $O(N)$ multiplicities after a bracket may increment the count of each name in the formula (inside those brackets), leading to an $O(N^2)$ complexity.

* Space Complexity: $O(N)$. We aren't recording more intermediate information than what is contained in the formula.

## Approach #2: Stack [Accepted]
**Intuition and Algorithm**

Instead of recursion, we can simulate the call stack by using a stack of `count`s directly.

```python
class Solution(object):
    def countOfAtoms(self, formula):
        N = len(formula)
        stack = [collections.Counter()]
        i = 0
        while i < N:
            if formula[i] == '(':
                stack.append(collections.Counter())
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                i_start = i
                while i < N and formula[i].isdigit(): i += 1
                multiplicity = int(formula[i_start: i] or 1)
                for name, v in top.items():
                    stack[-1][name] += v * multiplicity
            else:
                i_start = i
                i += 1
                while i < N and formula[i].islower(): i += 1
                name = formula[i_start: i]
                i_start = i
                while i < N and formula[i].isdigit(): i += 1
                multiplicity = int(formula[i_start: i] or 1)
                stack[-1][name] += multiplicity

        return "".join(name + (str(stack[-1][name]) if stack[-1][name] > 1 else '')
                       for name in sorted(stack[-1]))
```

**Complexity Analysis**

* Time Complexity $O(N^2)$, and Space Complexity $O(N)$. The analysis is the same as Approach #1.

## Approach #3: Regular Expressions [Accepted]
**Intuition and Algorithm**

Whenever parsing is involved, we can use regular expressions, a language for defining patterns in text.

Our regular expression will be `"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)"`. Breaking this down by capture group, this is:

    * `([A-Z][a-z]*)` Match an uppercase character followed by any number of lowercase characters, then `((\d*))` match any number of digits.
    * OR, `(\()` match a left bracket or `(\))` right bracket, then `(\d*)` match any number of digits.

Now we can proceed as in Approach #2.

* If we parsed a name and multiplicity `([A-Z][a-z]*)(\d*)`, we will add it to our current count.

* If we parsed a left bracket, we will append a new count to our stack, representing the nested depth of parentheses.

* If we parsed a right bracket (and possibly another multiplicity), we will multiply our deepest level count, `top = stack.pop()`, and add those entries to our current count.

```python
class Solution(object):
    def countOfAtoms(self, formula):
        parse = re.findall(r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)", formula)
        stack = [collections.Counter()]
        for name, m1, left_open, right_open, m2 in parse:
            if name:
              stack[-1][name] += int(m1 or 1)
            if left_open:
              stack.append(collections.Counter())
            if right_open:
                top = stack.pop()
                for k in top:
                  stack[-1][k] += top[k] * int(m2 or 1)

        return "".join(name + (str(stack[-1][name]) if stack[-1][name] > 1 else '')
                       for name in sorted(stack[-1]))
```

**Complexity Analysis**

* Time Complexity $O(N^2)$, and Space Complexity $O(N)$. The analysis is the same as Approach #1, as this regular expression did not look backwards when parsing.


# Submissions
---
**Solution 1: (Recursion)**
```
Runtime: 32 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse():
            N = len(formula)
            count = collections.Counter()
            while (self.i < N and formula[self.i] != ')'):
                if (formula[self.i] == '('):
                    self.i += 1
                    for name, v in parse().items():
                        count[name] += v
                else:
                    i_start = self.i
                    self.i += 1
                    while (self.i < N and formula[self.i].islower()):
                        self.i += 1
                    name = formula[i_start: self.i]
                    i_start = self.i
                    while (self.i < N and formula[self.i].isdigit()):
                        self.i += 1
                    count[name] += int(formula[i_start: self.i] or 1)
            self.i += 1
            i_start = self.i
            while (self.i < N and formula[self.i].isdigit()):
                self.i += 1
            if (i_start < self.i):
                multiplicity = int(formula[i_start: self.i])
                for name in count:
                    count[name] *= multiplicity

            return count

        self.i = 0
        ans = []
        count = parse()
        for name in sorted(count):
            ans.append(name)
            multiplicity = count[name]
            if multiplicity > 1:
                ans.append(str(multiplicity))
        return "".join(ans)
```

**Solution 2: (Stack)**
```
Runtime: 32 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        N = len(formula)
        stack = [collections.Counter()]
        i = 0
        while i < N:
            if formula[i] == '(':
                stack.append(collections.Counter())
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                i_start = i
                while i < N and formula[i].isdigit(): i += 1
                multiplicity = int(formula[i_start: i] or 1)
                for name, v in top.items():
                    stack[-1][name] += v * multiplicity
            else:
                i_start = i
                i += 1
                while i < N and formula[i].islower(): i += 1
                name = formula[i_start: i]
                i_start = i
                while i < N and formula[i].isdigit(): i += 1
                multiplicity = int(formula[i_start: i] or 1)
                stack[-1][name] += multiplicity

        return "".join(name + (str(stack[-1][name]) if stack[-1][name] > 1 else '')
                       for name in sorted(stack[-1]))
```

**Solution 3: (Regular Expressions)**
```
Runtime: 32 ms
Memory Usage: 12.6 MB
```
```python
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        parse = re.findall(r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)", formula)
        stack = [collections.Counter()]
        for name, m1, left_open, right_open, m2 in parse:
            if name:
                stack[-1][name] += int(m1 or 1)
            if left_open:
                stack.append(collections.Counter())
            if right_open:
                top = stack.pop()
                for k in top:
                    stack[-1][k] += top[k] * int(m2 or 1)

        return "".join(name + (str(stack[-1][name]) if stack[-1][name] > 1 else '')
                       for name in sorted(stack[-1]))
```