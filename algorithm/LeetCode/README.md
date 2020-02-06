
# Must do questions for a beginner!!

Start with the questions which are tagged easy. Keep a goal of solving 5 questions daily, if you are not able to solve 5 in a day, reduce it to 2-3 questions. In the same way, you can increase the count to 8-10 questions daily. Make sure you remember your approach and try to explore more approaches available for that question.

A must do list according to me:
(these are some of the easy questions - once your solution gets accepted, leetcode shows you suggestion for next similar questions, you can solve them too rather than following this list.)

👉 Save as list to practice these questions
```
#1 Two Sum
#268 Missing Number
#155 Min Stack
#7 Reverse Integer
#20 Valid Paranthesis
#21 Merge two sorted lists
#236 LCA of a binary tree
#189 Rotate array
#112 Path sum
```
(list of medium questions - once you get comfortable with the platform and the questions, you can jump to these questions.)

👉 Save as list to practice these questions
```
#15 3 Sum
#19 Remove Nth node from end of a Linked List
#98 Validate BST
#54 Spiral Matrix
#55 Jump Game
#215 Kth largest element in an array
#56 Merge Intervals
#23 Merge K sorted list
#32 Longest Valid Parantheses
#403 Frog Jump
#239 Sliding Window Maximum
```
(As you are now a pro already, you can jump to the hard questions and do whichever questions you find interesting)

Happy Coding!!

**Similar**

* 207. Course Schedule
* 802. Find Eventual Safe States

**Similar**

* 1143. Longest Common Subsequence
* 1312. Minimum Insertion Steps to Make a String Palindrome

**Note**

* Subarray need to be consecutive。
* Subsequence don't have to be consecutive.

