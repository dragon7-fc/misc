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

**Solution 2: (BFS)**
```
Runtime: 4 ms
Memory Usage: 6.9 MB
```
```c
#define max(a,b) ((a)>(b)?(a):(b))
typedef struct  {
    int *begin, *end, size, *front, *back;
} queue;
int maxsize;
queue *que_create(void);
void que_push(queue*, int);
int que_pop(queue*);
int que_isempty(queue*);
void que_resize(queue*);
int que_front(queue*);
queue *que_create(void){
    queue *que = malloc(sizeof(queue));
    que->size = 24;
    que->begin = malloc(sizeof(int) * que->size);
    que->end = que->begin + que->size;
    que->front = que->back = que->begin;
    return que;
}

void que_push(queue* que, int val) {
    *((que->back)++) = val;
    if (que->back == que->end)
        que->back = que->begin;
    if (que->back == que->front)
        que_resize(que);
}

int que_pop(queue* que) {
    int tmp = *(que->front);
    if (++(que->front) == que->end)
        que->front = que->begin;
    return tmp;
}

int que_isempty(queue* que) {
    return que->front == que-> back;
}

void que_resize(queue* que) {
    int frontdis = que->front - que->begin;
    que->begin = realloc(que->begin, sizeof(int) * ((que->size) *= 2));
    que->end = que->begin + que->size;
    que->front = que->begin + frontdis;
    int *s, *t;
    for (s = que->begin, t = s + (que->size / 2); s != que->front;)
        *(t++) = *(s++);
    que->back = t;
}

int que_front(queue* que) {
    return *(que->front);
}
int isnear(char *a, char *b) {
    int count = 0;
    while (*a)
        if (*a++ != *b++)
            ++count;
    return count == 1;
}

typedef struct a{
    int val;
    struct a *next;
}node;

void add_node(node **a,int val) {
    while (*a)
        a = &((*a)->next);
    *a = malloc(sizeof(node));
    (*a)->val = val;
    (*a)->next = NULL;
}
void add_to_list(int ***list, int *listSize, int len, int onesol[]) {
    *list = realloc(*list, sizeof(int*) * (*listSize + 1));
    int *now = (*list)[*listSize] = malloc(sizeof(int) * len);
    for (int i = 0; i < len; ++i)
        now[i] = onesol[i];
    ++(*listSize);
}
void dfs(node **next, int now, int dep, int final, int ***list, int *listSize, int onesol[]) {
    onesol[dep-1] = now; 
    if (dep == final) {
        add_to_list(list, listSize, final, onesol);
        return;
    }
    node * cur= next[now];
    while (cur) {
        dfs(next, cur->val, dep+1, final, list, listSize, onesol);
        cur = cur->next;
    }
}

void push_ans(char****res, char *beginWord, char **words, int wordsSize, int *returnSize, int **returnColomnSizes, int * newsolution, int solen) {
    //resize everything
    if (maxsize == *returnSize + 1) {
        maxsize *= 2;
    *res = realloc(*res, sizeof(char**) * maxsize);
    *returnColomnSizes = realloc(*returnColomnSizes, sizeof(int) * maxsize+100);    
     }
    (*returnColomnSizes)[*returnSize] = solen;
    char **now = (*res)[*returnSize] = malloc(sizeof(char *) * solen);
    now[0] = beginWord;
    for (int i = 1; i<solen; i++)
        now[i] = words[newsolution[i-1]];
    ++(*returnSize);
}

void gene_ans(char****res, char *beginWord, char **words, int wordsSize, int *returnSize, int **returnColomnSizes,
              int l, int lsize, int r, int rsize, node **next) {
    int **listl=NULL, **listr=NULL, listlSize = 0, listrSize = 0;
    int *onesol = malloc(sizeof(int) * max(lsize,rsize));
    int *newsolution = malloc(sizeof(int) * (lsize+rsize));
    dfs(next, l, 1, lsize, &listl, &listlSize, onesol);
    dfs(next, r, 1, rsize, &listr, &listrSize, onesol);
    for (int i = 0; i < listlSize; ++i)
        for (int j = 0; j < listrSize; ++j) {
            int pos = 0;
            for (int k = lsize-1; k>=0; --k,++pos)
                newsolution[pos] = listl[i][k];
            for (int k = 0; k < rsize; ++k,++pos)
                newsolution[pos] = listr[j][k];
            push_ans(res, beginWord, words, wordsSize, returnSize, returnColomnSizes, newsolution, lsize+rsize+1);
        }
    free(onesol); free(newsolution);
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char *** findLadders(char * beginWord, char * endWord, char ** wordList, int wordListSize, int* returnSize, int** returnColumnSizes){
    maxsize = 1;
    char ***res = malloc(0);
    *returnColumnSizes = malloc(0);
    *returnSize = 0;
    // find terminate
    int terminate = -1;
    for (int i = 0; i < wordListSize; ++i)
        if (strcmp(wordList[i], endWord) == 0)
            terminate = i;
    if (terminate == -1)
        return res;
    // list (result)
    node ** next = calloc(wordListSize , sizeof(node*));
    // direct result
    if (isnear(beginWord, endWord)) {
        int *tmp = malloc(sizeof(int));
        tmp[0] = terminate;
        push_ans(&res, beginWord, wordList, wordListSize, returnSize, returnColumnSizes,tmp,2);
        return res;
    }
    // creatqueue;
    queue *que1 = que_create(), *que2 = que_create();
    // status (1 for l, 2 for r, 3 for encounter)
    int *stat = calloc(wordListSize, sizeof(int));
    int *lock = calloc(wordListSize, sizeof(int));
    //push all node near beginword
    for (int i = 0; i < wordListSize; ++i)
        if (isnear(beginWord, wordList[i])) {
            que_push(que1, i);
            stat[i] = 1;
        }
    // push terminate to que2
    que_push(que2, terminate); stat[terminate] = 2;
    que_push(que1, -1); que_push(que2, -1);
    int cur, enconter = 0, lenl = 1, lenr = 1; 
    //till encounter or no path
    while (que_front(que1) != -1 && que_front(que2) != -1) {
        //deal que2
        while ((cur = que_pop(que2)) != -1)  {
            for (int i = 0; i < wordListSize; ++i)
                if (isnear(wordList[i],wordList[cur])) {
                    if (stat[i]==0) {
                        if (!lock[i]) {que_push(que2, i); lock[i] = 1;}
                        add_node(&next[i], cur);
                    }
                    else if (stat[i] == 1) {
                        enconter = 1;
                        gene_ans(&res, beginWord, wordList, wordListSize, returnSize, returnColumnSizes, i, lenl, cur, lenr, next);
                    }
                }
        }
        que_push(que2, -1);
        ++lenr;
        if (enconter)
            return res;
         while ((cur = que_pop(que2))!= -1) {
            stat[cur] = 2;
            que_push(que2, cur);
        }
        que_push(que2, -1);
        //deal que1
        while ((cur = que_pop(que1)) != -1)  {
            for (int i = 0; i < wordListSize; ++i)
                if (isnear(wordList[i],wordList[cur])) {
                    if (stat[i]==0) {
                        if (!lock[i]) {que_push(que1, i); lock[i] = 1;}
                        add_node(&next[i], cur);
                    }
                    else if (stat[i] == 2) {
                        enconter = 1;
                        gene_ans(&res, beginWord, wordList, wordListSize, returnSize, returnColumnSizes, cur, lenl, i, lenr, next);
                        if (*returnSize == 10)
                            return res;
                    }
                }
        }
        que_push(que1, -1);
        ++lenl;
        while ((cur = que_pop(que1))!= -1) {
            stat[cur] = 1;
            que_push(que1, cur);
        }
        if (enconter)
            return res;
        que_push(que1, -1);
    }
    return res;
}
```

