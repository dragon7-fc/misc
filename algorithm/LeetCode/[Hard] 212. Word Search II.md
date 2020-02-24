212. Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

**Example:**
```
Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
``` 

**Note:**

* All inputs are consist of lowercase letters `a-z`.
* The values of words are distinct.

# Submissions
---
**Solution 1: (Trie, DFS)**
```
Runtime: 5512 ms
Memory Usage: 23.3 MB
```
```python
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R, C = len(board), len(board[0])
        d = collections.defaultdict(list)
        for r in range(R):
            for c in range(C):
                d[board[r][c]].append((r, c))
        ans = []
        
        def neighbours(r, c):
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc
                    
        def dfs(r, c, node, idx, cands, path):
            if board[r][c] in node:
                letter = board[r][c]
                board[r][c] = ''
                if path in cands and path not in ans:
                    cands.remove(path)
                    ans.append(path)
                if cands:
                    for nr, nc in neighbours(r, c):
                        if board[nr][nc] != '':
                            new_cands = set([cand for cand in cands if len(cand) >= idx+2 and cand[idx+1] == board[nr][nc]])
                            if new_cands:
                                dfs(nr, nc, node[letter], idx+1, new_cands, path + board[nr][nc])
                board[r][c] = letter
     
        trie = {}
        for word in words:
            t = trie
            for c in word:
                t = t.setdefault(c, {})
                
        for k in d:
            cands = set([word for word in words if word[0] == k])
            if cands:
                for r, c in d[k]:
                    dfs(r, c, trie, 0, cands, k)

        return ans
```