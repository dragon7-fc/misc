394. Decode String

Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like `3a` or `2[4]`.

**Examples:**
```
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
```

# Submissions
---
**Solution 1: (Stack)**
```
Runtime: 20 ms
Memory Usage: 12.7 MB
```
```python
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        stack.append(["", 1])
        num = ""
        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == '[':
                stack.append(['', int(num)])
                num = ''
            elif ch.isalpha():
                stack[-1][0] += ch
            elif ch == ']':
                st, k = stack.pop()
                stack[-1][0] += st*k
        return stack[0][0]
```

**Solution 2: (DFS)**
```
Runtime: 20 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def decodeString(self, s: str) -> str:
        def dfs():
            text = ""
            num = 0
            # the dfs recursion call absorbed "]", so that outer recursion can continue
            while self.idx < len(s) and s[self.idx] != "]":
                if s[self.idx].isdigit():
                    num = num * 10 + int(s[self.idx])
                    self.idx += 1
                elif s[self.idx].isalpha():
                    text += s[self.idx]
                    self.idx += 1
                else:
                    self.idx += 1  # s[self.idx] == "["
                    res = dfs()
                    text += num * res
                    num = 0
            self.idx += 1
            return text
        self.idx = 0
        return dfs()
```

**Solution 3: (Stack)**
```
Runtime: 24 ms
Memory Usage: 12.8 MB
```
```python
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        keeper = []
        i = 0
        l = len(s)
        while i<l:
            if s[i] == ']':
                alpha = []
                while keeper and keeper[-1] != '[':
                    alpha.append(keeper.pop())
                keeper.pop()
                num = []
                while keeper and keeper[-1].isdigit():
                    num.append(keeper.pop())
                num = int(''.join(num[::-1]))
                alpha = alpha[::-1]
                keeper.append(''.join(alpha)*num)
            else:
                keeper.append(s[i])
            i += 1
        return ''.join(keeper)
```

**Solution 4: (Regular Expression)**
```
Runtime: 24 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def decodeString(self, s: str) -> str:
        parse = re.findall(r"(\d+)(\[)|([a-zA-Z]+)|(\])", s)
        stack = [['', 1]]
        for num, left_open, alpha, right_open in parse:
            if num:
                k = int(num)
            if left_open:
                stack.append(['', k])
            if alpha:
                stack[-1][0] += alpha
            if right_open:
                st, k = stack.pop()
                stack[-1][0] += st*k
            
        return stack[-1][0]
```

**Solution 5: (DFS)**
```
Runtime: 0 ms
Memory Usage: 10 MB
```
```c
int stringToInt(char c1, char c2, char c3) {

    int num = (c3 - 48);

    num += ((c2 - 48) * 10);

    num += ((c1 - 48) * 100);

    return num;
}

char * decodeString(char * s){
    char *string = (char *) malloc(10000 * sizeof(char));

    if (s[0] == '\0')
        return "\0";
    else if (s[0] >= 'a' && s[0] <= 'z') {
        string[0] = s[0];
        string[1] = '\0';

        strcat(string, decodeString(s + 1));

        return string;
    }
    else if (s[0] >= '1' && s[0] <= '9') {    
        int count = 1, pos = 2, aux = 0;
        char c1 = '0', c2 = '0', c3 = s[0];
    
        if (s[1] != '[') {
            c3 = s[1];
            c2 = s[0];

            pos++;

            if (s[2] != '[') {
                c3 = s[2];
                c2 = s[1];
                c1 = s[0];

                pos++;
            }
        }
    
        int k = stringToInt(c1, c2, c3);
    
        while (count != 0) {
            if (s[pos] == '[')
                count++;
            else if (s[pos] == ']')
                count--;

            if (count != 0)
                string[aux++] = s[pos++];
        }

        string[aux] = '\0';

        strcpy(string, decodeString(string));
    
        char tmp[10000];

        tmp[0] = '\0';

        strcpy(tmp, string);

        for (int i = 0; i < (k - 1); i++)
            strcat(string, tmp);

        strcat(string, decodeString(s + pos + 1));
    
        return string;
    }

    return string;
}
```

**Solution 6: (Stack)**

     "3 [ a 2 [ c ] ]"
                    ^
k  0  3 0   2 0
                          ans
stk                    vvvvvvvvvv
{0,""}              {0,"accaccacc"}
         {3,"a"}  {3,"acc"}x
                {2,"c"}x

        {2, "c"}     
        {3, "a"} -> {3, "acc"} 
        {0, ""}  -> {0, "accaccacc"}

```
Runtime: 0 ms, Beats 100.00%
Memory: 9.63 MB, Beats 25.94%
```
```c++
class Solution {
public:
    string decodeString(string s) {
        int k = 0;
        stack<pair<int,string>> stk;
        stk.push({0, ""});
        for (auto &c: s) {
            if (isalpha(c)) {
                stk.top().second += c;
                k = 0;
            } else if (isdigit(c)) {
                k = k*10 + c-'0';
            } else if (c == '[') {
                stk.push({k, ""});
                k = 0;
            } else {
                auto [k, s] = stk.top();
                stk.pop();
                while (k) {
                    stk.top().second += s;
                    k -= 1;
                }
                k = 0;
            }
        }
        return stk.top().second;
    }
};
```
