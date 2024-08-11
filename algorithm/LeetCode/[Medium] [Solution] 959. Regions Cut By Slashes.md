959. Regions Cut By Slashes

In a N x N `grid` composed of 1 x 1 squares, each 1 x 1 square consists of a `/`, `\`, or blank space.  These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a `\` is represented as `"\\"`.)

Return the number of regions.

 

**Example 1:**
```
Input:
[
  " /",
  "/ "
]
Output: 2
Explanation: The 2x2 grid is as follows:
```

**Example 2:**
```
Input:
[
  " /",
  "  "
]
Output: 1
Explanation: The 2x2 grid is as follows:
```

**Example 3:**
```
Input:
[
  "\\/",
  "/\\"
]
Output: 4
Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)
The 2x2 grid is as follows:
```

**Example 4:**
```
Input:
[
  "/\\",
  "\\/"
]
Output: 5
Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\, and "\\/" refers to \/.)
The 2x2 grid is as follows:
```

**Example 5:**
```
Input:
[
  "//",
  "/ "
]
Output: 3
Explanation: The 2x2 grid is as follows:
```
 

**Note:**

* `1 <= grid.length == grid[0].length <= 30`
* `grid[i][j]` is either `'/'`, `'\'`, or `' '`.

# Solution
---
## Approach 1: Union-Find
**Intuition**

To find the number of components in a graph, we can use either depth-first search or union find. The main difficulty with this problem is in specifying the graph.

One "brute force" way to specify the graph is to associate each grid square with 4 nodes (north, south, west, and east), representing 4 triangles inside the square if it were to have both slashes. Then, we can connect all 4 nodes if the grid square is `" "`, and connect two pairs if the grid square is `"/"` or `""`. Finally, we can connect all neighboring nodes (for example, the east node of the square at `grid[0][0]` connects with the west node of the square at `grid[0][1]`).

This is the most straightforward approach, but there are other approaches that use less nodes to represent the underlying information.

**Algorithm**

Create `4*N*N` nodes, one for each grid square, and connect them as described above. After, we use a union find structure to find the number of connected components.

We will skip the explanation of how a DSU structure is implemented. Please refer to https://leetcode.com/problems/redundant-connection/solution/ for a tutorial on DSU.

```python
class DSU:
    def __init__(self, N):
        self.p = range(N)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

class Solution(object):
    def regionsBySlashes(self, grid):
        N = len(grid)
        dsu = DSU(4 * N * N)
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                root = 4 * (r*N + c)
                if val in '/ ':
                    dsu.union(root + 0, root + 1)
                    dsu.union(root + 2, root + 3)
                if val in '\ ':
                    dsu.union(root + 0, root + 2)
                    dsu.union(root + 1, root + 3)

                # north/south
                if r+1 < N: dsu.union(root + 3, (root+4*N) + 0)
                if r-1 >= 0: dsu.union(root + 0, (root-4*N) + 3)
                # east/west
                if c+1 < N: dsu.union(root + 2, (root+4) + 1)
                if c-1 >= 0: dsu.union(root + 1, (root-4) + 2)

        return sum(dsu.find(x) == x for x in xrange(4*N*N))
```

**Complexity Analysis**

* Time Complexity: $O(N * N * \alpha(N))$, where $N$ is the length of the grid, and $\alpha$ is the Inverse-Ackermann function (if we were to use union-find by rank.)

*Space Complexity: $O(N * N)$.

# Submissions
---
**Solution: (Union-Find, Graph)**
```
Runtime: 344 ms
Memory Usage: 12.9 MB
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
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        dsu = DSU(4 * N * N)
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                root = 4 * (r*N + c)
                if val in '/ ':
                    dsu.union(root + 0, root + 1)
                    dsu.union(root + 2, root + 3)
                if val in '\ ':
                    dsu.union(root + 0, root + 2)
                    dsu.union(root + 1, root + 3)

                # north/south
                if r+1 < N: dsu.union(root + 3, (root+4*N) + 0)
                if r-1 >= 0: dsu.union(root + 0, (root-4*N) + 3)
                # east/west
                if c+1 < N: dsu.union(root + 2, (root+4) + 1)
                if c-1 >= 0: dsu.union(root + 1, (root-4) + 2)

        return sum(dsu.find(x) == x for x in range(4*N*N))
```

**Solution 1: (DFS, Graph)**

Create a graph with 3 times the original grid size. Set to false where the slashes would go. Then it's the same problem as solving the number of islands

