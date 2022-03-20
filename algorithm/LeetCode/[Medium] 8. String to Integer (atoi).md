8. String to Integer (atoi)

Implement `atoi` which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

**Note:**

* Only the space character ' ' is considered as whitespace character.
* Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.

**Example 1:**
```
Input: "42"
Output: 42
```

**Example 2:**
```
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
```
**Example 3:**
```
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
```

**Example 4:**
```
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
```

**Example 5:**
```
Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
```

## Submissions 
---
**Solution: (Follow the Rules)**
```
Runtime: 59 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1 
        result = 0
        index = 0
        n = len(s)
        
        INT_MAX = pow(2,31) - 1 
        INT_MIN = -pow(2,31)
        
        # Discard all spaces from the beginning of the input string.
        while index < n and s[index] == ' ':
            index += 1
        
        # sign = +1, if it's positive number, otherwise sign = -1. 
        if index < n and s[index] == '+':
            sign = 1
            index += 1
        elif index < n and s[index] == '-':
            sign = -1
            index += 1
        
        # Traverse next digits of input and stop if it is not a digit. 
        # End of string is also non-digit character.
        while index < n and s[index].isdigit():
            digit = int(s[index])
            
            # Check overflow and underflow conditions. 
            if ((result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10)):
                # If integer overflowed return 2^31-1, otherwise if underflowed return -2^31.    
                return INT_MAX if sign == 1 else INT_MIN
            
            # Append current digit to the result.
            result = 10 * result + digit
            index += 1
        
        # We have formed a valid number without any overflow/underflow.
        # Return it after multiplying it with its sign.
        return sign * result
```

**Solution: (Follow the Rules)**
```
Runtime: 4 ms
Memory Usage: 7 MB
```
```c++
class Solution {
public:
    int myAtoi(string s) {
        int sign = 1; 
        int result = 0; 
        int index = 0;
        int n = s.size();
        
        // Discard all spaces from the beginning of the input string.
        while (index < n && s[index] == ' ') { 
            index++; 
        }
        
        // sign = +1, if it's positive number, otherwise sign = -1. 
        if (index < n && s[index] == '+') {
            sign = 1;
            index++;
        } else if (index < n && s[index] == '-') {
            sign = -1;
            index++;
        }
        
        // Traverse next digits of input and stop if it is not a digit. 
        // End of string is also non-digit character.
        while (index < n && isdigit(s[index])) {
            int digit = s[index] - '0';

            // Check overflow and underflow conditions. 
            if ((result > INT_MAX / 10) || (result == INT_MAX / 10 && digit > INT_MAX % 10)) { 
                // If integer overflowed return 2^31-1, otherwise if underflowed return -2^31.    
                return sign == 1 ? INT_MAX : INT_MIN;
            }
            
            // Append current digit to the result.
            result = 10 * result + digit;
            index++;
        }
        
        // We have formed a valid number without any overflow/underflow.
        // Return it after multiplying it with its sign.
        return sign * result;
    }
};
```

**Solution: (Deterministic Finite Automaton (DFA))**
```
Runtime: 48 ms
Memory Usage: 14.4 MB
```
```python
class StateMachine:
    def __init__(self):
        self.State = { "q0": 1, "q1": 2, "q2": 3, "qd": 4 }
        self.INT_MAX, self.INT_MIN = pow(2, 31) - 1, -pow(2, 31)
        
        # Store current state value.
        self.__current_state = self.State["q0"]
        # Store result formed and its sign.
        self.__result = 0
        self.__sign = 1

    def to_state_q1(self, ch: chr) -> None:
        """Transition to state q1."""
        self.__sign = -1 if (ch == '-') else 1
        self.__current_state = self.State["q1"]
    
    def to_state_q2(self, digit: int) -> None:
        """Transition to state q2."""
        self.__current_state = self.State["q2"]
        self.append_digit(digit)
    
    def to_state_qd(self) -> None:
        """Transition to dead state qd."""
        self.__current_state = self.State["qd"]
    
    def append_digit(self, digit: int) -> None:
        """Append digit to result, if out of range return clamped value."""
        if ((self.__result > self.INT_MAX // 10) or 
            (self.__result == self.INT_MAX // 10 and digit > self.INT_MAX % 10)):
            if self.__sign == 1:
                # If sign is 1, clamp result to INT_MAX.
                self.__result = self.INT_MAX
            else:
                # If sign is -1, clamp result to INT_MIN.
                self.__result = self.INT_MIN
                self.__sign = 1
            
            # When the 32-bit int range is exceeded, a dead state is reached.
            self.to_state_qd()
        else:
            # Append current digit to the result. 
            self.__result = (self.__result * 10) + digit

    def transition(self, ch: chr) -> None:
        """Change state based on current input character."""
        if self.__current_state == self.State["q0"]:
            # Beginning state of the string (or some whitespaces are skipped).
            if ch == ' ':
                # Current character is a whitespaces.
                # We stay in same state. 
                return
            elif ch == '-' or ch == '+':
                # Current character is a sign.
                self.to_state_q1(ch)
            elif ch.isdigit():
                # Current character is a digit.
                self.to_state_q2(int(ch))
            else:
                # Current character is not a space/sign/digit.
                # Reached a dead state.
                self.to_state_qd()
        
        elif self.__current_state == self.State["q1"] or self.__current_state == self.State["q2"]:
            # Previous character was a sign or digit.
            if ch.isdigit():
                # Current character is a digit.
                self.to_state_q2(int(ch))
            else:
                # Current character is not a digit.
                # Reached a dead state.
                self.to_state_qd()
    
    def get_integer(self) -> None:
        """Return the final result formed with it's sign."""
        return self.__sign * self.__result
    
    def get_state(self) -> None:
        """Get current state."""
        return self.__current_state

class Solution:
    def myAtoi(self, s: str) -> int:
        q = StateMachine()
        
        for ch in s:
            q.transition(ch)
            if q.get_state() == q.State["qd"]:
                break

        return q.get_integer()
```

