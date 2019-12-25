500. Keyboard Row

Given a List of words, return the words that can be typed using letters of **alphabet** on only one row's of American keyboard like the image below.

![500_keyboard.png](img/500_keyboard.png)
 
**Example:**
```
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
```

**Note:**

* You may use one character in the keyboard more than once.
* You may assume the input string will only contain letters of alphabet.

# Submissions
---
**Solution 1:**
```
Runtime: 28 ms
Memory Usage: 12.6 MB
```
```python
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        raws = [
            ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        ]
        
        ans = []
        
        for word in words:
            r = [0, 0, 0]
            word_l = list(word)
            for char in word_l:
                if char.lower() in raws[0]:
                    r[0] += 1
                elif char in raws[1]:
                    r[1] += 1
                elif char in raws[2]:
                    r[2] += 1
                
            if (r[0] + r[1] == 0) or (r[1] + r[2] == 0) or (r[0] + r[2] == 0):
                ans.append(word)
        
        return ans
```