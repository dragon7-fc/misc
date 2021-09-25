1328. Break a Palindrome

Given a palindromic string `palindrome`, replace **exactly one** character by any lowercase English letter so that the string becomes the lexicographically smallest possible string that isn't a palindrome.

After doing so, return the final string.  If there is no way to do so, return the empty string.

 

**Example 1:**
```
Input: palindrome = "abccba"
Output: "aaccba"
```

**Example 2:**
```
Input: palindrome = "a"
Output: ""
```

**Constraints:**

* `1 <= palindrome.length <= 1000`
* `palindrome` consists of only lowercase English letters.

# Submissions
---
**Solution 1: (Greedy)**

* Check half of the string,
    
    replace a non 'a' character to `'a'`.
* If only one character, return empty string.
    
    Otherwise repalce the last character to `'b'`

```
Runtime: 28 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]
        return palindrome[:-1] + 'b' if palindrome[:-1] else ''
```

**Solution 2: (Greedy)**
```
Runtime: 0 ms
Memory Usage: 6.3 MB
```
```c++
class Solution {
public:
    string breakPalindrome(string palindrome) {
        string res;
        if (palindrome.size() == 1)
            return res;
        for (size_t i = 0; i < palindrome.size() / 2; i++)
        {
            if(palindrome[i] != 'a')
            {
                palindrome[i] = 'a';
                return palindrome;                
            }
        }
        palindrome[palindrome.size() - 1] = 'b';
        return palindrome;     
    }
};
```
