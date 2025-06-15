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
Runtime: 0 ms, Beats 100.00%
Memory: 10.82 MB, Beats 61.53%
```
```c++
class Solution {
public:
    string simplifyPath(string path) {
        stringstream ss(path);
        string s;
        vector<string> dp;
        int i;
        while (getline(ss, s, '/')) {
            if (s == "" || s == ".") {
                continue;
            } else if (s == "..") {
                if (dp.size()) {
                    dp.pop_back();
                }
            } else {
                dp.push_back(s);
            }
        }
        s = "";
        for (i = 0; i < dp.size(); i ++) {
            s += "/";
            s += dp[i];
        }
        return s == "" ? "/" : s;
    }
};
```

**Solution 4: (String, Stack)**
```
Runtime: 3 ms, Beats 59.24%
Memory: 10.37 MB, Beats 88.42%
```
```c++
class Solution {
public:
    string simplifyPath(string path) {
        int n = path.size(), i;
        vector<string> dp;
        string cur;
        i = 0;
        while (i < n) {
            while (i < n && path[i] == '/') {
                i += 1;
            }
            if (i == n) {
                break;
            }
            cur = "";
            while (i < n && path[i] != '/') {
                cur += path[i];
                i += 1;
            }
            if (cur == ".") {
                continue;
            } else if (cur == "..") {
                if (dp.size()) {
                    dp.pop_back();
                }
            } else {
                dp.push_back(cur);
            }
        }
        cur = "";
        for (i = 0; i < dp.size(); i ++) {
            cur += "/";
            cur += dp[i];
        }
        if (cur == "") {
            cur = "/";
        }
        return cur;
    }
};;
```
