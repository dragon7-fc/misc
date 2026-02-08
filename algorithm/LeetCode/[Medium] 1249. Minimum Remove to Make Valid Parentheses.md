1249. Minimum Remove to Make Valid Parentheses

Given a string s of `'('` , `')'` and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( `'('` or `')'`, in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

* It is the empty string, contains only lowercase characters, or
* It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid strings, or
* It can be written as `(A)`, where `A` is a valid string.
 

**Example 1:**
```
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
```

**Example 2:**
```
Input: s = "a)b(c)d"
Output: "ab(c)d"
```

**Example 3:**
```
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
```

**Example 4:**
```
Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
```

**Constraints:**

* `1 <= s.length <= 10^5`
* `s[i]` is one of  `'('` , `')'` and lowercase English letters.

# Submissions
---
**Solution 1: (Stack)**
```
Runtime: 116 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return
        stack = []
        for i, token in enumerate(s):
            if token == ")" and stack and stack[-1][1] == "(":
                stack.pop()
            elif token in ('(',')'):
                stack.append((i,token))     # Trick is to append index and token both to stack. All unmatched/extra brackets will be 
                                            # left on stack which have to be removed from given string.
            else:
                continue
        s = list(s)
        while stack:
            index = stack.pop()[0]
            s.pop(index)                # Remove unmatched from string.
            #s[:] = s[:index] + s[index+1:]

        return ''.join(s)
        
```

**Solution 2: (Stack)**
```
Runtime: 12 ms
Memory Usage: 8 MB
```
```c

#define STACK_SIZE_MAX 100000
char * minRemoveToMakeValid(char * s){
    int stack[STACK_SIZE_MAX];
    int stackSize = 0;
    
    for (int i = 0; s[i] != '\0'; i++)
    {
        if (s[i] == '(')
        {
            // printf("Pt 1: s[%d] = %c, stackSize = %d\n", i, s[i], stackSize);
            stack[stackSize++] = i;
        }
        else if (s[i] == ')')
        {
            if (stackSize == 0 || s[stack[stackSize-1]] != '(')
            {
                // printf("Pt 2: s[%d] = %c, stackSize = %d\n", i, s[i], stackSize);
                stack[stackSize++] = i;
            }
            else // stackSize != 0 && stack[stackSize-1] == '('
            {
                // printf("Pt 3: s[%d] = %c, stackSize = %d\n", i, s[i], stackSize);
                stackSize--;
            }
        }
    }
    
    char* ans = malloc(sizeof(char) * (strlen(s) - stackSize + 1));
    for (int i = 0; i < stackSize; i++)
    {
        // printf("s[%d] = %c\n", stack[i], s[stack[i]]);
        s[stack[i]] = '-';
    }
    
    int j = 0; // write pointer
    for (int i = 0; s[i] != '\0'; i++)
    {
        if (s[i] != '-')
        {
            ans[j++] = s[i];
        }
    }
    ans[j] = '\0';
    
    return ans;
}
```

**Solution 3: (Two Pointers)**
```
Runtime: 19 ms
Memory Usage: 7.1 MB
```
```c
#define DELETE 'X'
char * minRemoveToMakeValid(char * s){
    int i, j;
    int level = 0;
    for(i=0;s[i];++i) {
        if (s[i] == '(') {
            ++level;
        } else if (s[i] == ')') {
            (level == 0) ?  s[i] = DELETE : --level;
        }
    }
    level = 0;
    for(i=i-1;i>=0;--i) {
        if (s[i] == ')') {
            --level;
        } else if (s[i] == '(') {
            (level == 0) ?  s[i] = DELETE : ++level;
        }
    }
    for(i=j=0;s[i];++i) {
        if(s[i]==DELETE) {
            continue;
        }
        if (i!=j) {
            s[j]=s[i];
        }
        ++j;
    }
    s[j] = 0;
    
    return s;
}
```

**Solution 4: (Stack)**

         0 1 2 3 4 5 6 7 8 9 10 11 12
    s = "l e e ( t ( c ) o )  d  e  )"
dp             1   1   1   1
stk            3   5   3           12 
                   3

```
Runtime: 4 ms, Beats 84.32%
Memory: 16.55 MB, Beats 9.22%
```
```c++
class Solution {
public:
    string minRemoveToMakeValid(string s) {
        int n = s.length(), i;
        vector<int> dp(n);
        stack<int> stk;
        string ans;
        for (i = 0; i < n; i ++) {
            if (s[i] == '(') {
                stk.push(i);
            } else if (s[i] == ')') {
                if (stk.size()) {
                    dp[stk.top()] = 1;
                    dp[i] = 1;
                    stk.pop();
                }
            }
        }
        for (i = 0; i < n; i ++) {
            if (s[i] == '(' || s[i] == ')') {
                if (dp[i]) {
                    ans += s[i];
                }
            } else {
                ans += s[i];
            }
        }
        return ans;
    }
};
```
