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
**Solution 1: (DFS)**
```
Runtime: 5268 ms
Memory Usage: 16.9 MB
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
                    
        def dfs(r, c, idx, visited, cands, path):
            visited[r][c] = True
            if path in cands and path not in ans:
                cands.remove(path)
                ans.append(path)
            if cands:
                for nr, nc in neighbours(r, c):
                    if not visited[nr][nc]:
                        new_cands = set([cand for cand in cands if len(cand) >= idx+2 and cand[idx+1] == board[nr][nc]])
                        if new_cands:
                            dfs(nr, nc, idx+1, visited, new_cands, path + board[nr][nc])
            visited[r][c] = False
     
        for k in d:
            cands = set([word for word in words if word[0] == k])
            if cands:
                for r, c in d[k]:
                    seen = [[False]*C for _ in range(R)]
                    dfs(r, c, 0, seen, cands, k)

        return ans
```

**Solution 2: (Trie, DFS)**
```
Runtime: 3772 ms
Memory: 16.3 MB
```
```python
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R, C = len(board), len(board[0])
        ans = []
        
        def neighbours(r, c):
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc
                    
        def dfs(r, c, node, path):
            letter = board[r][c]
            board[r][c] = ''
            node = node[letter]
            if '#' in node:
                ans.append(path)
                del node['#']
            for nr, nc in neighbours(r, c):
                if board[nr][nc] != '' and board[nr][nc] in node:
                    if len(node[board[nr][nc]]) == 0:
                        del node[board[nr][nc]]
                        continue
                    dfs(nr, nc, node, path + board[nr][nc])
            board[r][c] = letter
     
        trie = {}
        for word in words:
            t = trie
            for c in word + '#':
                t = t.setdefault(c, {})
        for r in range(R):
            for c in range(C):
                if board[r][c] in trie:
                    dfs(r, c, trie, board[r][c])
                

        return ans
```

**Solution 3: (Trie)**
```
Runtime: 88 ms
Memory Usage: 32.6 MB
```
```c++
class Solution {
public:
    struct TrieNode{
        struct TrieNode* child[26];
        bool isEnd;
        int idx;
        TrieNode(){
            isEnd = false;
            idx = -1;
            for(int i=0; i<26; i++)
                child[i] = nullptr;
        }
    };
    
    TrieNode* root;
    vector<string> res;
    
    void addWord(string key, int v) {
        struct TrieNode* curr = root;
        for(int i=0; i<key.size(); i++){
            int idx = key[i]-'a';
            if(!curr->child[idx])
                curr->child[idx] = new TrieNode();
            curr = curr->child[idx];
        }
        curr->isEnd = true;
        curr->idx = v;
    }
    
    void dfs(TrieNode* parent, vector<vector<char>>& board, int i, int j , vector<string>& words){
        if(i<0 || j<0 || i>=board.size() || j>=board[0].size()){
            if(parent->isEnd && parent->idx!=-1){
                res.push_back(words[parent->idx]);
                parent->idx=-1;
            }
            return;
        }
        if(parent->isEnd && parent->idx!=-1){
            res.push_back(words[parent->idx]);
            parent->idx=-1;
        }
        for(int k=0; k<26; k++){
            if(parent->child[k]!=nullptr && (k == (int)(board[i][j]-'a'))){
                board[i][j] = '.';
                dfs(parent->child[k],board,i+1,j,words);
                dfs(parent->child[k],board,i,j+1,words);
                dfs(parent->child[k],board,i-1,j,words);
                dfs(parent->child[k],board,i,j-1,words);
                board[i][j] = (char)(k+'a');
            }
        }
        return;
    }
    
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        root = new TrieNode();
        for(int i=0; i<words.size(); i++)
            addWord(words[i],i);
        for(int i=0; i<board.size(); i++)
            for(int j=0; j<board[0].size();j++)
                dfs(root,board,i,j,words);
        return res;
    }
};
```
