680. Valid Palindrome II

Given a non-empty string `s`, you may delete **at most** one character. Judge whether you can make it a palindrome.

**Example 1:**
```
Input: "aba"
Output: True
```

**Example 2:**
```
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
```

**Note:**

* The string will only contain lowercase characters `a-z`. The maximum length of the string is `50000`.

# Solution
---
## Approach #1: Brute Force [Time Limit Exceeded]
**Intuition and Algorithm**

For each index `i` in the given string, let's remove that character, then check if the resulting string is a palindrome. If it is, (or if the original string was a palindrome), then we'll return `true`

```python
class Solution(object):
    def validPalindrome(self, s):
        for i in xrange(len(s)):
            t = s[:i] + s[i+1:]
            if t == t[::-1]: return True

        return s == s[::-1]
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$ where $N$ is the length of the string. We do the following $N$ times: create a string of length $N$ and iterate over it.

* Space Complexity: $O(N)$, the space used by our candidate answer.

## Approach #2: Greedy [Accepted]
**Intuition**

If the beginning and end characters of a string are the same (ie. `s[0] == s[s.length - 1]`), then whether the inner characters are a palindrome (`s[1], s[2], ..., s[s.length - 2]`) uniquely determines whether the entire string is a palindrome.

**Algorithm**

Suppose we want to know whether `s[i], s[i+1], ..., s[j]` form a palindrome. If `i >= j` then we are done. If `s[i] == s[j]` then we may take `i++; j--`. Otherwise, the palindrome must be either `s[i+1], s[i+2], ..., s[j]` or `s[i], s[i+1], ..., s[j-1]`, and we should check both cases.

```python
class Solution(object):
    def validPalindrome(self, s):
        def is_pali_range(i, j):
            return all(s[k] == s[j-k+i] for k in range(i, j))

        for i in xrange(len(s) / 2):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                return is_pali_range(i+1, j) or is_pali_range(i, j-1)
        return True
```

**Complexity Analysis**

* Time Complexity: $O(N)$ where $N$ is the length of the string. Each of two checks of whether some substring is a palindrome is $O(N)$.

* Space Complexity: $O(1)$ additional complexity. Only pointers were stored in memory.

# Submissions
---
**Solution 1: (Two Pointers)**
```
Runtime: 100 ms
Memory Usage: 13.1 MB
```
```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i , j = 0, len(s) - 1
        
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                c1 = s[i:j]
                c2 = s[i+1:j+1]
        
                if c1 == c1[::-1] or c2 == c2[::-1]:  # checking the candidate is palindrome or not
                    return True
                else:
                    return False
        return True
```

**Solution 2: (Two Pointers)**
```
Runtime: 62 ms
Memory Usage: 19.6 MB
```
```c++
class Solution {
public:
    bool validPalindrome(string s) {
        for (int i = 0, j = s.size()-1; i < s.size(); i++, j--) {
            if (s[i] != s[j]) {
                if (isPalindrome(s, i, j-1)) return true;
                return isPalindrome(s, i+1, j);
            }
        }
        return true;
    }
    
    bool isPalindrome(string& s, int l, int r) {
        for (; l < r && s[l] == s[r]; l++, r--);
        return l >= r;
    }
};
```
