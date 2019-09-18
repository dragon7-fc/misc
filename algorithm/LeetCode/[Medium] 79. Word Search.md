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
**Solution 1:**
```
Runtime: 320 ms
Memory Usage: 15.3 MB
```
```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        N = len(word)
        v = [[0 for _ in range(C)] for _ in range(R)]
        
        def dfs(row, column, index):
            if index == N:
                return True
            elif index < N and not 0 <= row < R or not 0 <= column < C:
                return False
            elif v[row][column]:
                return False
            
            if board[row][column] == word[index]:
                v[row][column] = True
                index += 1
                if dfs(row, column+1, index) or dfs(row+1, column, index) or dfs(row, column-1, index) or dfs(row-1, column, index):
                    return True
                
                v[row][column] = False
                return False
            else:
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

**Solution 2:**
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