**Solution: (Deterministic Finite Automaton (DFA))**
```
Runtime: 4 ms
Memory Usage: 7.1 MB
```
```c++
enum State { q0, q1, q2, qd };

class StateMachine {
    // Store current state value.
    State currentState;
    // Store result formed and it's sign.
    int result, sign;
    
    // Transition to state q1.
    void toStateQ1(char& ch) {
        sign = (ch == '-') ? -1 : 1;
        currentState = q1;
    }
    
    // Transition to state q2.
    void toStateQ2(int digit) {
        currentState = q2;
        appendDigit(digit);
    }
    
    // Transition to dead state qd.
    void toStateQd() {
        currentState = qd;
    }
    
    // Append digit to result, if out of range return clamped value.
    void appendDigit(int& digit) {
        if ((result > INT_MAX / 10) || 
            (result == INT_MAX / 10 && digit > INT_MAX % 10)) {
            if (sign == 1) {
                // If sign is 1, clamp result to INT_MAX.
                result = INT_MAX;
            } else {
                // If sign is -1, clamp result to INT_MIN.
                result = INT_MIN;
                sign = 1;
            }
            
            // When the 32-bit int range is exceeded, a dead state is reached.
            toStateQd();
        } else {
            // Append current digit to the result. 
            result = result * 10 + digit;
        }
    }

public:
    StateMachine() {
        currentState = q0;
        result = 0;
        sign = 1;
    }

    // Change state based on current input character.
    void transition(char& ch) {
        if (currentState == q0) {
            // Beginning state of the string (or some whitespaces are skipped).
            if (ch == ' ') {
                // Current character is a whitespaces.
                // We stay in same state. 
                return;
            } else if (ch == '-' || ch == '+') {
                // Current character is a sign.
                toStateQ1(ch);
            } else if (isdigit(ch)) {
                // Current character is a digit.
                toStateQ2(ch - '0');
            } else {
                // Current character is not a space/sign/digit.
                // Reached a dead state.
                toStateQd();
            }
        } else if (currentState == q1 || currentState == q2) {
            // Previous character was a sign or digit.
            if (isdigit(ch)) {
                // Current character is a digit.
                toStateQ2(ch - '0');
            } else {
                // Current character is not a digit.
                // Reached a dead state.
                toStateQd();
            }
        }
    }
    
    // Return the final result formed with it's sign.
    int getInteger() {
        return sign * result;
    }
    
    // Get current state.
    State getState() {
        return currentState;
    }
};

class Solution {
public:
    int myAtoi(string s) {
        StateMachine Q;
        
        for (int i = 0; i < s.size() && Q.getState() != qd; ++i) {
            Q.transition(s[i]);
        }
        
        return Q.getInteger();
    }
};
```

**Solution 1: (String, Math)**
```
Runtime: 32 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        N = len(str)
        sign = 1
        res = 0
        
        for i in range(N):
            c = str[i]
            if i == 0:
                if c == '-':
                    sign = -1
                elif c == '+':
                    sign = 1
                elif c.isdigit():
                    res = res * 10 + ord(c) - ord('0')
                else:
                    break
            else:
                if c.isdigit():
                    res = res * 10 + ord(c) - ord('0')
                else:
                    break
        
        res = sign * res
        if res > 2**31 - 1:
            res = 2**31 - 1
        if res < -2**31:
            res = -2**31
        return res
```

**Solution 2: (String, Math)**
```
Runtime: 4 ms
Memory Usage: 5.6 MB
```
```c
int myAtoi(char * s){
    int i = 0, digit = 0, ans = 0;
    bool pos = true;
    while (s[i] != '\0') {
        if (s[i] == ' ') {
            i += 1;
            continue;
        }
        break;
    }
    if (s[i] != '\0') {
        if (s[i] == '-') {
            pos = false;
            i += 1;
        } else if (s[i] == '+') {
            i += 1;
        }
    }
    while (isdigit(s[i])) {
        digit = s[i] - '0';
        if (ans == 0) {
            ans = digit;
            if (!pos)
                ans = -ans;
        } else {
            if (!pos)
                digit = -digit;
            if (ans > INT_MAX/10 || (ans == INT_MAX/10 && digit > 7))
                return INT_MAX;
            if (ans < INT_MIN/10 || (ans == INT_MIN/10 && digit < -8))
                return INT_MIN;
            ans = ans*10 + digit;
        }
        i += 1;
    }
    return ans;
}
```