**Libraries**
* library: `itertools`

    * `itertools.groupby(iterable, key=None)`
        
        * ex. [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
        * ex. [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
    * `itertools.product(*iterables, repeat=1)`
    
        * ex. product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
        * ex. product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    * `itertools.permutations(iterable, r=None)`
    
        * ex. permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
        * ex. permutations(range(3)) --> 012 021 102 120 201 210
    * `itertools.combinations(iterable, r)`
        
        * ex. combinations('ABCD', 2) --> AB AC AD BC BD CD
        * ex. combinations(range(4), 3) --> 012 013 023 123
    * `itertools.zip_longest(*iterables, fillvalue=None)`
    
        * ex. zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
* library: `functools`

    * `functools.lru_cache(user_function)`
    * `functools.reduce(function, iterable[, initializer])`

* library: `random`

    * `random.randrange(stop)`
    * `random.randrange(start, stop[, step])`
    * `random.randint(a, b)`
    * `random.uniform(a, b)`
    * `random.choice(seq)`

## Dynamic Programming

**Example 1: (Top-down)**
```python
from functools import lru_cache

class Solution:
    def stoneGame(self, piles):
        N = len(piles)

        @lru_cache(None)
        def dp(i, j):
            # The value of the game [piles[i], piles[i+1], ..., piles[j]].
            if i > j: return 0
            parity = (j - i - N) % 2
            if parity == 1:  # first player
                return max(piles[i] + dp(i+1,j), piles[j] + dp(i,j-1))
            else:
                return min(-piles[i] + dp(i+1,j), -piles[j] + dp(i,j-1))

        return dp(0, N - 1) > 0
```

**Example 2: (Bottom-up)**
```python
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        dp = [[0] * (len(s2) + 1) for _ in xrange(len(s1) + 1)]

        for i in xrange(len(s1) - 1, -1, -1):
            dp[i][len(s2)] = dp[i+1][len(s2)] + ord(s1[i])
        for j in xrange(len(s2) - 1, -1, -1):
            dp[len(s1)][j] = dp[len(s1)][j+1] + ord(s2[j])

        for i in xrange(len(s1) - 1, -1, -1):
            for j in xrange(len(s2) - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j] + ord(s1[i]),
                                   dp[i][j+1] + ord(s2[j]))

        return dp[0][0]
```

**Example 3: (Prefix/Range sum)**
```python
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return

        R = len(matrix)
        C = len(matrix[0])
        self.dp = [[0 for _ in range(C+1)] for _ in range(R+1)]
        for r in range(R):
            for c in range(C):
                self.dp[r + 1][c + 1] = self.dp[r + 1][c] + self.dp[r][c + 1] + matrix[r][c] - self.dp[r][c];

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]
```

**Example 4: (Floyd Warshall's shortest path)**
```python
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dis = [[float('inf')] * n for _ in range(n)]
        for i, j, w in edges:
            dis[i][j] = dis[j][i] = w
        for i in range(n):
            dis[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        res = {sum(d <= distanceThreshold for d in dis[i]): i for i in range(n)}
        return res[min(res)]
```

* [[Medium] [Solution] 877. Stone Game](%5BMedium%5D%20%5BSolution%5D%20877.%20Stone%20Game.md)
* [[Medium] [Solution] 712. Minimum ASCII Delete Sum for Two Strings](%5BMedium%5D%20%5BSolution%5D%20712.%20Minimum%20ASCII%20Delete%20Sum%20for%20Two%20Strings.md)
* [[Medium] [Solution] 304. Range Sum Query 2D - Immutable](%5BMedium%5D%20%5BSolution%5D%20304.%20Range%20Sum%20Query%202D%20-%20Immutable.md)
* [[Medium] 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance](%5BMedium%5D%201334.%20Find%20the%20City%20With%20the%20Smallest%20Number%20of%20Neighbors%20at%20a%20Threshold%20Distance.md)

## Depth-first Search

**Example 1:**
```python
class Solution(object):
    def findRedundantConnection(self, edges):
        graph = collections.defaultdict(set)

        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target: return True
                return any(dfs(nei, target) for nei in graph[source])

        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v):
                return u, v
            graph[u].add(v)
            graph[v].add(u)
```

**Example 2: (Union Find)**
```python
class DSU(object):
    def __init__(self):
        self.par = range(1001)
        self.rnk = [0] * 1001

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True

class Solution(object):
    def findRedundantConnection(self, edges):
        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return edge
```

**Example 3: (DFS, BFS)**
```python
class Solution(object):
    def shortestBridge(self, A):
        R, C = len(A), len(A[0])

        def neighbors(r, c):
            for nr, nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        def get_components():
            done = set()
            components = []
            for r, row in enumerate(A):
                for c, val in enumerate(row):
                    if val and (r, c) not in done:
                        # Start dfs
                        stack = [(r, c)]
                        seen = {(r, c)}
                        while stack:
                            node = stack.pop()
                            for nei in neighbors(*node):
                                if A[nei[0]][nei[1]] and nei not in seen:
                                    stack.append(nei)
                                    seen.add(nei)
                        done |= seen
                        components.append(seen)
            return components

        source, target = get_components()
        queue = collections.deque([(node, 0) for node in source])
        done = set(source)
        while queue:
            node, d = queue.popleft()
            if node in target: return d-1
            for nei in neighbors(*node):
                if nei not in done:
                    queue.append((nei, d+1))
                    done.add(nei)
```

**Exaomple 4: (Cycle)**
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

**Example 5: (connected component)**
```python
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: return -1
        g = [set() for i in range(n)]
        for i, j in connections:
            g[i].add(j)
            g[j].add(i)
        seen = [False] * n
        num_connected_components = 0

        def dfs(i):
            for j in g[i]:
                if not seen[j]:
                    seen[j] = True
                    dfs(j)
        
        for i in range(n):
            if not seen[i]:
                num_connected_components += 1
                seen[i] = True
                dfs(i)
        
        return num_connected_components - 1
```

**Example 6: (2*DFS)**
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        MOD = 10**9 + 7
        self.res = total = 0

        def dfs(node):
            if not node: return 0
            left, right = dfs(node.left), dfs(node.right)
            self.res = max(self.res, left * (total - left), right * (total - right))
            return left + right + node.val

        total = dfs(root)  # get the total sum.
        dfs(root)  # find the biggest product.
        return self.res % MOD
```

**Template 1: (Postorder)**
```python
ans = ...
def dfs(...):
    if not ...:
        return
    ...
    if ...:
        res ...
    return res

XXX = dfs(...)
if XXX:
    ans ...
return ans
```

**Template 2: (Matrix)**
```python
# 1. Check for an empty graph.
if not matrix:
    return []

# 2. Initialize
rows, cols = len(matrix), len(matrix[0])
seen = set()
directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

def dfs(i, j):
    # a. Check if seen
    if (i, j) in seen:
        return
    # b. Else add to seen
    seen.add((i, j))

    # c. Traverse neighbors.
    for direction in directions:
        next_i, next_j = i + direction[0], j + direction[1]
        if 0 <= next_i < rows and 0 <= next_j < cols:
            # d. Add in your question-specific checks.
            dfs(next_i, next_j)

# 3. For each point, traverse it.
for i in range(rows):
    for j in range(cols):
        dfs(i, j)
```

**Template 3: (Cycle)**
```python
seen = [0 for _ in range(N)]
def is_cycle(i):
    if seen[i] == -1:
        return True
    if seen[i] == i:
        return False
    seen[i] = -1
    for j in in i's neighbours:
        if is cycle(j):
            return True
    seen[i] = 1
    return False
for i in range(N):
    if is_cycle(i):
        return True
return False
```

**Template 4: (connected component)**
```python
g = [set() for ...]
for i, j in ...:
    g[i].add(j)
    g[j].add(i)
seen = [False]*N
num_connected_components = 0
def dfs(i):
    for j in g[i]:
        if not seen[j]:
            seen[j] = True
            dfs(j)
for i in range(N):
    if not seen[i]:
        num_connected_components += 1
        seen[i] = True
        dfs(i)

return num_connected_components        
```

* [[Medium] [Solution] 684. Redundant Connection](%5BMedium%5D%20%5BSolution%5D%20684.%20Redundant%20Connection.md)
* [[Medium] [Solution] 934. Shortest Bridge](%5BMedium%5D%20%5BSolution%5D%20934.%20Shortest%20Bridge.md)
* [[Medium] 207. Course Schedule](%5BMedium%5D%20207.%20Course%20Schedule.md)
* [[Medium] 1319. Number of Operations to Make Network Connected](%5BMedium%5D%201319.%20Number%20of%20Operations%20to%20Make%20Network%20Connected.md)
* [[Medium] 1110. Delete Nodes And Return Forest](%5BMedium%5D%201110.%20Delete%20Nodes%20And%20Return%20Forest.md)
* [[Medium] * 450. Delete Node in a BST](%5BMedium%5D%20*%20450.%20Delete%20Node%20in%20a%20BST.md)
* [[Medium] 1343. Maximum Product of Splitted Binary Tree](%5BMedium%5D%201343.%20Maximum%20Product%20of%20Splitted%20Binary%20Tree.md)

## Binary Search

**Example 1:**
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1
```
**Example 2:**
```python
class Solution(object):
    def peakIndexInMountainArray(self, A):
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mi = (lo + hi) / 2
            if A[mi] < A[mi + 1]:
                lo = mi + 1
            else:
                hi = mi
        return lo
```

**Template 1**
```python
def is_XXX(...):
    ...
    
lo, hi = 1, max(piles)
while lo < hi:
    mi = lo + (hi - lo) // 2
    if is_XXX(...):
        lo = mi + 1
    else:
        hi = mi
return lo
```

**Template 2:**
```python
def is_XXX(...):
    ...

lo, hi = ...
while lo <= hi: 
    mi = lo + (hi - lo) // 2
    if is_XXX(mi):
        ans = max(ans, mi)
        lo = mi + 1
    else:
        hi = mi - 1

return ans
```
* library: `bisect`
    * `bisect.bisect_left(a, x, lo=0, hi=len(a))`
        * ex. li = [1, 3, 4, 4, 4, 6, 7], bisect.bisect_left(li, 4) = 2
    * `bisect.bisect_right(a, x, lo=0, hi=len(a))` = `bisect.bisect(a, x, lo=0, hi=len(a))`
        * ex. li = [1, 3, 4, 4, 4, 6, 7], bisect.bisect(li, 4) = 5
* [[Medium] 1300. Sum of Mutated Array Closest to Target](%5BMedium%5D%201300.%20Sum%20of%20Mutated%20Array%20Closest%20to%20Target.md)
* [[Medium] 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold](%5BMedium%5D%201292.%20Maximum%20Side%20Length%20of%20a%20Square%20with%20Sum%20Less%20than%20or%20Equal%20to%20Threshold.md)
* [[Hard] 1231. Divide Chocolate](%5BHard%5D%201231.%20Divide%20Chocolate.md)
* [[Medium] 1201. Ugly Number III](%5BMedium%5D%201201.%20Ugly%20Number%20III.md)
* [[Medium] 1011. Capacity To Ship Packages Within D Days](%5BMedium%5D%201011.%20Capacity%20To%20Ship%20Packages%20Within%20D%20Days.md)
* [[Medium] [Solution] 875. Koko Eating Bananas](%5BMedium%5D%20%5BSolution%5D%20875.%20Koko%20Eating%20Bananas.md)

## Greedy

**Example 1:**
```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        Min, Max = prices[0], 0

        for price in prices:
            profit = price - Min - fee  # max profit = max price - min price
            if profit > 0:  # find max profit
                Max += profit
                Min = price - fee
            elif price < Min:  # find min price
                Min = price


        return Max
```

**Example 2:**
```python
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        sortedA = sorted(A)
        sortedB = sorted(B)

        # assigned[b] = list of a that are assigned to beat b
        # remaining = list of a that are not assigned to any b
        assigned = {b: [] for b in B}
        remaining = []

        # populate (assigned, remaining) appropriately
        # sortedB[j] is always the smallest unassigned element in B
        j = 0
        for a in sortedA:
            if a > sortedB[j]:
                assigned[sortedB[j]].append(a)
                j += 1
            else:
                remaining.append(a)

        # Reconstruct the answer from annotations (assigned, remaining)
        return [assigned[b].pop() if assigned[b] else remaining.pop()
                for b in B]
```

**Template 1:**
```python
ans = []
A.sort()
for i in ragen(len(A)):
    if /* max profit */:
        ans += ...
        
return ans
```

* [[Medium] [Solution] 714. Best Time to Buy and Sell Stock with Transaction Fee](%5BMedium%5D%20%5BSolution%5D%20714.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock%20with%20Transaction%20Fee.md)
* [[Medium] [Solution] 767. Reorganize String](%5BMedium%5D%20%5BSolution%5D%20767.%20Reorganize%20String.md)
* [[Medium] [Solution] 738. Monotone Increasing Digits](%5BMedium%5D%20%5BSolution%5D%20738.%20Monotone%20Increasing%20Digits.md)
* [[Easy] [Solution] 874. Walking Robot Simulation](%5BEasy%5D%20%5BSolution%5D%20874.%20Walking%20Robot%20Simulation.md)
* [[Medium] [Solution] 870. Advantage Shuffle](%5BMedium%5D%20%5BSolution%5D%20870.%20Advantage%20Shuffle.md)
* [[Medium] [Solution] 376. Wiggle Subsequence](%5BMedium%5D%20%5BSolution%5D%20376.%20Wiggle%20Subsequence.md)
* [[Medium] [Solution] 55. Jump Game](%5BMedium%5D%20%5BSolution%5D%2055.%20Jump%20Game.md)
* [[Medium] * 1111. Maximum Nesting Depth of Two Valid Parentheses Strings](%5BMedium%5D%20*%201111.%20Maximum%20Nesting%20Depth%20of%20Two%20Valid%20Parentheses%20Strings.md)

## Breadth-first Search

**Example 1:**
```python
from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


        # Queue for BFS
        queue = collections.deque([(beginWord, 1)])
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()      
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0
```

**Example 2: (Level order)**
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        level = root and [root]
        while level:
            ans.append([node.val for node in level])
            level = [c for node in level for c in node.children if c]
        return ans
```

**Example 3: (Dijkstra's Algorithm)**
```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, K)]  # distance, node
        # heapq.heapify(pq)
        dist = {}  # visited node -> distance
        while pq:
            d, node = heapq.heappop(pq)  # get next smallest distance node
            if node in dist: continue
            dist[node] = d
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d+d2, nei))  # append neighbor un-visited node

        return max(dist.values()) if len(dist) == N else -1
