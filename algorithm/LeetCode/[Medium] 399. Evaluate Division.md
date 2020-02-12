399. Evaluate Division

Equations are given in the format `A / B = k`, where `A` and `B` are variables represented as strings, and `k` is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return `-1.0`.

**Example:**
Given `a / b = 2.0, b / c = 3.0`.
queries are: `a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?` .
return `[6.0, 0.5, -1.0, 1.0, -1.0 ]`.

The input is: `vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries` , where `equations.size() == values.size()`, and the values are positive. This represents the equations. Return `vector<double>`.

According to the example above:
```
equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
``` 

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
    
# Submissions
---
**Solution 1: (DFS, Backtracking, Graph)**
```
Runtime: 28 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(source,dest,visited,dist):
            if source not in graph or dest not in graph:
                return -1
            visited.append(source)
            if source == dest:
                self.final_value = dist
                return  
            for neighbor,value in graph[source]:
                if neighbor not in visited:
                    dfs(neighbor, dest, visited,dist * value)

        graph = collections.defaultdict(list)
        ## creating the graph for each edge
        for edge , value in zip(equations,values):
            graph[edge[0]].append((edge[1],(value)))
            graph[edge[1]].append((edge[0],(1/value)))
        
        ans = []
        for query in queries:
            self.final_value = -1
            dfs(query[0],query[1],[],1)
            ans.append((self.final_value))
        
        return ans
```

**Solution 2: (DFS, Stack, Graph)**
```
Runtime: 24 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        equ_vals = [(a,b,v) for (a,b), v in zip(equations, values)] + [(b,a,1/v) for (a,b), v in zip(equations, values)]      
        G, res = collections.defaultdict(list), []  # build a Graph such that a ->  a / ...
        for (a,b,v) in equ_vals: 
            G[a].append((a,b,v))
        for (a,b) in queries:
            if a not in G or b not in G:
                res.append(-1)
                continue            
            stack = list(G[a])  # DFS traversal. Use 2 stacks for neighbors and product 
            prods = [1] * len(stack) 
            visits = set()
            while stack:
                (a2,b2,v2) = stack.pop()    
                p = prods.pop()*v2 
                if (a2,b2) in visits:
                    continue   
                if b2 == b: # query found
                    res.append(p)
                    break    
                visits.add((a2,b2)) # DFS... push neighbors and product                               
                stack.extend(G[b2])
                prods.extend([p] * len(G[b2]))            
            else:
                res.append(-1)
        
        return res
```