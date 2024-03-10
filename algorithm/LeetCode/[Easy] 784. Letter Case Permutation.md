784. Letter Case Permutation

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

**Examples:**
```
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
```

**Note:**

* `S` will be a string with length between `1` and `12`.
* `S` will consist only of letters or digits.

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 68 ms
Memory Usage: N/A
```
```python
class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = ['']
        for ch in S:
            if ch.isalpha():
                res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
            else:
                res = [i+ch for i in res]
                
        return res
```

**Solution 2: (Backtracking)**
```
Runtime: 56 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = []
        def backtrack(i, word):
            if i == len(S):
                ans.append("".join(word))
                return
            if S[i].isalpha():
                backtrack(i+1, word + S[i].lower())
                backtrack(i+1, word + S[i].upper())
            else:
                backtrack(i+1, word + S[i])
        backtrack(0, '') 
        
        return ans
```

**Solution 3: (itertools)**
```
Runtime: 48 ms
Memory Usage: 13.5 MB
```
```python
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        return set(map(''.join, itertools.product(*zip(S.lower(), S.upper()))))
```

**Solution 4: (Backtracking)**
```
Runtime: 8 ms
Memory Usage: 12.4 MB
```
```c++
class Solution {
    vector<string> ans;
    void getCombo(int index, int &n, string &s) {
        if (index == n) {
            ans.push_back(s);
            return;
        }
        
        if (s[index] >= 'a' && s[index] <= 'z') {
            getCombo(index+1, n, s);
            s[index] -= 32;
            getCombo(index+1, n, s);
            s[index] += 32;
            return;
        } else if (s[index] >= 'A' && s[index] <= 'Z') {
            getCombo(index+1, n, s);
            s[index] += 32;
            getCombo(index+1, n, s);
            s[index] -= 32;
            return;
        } else
            getCombo(index+1, n, s);
    }
public:
    vector<string> letterCasePermutation(string s) {
        int n = s.size();
        getCombo(0, n, s);
        return ans;
    }
};
```
