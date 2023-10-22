1136. Parallel Courses

There are `N` courses, labelled from 1 to N.

We are given `relations[i] = [X, Y]`, representing a prerequisite relationship between course `X` and course `Y`: course `X` has to be studied before course `Y`.

In one semester you can study any number of courses as long as you have studied all the prerequisites for the course you are studying.

Return the minimum number of semesters needed to study all courses.  If there is no way to study all the courses, return `-1`.

 

**Example 1:**

![1316_ex1.png](img/1316_ex1.png)
```
Input: N = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: 
In the first semester, courses 1 and 2 are studied. In the second semester, course 3 is studied.
```

**Example 2:**

![1316_ex2.png](img/1316_ex2.png)
```
Input: N = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: 
No course can be studied because they depend on each other.
```

**Note:**

* `1 <= N <= 5000`
* `1 <= relations.length <= 5000`
* `relations[i][0] != relations[i][1]`
* There are no repeated relations in the input.

# Submissions
---
**Solution 1: (Topological Sort)**
```
Runtime: 312 ms
Memory Usage: 16.3 MB
```
```python
class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        indeg = [0]*N
        g = collections.defaultdict(list)
        for X, Y in relations:
            g[X-1] += [Y-1]
            indeg[Y-1] += 1
        q = [(i, 1) for i, _ in enumerate(indeg) if _ == 0]
        ans = [0]*N
        while q:
            u, semester = q.pop()
            ans[u] = 1
            if all(ans):
                return semester
            for v in g[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.insert(0, (v, semester+1))
        
        return -1
```

**Solution 2: (Topological Sort)**
```
Runtime: 48 ms
Memory: 26.8 MB
```
```c++
class Solution {
public:
    int minimumSemesters(int n, vector<vector<int>>& relations) {
        vector<int> indeg(n);
        vector<vector<int>> g(n);
        for (auto &vec: relations) {
            g[vec[0]-1].push_back(vec[1]-1);
            indeg[vec[1]-1] += 1;
        }
        queue<int> q;
        int ans = 0, sz;
        vector<int> visited(n);
        for (int i = 0; i < n; i ++) {
            if (indeg[i] == 0) {
                q.push(i);
                visited[i] = true;
            }
        }
        while (!q.empty()) {
            ans += 1;
            sz = q.size();
            for (int i = 0; i < sz; i ++) {
                int v = q.front();
                q.pop();
                for (auto nv: g[v]) {
                    indeg[nv] -= 1;
                    if (indeg[nv] == 0) {
                        q.push(nv);
                        visited[nv] = true;
                    }
                }
            }
        }
        if (any_of(visited.begin(), visited.end(), [](bool v){return v != true;})) {
            return -1;
        }
        return ans;
    }
};
```
