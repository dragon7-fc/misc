
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

**Example 1: Top-down**
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

**Example 2: Bottom-up**
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

* [[Medium] [Solution] 877. Stone Game](%5BMedium%5D%20%5BSolution%5D%20877.%20Stone%20Game.md)
* [[Medium] [Solution] 712. Minimum ASCII Delete Sum for Two Strings](%5BMedium%5D%20%5BSolution%5D%20712.%20Minimum%20ASCII%20Delete%20Sum%20for%20Two%20Strings.md)
* [[Medium] [Solution] 304. Range Sum Query 2D - Immutable](%5BMedium%5D%20%5BSolution%5D%20304.%20Range%20Sum%20Query%202D%20-%20Immutable.md)

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

**Exaomple 4:**
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

**Template 3: (connected component)**
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
    * `bisect.bisect_right(a, x, lo=0, hi=len(a))` = `bisect.bisect(a, x, lo=0, hi=len(a))`
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

# Regular Expression
* library: `re`
    * `re.match(pattern, string, flags=0)`
    * `re.split(pattern, string, maxsplit=0, flags=0)`
    * `re.findall(pattern, string, flags=0)`
* [[Easy] 1309. Decrypt String from Alphabet to Integer Mapping](%5BEasy%5D%201309.%20Decrypt%20String%20from%20Alphabet%20to%20Integer%20Mapping.md)
* [[Medium] [Solution] 640. Solve the Equation](%5BMedium%5D%20%5BSolution%5D%20640.%20Solve%20the%20Equation.md)
* [[Medium] [Solution] 592. Fraction Addition and Subtraction](%5BMedium%5D%20%5BSolution%5D%20592.%20Fraction%20Addition%20and%20Subtraction.md)
* [[Medium] 468. Validate IP Address](%5BMedium%5D%20468.%20Validate%20IP%20Address.md)
* [[Medium] 227. Basic Calculator II](%5BMedium%5D%20227.%20Basic%20Calculator%20II.md)