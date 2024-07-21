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

**Solution 4: (Recursion)**
```
Runtime: 0 ms
Memory: 9.80 MB
```
```c++
class Solution {
    // Global variable
    int index = 0;
    // Recursively parse the formula
    unordered_map<string, int> parseFormula(string& formula) {
        // Local variable
        unordered_map<string, int> currMap;
        string currAtom;
        string currCount;

        // Iterate until the end of the formula
        while (index < formula.length()) {
            // UPPERCASE LETTER
            if (isupper(formula[index])) {
                if (!currAtom.empty()) {
                    if (currCount.empty()) {
                        currMap[currAtom] += 1;
                    } else {
                        currMap[currAtom] += stoi(currCount);
                    }
                }

                currAtom = formula[index];
                currCount = "";
                index++;
            }

            // lowercase letter
            else if (islower(formula[index])) {
                currAtom += formula[index];
                index++;
            }

            // Digit. Concatenate the count
            else if (isdigit(formula[index])) {
                currCount += formula[index];
                index++;
            }

            // Left Parenthesis
            else if (formula[index] == '(') {
                index++;
                unordered_map<string, int> nestedMap = parseFormula(formula);
                for (auto& [atom, count] : nestedMap) {
                    currMap[atom] += count;
                }
            }

            // Right Parenthesis
            else if (formula[index] == ')') {
                // Save the last atom and count of nested formula
                if (!currAtom.empty()) {
                    if (currCount.empty()) {
                        currMap[currAtom] += 1;
                    } else {
                        currMap[currAtom] += stoi(currCount);
                    }
                }

                index++;
                string multiplier;
                while (index < formula.length() && isdigit(formula[index])) {
                    multiplier += formula[index];
                    index++;
                }
                if (!multiplier.empty()) {
                    int mult = stoi(multiplier);
                    for (auto& [atom, count] : currMap) {
                        currMap[atom] = count * mult;
                    }
                }

                return currMap;
            }
        }

        // Save the last atom and count
        if (!currAtom.empty()) {
            if (currCount.empty()) {
                currMap[currAtom] += 1;
            } else {
                currMap[currAtom] += stoi(currCount);
            }
        }

        return currMap;
    }
public:
    string countOfAtoms(string formula) {
        // Recursively parse the formula
        unordered_map<string, int> finalMap = parseFormula(formula);

        // Sort the final map
        map<string, int> sortedMap(finalMap.begin(), finalMap.end());

        // Generate the answer string
        string ans;
        for (auto& [atom, count] : sortedMap) {
            ans += atom;
            if (count > 1) {
                ans += to_string(count);
            }
        }

        return ans;
    }
};
```

**Solution 5: (Stack)**
```
Runtime: 0 ms
Memory: 9.97 MB
```
```c++
class Solution {
public:
    string countOfAtoms(string formula) {
        // Stack to keep track of the atoms and their counts
        stack<unordered_map<string, int>> stack;
        stack.push(unordered_map<string, int>());

        // Index to keep track of the current character
        int index = 0;

        // Parse the formula
        while (index < formula.length()) {
            // If left parenthesis, insert a new hashmap to the stack. It will
            // keep track of the atoms and their counts in the nested formula
            if (formula[index] == '(') {
                stack.push(unordered_map<string, int>());
                index++;
            }

            // If right parenthesis, pop the top element from the stack
            // Multiply the count with the multiplicity of the nested formula
            else if (formula[index] == ')') {
                unordered_map<string, int> currMap = stack.top();
                stack.pop();
                index++;
                string multiplier;
                while (index < formula.length() && isdigit(formula[index])) {
                    multiplier += formula[index];
                    index++;
                }
                if (!multiplier.empty()) {
                    int mult = stoi(multiplier);
                    for (auto& [atom, count] : currMap) {
                        currMap[atom] = count * mult;
                    }
                }

                for (auto& [atom, count] : currMap) {
                    stack.top()[atom] += count;
                }
            }

            // Otherwise, it must be a UPPERCASE LETTER. Extract the complete
            // atom with frequency, and update the most recent hashmap
            else {
                string currAtom;
                currAtom += formula[index];
                index++;
                while (index < formula.length() && islower(formula[index])) {
                    currAtom += formula[index];
                    index++;
                }

                string currCount;
                while (index < formula.length() && isdigit(formula[index])) {
                    currCount += formula[index];
                    index++;
                }

                int count = currCount.empty() ? 1 : stoi(currCount);
                stack.top()[currAtom] += count;
            }
        }

        // Sort the final map
        map<string, int> finalMap(stack.top().begin(), stack.top().end());

        // Generate the answer string
        string ans;
        for (auto& [atom, count] : finalMap) {
            ans += atom;
            if (count > 1) {
                ans += to_string(count);
            }
        }

        return ans;
    }
};
```

