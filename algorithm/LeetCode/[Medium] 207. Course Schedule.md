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
**Solution 1: (DFS, Graph)**
```
Runtime: 96 ms
Memory Usage: 15.7 MB
```
```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        seen = [0 for _ in range(numCourses)]
        graph = [[] for i in range(numCourses)]
        for course, pre_course in prerequisites:
            graph[pre_course].append(course)
        def dfs(course: int) -> bool:
            if seen[course] == -1:
                return False
            if seen[course] == 1:
                return True
            seen[course] = -1
            for target in graph[course]:
                if not dfs(target):
                    return False
            seen[course] = 1
            return True
        return all(dfs(course) for course in range(numCourses))
```

**Solution 2: (BFS, Graph)**
```
Runtime: 100 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        indegrees = [0] * numCourses
        for course, pre_course in prerequisites:
            graph[pre_course].append(course)
            indegrees[course] += 1

        queue = collections.deque(course for course, degree in enumerate(indegrees) if not degree)
        while queue:
            course = queue.popleft()
            for next_course in graph[course]:
                indegrees[next_course] -= 1
                if not indegrees[next_course]:
                    queue.append(next_course)

        return not sum(indegrees)
```