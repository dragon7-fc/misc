690. Employee Importance

You are given a data structure of employee information, which includes the employee's **unique id**, his **importance value** and his **direct** subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is **not direct**.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all his subordinates.

**Example 1:**
```
Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
Explanation:
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.
```

**Note:**

* One employee has at most one **direct** leader and may have several subordinates.
* The maximum number of employees won't exceed `2000`.

# Solution
---
## Approach #1: Depth-First Search [Accepted]
**Intuition and Algorithm**

Let's use a hashmap `emap = {employee.id -> employee}` to query employees quickly.

Now to find the total importance of an employee, it will be the importance of that employee, plus the total importance of each of that employee's subordinates. This is a straightforward depth-first search.

```python
class Solution(object):
    def getImportance(self, employees, query_id):
        emap = {e.id: e for e in employees}
        def dfs(eid):
            employee = emap[eid]
            return (employee.importance +
                    sum(dfs(eid) for eid in employee.subordinates))
        return dfs(query_id)
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the number of employees. We might query each employee in dfs.

* Space Complexity: $O(N)$, the size of the implicit call stack when evaluating dfs.

# Submissions
---
**Solution: (DFS)**
```
Runtime: 152 ms
Memory Usage: 13.9 MB
```
```python
"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emap = {e.id: e for e in employees}
        def dfs(eid):
            employee = emap[eid]
            return (employee.importance +
                    sum(dfs(eid) for eid in employee.subordinates))
        return dfs(id)
```

**Solution 2: (BFS)**
```
Runtime: 216 ms
Memory Usage: 13.7 MB
```
```python
"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        ans = 0
        q = collections.deque()
        for e in employees:
            if e.id == id:
                ans += e.importance
                q.append(e.subordinates)
                break
        while(q):
            sub_es = q.popleft()
            for sub_e in sub_es:
                sublist = []
                for e in employees:
                    if e.id == sub_e:
                        ans += e.importance
                        sublist += e.subordinates
                q.append(sublist)
        return ans
```

**Solution 3: (BFS)**
```
Runtime: 32 ms
Memory Usage: 14.5 MB
```
```c++
/*
// Definition for Employee.
class Employee {
public:
    int id;
    int importance;
    vector<int> subordinates;
};
*/

class Solution {
public:
    int getImportance(vector<Employee*> employees, int id) {
        unordered_map<int, pair<int,vector<int>>> g;
        for (auto &e: employees) {
            g[e->id].first = e->importance;
            g[e->id].second = e->subordinates;
        }
        int ans = 0;
        queue<int> q;
        q.push(id);
        while(!q.empty()) {
            int id = q.front();
            q.pop();
            ans += g[id].first;
            for (auto &nid: g[id].second)
                q.push(nid);
        }
        return ans;
    }
};
```

**Solution 4: (DFS)**
```
Runtime: 32 ms
Memory Usage: 14.3 MB
```
```c++
/*
// Definition for Employee.
class Employee {
public:
    int id;
    int importance;
    vector<int> subordinates;
};
*/

class Solution {
    unordered_map<int, pair<int, vector<int>>> g;
public:
    int getImportance(vector<Employee*> employees, int id) {
        for (auto &e: employees) {
            g[e->id].first = e->importance;
            g[e->id].second = e->subordinates;
        }
        int ans = dfs(id);
        return ans;
    }
    
    int dfs(int id) {
        int rst = g[id].first;
        for (auto &nid: g[id].second)
            rst += dfs(nid);
        return rst;
    }
};
```