```

**Example 4: (Bipartite)**
```python
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}

        for from_node in range(len(graph)):
            if from_node in colors:
                continue
            queue = collections.deque([from_node])
            colors[from_node] = 1 # 1 is just starting color, could be -1 also

            while queue:
                from_node = queue.popleft()
                for to_node in graph[from_node]:
                    if to_node in colors:
                        if colors[to_node] == colors[from_node]:
                            return False
                    else:
                        queue.append(to_node)
                        colors[to_node] = colors[from_node] * -1

        return True
```

**Example 5: (Matrix)**
```python
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        R, C = len(board), len(board[0])
        visited = set()

        def neighbours(r, c):
            directions = ((r-1, c),(r+1, c),(r, c+1),(r, c-1),
                          (r+1, c+1),(r-1, c-1),(r-1, c+1),(r+1, c-1)
                         )
            for nr, nc in directions:
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        queue = collections.deque([click])
        while queue:
            (r, c) = queue.popleft()
            if (r, c) in visited:
                continue
            if board[r][c] == 'M':
                board[r][c] = 'X'
            else:
                count = 0
                for nr, nc in neighbours(r, c):
                    if board[nr][nc] in 'MX':
                        count += 1
                board[r][c] = 'B' if count == 0 else str(count)
            visited.add((r, c))
            if board[r][c] == 'B':
                for nr, nc in neighbours(r, c):
                    queue.append([nr, nc])

        return board
