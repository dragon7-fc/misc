207. Course Schedule

There are a total of `n` courses you have to take, labeled from `0` to `n-1`.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: `[0,1]`

Given the total number of courses and a list of prerequisite **pairs**, is it possible for you to finish all courses?

**Example 1:**
```
Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
```

**Example 2:**
```
Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
```

**Note:**

* The input `prerequisites` is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
* You may assume that there are no duplicate edges in the input prerequisites.

# Submissions
---
**Solution 1:**
```
Runtime: 104 ms
Memory Usage: 16.3 MB
```
```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {x : [] for x in range(numCourses)}
        visited = {x : 0 for x in range(numCourses)}
        
        for x, y in prerequisites:
            graph[x] += [y]
            
        def dfs(course):
            nonlocal graph, visited
            
            if visited[course] == -1:
                return False
            if visited[course] == 1:
                return True
            
            visited[course] = -1  # start visit
            
            for i in graph[course]:
                if not dfs(i):
                    return False
            
            visited[course] = 1  # end visit
            
            return True
            
        noCycle = all(dfs(i) for i in range(numCourses))
        
        return True if noCycle else False
```