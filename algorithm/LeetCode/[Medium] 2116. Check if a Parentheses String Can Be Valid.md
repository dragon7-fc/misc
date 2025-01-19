2116. Check if a Parentheses String Can Be Valid

A parentheses string is a non-empty string consisting only of `'('` and `')'`. It is valid if any of the following conditions is true:

* It is `()`.
* It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid parentheses strings.
* It can be written as `(A)`, where `A` is a valid parentheses string.

You are given a parentheses string `s` and a string `locked`, both of length `n`. `locked` is a binary string consisting only of `'0'`s and `'1'`s. For each index `i` of `locked`,

* If `locked[i]` is `'1'`, you cannot change `s[i]`.
* But if `locked[i]` is `'0'`, you can change `s[i]` to either `'('` or `')'`.

Return `true` if you can make s a valid parentheses string. Otherwise, return `false`.

 

**Example 1:**

![2116_eg1.png](img/2116_eg1.png)
```
Input: s = "))()))", locked = "010100"
Output: true
Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.
```

**Example 2:**
```
Input: s = "()()", locked = "0000"
Output: true
Explanation: We do not need to make any changes because s is already valid.
```

**Example 3:**
```
Input: s = ")", locked = "0"
Output: false
Explanation: locked permits us to change s[0]. 
Changing s[0] to either '(' or ')' will not make s valid.
```

**Constraints:**

* `n == s.length == locked.length`
* `1 <= n <= 10^5`
* `s[i]` is either `'('` or `')'`.
* `locked[i]` is either `'0'` or `'1'`.

# Submissions
---
**Solution 1: (Balance value, greedy 2-pass)**
```
Runtime: 373 ms
Memory: 15.4 MB
```
```python
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)&1: return False

        ## try '0' == '('        
        bal = 0
        for ch, lock in zip(s, locked):
            if lock == '0' or ch == '(': bal += 1
            elif ch == ')': bal -= 1
            if bal < 0: return False 
 
        ## try '0' == ')'
        bal = 0
        for ch, lock in zip(reversed(s), reversed(locked)): 
            if lock == '0' or ch == ')': bal += 1
            elif ch == '(': bal -= 1
            if bal < 0: return False
        return True
```

**Solution 2: (Stack, two stack)**

    lock (important) > unlock
   ^^^^^^
    /  \
   (    )
-> remove lock first
-> step 1: try to remove ( with ) (lock)
   step 2: try to remove ( with unlock
```
Runtime: 21 ms
Memory: 34.89 MB
```
```c++
class Solution {
public:
    bool canBeValid(string s, string locked) {
        int length = s.size();
        // If length of string is odd, return false.
        if (length % 2 == 1) {
            return false;
        }

        stack<int> openBrackets, unlocked;

        // Iterate through the string to handle '(' and ')'
        for (int i = 0; i < length; i++) {
            if (locked[i] == '0') {
                unlocked.push(i);
            } else if (s[i] == '(') {
                openBrackets.push(i);
            } else if (s[i] == ')') {
                if (!openBrackets.empty()) {
                    openBrackets.pop();
                } else if (!unlocked.empty()) {
                    unlocked.pop();
                } else {
                    return false;
                }
            }
        }

        // Match remaining open brackets with unlocked characters
        while (!openBrackets.empty() && !unlocked.empty() &&
               openBrackets.top() < unlocked.top()) {
            openBrackets.pop();
            unlocked.pop();
        }

        if (!openBrackets.empty()) {
            return false;
        }

        return true;
    }
};
```

**Solution 3: (Constant Space)**

s               )  )  (  )  )  )
locked          0  1  0  1  0  0
---------------------------------
openBrackets    0  0  0  0  0  0
unlocked        1  0  1  0  1  2
---------------------------------
openBrackets    0  0  0  0  0  0
unlocked       -2 -1 -1  0  0  1
balanced       -6 -5 -4 -3 -2 -1 0
                           


```
Runtime: 8 ms
Memory: 30.18 MB
```
```c++
class Solution {
public:
    bool canBeValid(string s, string locked) {
        int length = s.size();
        // If length of string is odd, return false.
        if (length % 2 == 1) {
            return false;
        }
        int openBrackets = 0, unlocked = 0;
        // Iterate through the string to handle '(' and ')'.
        for (int i = 0; i < length; i++) {
            if (locked[i] == '0') {
                unlocked++;
            } else if (s[i] == '(') {
                openBrackets++;
            } else if (s[i] == ')') {
                if (openBrackets > 0) {
                    openBrackets--;
                } else if (unlocked > 0) {
                    unlocked--;
                } else {
                    return false;
                }
            }
        }
        // Match remaining open brackets with unlocked characters.
        int balance = 0;  // track excess unmatched opening brackets.
        for (int i = length - 1; i >= 0; i--) {
            if (locked[i] == '0') {
                balance--;
                unlocked--;
            } else if (s[i] == '(') {
                balance++;
                openBrackets--;
            } else if (s[i] == ')') {
                balance--;
            }
            if (balance > 0) {
                return false;
            }
            if (unlocked == 0 and openBrackets == 0) {
                break;
            }
        }

        if (openBrackets > 0) {
            return false;
        }

        return true;
    }
};
```

**Solution 4: (Counter, left and right)**

step1: forward try 0 = '('
step2: backward try 0 = ')'

```
Runtime: 20 ms
Memory: 30.08 MB
```
```c++
class Solution {
public:
    bool canBeValid(string s, string locked) {
        int n = s.length();
        if (n % 2 != 0) {
            return false; // Odd length cannot form valid parentheses
        }

        // Left-to-right pass: Ensure there are enough open brackets
        int openCount = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] == '(' || locked[i] == '0') {
                openCount++;
            } else { // s[i] == ')' and locked[i] == '1'
                openCount--;
            }
            if (openCount < 0) {
                return false; // Too many ')' encountered
            }
        }

        // Right-to-left pass: Ensure there are enough close brackets
        int closeCount = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (s[i] == ')' || locked[i] == '0') {
                closeCount++;
            } else { // s[i] == '(' and locked[i] == '1'
                closeCount--;
            }
            if (closeCount < 0) {
                return false; // Too many '(' encountered
            }
        }

        return true;
    }
};
```
