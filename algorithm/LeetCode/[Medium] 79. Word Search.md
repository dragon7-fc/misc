79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

**Example:**
```
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
```

# Submissions
---
**Solution 1: (DFS, Backtracking)**
```
Runtime: 324 ms
Memory Usage: 14.8 MB
```
```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        N = len(word)
        v = [[0 for _ in range(C)] for _ in range(R)]

        def neighbours(r, c):
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc
                    
        def dfs(r, c, index):
            v[r][c] = True
            index += 1
            if index == N:
                return True
            for nr, nc in neighbours(r, c):
                if not v[nr][nc] and board[nr][nc] == word[index]:
                    if dfs(nr, nc, index):
                        return True
            v[r][c] = False
            return False

        ans = False
        for i in range(R):
            if word[0] in board[i]:
                for j in range(C):
                    if word[0] == board[i][j]:
                        ans = dfs(i, j, 0)
                        if ans:
                            return True
                        else:
                            continue
        return ans
```

**Solution 2:(DFS, Backtracking, stack)**
```
Runtime: 412 ms
Memory Usage: 30.8 MB
```
```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        N,M=len(board),len(board[0])
        stack=[]
        for i in range(N):
            for j in range(M):
                if board[i][j]==word[0]:
                    stack.append((i,j,0,{(i,j)}))
        while stack:
            i,j,step,visit=stack.pop()
            step+=1
            if step==len(word):
                return True
            for (ni,nj) in [(i+x,j+y) for x,y in [(1,0),(-1,0),(0,1),(0,-1)]]:
                if (ni,nj) not in visit and 0<=ni<N and 0<=nj<M and board[ni][nj] == word[step]:
                    stack.append((ni,nj,step,visit.union({(ni,nj)})))
        return False
```

**Solution 3: (Backtracking)**
```
Runtime: 56 ms
Memory Usage: 11 MB
```
```c++
class Solution {
public:
    bool existUtil(vector<vector<char>>& board,string& word, int i, int j, int curr_word_index){
        if(curr_word_index == word.size()){return true;}
        
        if(i<0 || j<0 || i>=board.size() ||  j>=board[0].size()) {
            return false;
        }
        char ch = word[curr_word_index];

        if(board[i][j]==ch){
            board[i][j]='$';
            if(existUtil(board,word,i+1,j,curr_word_index+1)) return true;
            if(existUtil(board,word,i-1,j,curr_word_index+1)) return true;
            if(existUtil(board,word,i,j+1,curr_word_index+1)) return true;
            if(existUtil(board,word,i,j-1,curr_word_index+1)) return true;
            board[i][j]=ch;
        }
        return false;
    }

    bool exist(vector<vector<char>>& board, string word) {
        for(int i = 0; i< board.size(); i++)
        {
            for(int j = 0; j< board[0].size(); j++)
            {
                if(existUtil(board,word,i,j,0)){
                    return true;
                }
            }
        }
        return false;
    }
};
```

**Solution 4: (Trie)**
```
Runtime: 1101 ms
Memory: 14.1 MB
```
```
board_cnt = collections.Counter(c for r in board for c in r)
        word_cnt = collections.Counter(word)
        if any(word_cnt[k] > board_cnt[k] for k in word_cnt):
            return False
        R, C = len(board), len(board[0])
        trie = {}
        t = trie
        for c in word:
            t = t.setdefault(c, {})
        t["#"] = True
        seen = set()

        def dfs(r, c, t):
            t = t[board[r][c]]
            if '#' in t:
                return True
            seen.add((r, c))
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < R and 0 <= nc < C:
                    if board[nr][nc] in t and not (nr, nc) in seen:
                        if dfs(nr, nc, t):
                            return True
            seen.remove((r, c))
            return False

        for r in range(R):
            for c in range(C):
                if board[r][c] in trie:
                    if dfs(r, c, trie):
                        return True
        return False
```