**Solution 6: (Regular Expression)**
```
Runtime: 26 ms
Memory: 19.85 MB
```
```c++
class Solution {
public:
    string countOfAtoms(string formula) {
        // Regular expression to extract atom, count, (, ), multiplier
        // Every element of matcher will be a quintuple
        regex reg("([A-Z][a-z]*)(\\d*)|(\\()|(\\))(\\d*)");
        sregex_iterator it(formula.begin(), formula.end(), reg);
        sregex_iterator end;

        // Stack to keep track of the atoms and their counts
        stack<unordered_map<string, int>> stack;
        stack.push(unordered_map<string, int>());

        // Parse the formula
        while (it != end) {
            smatch match = *it;
            string atom = match[1].str();
            string count = match[2].str();
            string left = match[3].str();
            string right = match[4].str();
            string multiplier = match[5].str();

            // If atom, add it to the top hashmap
            if (!atom.empty()) {
                stack.top()[atom] += count.empty() ? 1 : stoi(count);
            }

            // If left parenthesis, insert a new hashmap to the stack
            else if (!left.empty()) {
                stack.push(unordered_map<string, int>());
            }

            // If right parenthesis, pop the top element from the stack
            // Multiply the count with the attached multiplicity.
            // Add the count to the current formula
            else if (!right.empty()) {
                unordered_map<string, int> currMap = stack.top();
                stack.pop();
                if (!multiplier.empty()) {
                    int mult = stoi(multiplier);
                    for (auto& [atom, count] : currMap) {
                        currMap[atom] = count * mult;
                    }
                }

                for (auto& [atom, count] : currMap) {
                    stack.top()[atom] += count;
                }
            }

            it++;
        }

        // Sort the final map
        map<string, int> finalMap(stack.top().begin(), stack.top().end());

        // Generate the answer string
        string ans;
        for (auto& [atom, count] : finalMap) {
            ans += atom;
            if (count > 1) {
                ans += to_string(count);
            }
        }

        return ans;
    }
};
```

**Solution 7: (Reverse Scanning)**
```
Runtime: 0 ms
Memory: 9.06 MB
```
```c++
class Solution {
public:
    string countOfAtoms(string formula) {
        // For multipliers
        int runningMul = 1;
        stack<int> stack;
        stack.push(1);

        // Map to store the count of atoms
        unordered_map<string, int> finalMap;

        // Strings to take care of current atom and count
        string currAtom = "";
        string currCount = "";

        // Index to traverse the formula in reverse
        int index = formula.length() - 1;

        // Parse the formula
        while (index >= 0) {
            // If digit, update the count
            if (isdigit(formula[index])) {
                currCount = formula[index] + currCount;
            }

            // If a lowercase letter, prepend to the currAtom
            else if (islower(formula[index])) {
                currAtom = formula[index] + currAtom;
            }

            // If UPPERCASE LETTER, update the finalMap
            else if (isupper(formula[index])) {
                currAtom = formula[index] + currAtom;
                int count = currCount.empty() ? 1 : stoi(currCount);
                finalMap[currAtom] += count * runningMul;

                currAtom = "";
                currCount = "";
            }

            // If the right parenthesis, the currCount if any
            // will be considered as multiplier
            else if (formula[index] == ')') {
                int currMultiplier = currCount.empty() ? 1 : stoi(currCount);
                stack.push(currMultiplier);
                runningMul *= currMultiplier;
                currCount = "";
            }

            // If left parenthesis, update the runningMul
            else if (formula[index] == '(') {
                runningMul /= stack.top();
                stack.pop();
            }

            index--;
        }

        // Sort the final map
        map<string, int> sortedMap(finalMap.begin(), finalMap.end());

        // Generate the answer string
        string ans;
        for (auto& [atom, count] : sortedMap) {
            ans += atom;
            if (count > 1) {
                ans += to_string(count);
            }
        }

        return ans;
    }
};
```

