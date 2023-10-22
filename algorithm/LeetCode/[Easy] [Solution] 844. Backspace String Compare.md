844. Backspace String Compare

Given two strings `S` and `T`, return if they are equal when both are typed into empty text editors. `#` means a backspace character.

**Example 1:**
```
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
```

**Example 2:**
```
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
```

**Example 3:**
```
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
```

**Example 4:**
```
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
```

**Note:**

* `1 <= S.length <= 200`
* `1 <= T.length <= 200`
* `S` and `T` only contain lowercase letters and `'#'` characters.

**Follow up:**

* Can you solve it in `O(N)`` time and `O(1)`` space?

# Solutions
---
## Approach #1: Build String [Accepted]
**Intuition**

Let's individually build the result of each string (`build(S)` and `build(T)`), then compare if they are equal.

**Algorithm**

To build the result of a string `build(S)`, we'll use a stack based approach, simulating the result of each keystroke.

```python
class Solution(object):
    def backspaceCompare(self, S, T):
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(S) == build(T)
```

**Complexity Analysis**

* Time Complexity: $O(M + N)$, where $M, N$ are the lengths of `S` and `T` respectively.

* Space Complexity: $O(M + N)$.

## Approach #2: Two Pointer [Accepted]
**Intuition**

When writing a character, it may or may not be part of the final string depending on how many backspace keystrokes occur in the future.

If instead we iterate through the string in reverse, then we will know how many backspace characters we have seen, and therefore whether the result includes our character.

**Algorithm**

Iterate through the string in reverse. If we see a backspace character, the next non-backspace character is skipped. If a character isn't skipped, it is part of the final answer.

See the comments in the code for more details.

```python
class Solution(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))
```

**Complexity Analysis**

* Time Complexity: $O(M + N)$, where $M, N$ are the lengths of `S` and `T` respectively.

* Space Complexity: $O(1)$.

# Submissions
---
**Solution: (Stack)**
```
Runtime: 20 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(S) == build(T)
```

**Solution: (Two Pointers)**
```
Runtime: 28 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))
```

**Solution 1: (Stack)**
```
Runtime: 5 ms
Memory Usage: 6.6 MB
```
```c++
class Solution {
    string processString(string s) {
        stack<char> stk;
        for(char c : s) {
            if(c == '#') {
                if(!stk.empty())stk.pop();
            } else {
                stk.push(c);
            }
        }
        string processed = "";
        while(!stk.empty()) {
            processed += stk.top();
            stk.pop();
        }
        return processed;
    }
public:
    bool backspaceCompare(string s, string t) {
        string sFinal = processString(s);
        string tFinal = processString(t);
        return sFinal == tFinal;
    }
};
```

**Solution 2: (Two Pointers)**
```
Runtime: 9 ms
Memory Usage: 6.3 MB
```
```c++
class Solution {
public:
    bool backspaceCompare(string s, string t) {
        int i = s.size() - 1, j = t.size() - 1;
        int skipS = 0, skipT = 0;

        while (i >= 0 || j >= 0) { // While there may be chars in build(S) or build (T)
            while (i >= 0) { // Find position of next possible char in build(S)
                if (s[i] == '#') {skipS++; i--;}
                else if (skipS > 0) {skipS--; i--;}
                else break;
            }
            while (j >= 0) { // Find position of next possible char in build(T)
                if (t[j] == '#') {skipT++; j--;}
                else if (skipT > 0) {skipT--; j--;}
                else break;
            }
            // If two actual characters are different
            if (i >= 0 && j >= 0 && s[i] != t[j])
                return false;
            // If expecting to compare char vs nothing
            if ((i >= 0) != (j >= 0))
                return false;
            i--; j--;
        }
        return true;
    }
};
```

**Solution 3: (Stack)**
```
Runtime: 0 ms
Memory: 6.6 MB
```
```c++
class Solution {
public:
    bool backspaceCompare(string s, string t) {
        string s1, s2;
        for (char &c: s) {
            if (c == '#') {
                if (s1 != "") {
                    s1.pop_back();
                }
            } else {
                s1 += c;
            }
        }
        for (char &c: t) {
            if (c == '#') {
                if (s2 != "") {
                    s2.pop_back();
                }
            } else {
                s2 += c;
            }
        }
        return s1 == s2;
    }
};
```
