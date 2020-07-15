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