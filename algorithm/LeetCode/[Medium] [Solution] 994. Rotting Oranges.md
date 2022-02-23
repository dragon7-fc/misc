994. Rotting Oranges

In a given grid, each cell can have one of three values:

* the value `0` representing an empty cell;
* the value `1` representing a fresh orange;
* the value `2` representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return `-1` instead.

 

**Example 1:**

![994_oranges.png](img/994_oranges.png)
```
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```

**Example 2:**
```
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
```

**Example 3:**
```
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
```

**Note:**

* `1 <= grid.length <= 10`
* `1 <= grid[0].length <= 10`
* `grid[i][j]` is only `0`, `1`, or `2`.

# Solution
---
## Approach 1: Breadth-First Search
**Intuition**

Every turn, the rotting spreads from each rotting orange to other adjacent oranges. Initially, the rotten oranges have 'depth' 0 [as in the spanning tree of a graph], and every time they rot a neighbor, the neighbors have 1 more depth. We want to know the largest possible depth.

**Algorithm**

We can use a breadth-first search to model this process. Because we always explore nodes (oranges) with the smallest depth first, we're guaranteed that each orange that becomes rotten does so with the lowest possible depth number.

We should also check that at the end, there are no fresh oranges left.

```python
class Solution(object):
    def orangesRotting(self, grid):
        R, C = len(grid), len(grid[0])

        # queue - all starting cells with rotting oranges
        queue = collections.deque()
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c, 0))

        def neighbors(r, c):
            for nr, nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        d = 0
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in neighbors(r, c):
                if A[nr][nc] == 1:
                    A[nr][nc] = 2
                    queue.append((nr, nc, d+1))

        if any(1 in row for row in A):
            return -1
        return d
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the number of cells in the grid.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution: (BFS)**
```
Runtime: 48 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        # queue - all starting cells with rotting oranges
        queue = collections.deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c, 0))

        def neighbors(r, c):
            for nr, nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        d = 0
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d+1))

        if any(1 in row for row in grid):
            return -1
        return d
```

**Solution 2: (BFS)**
```
Runtime: 48 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        # Step 1). build the initial set of rotten oranges
        fresh_oranges = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # Mark the round / level, _i.e_ the ticker of timestamp
        queue.append((-1, -1))

        # Step 2). start the rotting process via BFS
        minutes_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            row, col = queue.popleft()
            if row == -1:
                # We finish one round of processing
                minutes_elapsed += 1
                if queue:  # to avoid the endless loop
                    queue.append((-1, -1))
            else:
                # this is a rotten orange
                # then it would contaminate its neighbors
                for d in directions:
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                    if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            # this orange would be contaminated
                            grid[neighbor_row][neighbor_col] = 2
                            fresh_oranges -= 1
                            # this orange would then contaminate other oranges
                            queue.append((neighbor_row, neighbor_col))

        # return elapsed minutes if no fresh orange left
        return minutes_elapsed if fresh_oranges == 0 else -1
```

**Solution 3: (BFS)**
```
Runtime: 4 ms
Memory Usage: 6.5 MB
```
```c
#define EMPTY 0
#define FRESH 1
#define ROTTEN 2

int directions[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};

typedef struct queue{
    int front;
    int rear;
    int currItemCount;
    int *arrayRow;
    int *arrayCol;
}queue_t;

queue_t *createQueue(int queueSize){
    queue_t *queue = malloc(sizeof(queue_t));
    if(!queue){
        return NULL;
    }
    queue->front = 0;
    queue->rear = -1;
    queue->currItemCount = 0;
    queue->arrayRow = malloc(sizeof(int)*queueSize);
    queue->arrayCol = malloc(sizeof(int)*queueSize);
    if(!queue->arrayRow || !queue->arrayCol){
        return NULL;
    }
    return queue;
}

bool isQueueEmpty(queue_t *queue){
    return queue->currItemCount == 0;
}

void queueEnqueue(queue_t *queue, int rowIdx, int colIdx){
    queue->arrayRow[++queue->rear] = rowIdx;
    queue->arrayCol[queue->rear] = colIdx;
    queue->currItemCount++;
}

