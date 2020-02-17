547. Friend Circles

There are **N** students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a **direct** friend of B, and B is a **direct** friend of C, then A is an **indirect** friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a **N*N** matrix **M** representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are **direct** friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

**Example 1:**
```
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
```

**Example 2:**
```
Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
```

**Note:**

* `N` is in range `[1,200]`.
* `M[i][i] = 1` for all students.
* If `M[i][j] = 1`, then `M[j][i] = 1`.

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 192 ms
Memory Usage: 13.4 MB
```
```python
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)
        seen = [False]*N
        ans = 0
        
        def dfs(n):
            if seen[n]:
                return
            seen[n]= True
            friend = [f for f, _ in enumerate(M[n]) if _]
            for f in friend:
                if not seen[f] and M[n][f] == 1:
                    dfs(f)
        
        for i in range(N):
            if not seen[i]:
                dfs(i)
                ans += 1
        
        return ans
```

**Solution 2: (Union Find)**
```
Runtime: 220 ms
Memory Usage: 12.8 MB
```
```python
class DSU:
    def __init__(self, N):
        self.p = [_ for _ in range(N)]

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr
        
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)
        dsu = DSU(N)
        for i in range(N):
            for j in range(N):
                if M[i][j] == 1:
                    dsu.union(i, j)
        
        return len(set([dsu.find(i) for i in range(N)]))
```