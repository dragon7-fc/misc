749. Contain Virus

A virus is spreading rapidly, and your task is to quarantine the infected area by installing walls.

The world is modeled as a 2-D array of cells, where `0` represents uninfected cells, and `1` represents cells contaminated with the virus. A wall (and only one wall) can be installed **between any two 4-directionally adjacent cells**, on the shared boundary.

Every night, the virus spreads to all neighboring cells in all four directions unless blocked by a wall. Resources are limited. Each day, you can install walls around only one region -- the affected area (continuous block of infected cells) that threatens the most uninfected cells the following night. There will never be a tie.

Can you save the day? If so, what is the number of walls required? If not, and the world becomes fully infected, return the number of walls used.

**Example 1:**
```
Input: grid = 
[[0,1,0,0,0,0,0,1],
 [0,1,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,0]]
Output: 10
Explanation:
There are 2 contaminated regions.
On the first day, add 5 walls to quarantine the viral region on the left. The board after the virus spreads is:

[[0,1,0,0,0,0,1,1],
 [0,1,0,0,0,0,1,1],
 [0,0,0,0,0,0,1,1],
 [0,0,0,0,0,0,0,1]]

On the second day, add 5 walls to quarantine the viral region on the right. The virus is fully contained.
```

**Example 2:**
```
Input: grid = 
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output: 4
Explanation: Even though there is only one cell saved, there are 4 walls built.
Notice that walls are only built on the shared boundary of two different cells.
```

**Example 3:**
```
Input: grid = 
[[1,1,1,0,0,0,0,0,0],
 [1,0,1,0,1,1,1,1,1],
 [1,1,1,0,0,0,0,0,0]]
Output: 13
Explanation: The region on the left only builds two new walls.
```

**Note:**

* The number of rows and columns of grid will each be in the range `[1, 50]`.
* Each `grid[i][j]` will be either `0` or `1`.
* Throughout the described process, there is always a contiguous viral region that will infect **strictly more** uncontaminated squares in the next round.

# Solution
---
## Approach #1: Simulation [Accepted]
**Intuition**

Let's work on simulating one turn of the process. We can repeat this as necessary while there are still infected regions.

**Algorithm**

Though the implementation is long, the algorithm is straightforward. We perform the following steps:

* Find all viral regions (connected components), additionally for each region keeping track of the frontier (neighboring uncontaminated cells), and the perimeter of the region.

* Disinfect the most viral region, adding it's perimeter to the answer.

* Spread the virus in the remaining regions outward by 1 square.

```python
class Solution(object):
    def containVirus(self, grid):
        R, C = len(grid), len(grid[0])
        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        def dfs(r, c):
            if (r, c) not in seen:
                seen.add((r, c))
                regions[-1].add((r, c))
                for nr, nc in neighbors(r, c):
                    if grid[nr][nc] == 1:
                        dfs(nr, nc)
                    elif grid[nr][nc] == 0:
                        frontiers[-1].add((nr, nc))
                        perimeters[-1] += 1

        ans = 0
        while True:
            #Find all regions, with associated frontiers and perimeters.
            seen = set()
            regions = []
            frontiers = []
            perimeters = []
            for r, row in enumerate(grid):
                for c, val in enumerate(row):
                    if val == 1 and (r, c) not in seen:
                        regions.append(set())
                        frontiers.append(set())
                        perimeters.append(0)
                        dfs(r, c)

            #If there are no regions left, break.
            if not regions: break

            #Add the perimeter of the region which will infect the most squares.
            triage_index = frontiers.index(max(frontiers, key = len))
            ans += perimeters[triage_index]

            #Triage the most infectious region, and spread the rest of the regions.
            for i, reg in enumerate(regions):
                if i == triage_index:
                    for r, c in reg:
                        grid[r][c] = -1
                else:
                    for r, c in reg:
                        for nr, nc in neighbors(r, c):
                            if grid[nr][nc] == 0:
                                grid[nr][nc] = 1

        return ans
```

**Complexity Analysis**

* Time Complexity: $O((R*C)^{\frac{4}{3}})$ where $R, C$ is the number of rows and columns. After time $t$, viral regions that are alive must have size at least $t^2 + (t-1)^2$, so the total number removed across all time is $\Omega(t^3) \leq R*C$.