```
Runtime: 316 ms
Memory Usage: 15 MB
```
```python
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid) * 3
        big_grid = [[True]*N for _ in range(N)]
        
        for r, row in enumerate(grid):
            for c, char in enumerate(row):
                if char == '/':
                    big_grid[3 * r][(3 * c) + 2] = False
                    big_grid[(3 * r) + 1][(3 * c) + 1] = False
                    big_grid[(3 * r) + 2][3 * c] = False
                elif char == '\\':
                    big_grid[3 * r][3 * c] = False
                    big_grid[(3 * r) + 1][(3 * c) + 1] = False
                    big_grid[(3 * r) + 2][(3 * c) + 2] = False
        
        def dfs(r, c):
            if r >= len(big_grid) or r < 0 or c < 0 or c >= len(big_grid[r]) or big_grid[r][c] == False:
                return

            big_grid[r][c] = False
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c-1)
            dfs(r, c+1)
        
        region_count = 0
        for r in range(len(big_grid)):
            for c in range(len(big_grid)):
                if big_grid[r][c]:
                    region_count += 1
                    dfs(r, c)
                           
        return region_count
```

**Solution 2: (DFS, Stack, Graph)**
```
Runtime: 260 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid) * 3
        big_grid = [[True]*N for _ in range(N)]
        
        for r, row in enumerate(grid):
            for c, char in enumerate(row):
                if char == '/':
                    big_grid[3 * r][(3 * c) + 2] = False
                    big_grid[(3 * r) + 1][(3 * c) + 1] = False
                    big_grid[(3 * r) + 2][3 * c] = False
                elif char == '\\':
                    big_grid[3 * r][3 * c] = False
                    big_grid[(3 * r) + 1][(3 * c) + 1] = False
                    big_grid[(3 * r) + 2][(3 * c) + 2] = False
        
        region_count = 0
        for r0 in range(len(big_grid)):
            for c0 in range(len(big_grid)):
                if big_grid[r0][c0]:
                    region_count += 1
                    stack = [(r0, c0)]
                    big_grid[r0][c0] = False
                    while stack:
                        r, c = stack.pop()
                        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                            if 0 <= nr < N and 0 <= nc < N and big_grid[nr][nc]:
                                stack.append((nr, nc))
                                big_grid[nr][nc] = False
                           
        return region_count
```

**Solution 3: (Union-Find)**
```
Runtime: 8 ms
Memory Usage: 11 MB
```
```c++
class Solution {
public:
    struct disjoint_set {
		vector<int> parent;
		void make_set(int n) {
			for(int i = 0; i <= 4 * n * n + 1; i++) 
				parent.push_back(i);
		}
		int find_parent(int v) {
			if(parent[v] == v) return v;
			return parent[v] = find_parent(parent[v]);
		}
		void union_set(int u, int v) {
			u = find_parent(u);
			v = find_parent(v);
			parent[u] = v;
		}
	};
    int regionsBySlashes(vector<string>& grid) {
        int n = grid.size(), ans = 0;
		disjoint_set dsu; dsu.make_set(n);
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				int x = (i * n + j) * 4;
				if(grid[i][j] == '/') {
					dsu.union_set(x + 1, x + 2);
					dsu.union_set(x + 3, x + 4);
				}
				else if(grid[i][j] == '\\') {
					dsu.union_set(x + 1, x + 4);
					dsu.union_set(x + 2, x + 3);
				}
				else {
					dsu.union_set(x + 1, x + 2);
					dsu.union_set(x + 3, x + 4);
					dsu.union_set(x + 1, x + 4);
				}
				if(j + 1 < n) dsu.union_set(x + 4, x + 6);
				if(i + 1 < n) dsu.union_set(x + 3, ((i + 1) * n + j) * 4 + 1);
			}
		}
		for(int i = 1; i <= 4 * n * n; i++)
			if(dsu.parent[i] == i) ans++;
		return ans;
    }
};
```