**Solution 3: (BFS)**
```
Runtime: 9 ms, Beats 86.98%
Memory: 14.28 MB, Beats 26.29%
```
```c++
class Solution {
    void bt(string u, string &t, vector<string> &p, vector<vector<string>> &ans, unordered_map<string,unordered_set<string>> &g) {
        if (u == t) {
            ans.push_back(vector<string>(p.rbegin(), p.rend()));
            return;
        }
        for (auto &v: g[u]) {
            p.push_back(v);
            bt(v, t, p, ans, g);
            p.pop_back();
        }
    }
public:
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        if (!count(wordList.begin(), wordList.end(), endWord)) {
            return {};
        }
        int n = beginWord.size(), sz, i, j, k = 1;
        char c;
        string nw;
        queue<array<string,2>> q;
        unordered_map<string,int> dist;
        for (auto &w: wordList) {
            dist[w] = INT_MAX;
        }
        unordered_map<string,unordered_set<string>> g;
        vector<vector<string>> ans;
        vector<string> p;
        q.push({beginWord, ""});
        dist[beginWord] = 1;
        g[beginWord].insert("");
        while (q.size() && g[endWord].empty()) {
            sz = q.size();
            for (i = 0; i < sz; i ++) {
                auto [w, p] = q.front();
                q.pop();
                if (w == endWord) {
                    continue;
                }
                for (j = 0; j < n; j ++) {
                    nw = w;
                    for (c = 'a'; c <= 'z'; c ++) {
                        nw[j] = c;
                        if (dist.count(nw)) {
                            if (k+1 < dist[nw]) {
                                q.push({nw, w});
                                dist[nw] = k+1;
                                g[nw].clear();
                                g[nw].insert(w);
                            } else if (k+1 == dist[nw]) {
                                g[nw].insert(w);
                            }
                        }
                    }
                }
            }
            k += 1;
        }
        p.push_back(endWord);
        bt(endWord, beginWord, p, ans, g);
        return ans;
    }
};
```
