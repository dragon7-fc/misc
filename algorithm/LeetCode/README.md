
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

* 785. Is Graph Bipartite?
* 886. Possible Bipartition

**Similar**

* 207. Course Schedule
* 802. Find Eventual Safe States

**Similar**

* 1143. Longest Common Subsequence
* 1312. Minimum Insertion Steps to Make a String Palindrome

**Similar (Prefix/Range sum)**

* [[Medium] 1314. Matrix Block Sum](%5BMedium%5D%201314.%20Matrix%20Block%20Sum.md)
* [[Medium] [Solution] 304. Range Sum Query 2D - Immutable](%5BMedium%5D%20%5BSolution%5D%20304.%20Range%20Sum%20Query%202D%20-%20Immutable.md)

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

* [[Medium] [Solution] 877. Stone Game](%5BMedium%5D%20%5BSolution%5D%20877.%20Stone%20Game.md)
* [[Medium] [Solution] 712. Minimum ASCII Delete Sum for Two Strings](%5BMedium%5D%20%5BSolution%5D%20712.%20Minimum%20ASCII%20Delete%20Sum%20for%20Two%20Strings.md)

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

**Example 2:**
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

**Example 3:**
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
        print source, target
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
* [[Medium] [Solution] 684. Redundant Connection](%5BMedium%5D%20%5BSolution%5D%20684.%20Redundant%20Connection.md)
* [[Medium] [Solution] 934. Shortest Bridge](%5BMedium%5D%20%5BSolution%5D%20934.%20Shortest%20Bridge.md)

## Binary Search

**Example 1:**
```
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