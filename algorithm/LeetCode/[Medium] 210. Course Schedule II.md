210. Course Schedule II

There are a total of `n` courses you have to take, labeled from `0` to `n-1`.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: `[0,1]`

Given the total number of courses and a list of `prerequisite` **pairs**, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

**Example 1:**
```
Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
```

**Example 2:**
```
Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
```

**Note:**

* The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
* You may assume that there are no duplicate edges in the input prerequisites.

# Submissions
---
**Solution 1:**
```
Runtime: 100 ms
Memory Usage: 16 MB
```
```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        visited = collections.defaultdict(int) 
        # visit = -1 currently processing the node 
        # visit = 1 already processed the node
        # visit = 0 node is not processed yet
        ans = []

        for course, dep in prerequisites : 
            graph[course].append(dep)
        
        def is_cycle(course, out):
            nonlocal graph, visited
            if visited[course] == -1 : 
                return True
            if visited[course] == 1 :
                return False
            visited[course] = -1 

            for other in graph[course] : 
                if is_cycle(other, out) :
                    return True

            visited[course] = 1
            out.append(course)  # successfully visited and add to answer (postorder)
        
        for course in range(numCourses):
            if is_cycle(course, ans) :
                return []
        return ans     
```