58. Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters `' '`, return the length of last word in the string.

If the last word does not exist, return `0`.

**Note:** A word is defined as a character sequence consists of non-space characters only.

**Example:**
```
Input: "Hello World"
Output: 5
```

# Submissions
---
**Solution 1: (String)**
```
Runtime: 28 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        if words:
            return len(words[-1])
        else:
            return 0
```

**Solution 2: (String)**
```
Runtime: 52 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])
```

**Solution 3: (String)**
```
Runtime: 2 ms
Memory: 8.04 MB
```
```c++
class Solution {
public:
    int lengthOfLastWord(string s) {
        stringstream ss(s);
        string cur, ans;
        while (getline(ss, cur, ' ')) {
            if (cur != "") {
                ans = cur;
            }
        }
        return ans.size();
    }
};
```

**Solution 4: (String)**

    s = "   fly me   to   the moon  "
count                        f   t
ans                          x4321   

```
Runtime: 0 ms
Memory: 7.69 MB
```
```c++
class Solution {
public:
    int lengthOfLastWord(string s) {
        int ans = 0;
        bool counting = false;
        
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s[i] != ' ') {
                counting = true;
                ans++;
            }
            else if (counting) {
                break;
            }
        }
        
        return ans;
    }
};
```