```

**Template 1:**
```python
seen = [False ...]
q = collections.deque([...])
seen[(...)] = True
while q:
    el = q.popleft()
    ...
    ans ...
    for nei in el's neighbours:
        if not seen[nei]:
            q.append(nei)
            seen[nei] = True
return ans
```

**Template 2:**
```python
q = collections.deque([..., 1])
grid[...] = 1
while q:
    r, c step in q.popleft():
    if ...:
        return step
    for nr, nc in (r, c)'s neighbours:
        if not grid[nr][nc]:
            grid[nr][nc] = 1
            q.append((nr, nc, step+1))
return -1
```

**Template 3:**
```python
q = collections.deque([..., 1])
seen = ((...))
step = 0
while q:
    for _ in range(len(q)):
        r, c = q.popleft()
        if ...:
            return step
        for nr, nc in (r, c)'s neighbours:
            if (nr, nc) not in seen:
                q.append((nr, nc))
                seen.add((nr, nc))
    step += 1
return -1
```

* [[Medium] [Solution] 127. Word Ladder](%5BMedium%5D%20%5BSolution%5D%20127.%20Word%20Ladder.md)
* [[Medium] 429. N-ary Tree Level Order Traversal](%5BMedium%5D%20429.%20N-ary%20Tree%20Level%20Order%20Traversal.md)
* [[Medium] [Solution] 743. Network Delay Time](%5BMedium%5D%20%5BSolution%5D%20743.%20Network%20Delay%20Time.md)
* [[Medium] 785. Is Graph Bipartite?](%5BMedium%5D%20785.%20Is%20Graph%20Bipartite?.md)
* [[Medium] 529. Minesweeper](%5BMedium%5D%20529.%20Minesweeper.md)
* [[Medium] * 1129. Shortest Path with Alternating Colors](%5BMedium%5D%20*%201129.%20Shortest%20Path%20with%20Alternating%20Colors.md)

## Two pointer

**Example 1: (Cycle)**
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
```