**Solution 4: (DFS)**
```
Runtime: 22 ms
Memory Usage: 11.6 MB
```
```c++
class Solution {
public:
    void build(vector<vector<int>>& graph, vector<string>& grid, int n) {
		for(int i = 0; i < n * 3 + 2; i++) 
			graph[0][i] = 1, graph[i][0] = 1, graph[i][n * 3 + 1] = 1, graph[n * 3 + 1][i] = 1;
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				int y = (j + 1) * 3, x = (i + 1) * 3;
				if(grid[i][j] == '/') 
					graph[x - 2][y] = 1, graph[x - 1][y - 1] = 1, graph[x][y - 2] = 1;    
				else if(grid[i][j] == '\\') 
					graph[x - 2][y - 2] = 1, graph[x - 1][y - 1] = 1, graph[x][y] = 1;
			}
		}
	}
	void dfs(int x, int y, vector<vector<int>>& graph) {
		if(graph[x][y] != 0)
			return;
		graph[x][y] = 1;
		dfs(x + 1, y, graph); dfs(x - 1, y, graph); dfs(x, y - 1, graph); dfs(x, y + 1, graph);
	}
    int regionsBySlashes(vector<string>& grid) {
        int n = grid.size();
		vector<vector<int>> graph(n * 3 + 2, vector<int>(n * 3 + 2));
		build(graph, grid, n);
		int ans = 0;
		for(int i = 1; i <= n * 3; i++) {
			for(int j = 1; j <= n * 3; j++) {
				if(graph[i][j] == 0) 
					ans++, dfs(i, j, graph);
			}
		}
		return ans;
    }
};
```

**Solution 5: (Expanded Grid)**
```
Runtime: 18 ms
Memory: 19.40 MB
```
```c++
class Solution {
    // Directions for traversal: right, left, down, up
    const vector<vector<int>> DIRECTIONS = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    // Flood fill algorithm to mark all cells in a region
    void floodFill(vector<vector<int>>& expandedGrid, int row, int col) {
        queue<pair<int, int>> q;
        expandedGrid[row][col] = 1;
        q.push({row, col});

        while (!q.empty()) {
            auto [currentRow, currentCol] = q.front();
            q.pop();
            // Check all four directions from the current cell
            for (const auto& direction : DIRECTIONS) {
                int newRow = direction[0] + currentRow;
                int newCol = direction[1] + currentCol;
                // If the new cell is valid and unvisited, mark it and add to
                // queue
                if (isValidCell(expandedGrid, newRow, newCol)) {
                    expandedGrid[newRow][newCol] = 1;
                    q.push({newRow, newCol});
                }
            }
        }
    }

    // Check if a cell is within bounds and unvisited
    bool isValidCell(const vector<vector<int>>& expandedGrid, int row,
                     int col) {
        int n = expandedGrid.size();
        return row >= 0 && col >= 0 && row < n && col < n &&
               expandedGrid[row][col] == 0;
    }
public:
    int regionsBySlashes(vector<string>& grid) {
        int gridSize = grid.size();
        // Create a 3x3 matrix for each cell in the original grid
        vector<vector<int>> expandedGrid(gridSize * 3,
                                         vector<int>(gridSize * 3, 0));

        // Populate the expanded grid based on the original grid
        // 1 represents a barrier in the expanded grid
        for (int i = 0; i < gridSize; i++) {
            for (int j = 0; j < gridSize; j++) {
                int baseRow = i * 3;
                int baseCol = j * 3;
                // Check the character in the original grid
                if (grid[i][j] == '\\') {
                    // Mark diagonal for backslash
                    expandedGrid[baseRow][baseCol] = 1;
                    expandedGrid[baseRow + 1][baseCol + 1] = 1;
                    expandedGrid[baseRow + 2][baseCol + 2] = 1;
                } else if (grid[i][j] == '/') {
                    // Mark diagonal for forward slash
                    expandedGrid[baseRow][baseCol + 2] = 1;
                    expandedGrid[baseRow + 1][baseCol + 1] = 1;
                    expandedGrid[baseRow + 2][baseCol] = 1;
                }
            }
        }

        int regionCount = 0;
        // Count regions using flood fill
        for (int i = 0; i < gridSize * 3; i++) {
            for (int j = 0; j < gridSize * 3; j++) {
                // If we find an unvisited cell (0), it's a new region
                if (expandedGrid[i][j] == 0) {
                    // Fill that region
                    floodFill(expandedGrid, i, j);
                    regionCount++;
                }
            }
        }
        return regionCount;
    }
};
```

