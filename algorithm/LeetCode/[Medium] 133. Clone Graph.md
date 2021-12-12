133. Clone Graph

Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (`int`) and a list (`List[Node]`) of its neighbors.

 

**Example:**

![133_clone_graph_question.png](img/133_clone_graph_question.png)
```
Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.
```

**Note:**

* The number of nodes will be between `1` and `100`.
* The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
* Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
* You must return the **copy of the given node** as a reference to the cloned graph.

# Submissions
---
**Solution 1: (DFS, Hash Table)**
```
Runtime: 40 ms
Memory Usage: 13.5 MB
```
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        seen = {}
        
        def dfs(node):
            if node in seen:
                return seen[node]

            new_node = Node(node.val, [])
            seen[node] = new_node
            for nei in node.neighbors:
                new_node.neighbors.append(dfs(nei))
            return new_node
            
        return dfs(node)
```

**Solution 2: (BFS, Hash Table)**
```
Runtime: 32 ms
Memory Usage: 13 MB
```
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        seen = {}
        q = collections.deque([node])
        seen[node] = Node(node.val, [])
        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in seen:
                    seen[nei] = Node(nei.val, [])
                    q.append(nei)
                seen[cur].neighbors.append(seen[nei])
            
        return seen[node]
```

**Solution 3: (DFS, Array)**
```
Runtime: 32 ms
Memory Usage: 14.5 MB
```
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        ans = [Node(_) for _ in range(1, 101)]
        seen = set()
        
        def dfs(src):
            seen.add(src)
            for nei in src.neighbors:
                ans[src.val-1].neighbors += [ans[nei.val-1]]
                if nei not in seen:
                    dfs(nei)

        dfs(node)
        return ans[node.val-1]
```

**Solution 4: (DFS)**
```
Runtime: 8 ms
Memory Usage: 7.1 MB
```
```c
/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     int numNeighbors;
 *     struct Node** neighbors;
 * };
 */
void dfs(struct Node *head, struct Node *s, struct Node** visit){
    head->val = s->val;
    head->numNeighbors = s->numNeighbors;
    visit[s->val] = head;
    if((s->numNeighbors) == 0) return;
    head->neighbors = (struct Node**)malloc(sizeof(struct Node*)*(s->numNeighbors));
    for(int i=0;i<(s->numNeighbors);i++)
        if(visit[s->neighbors[i]->val] == NULL){
            head->neighbors[i] = (struct Node*)malloc(sizeof(struct Node));
            dfs(head->neighbors[i], s->neighbors[i], visit);
        }
        else
            head->neighbors[i] = visit[s->neighbors[i]->val];
    return;
}

struct Node *cloneGraph(struct Node *s) {
	struct Node *head = (struct Node*)malloc(sizeof(struct Node));
    struct Node *visit[101] = {NULL};
    if (s == NULL) return NULL;
    dfs(head, s, visit);
    return head;  
}
```
