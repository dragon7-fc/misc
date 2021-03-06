792. Number of Matching Subsequences

Given string `S` and a dictionary of words `words`, find the number of `words[i]` that is a subsequence of `S`.

**Example :**
```
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
```

**Note:**

* All words in `words` and `S` will only consists of lowercase letters.
* The length of `S` will be in the range of `[1, 50000]`.
* The length of `words` will be in the range of `[1, 5000]`.
* The length of `words[i]` will be in the range of `[1, 50]`.

# Submissions
---
**Solution 1: (Rolling Hash)**
```
Runtime: 504 ms
Memory Usage: 15.2 MB
```
```python
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        word_dict = collections.defaultdict(list)
        count = 0
        
        for word in words:
            word_dict[word[0]].append(word)            
        
        for char in S:
            words_expecting_char = word_dict[char]
            word_dict[char] = []
            for word in words_expecting_char:
                if len(word) == 1:
                    # Finished subsequence! 
                    count += 1
                else:
                    word_dict[word[1]].append(word[1:])
        
        return count
```