**Example 2: (Cycle entrance)**
```python
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Find the intersection point of the two runners.
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Find the "entrance" to the cycle.
        ptr1 = nums[0]
        ptr2 = tortoise
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1
```

**Example 3: (Sliding window, Two pointer, iterate right pointer)**
```python
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans             
```

**Example 4: (Greedy, Two pointer, iterate left pointer)**
```python
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
            
        return ans
```

**Example 5: (Two pointer, iterate left and right pointer)**
```python
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]

        ans = list(dominoes)
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            if x == y:
                for k in range(i+1, j):
                    ans[k] = x
            elif x > y: #RL
                for k in range(i+1, j):
                    ans[k] = '.LR'[(k-i > j-k) - (k-i < j-k)]

        return "".join(ans)
```

**Example 6: (Two pointer, iterate left and right pointer with yield)**
```python
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))
```

**Example 7: (Three pointer)**
```python
class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        MOD = 10**9 + 7
        count = collections.Counter(A)
        keys = sorted(count)

        ans = 0

        # Now, let's do a 3sum on "keys", for i <= j <= k.
        # We will use count to add the correct contribution to ans.
        for i, x in enumerate(keys):
            T = target - x
            j, k = i, len(keys) - 1
            while j <= k:
                y, z = keys[j], keys[k]
                if y + z < T:
                    j += 1
                elif y + z > T:
                    k -= 1
                else: # x+y+z == T, now calculate the size of the contribution
                    if i < j < k:
                        ans += count[x] * count[y] * count[z]
                    elif i == j < k:
                        ans += count[x] * (count[x] - 1) // 2 * count[z]
                    elif i < j == k:
                        ans += count[x] * count[y] * (count[y] - 1) // 2
                    else:  # i == j == k
                        ans += count[x] * (count[x] - 1) * (count[x] - 2) // 6

                    j += 1
                    k -= 1

        return ans % MOD
```

**Example 8: (Group into Blocks)**
```python
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        g1 = [(k, len(list(grp))) for k, grp in itertools.groupby(name)]
        g2 = [(k, len(list(grp))) for k, grp in itertools.groupby(typed)]
        if len(g1) != len(g2):
            return False

        return all(k1 == k2 and v1 <= v2
                   for (k1,v1), (k2,v2) in zip(g1, g2))
```

**Solution 9: (Three pointer)**
```python
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        i_lo = i_hi = 0
        sum_lo = sum_hi = 0
        ans = 0
        for j, x in enumerate(A):
            # Maintain i_lo, sum_lo:
            # While the sum is too big, i_lo += 1
            sum_lo += x
            while i_lo < j and sum_lo > S:
                sum_lo -= A[i_lo]
                i_lo += 1

            # Maintain i_hi, sum_hi:
            # While the sum is too big, or equal and we can move, i_hi += 1
            sum_hi += x
            while i_hi < j and (
                    sum_hi > S or sum_hi == S and not A[i_hi]):
                sum_hi -= A[i_hi]
                i_hi += 1

            if sum_lo == S:
                ans += i_hi - i_lo + 1

        return ans
```

