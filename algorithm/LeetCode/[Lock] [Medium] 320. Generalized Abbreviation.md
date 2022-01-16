320. Generalized Abbreviation

A word's generalized abbreviation can be constructed by taking any number of non-overlapping and non-adjacent substrings and replacing them with their respective lengths.

* For example, `"abcde"` can be abbreviated into:
    * `"a3e"` (`"bcd"` turned into `"3"`)
    * `"1bcd1"` (`"a"` and `"e"` both turned into `"1"`)
    * `"5"` (`"abcde"` turned into `"5"`)
    * `"abcde"` (no substrings replaced)
* However, these abbreviations are invalid:
    * `"23"` (`"ab"` turned into `"2"` and `"cde"` turned into `"3"`) is invalid as the substrings chosen are adjacent.
    * `"22de"` (`"ab"` turned into `"2"` and `"bc"` turned into `"2"`) is invalid as the substring chosen overlap.

Given a string `word`, return a list of all the possible **generalized abbreviations** of `word`. Return the answer in **any order**.

 

**Example 1:**
```
Input: word = "word"
Output: ["4","3d","2r1","2rd","1o2","1o1d","1or1","1ord","w3","w2d","w1r1","w1rd","wo2","wo1d","wor1","word"]
```

**Example 2:**
```
Input: word = "a"
Output: ["1","a"]
```

**Constraints:**

* `1 <= word.length <= 15`
* `word` consists of only lowercase English letters.

# Submissions
---
**Solution 1: (Backtracking)**
```
Runtime: 184 ms
Memory Usage: 21.3 MB
```
```python
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        combinations = []
        
        def backtrack(currentCombination, n):
            if n == len(word):
                combinations.append(''.join(list(currentCombination)))
                return
            
            if len(currentCombination) > 0 and currentCombination[-1].isdigit():
                temp = currentCombination[-1]
                currentCombination[-1] = str(int(currentCombination[-1]) + 1)
                backtrack(currentCombination, n + 1)
                currentCombination[-1] = temp
            else:
                currentCombination.append('1')
                backtrack(currentCombination, n + 1)
                currentCombination.pop()
                
            currentCombination.append(word[n])
            backtrack(currentCombination, n + 1)
            currentCombination.pop()
                        
        backtrack([], 0)
        return combinations
```