* Space Complexity: $O(R*C)$ in additional space.

# Submissions
---
**Solution: (Simulation)**
```
Runtime: 172 ms
Memory Usage: 16.3 MB
```
```python
class Solution:
    def containVirus(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        def dfs(r, c):
            if (r, c) not in seen:
                seen.add((r, c))
                regions[-1].add((r, c))
                for nr, nc in neighbors(r, c):
                    if grid[nr][nc] == 1:
                        dfs(nr, nc)
                    elif grid[nr][nc] == 0:
                        frontiers[-1].add((nr, nc))
                        perimeters[-1] += 1

        ans = 0
        while True:
            #Find all regions, with associated frontiers and perimeters.
            seen = set()
            regions = []
            frontiers = []
            perimeters = []
            for r, row in enumerate(grid):
                for c, val in enumerate(row):
                    if val == 1 and (r, c) not in seen:
                        regions.append(set())
                        frontiers.append(set())
                        perimeters.append(0)
                        dfs(r, c)

            #If there are no regions left, break.
            if not regions: break

            #Add the perimeter of the region which will infect the most squares.
            triage_index = frontiers.index(max(frontiers, key = len))
            ans += perimeters[triage_index]

            #Triage the most infectious region, and spread the rest of the regions.
            for i, reg in enumerate(regions):
                if i == triage_index:
                    for r, c in reg:
                        grid[r][c] = -1
                else:
                    for r, c in reg:
                        for nr, nc in neighbors(r, c):
                            if grid[nr][nc] == 0:
                                grid[nr][nc] = 1

        return ans
```

**Solution 2: (DFS)**
```
Runtime: 24 ms
Memory Usage: 9.6 MB
```
```c++
class Solution {
    int dir[4][2] = {
        {-1, 0}, {1, 0}, {0, -1}, {0, 1}  
    };
    int m, n;
public:
    int containVirus(vector<vector<int>>& grid) {
        m = grid.size(), n = grid[0].size();
        int ans = 0;
        unordered_set<int> zeroes;
        int nextStart;
        while((nextStart = markAndGetNextStart(grid, zeroes)) != -1){
            ans += cleanAndWall(grid, nextStart / n, nextStart % n);
            spread(grid);
        }
        return ans;
    }
    
    int markAndGetNextStart(vector<vector<int>>& grid, unordered_set<int>& zeroes){
        int nextStart = -1;
        int nextSaved = 0;
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] != 1) continue;
                zeroes.clear();
                markAndCountZeroes(grid, i, j, zeroes);
                if(zeroes.size() > nextSaved){
                    nextStart = i * n + j;
                    nextSaved = zeroes.size();
                }
            }
        }
        return nextStart;
    }
    
    void markAndCountZeroes(vector<vector<int>>& grid, int i, int j, unordered_set<int>& zeroes){
        grid[i][j] = 2;
        for(int d = 0; d < 4; d++){
            int ni = i + dir[d][0];
            int nj = j + dir[d][1];
            if(ni >= 0 && ni < m && nj >= 0 && nj < n){
                if(grid[ni][nj] <= 0){
                    zeroes.insert(ni * n + nj);
                    grid[ni][nj]--;
                }else if(grid[ni][nj] == 1){
                    markAndCountZeroes(grid, ni, nj, zeroes);
                }
            }
        }
    }
    
    int cleanAndWall(vector<vector<int>>& grid, int i, int j){
        int walls = 0;
        // 3: walled 1's
        grid[i][j] = 3;
        for(int d = 0; d < 4; d++){
            int ni = i + dir[d][0];
            int nj = j + dir[d][1];
            if(ni >= 0 && ni < m && nj >= 0 && nj < n){
                if(grid[ni][nj] <= 0){
                    walls++;
                    grid[ni][nj]++;
                }else if(grid[ni][nj] == 2){
                    walls += cleanAndWall(grid, ni, nj);
                }
            }
        }
        
        return walls;
    }
    
    void spread(vector<vector<int>>& grid){
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] < 0 || grid[i][j] == 2) grid[i][j] = 1;
            }
        }
    }
};
```