**Example 10: (Two pointer, Counter)**
```python
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        ans = i = 0
        count = collections.Counter()
        for j, x in enumerate(tree):
            count[x] += 1
            while len(count) >= 3:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
            ans = max(ans, j - i + 1)
        return ans
```

**Example 11: (Four pointer)**
```python
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        arr = [-1] + [i for i, num in enumerate(nums) if num & 1] + [len(nums)]
        return sum([(s - r) * (u - t) for r, s, t, u in zip(
            arr,
            arr[1:],
            arr[k:],
            arr[k+1:]
        )])
```

**Template 1: (Linked list)**
```python
dummy = ListNode(0)
dummy.next = head
first = second = dummy
...
while ...:
    first = ....
    second = ...
...
return dummy.next
```

**Template 2: (Sliding window)**
```python
left, right = 0, N-1
while left < right:
    while ...:
        left += 1
    while ...:
        right -= 1
    ans = ...left...right...
    
return ans
```

**Template 3: (Sliding window)**
```python
i = 0
count = collections.Counter(nums)
for j, x in enumerate(N):
    count[x] += 1
    while ...:
        count[nums[i]] -= 1
        if count[nums[i]] == 0:
            del count[i]
        i += 1
    ans = max(ans, j - i + 1)

return ans
```

**Template 4: (Two pointer, Binary search)**
```python
for i in range(N):
    left, right = i+1, N-1
    while left < right:
        if ...[left] + ...[right] == target:
            ans = max(ans, right - left + 1)
        elif ...[left] + ...[right] < target:
            left += 1
        elif ...[left] + ...[right] > target:
            right -= 1

return ans
```

* [[Easy] [Solution] 141. Linked List Cycle](%5BEasy%5D%20%5BSolution%5D%20141.%20Linked%20List%20Cycle.md)
* [[Medium] [Solution] 287. Find the Duplicate Number](%5BMedium%5D%20%5BSolution%5D%20287.%20Find%20the%20Duplicate%20Number.md)
* [[Medium] [Solution] 713. Subarray Product Less Than K](%5BMedium%5D%20%5BSolution%5D%20713.%20Subarray%20Product%20Less%20Than%20K.md)
* [[Medium] [Solution] 763. Partition Labels](%5BMedium%5D%20%5BSolution%5D%20763.%20Partition%20Labels.md)
* [[Medium] [Solution] 838. Push Dominoes](%5BMedium%5D%20%5BSolution%5D%20838.%20Push%20Dominoes.md)
* [[Easy] [Solution] 844. Backspace String Compare](%5BEasy%5D%20%5BSolution%5D%20844.%20Backspace%20String%20Compare.md)
* [[Medium] [Solution] 923. 3Sum With Multiplicity](%5BMedium%5D%20%5BSolution%5D%20923.%203Sum%20With%20Multiplicity.md)
* [[Easy] [Solution] 925. Long Pressed Name](%5BEasy%5D%20%5BSolution%5D%20925.%20Long%20Pressed%20Name.md)
* [[Medium] [Solution] 930. Binary Subarrays With Sum](%5BMedium%5D%20%5BSolution%5D%20930.%20Binary%20Subarrays%20With%20Sum.md)
* [[Medium] [Solution] 904. Fruit Into Baskets](%5BMedium%5D%20%5BSolution%5D%20904.%20Fruit%20Into%20Baskets.md)
* [[Medium] 1248. Count Number of Nice Subarrays](%5BMedium%5D%201248.%20Count%20Number%20of%20Nice%20Subarrays.md)

## Stack
**Example 1: (PreOrder)**
```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        preorder, stack = [], [(root, False)]
        while stack:
            (node, visited) = stack.pop()
            if not node:
                continue
            if visited:
                preorder.append(node.val)
            else:
                stack.append((node.right, False))
                stack.append((node.left, False))
                stack.append((node, True))
        return preorder
```

**Example 2: (InOrder)**
```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        inorder, stack = [], [(root, False)]
        while stack:
            (node, visited) = stack.pop()
            if node:
                if visited:
                    inorder.append(node.val)
                else:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return inorder
```
**Example 3: (PostOrder)**
```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        postorder, stack = [], [(root, False)]
        while stack:
            (node, visited) = stack.pop()
            if node:
                if visited:
                    postorder.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return postorder
```

**Example 4: (Stack, Hash table)**
```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': operator.add, 
            '-': operator.sub, 
            '*': operator.mul, 
            '/': operator.truediv
        }
        stack = []
        for token in tokens:
            if token in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(int(ops[token](a, b)))
            else:
                stack.append(int(token))
        
        return stack.pop()
```

