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

**Solution 4: (String)**
```
Runtime: 0 ms
Memory Usage: 6.2 MB
```
```c

char * reverseWords(char * s){
    int i, j, n = strlen(s), top = -1;
    char *ans = malloc((n+1)*sizeof(char));
    i = n-1;
    while (i >= 0) {
        while (i >= 0 && s[i] == ' ')
            i -= 1;
        if (i < 0)
            break;
        j = i;
        while (j >= 0 && s[j] != ' ')
            j -= 1;
        memcpy(&ans[top+1], &s[j+1], (i-j)*sizeof(char));
        top += i-j;
        i = j;
        ans[++top] = ' ';
    }
    ans[top] = 0;
    return ans;
}
```

**Solution 5: (String)**
```
Runtime: 4 ms
Memory Usage: 7.2 MB
```
```c++
class Solution {
public:
    string reverseWords(string s) {
        reverse(s.begin(), s.end());
        istringstream iss(s);
        string str;
        string ans;
        while (getline(iss, str, ' ')) {
            if (str.size() != 0) {
                reverse(str.begin(), str.end());
                ans += str + " ";
            }
        }
        ans.pop_back();
        return ans;
    }
};
```

**Solution 6: (String, Stack)**
```
Runtime: 3 ms
Memory Usage: 7.6 MB
```
```c++
class Solution {
public:
    string reverseWords(string s) {
        string ans;
		if(s.size()==0)
			return s;
		stack<string>st;
		for(int i=0;i<s.size();i++){
			string word;
			if(s[i]==' ')
				continue;
			while(s[i]!=' ' && i<s.size()){
					word+=s[i];  i++;
			}
            st.push(word);
		}

		while(!st.empty()){
				ans+=st.top(); st.pop();
			if(!st.empty())
				ans+=" ";
		}
		return ans;
    }
};
```
