542. 01 Matrix

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

**Example 1:**
```
Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
```

**Example 2:**
```
Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
``` 

**Note:**

* The number of elements of the given matrix will not exceed `10,000`.
* There are at least one 0 in the given matrix.
* The cells are adjacent in only four directions: up, down, left and right.

# Solution
---
## Approach #1 Brute force [Time Limit Exceeded]
**Intuition**

Do what the question says.

**Algorithm**

* Initialize `dist[i][j]=INT_MAX` for all `{i,j}` cells.
* Iterate over the matrix.
    * If cell is `0`, `dist[i][j]=0`,
    * Else, for each `1` cell,
        * Iterate over the entire matrix
        * If the cell is `0`, calculate its distance from current cell as `abs(k-i)+abs(l-j)`.
        * If the distance is smaller than the current distance, update it.
        
```c++
vector<vector<int> > updateMatrix(vector<vector<int> >& matrix)
{
    int rows = matrix.size();
    if (rows == 0)
        return matrix;
    int cols = matrix[0].size();
    vector<vector<int> > dist(rows, vector<int>(cols, INT_MAX));
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (matrix[i][j] == 0)
                dist[i][j] = 0;
            else {
                for (int k = 0; k < rows; k++)
                    for (int l = 0; l < cols; l++)
                        if (matrix[k][l] == 0) {
                            int dist_01 = abs(k - i) + abs(l - j);
                            dist[i][j] = min(dist[i][j], abs(k - i) + abs(l - j));
                        }
            }
        }
    }
    return dist;
}
```

**Complexity Analysis**

* Time complexity: $O((r \cdot c)^2)$. Iterating over the entire matrix for each `1` in the matrix.

* Space complexity: $O(r \cdot c)$. No extra space required than the `vector<vector<int> > dist`

## Approach #2 Using BFS [Accepted]
**Intuition**

A better brute force: Looking over the entire matrix appears wasteful and hence, we can use Breadth First Search(BFS) to limit the search to the nearest `0` found for each `1`. As soon as a `0` appears during the BFS, we know that the `0` is nearest, and hence, we move to the next `1`.

Think again: But, in this approach, we will only be able to update the distance of one `1` using one BFS, which could in fact, result in slightly higher complexity than the Approach #1 brute force. But hey,this could be optimised if we start the BFS from `0`s and thereby, updating the distances of all the `1`s in the path.

**Algorithm**

* For our BFS routine, we keep a queue, `q` to maintain the queue of cells to be examined next.
* We start by adding all the cells with `0`s to `q`.
* Intially, distance for each `0` cell is `0` and distance for each `1` is `INT_MAX`, which is updated during the BFS.
* Pop the cell from queue, and examine its neighbours. If the new calculated distance for neighbour `{i,j}` is smaller, we add `{i,j}` to `q` and update `dist[i][j]`.

```c++
vector<vector<int> > updateMatrix(vector<vector<int> >& matrix)
{
    int rows = matrix.size();
    if (rows == 0)
        return matrix;
    int cols = matrix[0].size();
    vector<vector<int> > dist(rows, vector<int>(cols, INT_MAX));
    queue<pair<int, int> > q;
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            if (matrix[i][j] == 0) {
                dist[i][j] = 0;
                q.push({ i, j }); //Put all 0s in the queue.
            }

    int dir[4][2] = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
    while (!q.empty()) {
        pair<int, int> curr = q.front();
        q.pop();
        for (int i = 0; i < 4; i++) {
            int new_r = curr.first + dir[i][0], new_c = curr.second + dir[i][1];
            if (new_r >= 0 && new_c >= 0 && new_r < rows && new_c < cols) {
                if (dist[new_r][new_c] > dist[curr.first][curr.second] + 1) {
                    dist[new_r][new_c] = dist[curr.first][curr.second] + 1;
                    q.push({ new_r, new_c });
                }
            }
        }
    }
    return dist;
}
```

**Complexity analysis**

* Time complexity: $O(r \cdot c)$.

    * Since, the new cells are added to the queue only if their current distance is greater than the calculated distance, cells are not likely to be added multiple times.
* Space complexity: $O(r \cdot c)$. Additional $O(r \cdot c)$ for `queue` than in Approach #1

## Approach #3 DP Approach [Accepted]
**Intuition**

The distance of a cell from `0` can be calculated if we know the nearest distance for all the neighbours, in which case the distance is minimum distance of any neightbour + 1. And, instantly, the word come to mind DP!!
For each `1`, the minimum path to `0` can be in any direction. So, we need to check all the 4 direction. In one iteration from top to bottom, we can check left and top directions, and we need another iteration from bottom to top to check for right and bottom direction.

**Algorithm**

* Iterate the matrix from top to bottom-left to right:
* Update $\text{dist}[i][j]=\min(\text{dist}[i][j],\min(\text{dist}[i][j-1],\text{dist}[i-1][j])+1)$ i.e., minimum of the current dist and distance from top or left neighbour +1, that would have been already calculated previously in the current iteration.
* Now, we need to do the back iteration in the similar manner: from bottom to top-right to left:
* Update $\text{dist}[i][j]=\min(\text{dist}[i][j],\min(\text{dist}[i][j+1],\text{dist}[i+1][j])+1)$ i.e. minimum of current dist and distances calculated from bottom and right neighbours, that would be already available in current iteration.