**Example 5:**
```python
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        stack.append(["", 1])
        num = ""
        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == '[':
                stack.append(['', int(num)])
                num = ''
            elif ch.isalpha():
                stack[-1][0] += ch
            elif ch == ']':
                st, k = stack.pop()
                stack[-1][0] += st*k
        return stack[0][0]
```

**Example 6: (Preprocessing, stack maintain variance from right)**
```python
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        N = len(nums)
        if N < 3:
            return False
        stack = []
        mi = [None]*N
        mi[0] = nums[0]
        for i in range(1, N):
            mi[i] = min(mi[i-1], nums[i])
        for j in range(N-1, -1, -1):
            if nums[j] > mi[j]:
                while stack and stack[-1] <= mi[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])

        return False
```

**Exaomple 7: (weighted stack)**
```python
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        weight = 1
        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]
        self.stack.append((price, weight))
        return weight


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
```

**Example 8: (Maintain Stack of Minimums)**
```python
class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        MOD = 10**9 + 7

        stack = []
        ans = dot = 0
        for j, y in enumerate(A):
            # Add all answers for subarrays [i, j], i <= j
            count = 1
            while stack and stack[-1][0] >= y:
                x, c = stack.pop()
                count += c
                dot -= x * c

            stack.append((y, count))
            dot += y * count
            ans += dot
        return ans % MOD
```

**Example 9: (Greedy, Stack simulation)**
```python
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return j == len(popped)
```

**Example 10: (Heap)**
```python
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        cost, heap = 0, [float('inf')]
        for leaf in arr:
            while heap[0] < leaf: # join the cheapest possible leaves
                cost += heapq.heappop(heap) * min(leaf, heap[0])
            heapq.heappush(heap, leaf)
        while len(heap) > 2: # no choice but to join the remaining leaves
            cost += heapq.heappop(heap) * heap[0]
        return cost
```

**Template 1:**
```python
stack = []
ans = 0
for ...:
    while stack and stack[-1]...:
        stack.pop()
    ...
    ans = ...
    stack.append(...)

return ans
```

* [[Medium] 150. Evaluate Reverse Polish Notation](%5BMedium%5D%20150.%20Evaluate%20Reverse%20Polish%20Notation.md)
* [![Medium] 394. Decode String](!%5BMedium%5D%20394.%20Decode%20String.md)
* [[Medium] [Solution] 456. 132 Pattern](%5BMedium%5D%20%5BSolution%5D%20456.%20132%20Pattern.md)
* [[Medium] [Solution] 503. Next Greater Element II](%5BMedium%5D%20%5BSolution%5D%20503.%20Next%20Greater%20Element%20II.md)
* [[Medium] [Solution] 636. Exclusive Time of Functions](%5BMedium%5D%20%5BSolution%5D%20636.%20Exclusive%20Time%20of%20Functions.md)
* [[Medium] [Solution] 901. Online Stock Span](%5BMedium%5D%20%5BSolution%5D%20901.%20Online%20Stock%20Span.md)
* [[Medium] [Solution] 907. Sum of Subarray Minimums](%5BMedium%5D%20%5BSolution%5D%20907.%20Sum%20of%20Subarray%20Minimums.md)
* [[Medium] [Solution] 946. Validate Stack Sequences](%5BMedium%5D%20%5BSolution%5D%20946.%20Validate%20Stack%20Sequences.md)
* [[Medium] 1130. Minimum Cost Tree From Leaf Values](%5BMedium%5D%201130.%20Minimum%20Cost%20Tree%20From%20Leaf%20Values.md)

## Backtracking

**Example 1: (combination, Hash table)**
```python
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map 
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])

        output = []
        if digits:
            backtrack("", digits)
        return output
```

**Example 2: (permutation)**
```python
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(path):
            if len(path) == len(nums):
                ans.append(path)
                return
            for num in nums:
                if num not in path:
                    backtrack(path + [num])
        ans = []
        backtrack([])

        return ans
```

**Example 3: (subset)**
```python
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
```

**Example 4: (Trie)**
```python
class Node:
    def __init__(self):
        self.sub = collections.defaultdict(Node)
        self.isend = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for i in word: cur = cur.sub[i]
        cur.isend = True
        
    def searchnode(self, word: str, st, node) -> bool:
        for i in range(st, len(word)):
            if word[i] == '.':
                for n in node.sub.values():
                    if self.searchnode(word, i+1, n): return True
                return False
            else:
                node = node.sub.get(word[i], None)
                if node is None: return False
        return node and node.isend

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.searchnode(word, 0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```

