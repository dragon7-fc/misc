1087. Brace Expansion

You are given a string `s` representing a list of words. Each letter in the word has one or more options.

* If there is one option, the letter is represented as is.
* If there is more than one option, then curly braces delimit the options. For example, `"{a,b,c}"` represents options `["a", "b", "c"]`.

For example, if `s = "a{b,c}"`, the first character is always `'a'`, but the second character can be `'b'` or `'c'`. The original list is `["ab", "ac"]`.

Return all words that can be formed in this manner, **sorted** in lexicographical order.

 

**Example 1:**
```
Input: s = "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]
```

**Example 2:**
```
Input: s = "abcd"
Output: ["abcd"]
```

**Constraints:**

* `1 <= s.length <= 50`
* `s` consists of curly brackets `'{}'`, commas `','`, and lowercase English letters.
* `s` is guaranteed to be a valid input.
* There are no nested curly brackets.
* All characters inside a pair of consecutive opening and ending curly brackets are different.

# Submissions
---
**Solution 1: (Backtracking)**
```
Runtime: 63 ms
Memory Usage: 14.7 MB
```
```python
class Solution:
    def expand(self, s: str) -> List[str]:
        arr = []
        idx = 0
        while idx < len(s):
            sub = []
            if s[idx] == '{':
                while s[idx] != '}':
                    if s[idx].isalpha():
                        sub.append(s[idx])
                    idx += 1
            else:
                sub.append(s[idx])
            
            idx += 1 
            arr.append(sub)
        res = []
        
        def backtrack(idx, res, cur_lst):
            if idx == len(arr):
                res.append(''.join(cur_lst))
                return 

            sub_list = arr[idx]
            for symbol in sub_list:
                backtrack(idx + 1, res, cur_lst + [symbol])
        
        backtrack(0, res, [])
        
        return sorted(res)
```

**Solution 2: (Backtracking)**

    s = "{a,b}c{d,e}f"
               0  1  2
allOptions     a  c  d
               b     e
expandedWords  a  c  dx
               a  c  ex
               b  c  dx
               b  c  ex

```
Runtime: 0 ms, Beats 100.00%
Memory: 12.60 MB, Beats 45.95%
```
```c++
class Solution {
    vector<vector<char>> allOptions;
    
    void storeAllOptions(string& s) {
        for (int pos = 0; pos < s.size(); pos++) {
            vector<char> currOptions;
            
            // If the first character is not '{', it means a single character
            if (s[pos] != '{') {
                currOptions.push_back(s[pos]);
            } else {
                // Store all the characters between '{' and '}'
                while (s[pos] != '}') {
                    if (s[pos] >= 'a' && s[pos] <= 'z') {
                        currOptions.push_back(s[pos]);
                    }
                    pos++;
                }
                // Sort the list
                sort(currOptions.begin(), currOptions.end());
            }
            allOptions.push_back(currOptions);
        }
    }
    
    void generateWords(string currString, vector<string>& expandedWords) {
        // If the currString is complete, we can store and return
        if (currString.size() == allOptions.size()) {
            expandedWords.push_back(currString);
            return;
        }
        
        // Fetch the options for the current index
        vector<char> currOptions = allOptions[currString.size()];

        // Add the character and go into recursion
        for (char c : currOptions) {
            currString += c;
            generateWords(currString, expandedWords);
            // Backtrack to previous state
            currString.pop_back();
        }
    }
public:
    vector<string> expand(string s) {
        // Store the character options for different indices
        storeAllOptions(s);
        
        vector<string> expandedWords;
        generateWords("", expandedWords);
        return expandedWords;
    }
};
```
