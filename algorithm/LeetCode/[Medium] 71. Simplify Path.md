71. Simplify Path

Given an **absolute path** for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

In a UNIX-style file system, a period `.` refers to the current directory. Furthermore, a double period `..` moves the directory up a level. For more information, see: Absolute path vs relative path in Linux/Unix

Note that the returned canonical path must always begin with a slash `/`, and there must be only a single slash `/` between two directory names. The last directory name (if it exists) must not end with a trailing `/`. Also, the canonical path must be the **shortest** string representing the absolute path.

 

**Example 1:**
```
Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
```

**Example 2:**
```
Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
```

**Example 3:**
```
Input: "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
```

**Example 4:**
```
Input: "/a/./b/../../c/"
Output: "/c"
```

**Example 5:**
```
Input: "/a/../../b/../c//.//"
Output: "/c"
```

**Example 6:**
```
Input: "/a//b////c/d//././/.."
Output: "/a/b/c"
```

# Submissions
---
**Solution 1: (Stack)**
```
Runtime: 32 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path_split = path.split("/")
        for subdir in path_split:
            if subdir == "." or len(subdir) == 0:
                continue
            elif subdir == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(subdir)
                
        return "/"+"/".join(stack)
```

**Solution 2: (Stack)**
```
Runtime: 4 ms
Memory Usage: 8.9 MB
```
```c


char * simplifyPath(char * path){
    int size = 0, save[1024];
    char* token = strtok(path,"/");
    char **temp = (char**)malloc(sizeof(char*) * 1024);
    char *result = (char*)malloc(sizeof(char) * 1024);
    while(token != NULL){
        temp[size] = (char*)malloc(sizeof(char) * strlen(token) + 1);
        strcpy(temp[size], token);
        size++;
        token = strtok(NULL, "/");
    }
    int idx = 0;
    for(int i = 0; i < size; i++){
        if (idx < 0) idx = 0;
        if (idx >= 0) save[idx] = i;
        if(temp[i][0] == '.' && temp[i][1] == '.' && temp[i][2] == '\0') idx--;
        else if(temp[i][0] == '.' && temp[i][1] == '\0');
        else idx++;
    }
    result[0] = '\0';
    for(int i = 0; i < idx; i++){
        strcat(result, "/");
        strcat(result, temp[save[i]]);
    }
    if(result[0] == '\0') strcat(result, "/");
    return result;
}
```

**Solution 3: (Stack)**
```
Runtime: 7 ms
Memory Usage: 9.4 MB
```
```c++
class Solution {
public:
    string simplifyPath(string path) {
        vector<string> stk; 
        istringstream iss(path); 
        string buf; 
        while (getline(iss, buf, '/')) 
            if (buf == "..") {
                if (stk.size()) stk.pop_back(); 
            } else if (buf.size() && buf != ".") 
                stk.push_back(buf); 
        string ans; 
        for (auto& x : stk) ans += "/" + x; 
        return ans.size() ? ans : "/"; 
    }
};
```

**Solution 4: (String)**
```
Runtime: 11 ms
Memory: 9.5 MB
```
```c++
class Solution {
public:
    string simplifyPath(string path) {
        int N = path.size(), i = 1;
        vector<string> stk;
        while (i < N) {
            string cur;
            while (i < N && path[i] != '/') {
                cur += path[i];
                i += 1;
            }
            if (cur == "..") {
                if (!stk.empty()) {
                    stk.pop_back();
                }
            } else if (cur != "" && cur != ".") {
                stk.push_back(cur);
            }
            i += 1;
        }
        string ans;
        for (int i = 0; i < stk.size(); i ++) {
            ans += "/" + stk[i];
        }
        return ans != "" ? ans : "/";
    }
};
```
