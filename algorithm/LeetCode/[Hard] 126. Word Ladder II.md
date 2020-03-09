126. Word Ladder II

Given two words (`beginWord` and `endWord`), and a dictionary's word list, find all shortest transformation sequence(s) from `beginWord` to `endWord`, such that:

1. Only one letter can be changed at a time
1. Each transformed word must exist in the word list. Note that `beginWord` is not a transformed word.

**Note:**

* Return an empty list if there is no such transformation sequence.
* All words have the same length.
* All words contain only lowercase alphabetic characters.
* You may assume no duplicates in the word list.
* You may assume `beginWord` and `endWord` are non-empty and are not the same.

**Example 1:**
```
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
```

**Example 2:**
```
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
```

# Submissions
---
**Solution 1: (BFS)**

Build a graph to store the next possible words from current word.  
The key is a word with a letter masked while the value is a list of words reachable from the key.  
Do BFS from the beginWord.  
Remove every checked word from the wordList to avoid duplicate.  
Iterate all possible next word from the current word based on the graph.  
If that next word is not checked, put it to the next BFS level.  
Use a path_dict to record paths to a word. key is the word, while the value is a list of paths ending at the key.  
Each BFS step will update the path_dict  
Whenever a new word is put into the next BFS level, construct the path to the new word based on paths to the word before it.  

* Time: `O(N*L*W)`  
N is the number of words in wordList; L is the length of words; W is the width of BFS which depends on input.
* Space: `O(N*L+W*L*N)`  
I am not confident about the Time/Space complexity, let me know if you have different answer.

```
Runtime: 264 ms
Memory Usage: 24.7 MB
```
```python
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        if beginWord == endWord:
            return [beginWord]

        g = collections.defaultdict(list)
        N = len(beginWord)
        wordList.append(beginWord)
        for w in wordList:
            for i in range(N):
                wildcast = w[:i] + '*' + w[i+1:]
                g[wildcast].append(w)
                
        path_dict = collections.defaultdict(list)
        path_dict[beginWord] = [[beginWord]]
        level = {beginWord}
        while level:
            next_level = set()
            new_path_dict = collections.defaultdict(list)
            for cur in level:
                wordSet.discard(cur)
                for i in range(N):
                    wildcast = cur[:i] + '*' + cur[i+1:]
                    for nei in g[wildcast]:
                        if nei in wordSet:
                            next_level.add(nei)
                            for pre_path in path_dict[cur]:
                                new_path_dict[nei].append(pre_path+[nei])
            if endWord in new_path_dict:
                return new_path_dict[endWord]
            level = next_level
            path_dict = new_path_dict
        return []
```