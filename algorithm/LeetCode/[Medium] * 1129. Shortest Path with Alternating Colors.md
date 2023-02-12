1129. Shortest Path with Alternating Colors

Consider a directed graph, with nodes labelled `0, 1, ..., n-1`.  In this graph, each edge is either red or blue, and there could be self-edges or parallel edges.

Each `[i, j]` in `red_edges` denotes a red directed edge from node `i` to node `j`.  Similarly, each `[i, j]` in `blue_edges` denotes a blue directed edge from node `i` to node `j`.

Return an array `answer` of length `n`, where each `answer[X]` is the length of the shortest path from node `0` to node `X` such that the edge colors alternate along the path (or `-1` if such a path doesn't exist).

 

**Example 1:**
```
Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
Output: [0,1,-1]
```

**Example 2:**
```
Input: n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
Output: [0,1,-1]
```

**Example 3:**
```
Input: n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
Output: [0,-1,-1]
```

**Example 4:**
```
Input: n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
Output: [0,1,2]
```

**Example 5:**
```
Input: n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
Output: [0,1,1]
```

**Constraints:**

* `1 <= n <= 100`
* `red_edges.length <= 400`
* `blue_edges.length <= 400`
* `red_edges[i].length == blue_edges[i].length == 2`
* `0 <= red_edges[i][j], blue_edges[i][j] < n`

# Submissions
---
**Solution 1: (BFS, Graph)**
```
Runtime: 88 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        queue = [(0,0,0),(0,1,0)]
        seen = set()
        ans = [-1]*(n)

        graph = collections.defaultdict(list)

        for s,e in red_edges:
            graph[s].append((e,0))
        for s,e in blue_edges:
            graph[s].append((e,1))

        while queue:
            cur, color,depth = queue.pop(0)
            seen.add((cur, color))
            if ans[cur] == -1:
                ans[cur] = depth 
            for nei, nei_color in graph[cur]:
                if nei_color == (1-color):
                    if (nei, nei_color) not in seen:
                        queue.append((nei, nei_color, depth+1))
        return ans
```

**Solution 2: (BFS)**
```
Runtime: 16 ms
Memory Usage: 11.5 MB
```
```c


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* shortestAlternatingPaths(int n, int** redEdges, int redEdgesSize, int* redEdgesColSize, int** blueEdges, int blueEdgesSize, int* blueEdgesColSize, int* returnSize){
    int i, step, size;
    int *answer;
    int **red_table, **blue_table;
	bool visited[n][2];
	int queue[800][2], current[2];
	int front = 0, rear = 0;

    answer = (int*)malloc(sizeof(int)*n);
    for(i=0; i<n; i++)
        answer[i] = -1;

	//Construct the two color visited table
	for(i=0; i<n; i++) {
		visited[i][0] = false;
		visited[i][1] = false;
	}

	//===============================================
	//Set up the red and blue table
    red_table = (int**)malloc(sizeof(int*)*n);
    for(i=0; i<n; i++) {
        red_table[i] = (int*)malloc(sizeof(int)*n);
        memset(red_table[i], 0x0, sizeof(int)*n);
    }

    blue_table = (int**)malloc(sizeof(int*)*n);
    for(i=0; i<n; i++) {
        blue_table[i] = (int*)malloc(sizeof(int)*n);
        memset(blue_table[i], 0x0, sizeof(int)*n);
    }

    for(i=0; i<redEdgesSize; i++)
        red_table[redEdges[i][0]][redEdges[i][1]] = 1;

    for(i=0; i<blueEdgesSize; i++)
        blue_table[blueEdges[i][0]][blueEdges[i][1]] = 1;
	//===============================================

	step = 0;
	// Index 2 record the next one should find on red or blue edges
	// 0: means next to find in red
	// 1: means next to find in blue
	queue[0][0] = 0;
	queue[0][1] = 0;
	front++;
	queue[1][0] = 0;
	queue[1][1] = 1;
	front++;
	while(front != rear)
	{
		size = front - rear;
		while(size-- > 0)
		{
			current[0] = queue[rear][0];
			current[1] = queue[rear][1];
			rear++;

			if(visited[current[0]][current[1]])
				continue;
			visited[current[0]][current[1]] = true;

			if(answer[current[0]] == -1)
				answer[current[0]] = step;

			if(current[1] == 0) {
				for(i=0; i<n; i++) {
					if(red_table[current[0]][i] != 0) {
						queue[front][0] = i;
						queue[front][1] = 1;
						front++;
					}
				}
			} else {
				for(i=0; i<n; i++) {
					if(blue_table[current[0]][i] != 0) {
						queue[front][0] = i;
						queue[front][1] = 0;
						front++;
					}
				}
			}
		}
		step++;
	}

    *returnSize = n;
    return answer;
}
```

**Solution 3: (BFS)**
```
Runtime: 19 ms
Memory: 15.1 MB
```
```c++
class Solution {
public:
    vector<int> shortestAlternatingPaths(int n, vector<vector<int>>& redEdges, vector<vector<int>>& blueEdges) {
        vector<vector<pair<int, int>>> adj(n);
        for (auto& redEdge : redEdges) {
            adj[redEdge[0]].push_back({redEdge[1], 0});
        }
        for (auto& blueEdge : blueEdges) {
            adj[blueEdge[0]].push_back(make_pair(blueEdge[1], 1));
        }

        vector<int> answer(n, -1);
        vector<vector<bool>> visit(n, vector<bool>(2));
        queue<vector<int>> q;

        // Start with node 0, with number of steps as 0 and undefined color -1.
        q.push({0, 0, -1});
        visit[0][1] = visit[0][0] = true;
        answer[0] = 0;

        while (!q.empty()) {
            auto element = q.front();
            int node = element[0], steps = element[1], prevColor = element[2];
            q.pop();

            for (auto& [neighbor, color] : adj[node]) {
                if (!visit[neighbor][color] && color != prevColor) {
                    visit[neighbor][color] = true;
                    q.push({neighbor, 1 + steps, color});
                    if (answer[neighbor] == -1) answer[neighbor] = 1 + steps;
                }
            }
        }
        return answer;
    }
};
```