**Solution 6: (Disjoint Set Union (Triangles))**
```
Runtime: 9 ms
Memory: 12.19 MB
```
```c++
class Solution {
    // Calculate the index of a triangle in the flattened array
    // Each cell is divided into 4 triangles, numbered 0 to 3 clockwise from the
    // top
    int getTriangleIndex(int gridSize, int row, int col, int triangleNum) {
        return (gridSize * row + col) * 4 + triangleNum;
    }

    // Union two triangles and return 1 if they were not already connected, 0
    // otherwise
    int unionTriangles(vector<int>& parentArray, int x, int y) {
        int parentX = findParent(parentArray, x);
        int parentY = findParent(parentArray, y);

        if (parentX != parentY) {
            parentArray[parentX] = parentY;
            return 1;  // Regions were merged, so count decreases by 1
        }

        return 0;  // Regions were already connected
    }

    // Find the parent (root) of a set
    int findParent(vector<int>& parentArray, int x) {
        if (parentArray[x] == -1) return x;

        return parentArray[x] = findParent(parentArray, parentArray[x]);
    }
public:
    int regionsBySlashes(vector<string>& grid) {
        int gridSize = grid.size();
        int totalTriangles = gridSize * gridSize * 4;
        vector<int> parentArray(totalTriangles, -1);

        // Initially, each small triangle is a separate region
        int regionCount = totalTriangles;

        for (int row = 0; row < gridSize; row++) {
            for (int col = 0; col < gridSize; col++) {
                // Connect with the cell above
                if (row > 0) {
                    regionCount -= unionTriangles(
                        parentArray,
                        getTriangleIndex(gridSize, row - 1, col, 2),
                        getTriangleIndex(gridSize, row, col, 0));
                }
                // Connect with the cell to the left
                if (col > 0) {
                    regionCount -= unionTriangles(
                        parentArray,
                        getTriangleIndex(gridSize, row, col - 1, 1),
                        getTriangleIndex(gridSize, row, col, 3));
                }

                // If not '/', connect triangles 0-1 and 2-3
                if (grid[row][col] != '/') {
                    regionCount -= unionTriangles(
                        parentArray, getTriangleIndex(gridSize, row, col, 0),
                        getTriangleIndex(gridSize, row, col, 1));
                    regionCount -= unionTriangles(
                        parentArray, getTriangleIndex(gridSize, row, col, 2),
                        getTriangleIndex(gridSize, row, col, 3));
                }

                // If not '\', connect triangles 0-3 and 1-2
                if (grid[row][col] != '\\') {
                    regionCount -= unionTriangles(
                        parentArray, getTriangleIndex(gridSize, row, col, 0),
                        getTriangleIndex(gridSize, row, col, 3));
                    regionCount -= unionTriangles(
                        parentArray, getTriangleIndex(gridSize, row, col, 2),
                        getTriangleIndex(gridSize, row, col, 1));
                }
            }
        }
        return regionCount;
    }
};
```

**Solution 7: (Disjoint Set Union (Graph))**
```
Runtime: 8 ms
Memory: 11.74 MB
```
```c++
class Solution {
    // Find the parent of a set
    int find(vector<int>& parentArray, int node) {
        if (parentArray[node] == -1) return node;

        return parentArray[node] = find(parentArray, parentArray[node]);
    }

    // Union two sets and return 1 if a new region is formed, 0 otherwise
    int union_sets(vector<int>& parentArray, int node1, int node2) {
        int parent1 = find(parentArray, node1);
        int parent2 = find(parentArray, node2);

        if (parent1 == parent2) {
            return 1;  // Nodes are already in the same set, new region formed
        }

        parentArray[parent2] = parent1;  // Union the sets
        return 0;                        // No new region formed
    }
public:
    int regionsBySlashes(vector<string>& grid) {
        int gridSize = grid.size();
        int pointsPerSide = gridSize + 1;
        int totalPoints = pointsPerSide * pointsPerSide;

        // Initialize disjoint set data structure
        vector<int> parentArray(totalPoints, -1);

        // Connect border points
        for (int i = 0; i < pointsPerSide; i++) {
            for (int j = 0; j < pointsPerSide; j++) {
                if (i == 0 || j == 0 || i == pointsPerSide - 1 ||
                    j == pointsPerSide - 1) {
                    int point = i * pointsPerSide + j;
                    parentArray[point] = 0;
                }
            }
        }

        // Set the parent of the top-left corner to itself
        parentArray[0] = -1;
        int regionCount = 1;  // Start with one region (the border)

        // Process each cell in the grid
        for (int i = 0; i < gridSize; i++) {
            for (int j = 0; j < gridSize; j++) {
                // Treat each slash as an edge connecting two points
                if (grid[i][j] == '/') {
                    int topRight = i * pointsPerSide + (j + 1);
                    int bottomLeft = (i + 1) * pointsPerSide + j;
                    regionCount +=
                        union_sets(parentArray, topRight, bottomLeft);
                } else if (grid[i][j] == '\\') {
                    int topLeft = i * pointsPerSide + j;
                    int bottomRight = (i + 1) * pointsPerSide + (j + 1);
                    regionCount +=
                        union_sets(parentArray, topLeft, bottomRight);
                }
            }
        }

        return regionCount;
    }
};
```