**Solution 8: (Preprocessing)**
```
Runtime: 0 ms
Memory: 9.28 MB
```
```c++
class Solution {
public:
    string countOfAtoms(string formula) {
        // For every index, store the valid multiplier
        vector<int> muls(formula.length());
        int runningMul = 1;

        // Stack to take care of nested formula
        stack<int> stack;
        stack.push(1);

        // Preprocess the formula and extract all multipliers
        int index = formula.length() - 1;
        string currNumber = "";
        while (index >= 0) {
            if (isdigit(formula[index])) {
                currNumber = formula[index] + currNumber;
            }

            // If we encountered a letter, then the scanned
            // number was count and not a multiplier. Discard it.
            else if (isalpha(formula[index])) {
                currNumber = "";
            }

            // If we encounter a right parenthesis, then the
            // scanned number was multiplier. Store it.
            else if (formula[index] == ')') {
                int currMultiplier = currNumber.empty() ? 1 : stoi(currNumber);
                runningMul *= currMultiplier;
                stack.push(currMultiplier);
                currNumber = "";
            }

            // If we encounter a left parenthesis, then the
            // most recent multiplier will cease to exist.
            else if (formula[index] == '(') {
                runningMul /= stack.top();
                stack.pop();
                currNumber = "";
            }

            // For every index, store the valid multiplier
            muls[index] = runningMul;
            index--;
        }

        // Map to store the count of atoms
        unordered_map<string, int> finalMap;

        // Traverse left to right in the formula
        index = 0;
        while (index < formula.length()) {
            // If UPPER CASE LETTER, extract the entire atom
            if (isupper(formula[index])) {
                string currAtom = "";
                currAtom += formula[index];
                string currCount = "";
                index++;
                while (index < formula.length() && islower(formula[index])) {
                    currAtom += formula[index];
                    index++;
                }

                // Extract the count
                while (index < formula.length() && isdigit(formula[index])) {
                    currCount += formula[index];
                    index++;
                }

                // Update the final map
                int count = currCount.empty() ? 1 : stoi(currCount);
                finalMap[currAtom] += count * muls[index - 1];
            } else {
                index++;
            }
        }

        // Sort the final map
        map<string, int> sortedMap(finalMap.begin(), finalMap.end());

        // Generate the answer string
        string ans;
        for (auto& [atom, count] : sortedMap) {
            ans += atom;
            if (count > 1) {
                ans += to_string(count);
            }
        }

        return ans;
    }
};
```

**Solution 9: (Reverse Scanning with Regex)**
```
Runtime: 22 ms
Memory: 19.67 MB
```
```c++
class Solution {
public:
    string countOfAtoms(string formula) {
        // Every element of matcher will be a quintuple
        regex reg("([A-Z][a-z]*)(\\d*)|(\\()|(\\))(\\d*)");
        sregex_iterator it(formula.begin(), formula.end(), reg);
        sregex_iterator end;
        vector<tuple<string, string, string, string, string>> matcher;
        while (it != end) {
            matcher.push_back(
                {(*it)[1], (*it)[2], (*it)[3], (*it)[4], (*it)[5]});
            it++;
        }
        reverse(matcher.begin(), matcher.end());

        // Map to store the count of atoms
        unordered_map<string, int> finalMap;

        // Stack to keep track of the nested multiplicities
        stack<int> stack;
        stack.push(1);

        // Current Multiplicity
        int runningMul = 1;

        // Parse the formula
        for (auto& quintuple : matcher) {
            string atom = get<0>(quintuple);
            string count = get<1>(quintuple);
            string left = get<2>(quintuple);
            string right = get<3>(quintuple);
            string multiplier = get<4>(quintuple);

            // If atom, add it to the final map
            if (!atom.empty()) {
                int cnt = count.empty() ? 1 : stoi(count);
                finalMap[atom] += cnt * runningMul;
            }

            // If the right parenthesis, multiply the runningMul
            else if (!right.empty()) {
                int currMultiplier = multiplier.empty() ? 1 : stoi(multiplier);
                runningMul *= currMultiplier;
                stack.push(currMultiplier);
            }

            // If left parenthesis, divide the runningMul
            else if (!left.empty()) {
                runningMul /= stack.top();
                stack.pop();
            }
        }

        // Sort the final map
        map<string, int> sortedMap(finalMap.begin(), finalMap.end());

        // Generate the answer string
        string ans;
        for (auto& [atom, count] : sortedMap) {
            ans += atom;
            if (count > 1) {
                ans += to_string(count);
            }
        }

        return ans;
    }
};
```

**Solution 10: (Stack)**
```
Runtime: 0 ms
Memory: 10.41 MB
```
```c++
class Solution {
public:
    string countOfAtoms(string formula) {
        stack<map<string, int>> stk;
        stk.push({});
        string cur = "";
        int n = formula.size(), i = 0, c;
        while (i < n) {
            if (formula[i] >= 'A' && c <= 'Z') {
                cur = formula[i];
                while (i+1 < n && formula[i+1] >= 'a' && formula[i+1] <= 'z') {
                    cur += formula[i+1];
                    i += 1;
                }
                c = 0;
                while (i+1 < n && formula[i+1] >= '0' && formula[i+1] <= '9') {
                    c = c*10 + formula[i+1]-'0';
                    i += 1;
                }
                if (c == 0) {
                    c = 1;
                }
                stk.top()[cur] += c;
            } else if (formula[i] == '(') {
                stk.push({});
            } else {
                c = 0;
                while (i+1 < n && formula[i+1] >= '0' && formula[i+1] <= '9') {
                    c = c*10 + formula[i+1] - '0';
                    i += 1;
                }
                if (c == 0) {
                    c = 1;
                }
                auto m = stk.top();
                stk.pop();
                for (auto [k, v]: m) {
                    stk.top()[k] += v*c;
                }
            }
            i += 1;
        }
        string ans;
        auto m2 = stk.top();
        for (auto [k, v]: m2) {
            ans += k;
            if (v > 1) {
                ans += to_string(v);
            }
        }
        return ans;
    }
};
```