**Example 5: (count)**
```python
class Solution:
    def countArrangement(self, N: int) -> int:
        def calculate(pos):
            nonlocal count
            if pos > N:
                count += 1
            for i in range(1, N+1):
                if not visited[i] and (pos % i == 0 or i % pos == 0):
                    visited[i] = True
                    calculate(pos + 1)
                    visited[i] = False
        count = 0
        visited = [False] * (N+1)
        calculate(1)
        
        return count
```

**Example 6: (partition)**
```python
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        def backtrack(seq, path):
            if self.res:
                return
            if not seq and len(path) > 2:
                self.res = path
                return
            for i in range(len(seq)):
                if seq.startswith('0') and i > 0:
                    break
                if int(seq[:i+1]) > 2**31-1:
                    break
                if len(path) < 2 or (len(path) >= 2 and int(seq[:i+1]) == int(path[-1])+int(path[-2])):
                    path.append(seq[:i+1])
                    backtrack(seq[i+1:], path[:])
                    path.pop()
        if not S:
            return None

        self.res = None
        backtrack(S, [])

        return self.res
```

**Template 1:**
```python
ans = []
def backtrack(index, path):
    if ...:
        ans.append(path)
        return
    for i in range(index, N):
        if ...:
            path.append(...)
            backtrack(i+1, path + ...[i])
            path.pop()
backtrack(0, [])
return ans
```

**Template 2:**
```python
ans = []
seen = [False]*N
def backtrack(...):
    if ...:
        ans.append(...)
        return
    for i in range(...):
        if not seen[i]:
            seen[i] = True
            backtrack(...)
            seen[i] = False
backtrack(...)
return ans
```

* [[Medium] [Solution] 17. Letter Combinations of a Phone Number](%5BMedium%5D%20%5BSolution%5D%2017.%20Letter%20Combinations%20of%20a%20Phone%20Number.md)
* [[Medium] 46. Permutations](%5BMedium%5D%2046.%20Permutations.md)
* [[Medium] [Solution] 78. Subsets](%5BMedium%5D%20%5BSolution%5D%2078.%20Subsets.md)
* [[Medium] 211. Add and Search Word - Data structure design](%5BMedium%5D%20211.%20Add%20and%20Search%20Word%20-%20Data%20structure%20design.md)
* [[Medium] [Solution] 526. Beautiful Arrangement](%5BMedium%5D%20%5BSolution%5D%20526.%20Beautiful%20Arrangement.md)
* [[Medium] [Solution] 842. Split Array into Fibonacci Sequence](%5BMedium%5D%20%5BSolution%5D%20842.%20Split%20Array%20into%20Fibonacci%20Sequence.md)

## Bit
---
**Example: (Gray code)**
```python
def binaryToGray(self, n: int) -> int:
    return n ^ (n >> 1)
```

**Example 1: (Subsets)**
```python
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        output = []

        for i in range(2**n, 2**(n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]

            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])

        return output
```

**Example 2: (Single number)**
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a
```

**Example 3: (Number of 1 bits)**
```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n != 0:
            ans += 1
            n &= (n - 1)

        return ans
```

**Example 4: (Missing Number)**
```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
```

* [[Medium] [Solution] 78. Subsets](%5BMedium%5D%20%5BSolution%5D%2078.%20Subsets.md)
* [[Easy] [Solution] 136. Single Number](%5BEasy%5D%20%5BSolution%5D%20136.%20Single%20Number.md)
* [[Easy] [Solution] 191. Number of 1 Bits](%5BEasy%5D%20%5BSolution%5D%20191.%20Number%20of%201%20Bits.md)
* [[Easy] [Solution] 268. Missing Number](%5BEasy%5D%20%5BSolution%5D%20268.%20Missing%20Number.md)

## Regular Expression
* library: `re`
    * `re.match(pattern, string, flags=0)`
    * `re.split(pattern, string, maxsplit=0, flags=0)`
    * `re.findall(pattern, string, flags=0)`
* [[Easy] 1309. Decrypt String from Alphabet to Integer Mapping](%5BEasy%5D%201309.%20Decrypt%20String%20from%20Alphabet%20to%20Integer%20Mapping.md)
* [[Medium] [Solution] 640. Solve the Equation](%5BMedium%5D%20%5BSolution%5D%20640.%20Solve%20the%20Equation.md)
* [[Medium] [Solution] 592. Fraction Addition and Subtraction](%5BMedium%5D%20%5BSolution%5D%20592.%20Fraction%20Addition%20and%20Subtraction.md)
* [[Medium] 468. Validate IP Address](%5BMedium%5D%20468.%20Validate%20IP%20Address.md)
* [[Medium] 227. Basic Calculator II](%5BMedium%5D%20227.%20Basic%20Calculator%20II.md)