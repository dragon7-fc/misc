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