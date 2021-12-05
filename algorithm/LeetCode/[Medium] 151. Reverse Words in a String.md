151. Reverse Words in a String

Given an input string, reverse the string word by word.

 

**Example 1:**
```
Input: "the sky is blue"
Output: "blue is sky the"
```

**Example 2:**
```
Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
```

**Example 3:**
```
Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
```

**Note:**

* A word is defined as a sequence of non-space characters.
* Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
* You need to reduce multiple spaces between two words to a single space in the reversed string.
 

**Follow up:**

* For C programmers, try to solve it in-place in O(1) extra space.

# Submissions
---
**Solution 1: (String)**
```
Runtime: 16 ms
Memory Usage: 13.3 MB
```
```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])  #first split then reverse and then join to form new string
```

**Solution 2: (String)**
```
Runtime: 32 ms
Memory Usage: 65.1 MB
```
```c++
class Solution {
public:
    string reverseWords(string s) {
        stringstream all(s); 
        string word,ans = "";
        while (all >> word)
            ans = word + " " + ans;
        return ans.substr(0,ans.length()-1);
    }
};
```

**Solution 3: (String)**
```
Runtime: 4 ms
Memory Usage: 6.6 MB
```
```c
void reverse(char *_s, int _i, int _j) {
    char tmp;
    while (_i < _j) {
        tmp = _s[_i];
        _s[_i] = _s[_j];
        _s[_j] = tmp;
        _i += 1;
        _j -= 1;
    }
}

char * reverseWords(char * s){
    int N = strlen(s);
    char *ans = calloc(strlen(s) + 1, sizeof(char));
    char *token = strtok(s, " ");
    int i = 0, j = 0;
    char tmp;
    while (token) {
        memcpy(&ans[i], token, strlen(token));
        i += strlen(token);
        ans[i] = ' ';
        i += 1;
        token = strtok(NULL, " ");
    }
    ans[i-1] = 0;
    reverse(ans, 0, i-2);
    i = 0, j = 0;
    while (j < strlen(ans)) {
        while (j < strlen(ans) && ans[j] != ' ')
            j += 1;
        reverse(ans, i, j-1);
        i = j + 1;
        j = j + 1;
    }
    return ans;
}
```
