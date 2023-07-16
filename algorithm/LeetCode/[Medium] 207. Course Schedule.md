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
**Solution 3: (BFS, Graph)**
```
Runtime: 30 ms
Memory Usage: 14 MB
```
```c++
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        std::unordered_map<int, std::vector<int>>g;
        std::vector<int> indegree(numCourses, 0);
        for (auto &v: prerequisites) {
            g[v[1]].push_back(v[0]);
            indegree[v[0]] += 1;
        }
        std::queue<int> q;
        for (int i = 0; i < numCourses; i ++) {
            if (indegree[i] == 0)
                q.push(i);
        }
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (auto v: g[u]) {
                indegree[v] -= 1;
                if (indegree[v] == 0)
                    q.push(v);
            }
        }
        return std::all_of(indegree.begin(), indegree.end(), [](int x){return x == 0;});
    }
};
```

**Solution 4: (DFS)**
```
Runtime: 21 ms
Memory: 13.8 MB
```
```c++
class Solution {
    bool dfs(int v, vector<vector<int>> &m, vector<int> &seen) {
        if (seen[v] == -1) {
            return false;
        }
        if (seen[v] == 1) {
            return true;
        }
        seen[v] = -1;
        for (auto &nv: m[v]) {
            if (!dfs(nv, m, seen)) {
                return false;
            }
        }
        seen[v] = 1;
        return true;
    }
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> m(numCourses);
        for (int i = 0; i < prerequisites.size(); i ++) {
            m[prerequisites[i][1]].push_back(prerequisites[i][0]);
        }
        vector<int> seen(numCourses);
        for (int i = 0; i < numCourses; i ++) {
            if (!seen[i]) {
                if (!dfs(i, m, seen)) {
                    return false;
                }
            }
        }
        return all_of(seen.begin(), seen.end(), [](int v){return v == 1;});
    }
};
```
