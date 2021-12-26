227. Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, `+`, `-`, `*`, `/` operators and empty spaces ` `. The integer division should truncate toward zero.

**Example 1:**
```
Input: "3+2*2"
Output: 7
```

**Example 2:**
```
Input: " 3/2 "
Output: 1
```

**Example 3:**
```
Input: " 3+5 / 2 "
Output: 5
```

**Note:**

* You may assume that the given expression is always valid.
* Do not use the eval built-in library function.

# Submissions
---
**Solution 1: (Stack)**
```
Runtime: 84 ms
Memory Usage: 16 MB
```
```python
class Solution:
    def calculate(self, s: str) -> int:
        if not s.replace(' ', ''):
            return 0
        nums = list(map(int, re.split('\+|\-|\*|\/', s.replace(' ', ''))))
        sign = [_ for _ in s if _ == '+' or _ == '-' or _ == '*' or _ == '/']
        sign.append('#')
        stack = []
        temp_sign = '+'
        for i, num in enumerate(nums):
            if temp_sign == '+':
                stack.append(num)
                temp_sign = sign[i]
            elif temp_sign == '-':
                stack.append(-num)
                temp_sign = sign[i]
            elif temp_sign == '*':
                stack.append(stack.pop() * num)
                temp_sign = sign[i]
            else:
                stack.append(int(stack.pop() / num))
                temp_sign = sign[i]
        return sum(stack)
```

**Solution 2: (Stack, previous operator and append magic end signature)**
```
Runtime: 68 ms
Memory Usage: 14.6 MB
```
```python
class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        pre_op = '+'
        s += '#'
        stack = []
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c == ' ': continue
            else:
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    operant = stack.pop()
                    stack.append((operant*num))
                elif pre_op == '/':
                    operant = stack.pop()
                    stack.append(int(operant/num))
                num = 0
                pre_op = c
        return sum(stack)
```

**Solution 3: (Stack)**
```
Runtime: 0 ms
Memory Usage: 7.3 MB
```
```c


int calculate(char * s){
    int len=strlen(s)+3;
    int *num=malloc(sizeof(int)*len/2);
    int total=0,idx=0,i=0,j=0;
    char *stack=malloc(len);
    while(s[i])
    {
        switch(s[i])
        {
            case '+': case '-':
                stack[++j]=s[i];
                break;
            case '*': 
                i++;
                while(s[i]==' ')
                    i++;
                while(s[i]>='0'&&s[i]<='9')
                {
                    int n=s[i++]-'0';
                    total=total*10+n;
                }
                num[++idx]=total;
                total=0;
                i--;
                num[idx-1]=num[idx-1]*num[idx];
                idx--;
                break;
            case '/':
                i++;
                while(s[i]==' ')
                    i++;
                while(s[i]>='0'&&s[i]<='9')
                {
                    int n=s[i++]-'0';
                    total=total*10+n;
                }
                num[++idx]=total;
                total=0;
                i--;
                num[idx-1]=num[idx-1]/num[idx];
                idx--;
                break;
            case '0' ... '9':
                while(s[i]>='0'&&s[i]<='9')
                {
                    int n=s[i++]-'0';
                    total=total*10+n;
                }
                num[++idx]=total;
                total=0;
                i--;
                break;
        }
         i++;
                
    }

    int tmp=j;
    j=1;
    idx=1;
    while(j <= tmp) { 
        if(stack[j]=='+')
            num[idx+1]=num[idx]+num[idx+1];
        else
            num[idx+1]=num[idx]-num[idx+1];
        idx++;j++;
    }
    return num[idx];
}
```
