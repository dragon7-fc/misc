245. Shortest Word Distance III

Given a list of `words` and two words `word1` and `word2`, return the shortest distance between these two words in the list.

`word1` and `word2` may be the same and they represent two individual words in the list.

**Example:**
```
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “makes”, word2 = “coding”
Output: 1
Input: word1 = "makes", word2 = "makes"
Output: 3
```

**Note:**

* You may assume `word1` and `word2` are both in the list.

# Submissions
---
**Solution 1: (Array, Hash Table)**
```
Runtime: 56 ms
Memory Usage: 17.4 MB
```
```python
class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        d = collections.defaultdict(list)
        for i, word in enumerate(words):
            if word == word1:
                d[word1] += [i]
            elif word == word2:
                d[word2] += [i]
        
        return min([abs(a-b) for a in d[word1] for b in d[word2] if a != b])
```

**Solution 2: (Array, Greedy)**
```
Runtime: 24 ms
Memory Usage: 11.9 MB
```
```c++
class Solution {
public:
    int shortestWordDistance(vector<string>& words, string word1, string word2) {
        int i = 0;
        int i1, i2; i1 = i2 = -1;
        int dist = INT_MAX;
        bool skipSameWord = false;
        
        for (auto& w : words) {
            
            if (!skipSameWord && w == word1) {
                i1 = i;
                if (word1 == word2) skipSameWord = true;
            }
            else if (w == word2) {
                i2 = i;
                if (word1 == word2) skipSameWord = false;
            }
            
            i++;
            
            if (i1 != -1 && i2 != -1) dist = min(dist, abs(i1-i2));
            
        }//for
        
        return dist;
    }
};
```