int queueDequeueRow(queue_t *queue){
    return queue->arrayRow[queue->front];
}

int queueDequeueCol(queue_t *queue){
    queue->currItemCount--;
    return queue->arrayCol[queue->front++];
}

void freeQueue(queue_t *queue){
    free(queue->arrayRow);
    free(queue->arrayCol);
    free(queue);
}

void printQueue(queue_t *queue, int queueSize){
    printf("Row:    [");
    for(int i=0; i<queueSize; i++){
        printf("%d,",queue->arrayRow[i]);
    }
    printf("]\n");
    printf("Column: [");
    for(int i=0; i<queueSize; i++){
        printf("%d,",queue->arrayCol[i]);
    }
    printf("]\n");
}


int orangesRotting(int** grid, int gridSize, int* gridColSize){
    if((gridSize == 0) || (*gridColSize == 0)){
        return 0;
    }
    
    int numOfRows = gridSize;
    int numOfCols = *gridColSize;
    int freshOranges = 0;
    int queueSize = numOfCols*numOfRows*2;
    
    queue_t *queue = createQueue(queueSize);
    
    for(int i=0; i<numOfRows; i++){
        for(int j=0; j<numOfCols; j++){
            if(grid[i][j] == ROTTEN){
                queueEnqueue(queue, i, j);
            }
            else if(grid[i][j] == FRESH){
                freshOranges++;
            }
        }
    }
    
    queueEnqueue(queue, -1, -1);
    int minutesElapsed = -1;
    // printQueue(queue, numOfRows, numOfCols);
    while(!isQueueEmpty(queue)){
        // printQueue(queue, queueSize);
        int rowIdx = queueDequeueRow(queue);
        int colIdx = queueDequeueCol(queue);
        if(rowIdx == -1){
            minutesElapsed++;
            if(!isQueueEmpty(queue)){
                queueEnqueue(queue, -1, -1);
            }
            // printf("\nAdding -1 again\n");
            // printQueue(queue, queueSize);
        }
        else{
            for(int i=0; i<4; i++){
                int r = rowIdx + directions[i][0];
                int c = colIdx + directions[i][1];
                if(r >= 0 && r < numOfRows && c >= 0 && c < numOfCols){
                    if(grid[r][c] == FRESH){
                        grid[r][c] = ROTTEN;
                        freshOranges--;
                        queueEnqueue(queue, r, c);
                    }
                }
            }
            // printQueue(queue, queueSize);
        }
    }
    
    freeQueue(queue);
    return freshOranges == 0 ? minutesElapsed : -1;
}
```

**Solution 4: (BFS)**
```
Runtime: 3 ms
Memory Usage: 13.1 MB
```
```c++
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m=grid[0].size();
        int n=grid.size();
        int tot=0;
        
       queue<pair<int,int>>q;
        
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(grid[i][j]!=0){tot++;}    // maintaining count of number of total oranges
                if(grid[i][j]==2)
                {
                    q.push({i,j}); // pushing rotten oranges inside queue for out approach
                }
            }
        }
        int cn=0;
        
        int dir[4][2] = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } }; // directions 
        int days=0;
        
        while(q.empty()==false)
        {
            int si=q.size(); // looping till its size
            
            cn+=si; // updating all rotten oranges
            while(si--)
            {
                auto it=q.front();
                q.pop();
                int r=it.first;
                int c=it.second;
                // getting row and col of rotten oranges 
                
                for(int i=0;i<4;i++)  // iterating in all 4 directions 
                {
                    int fir=r+dir[i][0];
                    int sec=c+dir[i][1];
                        
                    // Boundary condition checks
                    
                    if(fir>=0 and fir<n and sec<m and sec>=0 and grid[fir][sec]==1)
                    {
                        grid[fir][sec]=2;
                        q.push({fir,sec});
                    }
                }
            }
            if(!q.empty()){
                
                 days++;            // if size of queue is greater than 0 it means that 
                                    // it still has some oranges to be processed
            } 
        }     
     
        if(cn!=tot) // if not then it means we have still some oranges left
        {
            return -1;
        }
            
        return days;
    }
};
```