```c++
vector<vector<int> > updateMatrix(vector<vector<int> >& matrix)
{
    int rows = matrix.size();
    if (rows == 0)
        return matrix;
    int cols = matrix[0].size();
    vector<vector<int> > dist(rows, vector<int>(cols, INT_MAX - 100000));

    //First pass: check for left and top
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (matrix[i][j] == 0)
                dist[i][j] = 0;
            else {
                if (i > 0)
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1);
                if (j > 0)
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1);
            }
        }
    }

    //Second pass: check for bottom and right
    for (int i = rows - 1; i >= 0; i--) {
        for (int j = cols - 1; j >= 0; j--) {
            if (i < rows - 1)
                dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1);
            if (j < cols - 1)
                dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1);
        }
    }

    return dist;
}
```

**Complexity analysis**

* Time complexity: $O(r \cdot c)$. 2 passes of $r \cdot c$ each
* Space complexity: $O(r \cdot c)$. No additional space required than `dist vector<vector<int> >`

# Submissions
---
**Solution 1: (BFS)**
```
Runtime: 852 ms
Memory Usage: 15.8 MB
```
```python
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        R, C = len(matrix), len(matrix[0])
        ans = [[float("inf") if matrix[r][c] == 1 else 0 for c in range(C)] for r in range(R)]
        
        def neighbours(r, c):
            directions = ((r-1, c),(r+1, c),(r, c+1),(r, c-1))
            for nr, nc in directions:
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc
        
        queue = collections.deque([])
        
        for r in range(R):
            for c in range(C):          
                if matrix[r][c] == 0:
                    queue.append((r, c))
                    
        while queue:
            r, c = queue.popleft()
            for nr, nc in neighbours(r, c):
                if ans[nr][nc] > ans[r][c] + 1:
                    ans[nr][nc] = ans[r][c] + 1
                    queue.append((nr, nc))
 
        return ans
```

**Solution 2: (DP)**
```
Runtime: 628 ms
Memory Usage: 15.6 MB
```
```python
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        ## DP
        # upperLeft[r, c] = min(upperLeft[r-1, c], upperLeft[r, c-1]) + 1
        # lowerRight[r, c] = min(lowerRight[r+1, c], lowerRight[r, c+1]) + 1
        # f[r, c] = min(upperLeft[r, c], lowerRight[r, c])

        R, C = len(matrix), len(matrix[0])
        ans = [[float("inf")]*C for _ in range(R)]
        
        # calc upperLeft
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    ans[r][c] = 0
                else:
                    if r > 0:
                        ans[r][c] = min(ans[r][c], ans[r-1][c] + 1)
                    if c > 0:
                        ans[r][c] = min(ans[r][c], ans[r][c-1] + 1)
    
        # calc lowerRight
        for r in range(R-1, -1, -1):
            for c in range(C-1, -1, -1):
                if r+1 < R:
                    ans[r][c] = min(ans[r][c], ans[r+1][c] + 1)
                if c+1 < C:
                    ans[r][c] = min(ans[r][c], ans[r][c+1] + 1)

        return ans
```

**Solution 3: (BFS)**
```
Runtime: 321 ms
Memory Usage: 30.2 MB
```
```c
struct node {
        int x;
        int y;
};

void update_around(int **rt, int h, int w, int x, int y, struct node *q, int *head, int d)
{
        if (x > 0 && rt[x - 1][y] < 0) {
                ++(*head);
                q[*head].x = x - 1;
                q[*head].y = y;
                rt[x - 1][y] = d;
        }
        if (x + 1 < h && rt[x + 1][y] < 0) {
                ++(*head);
                q[*head].x = x + 1;
                q[*head].y = y;
                rt[x + 1][y] = d;
        }
        if (y > 0 && rt[x][y - 1] < 0) {
                ++(*head);
                q[*head].x = x;
                q[*head].y = y - 1;
                rt[x][y - 1] = d;
        }
        if (y + 1 < w && rt[x][y + 1] < 0) {
                ++(*head);
                q[*head].x = x;
                q[*head].y = y + 1;
                rt[x][y + 1] = d;
        }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** updateMatrix(int** mat, int matSize, int* matColSize, int* returnSize, int** returnColumnSizes){
    int i, j;
        int w = matColSize[0];
        int h = matSize;
        
        int **rt = malloc(sizeof(int *) * h); //return matrix initlize to -1
        for (i = 0; i < h; i++) {
                rt[i] = malloc(w * sizeof(int));
                memset(rt[i], 0xff, sizeof(int) * w);
        }
        
        struct node *q = malloc(sizeof(struct node) * 40000);
        int head = -1;
        int tail = -1;
        
        int d = 1;
        for (i = 0; i < h; i++) {
                for (j = 0; j < w; j++) {
                        if (!mat[i][j]) {
                                rt[i][j] = 0;
                                update_around(rt, h, w, i, j, q, &head, d);
                        }
                }
        }
        
        while (tail < head) {
                d++;
                int tmp_head = head;
                int tmp_tail = tail;
                while (++tmp_tail <= tmp_head)
                        update_around(rt, h, w, q[tmp_tail].x, q[tmp_tail].y, q, &head, d);
                tail = tmp_head;
        }
        
        *returnSize = matSize;
        *returnColumnSizes = matColSize;
        return rt;
}
```
