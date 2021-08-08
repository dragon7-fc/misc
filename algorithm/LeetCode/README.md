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


### Table of Contents

1. [Libraries](#libraries)
1. [Concepts](#concept)
1. [Top Microsoft Questions](#top_ms)
1. [Top Google Questions](#top_go)
1. [Top Amazon Questions](#top_az)
1. [Nvidia](#nvidia)
1. [Array](#array)
1. [Dynamic Programming](#dp)
1. [Math](#math)
1. [String](#string)
1. [Tree](#tree)
1. [Hash Table](#ht)
1. [Depth-first Search](#dfs)
1. [Binary Search](#bs)
1. [Greedy](#greedy)
1. [Breadth-first Search](#bfs)
1. [Two Pointers](#tp)
1. [Stack](#stack)
1. [Backtracking](#backtracking)
1. [Bit Manipulation](#bm)
1. [Sort](#sort)
1. [Linked List](#ll)
1. [Heap](#heap)
1. [Union Find](#uf)
1. [Sliding Window](#sw)
1. [Divide and Conquer](#dc)
1. [Trie](#trie)
1. [Recursion](#recursion)
1. [Segment Tree](#st)
1. [Ordered Map](#om)
1. [Queue](#queue)
1. [Minimax](#minimax)
1. [Line Sweep](#ls)
1. [Random](#random)
1. [Topological Sort](#ts)
1. [Brainteaser](#brainteaser)
1. [Geometry](#geometry)
1. [Regular Expression](#re)

**Note**

* Subarray/Substring need to be consecutive.
* Subsequence don't have to be consecutive, but maintain relative order.

## Libraries <a name="libraries"></a>
---
### itertools

* `itertools.accumulate(iterable[, func, *, initial=None])`

    * ex. accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    * ex. accumulate([1,2,3,4,5], initial=100) --> 100 101 103 106 110 115
    * ex. accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
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
### functools

* `functools.lru_cache(user_function)`
* `functools.reduce(function, iterable[, initializer])`

### bisect
* `bisect.bisect_left(a, x, lo=0, hi=len(a))`
    * ex. li = [1, 3, 4, 4, 4, 6, 7], bisect.bisect_left(li, 4) = 2
* `bisect.bisect_right(a, x, lo=0, hi=len(a))` = `bisect.bisect(a, x, lo=0, hi=len(a))`
    * ex. li = [1, 3, 4, 4, 4, 6, 7], bisect.bisect(li, 4) = 5

### heapq

* `heapq.heappush(heap, item)`
* `heapq.heappop(heap)`
* `heapq.heappushpop(heap, item)`
* `heapq.heapify(x)`
* `heapq.heapreplace(heap, item)`
* `heapq.merge(*iterables, key=None, reverse=False)`
* `heapq.nlargest(n, iterable, key=None)`
* `heapq.nsmallest(n, iterable, key=None)`

### random

* `random.randrange(stop)`

    * ex. randrange(10) --> Integer from 0 to 9 inclusive
* `random.randrange(start, stop[, step])`

    * ex. randrange(0, 101, 2) --> Even integer from 0 to 100 inclusive
* `random.randint(a, b)`

    * Alias for randrange(a, b+1)
    * ex. randint(1, 10) --> Integer from 1 to 10 inclusive
* `random.uniform(a, b)`

    * ex. uniform(2.5, 10.0) --> Random float:  2.5 <= x < 10.0
* `random.choice(seq)`
    
    * ex. choice(['win', 'lose', 'draw']) --> Single random element from a sequence

### re

* `re.match(pattern, string, flags=0)`

    * ex.
    ```python
    >>> m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
    >>> m.group(0)       # The entire match
    'Isaac Newton'
    >>> m.group(1)       # The first parenthesized subgroup.
    'Isaac'
    >>> m.group(2)       # The second parenthesized subgroup.
    'Newton'
    >>> m.group(1, 2)    # Multiple arguments give us a tuple.
    ('Isaac', 'Newton')
    ```
* `re.search(pattern, string, flags=0)`

    * ex.
    ```python
    match = re.search(pattern, string)
    if match:
        process(match)
    ```
* `re.split(pattern, string, maxsplit=0, flags=0)`

    * ex.  re.split('\d+', 'Twelve:12 Eighty nine:89.') --->  ['Twelve:', ' Eighty nine:', '.']
* `re.findall(pattern, string, flags=0)`
    
    * ex. re.findall('\d+', 'hello 12 hi 89. Howdy 34') ---> ['12', '89', '34']
* `re.sub(pattern, repl, string, count=0, flags=0)`

    * ex. re.sub('\s+', '', 'abc 12 de 23 \n f45 6') ---> 'abc12de23f456'
* `re.fullmatch(pattern, string, flags=0)`

### datetime

* `datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)`

    * ex. datetime.datetime(2011, 11, 4, 0, 0) --> datetime.fromisoformat('2011-11-04T00:05:23')
* `datetime.strftime(format)`

    * ex. dt.strftime("%A, %d. %B %Y %I:%M%p") --> 'Tuesday, 21. November 2006 04:30PM'
* `datetime.strptime(date_string, format)`

    * ex. datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M") --> datetime.datetime(2006, 11, 21, 16, 30)

### operator

* `operator.add(a, b)`
* `operator.sub(a, b)`
* `operator.mul(a, b)`
* `operator.truediv(a, b)`
* `operator.xor(a, b)`

## Concepts <a name="concept"></a>
---
* [Rolling hash, a constant time window search](https://medium.com/algorithm-and-datastructure/rolling-hash-a-constant-time-window-search-f8af6ee12d3f)
* [Kadane’s Algorithm — (Dynamic Programming) — How and Why does it Work?](https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d)

## Top Microsoft Questions <a name="top_ms"></a>
---
146, 200, 42, 2, 3, 273, 295, 5, 139, 49, 443, 460, 53, 41, 17, 297, 54, 138, 236, 234, 445, 25, 227, 212, 98, 362, 642, 348, 128, 72, 545, 218, 1578, 62, 151, 1239, 99, 1448, 836, 277, 59, 658, 1647, 116, 117, 266, 722, 285, 1466, 1576

## Top Google Questions <a name="top_go"></a>
---

## Top Amazon Questions <a name="top_az"></a>
---
1, 146, 200, 42, 1041, 1335, 238, 829, 273, 253, 380, 295, 973, 221, 1010, 127, 588, 23, 239, 1465, 460, 1192, 547, 138, 21, 1152, 140, 692, 210, 994, 937, 103, 863, 735, 1091, 572, 763, 240, 503, 472, 1328, 323, 353, 957, 1710, 1167, 1629, 1648, 1135, 1597

## Nvidia <a name="nvidia"></a>
---
274, 380, 295, 33, 443, 74, 75, 48, 22, 238, 70, 200

## Array <a name="array"></a>
---
### Greedy
```python
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        curr_sum = max_sum = nums[0]

        for i in range(1, N):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum
```
* [Easy] 53. Maximum Subarray

### Locate and Analyze Problem Index
```python
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        p = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                if p is not None:
                    return False
                p = i

        return (p is None or p == 0 or p == len(nums)-2 or
                nums[p-1] <= nums[p+1] or nums[p] <= nums[p+2])
```
* [Easy] [Solution] 665. Non-decreasing Array

### Accumulate
```python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return itertools.accumulate(nums)
```
* [Easy] 1480. Running Sum of 1d Array

### Simulate hash table
```python
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = [-1 for _ in range(1000001)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.buckets[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.buckets[key]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        """
        self.buckets[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
```
* [Easy] 706. Design HashMap

### Mask as visited
```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = -1
        missing = 1
        for num in nums:
            if nums[abs(num) - 1] < 0:
                dup = abs(num);
            else:
                nums[abs(num) - 1] *= -1

        for i in range(1, len(nums)):
            if nums[i] > 0:
                missing = i + 1
        return [dup, missing]
```
* [Easy] [Solution] 645. Set Mismatch

### Sort by value and index
```python
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return list(zip(*sorted((sum(row), i) for i, row in enumerate(mat))[:k]))[1]
```
* [Easy] 1337. The K Weakest Rows in a Matrix

### Min Array, Two Pass
```python
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        prev = float('-inf')
        ans = []
        for i, x in enumerate(S):
            if x == C: prev = i
            ans.append(i - prev)

        prev = float('inf')
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C: prev = i
            ans[i] = min(ans[i], prev - i)

        return ans
```
* [Easy] [Solution] 821. Shortest Distance to a Character

### Simulate
```python
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if not n: return 0 # edge case 
        nums = [0, 1]
        for i in range(2, n+1): 
            if i&1: nums.append(nums[i//2] + nums[i//2+1])
            else: nums.append(nums[i//2])
        return max(nums)
```
* [Easy] 1646. Get Maximum in Generated Array

### Greedy
```python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr = [0] + arr
        nk = k
        for a, b in zip(arr[:], arr[1:]):
            nk -= b-a-1
            if nk <= 0:
                return a+k
            k = nk
        return arr[-1]+k
```
* [Easy] 1539. Kth Missing Positive Number

### Two while loop for Walk up and down
```python
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        N = len(arr)
        i = 0

        # walk up
        while i+1 < N and arr[i] < arr[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and arr[i] > arr[i+1]:
            i += 1

        return i == N-1
```
* [Easy] [Solution] 941. Valid Mountain Array

### Counter
```python
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        c = collections.Counter(map(lambda x: x % 60, time))
        ans = 0
        for k in c.keys():
            if k <= 30 and c[(60-k) % 60]:
                if k == 0 or k == 30:
                    ans += (c[k] * (c[k]-1)) // 2
                else:
                    ans += c[k] * c[60-k]
        return ans
```
* [Easy] 1010. Pairs of Songs With Total Durations Divisible by 60

### space transformation
```python
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k < 0: return self.decrypt(code[::-1], -k)[::-1]
        n = len(code)
        prefix = code * 2
        for i in range(1, 2 * n):
            prefix[i] += prefix[i - 1]
        for i in range(n):
            code[i] = prefix[i + k] - prefix[i]
        return code
```
* [Easy] 1652. Defuse the Bomb

### Groupby
```python
class Solution:
    def maxPower(self, s: str) -> int:
        return max(len(list(g)) for k, g in itertools.groupby(s))
```
* [Easy] 1446. Consecutive Characters

### Preprocess array
```python
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ones = [i for i, v in enumerate(seats) if v]
        ans = 0
        ans = max(ans, ones[0])
        for i, j in zip(ones[:], ones[1:]):
            ans = max(ans, (j-i) // 2)
        ans = max(ans, len(seats)-ones[-1]-1) 
        return ans
```
* [Easy] [Solution] 849. Maximize Distance to Closest Person

### Direct
```python
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            for i in range((len(row) + 1) // 2):
                """
                In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i]
                helps us find the i-th value of the row, counting from the right.
                """
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return A

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[col^1 for col in row[::-1]] for row in A]
```
* [Easy] [Solution] 832. Flipping an Image

### Rotate array = 1 whole reverse + 2 partial reverse
```python
class Solution:
    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
```
* [Easy] [Solution] 189. Rotate Array

### Boyer-Moore Voting Algorithm
```python
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
```
* [Easy] [Solution] 169. Majority Element

### Using division and modulus
```python
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        R , C = len(mat), len(mat[0])
        if R*C != r*c: return mat
        ans = []
        i = 0
        for ri in range(r):
            for ci in range(c):
                cur_r, cur_c = divmod(i, C)
                if ci == 0:
                    ans += [[mat[cur_r][cur_c]]]
                else:
                    ans[-1] += [mat[cur_r][cur_c]]
                i += 1
        return ans
```
* [Easy] [Solution] 566. Reshape the Matrix

### Locate and Analyze Problem Index
```python
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        p = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                if p is not None:
                    return False
                p = i

        return (p is None or p == 0 or p == len(nums)-2 or
                nums[p-1] <= nums[p+1] or nums[p] <= nums[p+2])
```
* [Easy] [Solution] 665. Non-decreasing Array

### Prefix Sum
```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1
```
* [Easy] [Solution] 724. Find Pivot Index

### Compare With Top-Left Neighbor
```python
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))
```
* [Easy] [Solution] 766. Toeplitz Matrix

### Brute Force
```python
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def magic(a,b,c,d,e,f,g,h,i):
            return (sorted([a,b,c,d,e,f,g,h,i]) == list(range(1, 10)) and
                (a+b+c == d+e+f == g+h+i == a+d+g ==
                 b+e+h == c+f+i == a+e+i == c+e+g == 15))

        ans = 0
        for r in range(R-2):
            for c in range(C-2):
                if grid[r+1][c+1] != 5: continue  # optional skip
                if magic(grid[r][c], grid[r][c+1], grid[r][c+2],
                         grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
                         grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]):
                    ans += 1
        return ans
```
* [Easy] [Solution] 840. Magic Squares In Grid

### Copy Directly
```python
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return zip(*A)
```
* [Easy] [Solution] 867. Transpose Matrix

### Greatest Common Divisor
```python
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from functools import reduce
        vals = collections.Counter(deck).values()
        return reduce(math.gcd, vals) >= 2
```
* [Easy] [Solution] 914. X of a Kind in a Deck of Cards

### One Pass (Simple Variant)
```python
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        increasing = decreasing = True

        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                increasing = False
            if A[i] < A[i+1]:
                decreasing = False

        return increasing or decreasing
```
* [Easy] [Solution] 896. Monotonic Array

### Maintain Array Sum
```python
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        S = sum(x for x in A if x % 2 == 0)
        ans = []

        for x, k in queries:
            if A[k] % 2 == 0: S -= A[k]
            A[k] += x
            if A[k] % 2 == 0: S += A[k]
            ans.append(S)

        return ans
```
* [Easy] [Solution] 985. Sum of Even Numbers After Queries

### Groupby
```python
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        h = sum(k for row in grid for k, _ in itertools.groupby(row))
        v = sum(k for col in zip(*grid) for k, _ in itertools.groupby(col))
        return 2*(h+v)
```
* [Easy] 463. Island Perimeter

### Design HashSet
```python
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hs = [0]*1000001


    def add(self, key: int) -> None:
        self.hs[key] = 1

    def remove(self, key: int) -> None:
        self.hs[key] = 0

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.hs[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
```
* [Easy] 705. Design HashSet

### Row XOR Column
```python
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        row, col = [False] * n, [False] * m
        for r, c in indices:
            row[r] ^= True
            col[c] ^= True
        return sum(ro ^ cl for ro in row for cl in col)
```
* [Easy] 1252. Cells with Odd Values in a Matrix

### In-Degree/Out-Degree
```python
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        in_edges, out_edges = [0]*N, [0]*N
        for t in trust:
            s, d = t[0]-1, t[1]-1
            in_edges[d] += 1
            out_edges[s] += 1
        for i in range(0, N):
            if in_edges[i] == N-1 and out_edges[i] == 0:
                return i+1

        return -1
```
* [Easy] 997. Find the Town Judge

### Generator
```python
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return sum(([nums[i], nums[i+n]] for i in range(n)), [])
```
* [Easy] 1470. Shuffle the Array

### Rotate Groups of Four Cells
```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp
```
* [Medium] 48. Rotate Image

### Current and accumulate
```python
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        curr, steps = 0, 0
        for i in range(n):
            answer[i] += steps
            if boxes[i] == '1': curr += 1
            steps += curr
        curr, steps = 0, 0
        for i in reversed(range(n)):
            answer[i] += steps
            if boxes[i] == '1': curr += 1
            steps += curr
        return answer
```
* [Medium] 1769. Minimum Number of Operations to Move All Balls to Each Box

### submatrix rearrangement, prefix sum
```python
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ans = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] != 0 and row > 0:
                    matrix[row][col] += matrix[row - 1][col]

            curr = sorted(matrix[row], reverse=True) 
            for i in range(len(matrix[0])):
                ans = max(ans, curr[i] * (i + 1))
        
        return ans
```
* [Medium] 1727. Largest Submatrix With Rearrangements

### scan neighbor of each cell
```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Neighbors array to find 8 neighboring cells for a given cell
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        rows = len(board)
        cols = len(board[0])

        # Iterate through board cell by cell.
        for row in range(rows):
            for col in range(cols):

                # For each cell count the number of live neighbors.
                live_neighbors = 0
                for neighbor in neighbors:

                    # row and column of the neighboring cell
                    r = (row + neighbor[0])
                    c = (col + neighbor[1])

                    # Check the validity of the neighboring cell and if it was originally a live cell.
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and abs(board[r][c]) == 1:
                        live_neighbors += 1

                # Rule 1 or Rule 3
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    # -1 signifies the cell is now dead but originally was live.
                    board[row][col] = -1
                # Rule 4
                if board[row][col] == 0 and live_neighbors == 3:
                    # 2 signifies the cell is now live but was originally dead.
                    board[row][col] = 2

        # Get the final representation for the newly updated board.
        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0
```
* [Medium] [Solution] 289. Game of Life

### Diagonal Iteration and Reversal
```python
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        # Check for empty matrices
        if not matrix or not matrix[0]:
            return []

        # Variables to track the size of the matrix
        N, M = len(matrix), len(matrix[0])

        # The two arrays as explained in the algorithm
        result, intermediate = [], []

        # We have to go over all the elements in the first
        # row and the last column to cover all possible diagonals
        for d in range(N + M - 1):

            # Clear the intermediate array everytime we start
            # to process another diagonal
            intermediate.clear()

            # We need to figure out the "head" of this diagonal
            # The elements in the first row and the last column
            # are the respective heads.
            r, c = 0 if d < M else d - M + 1, d if d < M else M - 1

            # Iterate until one of the indices goes out of scope
            # Take note of the index math to go down the diagonal
            while r < N and c > -1:
                intermediate.append(matrix[r][c])
                r += 1
                c -= 1

            # Reverse even numbered diagonals. The
            # article says we have to reverse odd 
            # numbered articles but here, the numbering
            # is starting from 0 :P
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
        return result   
```
* [Medium] 498. Diagonal Traverse

### Vote
```python
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        cntA = [0] * 7
        cntB = [0] * 7
        cntSame = [0] * 7
        for i in range(n):
            a, b = A[i], B[i]
            cntA[a] += 1
            cntB[b] += 1
            if a == b: cntSame[a] += 1
        ans = n
        for v in range(1, 7):
            if cntA[v] + cntB[v] - cntSame[v] == n:
                minSwap = min(cntA[v], cntB[v]) - cntSame[v]
                ans = min(ans, minSwap)
        return -1 if ans == n else ans
```
* [Medium] 1007. Minimum Domino Rotations For Equal Row

### Count from left and right side for each element
```python
class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_right_count = [0] * len(s)
        b_left_count = [0] * len(s)
        
        count = 0
        for i in range(len(s)):
            b_left_count[i] = count
            if s[i] == 'b':
                count += 1
        
        count = 0
        for i in range(len(s) - 1 ,-1, -1):
            a_right_count[i] = count
            if s[i] == 'a':
                count += 1
        
        min_delete = len(s)
        for i in range(len(s)):
            min_delete = min(min_delete, a_right_count[i] + b_left_count[i])
        return min_delete

class Solution:
    def minimumDeletions(self, s: str) -> int:
        cnt_b = 0
        dp = [0]
        for c in s:
            if c == 'b':
                cnt_b+=1
                dp.append( dp[-1] )
            else:
                dp.append( min(cnt_b,dp[-1]+1) )
        return dp[-1]
```
* [Medium] 1653. Minimum Deletions to Make String Balanced

### The robot stays in the circle iff (looking at the final vector) it changes direction (ie. doesn't stay pointing north), or it moves 0.
```python
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # directions -> North, East, South, West -> i.e Up -> Right -> Down -> Left
        # clockwise sequence for right direction
        directions = [(0,1), (1,0), (0,-1), (-1,0)] 
        x = y = 0
        #we face towards north intially as specified in problem
        curr_dir = 0 
        for instr in instructions:
            if instr == 'G':
                x += directions[curr_dir][0]
                y += directions[curr_dir][1]
            elif instr == 'L':
                curr_dir = (curr_dir - 1) % 4 # counter clockwise
            else:
                curr_dir = (curr_dir + 1) % 4 # clockwise

        return (x,y) == (0,0) or directions[curr_dir] != (0,1) 
```
* [Medium] 1041. Robot Bounded In Circle

### Using Cumulative Sum and HashSet
```python
class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        N = len(nums)
        if N < 7: 
            return False
        cum = [nums[0]] + [0]*(N-1)
        for i in range(1, N):
            cum[i] += cum[i-1] + nums[i]
        for j in range(3, N-3):
            s = set()
            for i in range(1, j-1):
                if cum[i-1] == cum[j-1] - cum[i]:
                    s.add(cum[i-1])
            for k in range(j+2, N-1):
                if cum[N-1]-cum[k] == cum[k-1]-cum[j] and (cum[k-1]-cum[j]) in s:
                    return True

        return False
```
* [Lock] [Medium] [Solution] 548. Split Array with Equal Sum

### Single Scan
```python
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        min_val, max_val = arrays[0][0], arrays[0][-1]
        for i in range(1, len(arrays)):
            res = max(res, max(abs(arrays[i][-1] - min_val), abs(max_val - arrays[i][0])))
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])

        return res
```
* [Lock] [Medium] [Solution] 624. Maximum Distance in Arrays

### Mark Visited Elements in the Input Array itself
```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            num = abs(num)
            if nums[num-1] < 0:
                ans.append(num)
            else:
                nums[num-1] = -nums[num-1]
        return ans
```
* [Medium] [Solution] 442. Find All Duplicates in an Array

### Ad-Hoc
```python
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        R, C = len(board), len(board[0])
        todo = False

        for r in range(R):
            for c in range(C-2):
                if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:
                    board[r][c] = board[r][c+1] = board[r][c+2] = -abs(board[r][c])
                    todo = True

        for r in range(R-2):
            for c in range(C):
                if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                    board[r][c] = board[r+1][c] = board[r+2][c] = -abs(board[r][c])
                    todo = True

        for c in range(C):
            wr = R-1
            for r in range(R-1, -1, -1):
                if board[r][c] > 0:
                    board[wr][c] = board[r][c]
                    wr -= 1
            for wr in range(wr, -1, -1):
                board[wr][c] = 0

        return self.candyCrush(board) if todo else board
```
* [Lock] [Medium] [Solution] 723. Candy Crush

### Linear Scan, remember last position
```python
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        for i in range(len(nums)-2):
            k = i + 2
            if nums[i] != 0:
                for j in range(i+1, len(nums)- 1):
                    while (k < len(nums)) and (nums[i]+nums[j] > nums[k]):
                        k += 1
                    count += k - j - 1
        return count
```
* [Medium] [Solution] 611. Valid Triangle Number

### Mark Visited Element
```python
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            if nums[i] != float('inf'):
                start = nums[i]
                count = 0
                while nums[start] != float('inf'):
                    tmp = start
                    start = nums[start]
                    count += 1
                    nums[tmp] = float('inf')
            ans = max(ans, count)
        return ans
```
* [Medium] [Solution] 565. Array Nesting

### Left/Right Prefix Sum
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      
        # The length of the input array 
        length = len(nums)
        
        # The answer array to be returned
        answer = [0]*length
        
        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):
            
            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]
        
        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1;
        for i in reversed(range(length)):
            
            # For the index 'i', R would contain the 
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer
```
* [Medium] [Solution] 238. Product of Array Except Self

### O(1) Space, Efficient Solution, symbol mask
```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            # Since first cell for both first row and first column is the same i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                # If an element is zero, we set the first element of the corresponding row and column to 0
                if matrix[i][j]  == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Iterate over the array once again and using the first row and first column, update the elements.
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well        
        if is_col:
            for i in range(R):
                matrix[i][0] = 0
```
* [Medium] [Solution] 73. Set Matrix Zeroes

### Balanced Tree
```python
class Node:
    __slots__ = 'start', 'end', 'left', 'right'
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None

    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False

class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
```
* [Medium] [Solution] 729. My Calendar I

### Counting
```python
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = [0] * 121
        for age in ages:
            count[age] += 1

        ans = 0
        for ageA, countA in enumerate(count):
            for ageB, countB in enumerate(count):
                if ageA * 0.5 + 7 >= ageB: continue
                if ageA < ageB: continue
                if ageA < 100 < ageB: continue
                ans += countA * countB
                if ageA == ageB: ans -= countA

        return ans
```
* [Medium] [Solution] 825. Friends Of Appropriate Ages

### Store Exhausted Position and Quantity
```python
class RLEIterator:

    def __init__(self, A: List[int]):
        self.A = A
        self.i = 0
        self.q = 0

    def next(self, n: int) -> int:
        while self.i < len(self.A):
            if self.q + n > self.A[self.i]:
                n -= self.A[self.i] - self.q
                self.q = 0
                self.i += 2
            else:
                self.q += n
                return self.A[self.i+1]
        return -1




# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
```
* [Medium] [Solution] 900. RLE Iterator

### Next Array
```python
class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        N = len(A)
        maxleft = [None] * N
        minright = [None] * N

        m = A[0]
        for i in range(N):
            m = max(m, A[i])
            maxleft[i] = m

        m = A[-1]
        for i in range(N-1, -1, -1):
            m = min(m, A[i])
            minright[i] = m

        for i in range(1, N):
            if maxleft[i-1] <= minright[i]:
                return i
```
* [Medium] [Solution] 915. Partition Array into Disjoint Intervals

### Kadane's (Min Variant)
```python
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # ans1: answer for one-interval subarray  -> A[:]
        ans1 = cur = float('-inf')
        for x in A:
            cur = x + max(cur, 0)
            ans1 = max(ans1, cur)

        # ans2: answer for two-interval subarray, interior in A[1:]  -> [A[0], [A[1:x], A[x:]]]
        ans2 = cur = float('inf')
        for i in range(1, len(A)):
            cur = A[i] + min(cur, 0)
            ans2 = min(ans2, cur)
        ans2 = sum(A) - ans2

        # ans3: answer for two-interval subarray, interior in A[:-1]  -> [[A[:x], A[x:-1]], A[-1]]
        ans3 = cur = float('inf')
        for i in range(len(A)-1):
            cur = A[i] + min(cur, 0)
            ans3 = min(ans3, cur)
        ans3 = sum(A) - ans3

        return max(ans1, ans2, ans3)
```
* [Medium] [Solution] 918. Maximum Sum Circular Subarray

### Prefix Sums
```python
class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        P = [0]
        for x in S:
            P.append(P[-1] + int(x))

        return min(P[j] + len(S)-j-(P[-1]-P[j])
                   for j in range(len(P)))
```
* [Medium] [Solution] 926. Flip String to Monotone Increasing

### Maintain Duplicate Info
```python
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        A.append(100000)
        ans = taken = 0

        for i in range(1, len(A)):
            if A[i-1] == A[i]:
                taken += 1
                ans -= A[i]
            else:
                give = min(taken, A[i] - A[i-1] - 1)
                ans += give * (give + 1) // 2 + give * A[i-1]
                taken -= give

        return ans
```
* [Medium] [Solution] 945. Minimum Increment to Make Array Unique

### Simulation
```python
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        index = collections.deque(range(N))
        ans = [None] * N

        for card in sorted(deck):
            ans[index.popleft()] = card
            if index:
                index.append(index.popleft())

        return ans
```
* [Medium] [Solution] 950. Reveal Cards In Increasing Order

### Sort
```python
class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        ans = 0
        m = float('inf')
        for i in sorted(range(len(A)), key = A.__getitem__):
            ans = max(ans, i - m)
            m = min(m, i)
        return ans
```
* [Medium] [Solution] 962. Maximum Width Ramp

### Sort
```python
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        ans = []

        for i in range(len(A)-1, 0, -1):
            if A[i] != i+1:
                vi = A.index(i+1)
                if vi != 0:
                    A[:vi + 1] = A[vi::-1]
                    A[:i+1] = A[i::-1]
                    ans.append(vi +1)
                    ans.append(i+1)
                else:
                    A[:i+1] = A[i::-1]
                    ans.append(i+1)
        return ans
```
* [Medium] [Solution] 969. Pancake Sorting

### Prefix Sums and Counting
```python
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        P = [0]
        for x in A:
            P.append((P[-1] + x) % K)

        count = collections.Counter(P)
        return sum(v*(v-1)//2 for v in count.values())
```
* [Medium] [Solution] 974. Subarray Sums Divisible by K

### Prefix Sum Range
```python
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n

        for booking in bookings:
            i, j, k = booking
            # mark all the i and js to the res
            res[i-1] = k + res[i-1]
            try: # handling the index out of range problem, can use "if" instead
                res[j] = res[j] - k 
            except:
                continue

        # calculate the accumulative sum
        for i in range(1, len(res)):
            res[i] = res[i-1] + res[i]
        return res
```
* [Medium] 1109. Corporate Flight Bookings

### Prefix XOR
```python
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        arr.insert(0, 0)
        n = len(arr)
        for i in range(n - 1):
            arr[i + 1] ^= arr[i]
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] == arr[j]:
                    res += j - i - 1
        return res
```
* [Medium] 1442. Count Triplets That Can Form Two Arrays of Equal XOR

### Expand Around Center
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ''

        def expandAroundCenter(left, right):
            L, R = left, right
            while L >= 0 and R < len(s) and s[L] == s[R]:
                L -= 1
                R += 1
            return R - L - 1

        start, end = 0, 0
        for i in range(len(s)):
            len1 = expandAroundCenter(i, i);
            len2 = expandAroundCenter(i, i + 1);
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2;
                end = i + max_len // 2;

        return s[start:end + 1]
```
* [Medium] [Solution] 5. Longest Palindromic Substring

### Find Latest Group of Size M
```python
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        length = [0] * (len(arr) + 2)
        count = [0] * (len(arr) + 1)
        res = -1
        for i, a in enumerate(arr):
            left, right = length[a - 1], length[a + 1]
            length[a] = length[a - left] = length[a + right] = left + right + 1
            count[left] -= 1
            count[right] -= 1
            count[length[a]] += 1
            if count[m]:
                res = i + 1
        return res
```
* [Medium] 1562. Find Latest Group of Size M

### Sorted List
```python
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        SList = SortedList()
        ans = 0
        for num in instructions:
            ans += min(SList.bisect_left(num), len(SList) - SList.bisect_right(num))
            ans %= (10**9 + 7)
            SList.add(num)

        return ans
```
* [Hard] 1649. Create Sorted Array through Instructions

### Ad-Hoc
```python
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], K: int) -> List[int]:
        W = [] #array of sums of windows
        sum_ = 0
        for i, x in enumerate(nums):
            sum_ += x
            if i >= K: sum_ -= nums[i-K]
            if i >= K-1: W.append(sum_)

        left = [0] * len(W)
        best = 0
        for i in range(len(W)):
            if W[i] > W[best]:
                best = i
            left[i] = best

        right = [0] * len(W)
        best = len(W) - 1
        for i in range(len(W) - 1, -1, -1):
            if W[i] >= W[best]:
                best = i
            right[i] = best

        ans = None
        for j in range(K, len(W) - K):
            i, k = left[j-K], right[j+K]
            if ans is None or (W[i] + W[j] + W[k] >
                    W[ans[0]] + W[ans[1]] + W[ans[2]]):
                ans = i, j, k
        return ans
```
* [Hard] [Solution] 689. Maximum Sum of 3 Non-Overlapping Subarrays

### Sorted Count Pairs
```python
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count = collections.Counter()
        counted = []
        for x in arr:
            count[x] += 1
            counted.append((x, count[x]))

        ans, cur = 0, None
        for X, Y in zip(counted, sorted(counted)):
            cur = max(cur, X) if cur else X
            if cur == Y:
                ans += 1
        return ans
```
* [Hard] [Solution] 768. Max Chunks To Make Sorted II

### Reverse Subarray
```python
class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        total, res, min2, max2 = 0, 0, float('inf'), -float('inf')
        for a, b in zip(nums, nums[1:]):
            total += abs(a - b)
            res = max(res, abs(nums[0] - b) - abs(a - b))
            res = max(res, abs(nums[-1] - a) - abs(a - b))
            min2, max2 = min(min2, max(a, b)), max(max2, min(a, b))
        return total + max(res, (max2 - min2) * 2)
```
* [Hard] 1330. Reverse Subarray To Maximize Array Value

### Interval Stabbing
```python
class Solution:
    def bestRotation(self, A: List[int]) -> int:
        N = len(A)
        bad = [0] * N
        for i, x in enumerate(A):
            left, right = (i - x + 1) % N, (i + 1) % N
            bad[left] -= 1
            bad[right] += 1
            if left > right:
                bad[0] -= 1

        best = -N
        ans = cur = 0
        for i, score in enumerate(bad):
            cur += score
            if cur > best:
                best = cur
                ans = i

        return ans
```
* [Hard] [Solution] 798. Smallest Rotation with Highest Score

### Append and Sort, Greedy
```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals)
        ans = [intervals[0]]

        for s, e in intervals[1:]:
            top = ans[-1]
            if top[1] >= s:
                # tops' end is earlier than the start
                ans.pop()
                top[1] = max(e, top[1])
                ans.append(top)
            else:
                ans.append([s, e])

        return ans
```
* [Hard] 57. Insert Interval

## Dynamic Programming <a name="dp"></a>
---
### Prefix Sum
```python
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []

        for row_num in range(numRows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

            triangle.append(row)

        return triangle
```
* [Easy] [Solution] 118. Pascal's Triangle

### Bottom-Up
```python
class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.memoize(N)

    def memoize(self, N: int) -> {}:
        cache = {0: 0, 1: 1}

        # Since range is exclusive and we want to include N, we need to put N+1.
        for i in range(2, N+1):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[N]
```
* [Easy] [Solution] 509. Fibonacci Number

### Typical
```python
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        n = len(nums)
        rob = [0]*(n+1)
        rob[0] = 0
        rob[1] = nums[0]
        for i in range(2, n+1):
            rob[i] = max(rob[i-1], nums[i-1]+rob[i-2])
        return rob[n]

class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)

        @functools.lru_cache(None)
        def dp(i):
            if i >= N:
                return 0
            return max(nums[i] + dp(i+2), dp(i+1))

        return dfs(0)
```
[[Easy] 198. House Robber](%5BEasy%5D%20198.%20House%20Robber.md)

### Pascal's Triangle
```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev_row = []

        for row_number in range(rowIndex+1):
            row = [None for _ in range(row_number+1)]
            row[0], row[-1] = 1,1
            for column_number in range(1,len(row)-1):
                row[column_number] = prev_row[column_number-1] + prev_row[column_number]
            prev_row = row
        return prev_row
```
* [Easy] 119. Pascal's Triangle II

### Fibonacci Number
```python
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        first = 1
        second = 2
        for n in range(3, n+1):
            third = first+second
            first = second
            second = third
        return second
```
* [Easy] [Solution] 70. Climbing Stairs

### 1D state
```python
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp = [0]*n

        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

        return min(dp[n-1], dp[n-2])

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f1 = f2 = 0
        for x in reversed(cost):
            f1, f2 = x + min(f1, f2), f1
        return min(f1, f2)
```
* [Easy] [Solution] 746. Min Cost Climbing Stairs

### Count
```python
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        MOD = 10**9 + 7
        
        @functools.lru_cache(None)
        def dfs(r, c, target):
            if r == m or c == n or r < 0 or c < 0:
                return 1
            if target == 0:
                return 0
            return ((dfs(r-1,c, target-1) + dfs(r+1, c, target-1))%MOD + (dfs(r, c-1, target-1) + dfs(r, c+1, target-1))%MOD) % MOD
        
        return dfs(i, j, N)
```
* [Medium] [Solution] 576. Out of Boundary Paths.md

### bitmask state as parameter
```python
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        # If there are no matchsticks, then we can't form any square.
        if not matchsticks:
            return False

        # Number of matchsticks
        L = len(matchsticks)

        # Possible perimeter of our square
        perimeter = sum(matchsticks)

        # Possible side of our square from the given matchsticks
        possible_side =  perimeter // 4

        # If the perimeter isn't equally divisible among 4 sides, return False.
        if possible_side * 4 != perimeter:
            return False

        # Memoization cache for the dynamic programming solution.
        memo = {}

        # mask and the sides_done define the state of our recursion.
        def recurse(mask, sides_done):

            # This will calculate the total sum of matchsticks used till now using the bits of the mask.
            total = 0
            for i in range(L - 1, -1, -1):
                if not (mask & (1 << i)):
                    total += matchsticks[L - 1 - i]

            # If some of the matchsticks have been used and the sum is divisible by our square's side, then we increment the number of sides completed.
            if total > 0 and total % possible_side == 0:
                sides_done += 1

            # If we were successfully able to form 3 sides, return True
            if sides_done == 3:
                return True

            # If this recursion state has already been calculated, just return the stored value.
            if (mask, sides_done) in memo:
                return memo[(mask, sides_done)]

            # Common variable to store answer from all possible further recursions from this step.
            ans = False

            # rem stores available space in the current side (incomplete).
            c = int(total / possible_side)
            rem = possible_side * (c + 1) - total

            # Iterate over all the matchsticks
            for i in range(L - 1, -1, -1):

                # If the current one can fit in the remaining space of the side and it hasn't already been taken, then try it out
                if matchsticks[L - 1 - i] <= rem and mask&(1 << i):

                    # If the recursion after considering this matchstick gives a True result, just break. No need to look any further.
                    # mask ^ (1 << i) makes the i^th from the right, 0 making it unavailable in future recursions.
                    if recurse(mask ^ (1 << i), sides_done):
                        ans = True
                        break
            # cache the result for the current recursion state.            
            memo[(mask, sides_done)] = ans
            return ans

        # recurse with the initial mask with all matchsticks available.
        return recurse((1 << L) - 1, 0)
```
* [Medium] [Solution] 473. Matchsticks to Square.md

### value chain
```python
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        CSum = [0] + list(accumulate(stones))
        
        @lru_cache(2000)
        def dp(i, j):
            if i > j: return 0
            sm = CSum[j + 1] - CSum[i]
            return sm - min(stones[i] + dp(i+1, j), stones[j] + dp(i, j-1))
        
        return dp(0, len(stones) - 1)

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        presum = [0] + stones[:]
        for i in range(1, len(presum)):
            presum[i] += presum[i-1]

        def score(i, j):
            j += 1
            return presum[j] - presum[i]

        n = len(stones)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                dp[i][j] = max(score(i+1, j) - dp[i+1][j], score(i, j-1) - dp[i][j-1])

        return dp[0][n-1]
```
* [Medium] 1690. Stone Game VII.md

### Think backward
```python
class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        @functools.lru_cache(None)
        def dfs(word):
            count = 0
            for i in range(len(word)):
                cur = word[:i] + word[i+1:]  # Delete One at Once
                if cur in s: 
                    count = max(count, dfs(cur))
            return count + 1

        rst, s, history = 1, set(words), {}
        for word in words:
            rst = max(rst, dfs(word))
        return rst
```
* [Medium] 1048. Longest String Chain

### Count
```python
import functools
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        @functools.lru_cache
        def dfs(i, j):
            if obstacleGrid[i][j] == 1:
                return 0
            elif i == 0 and j == 0:
                return 1
            count = 0
            if i >= 1:
                count += dfs(i-1, j)    # go down
            if j >= 1:
                count += dfs(i, j-1)    # go right
            return count
        return dfs(m-1, n-1)
```
* [Medium] [Solution] 63. Unique Paths II

### 1-D array DP
```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        R = len(triangle)

        if R == 0:
            return 0
        if R == 1:
            return triangle[0][0]

        dp = triangle[-1][:]

        for i in range(R-2, -1, -1):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]

        return dp[0]
```
* [Medium] 120. Triangle

### all combination
```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for i in range(1, target+1):
            dp[i] = sum([dp[i-num] for num in nums if i-num >= 0])
        return dp[target]

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @functools.lru_cache(None)
        def dfs(s):
            if s == 0:
                return 1
            elif s < 0:
                return 0
            rst = 0
            for num in nums:
                rst += dfs(s - num)
            return rst

        return dfs(target)
```
* [Medium] 377. Combination Sum IV

### taken not-taken
```python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        N = len(strs)

        @functools.lru_cache(None)
        def dp(index, m_zeroes, n_ones):
            if index >= N:
                return 0
            else:
                s = strs[index]
                ones, zeroes = s.count('1'), s.count('0')
                if m_zeroes - zeroes >= 0 and n_ones - ones >= 0:
                    return max(1 + dp(index + 1, m_zeroes - zeroes, n_ones - ones), dp(index + 1, m_zeroes, n_ones))
                else:
                    return dp(index + 1, m_zeroes, n_ones)
        return dp(0, m, n)
    
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            zeros, ones = s.count("0"), s.count("1")
            for i in range(m, zeros-1, -1):
                for j in range(n , ones-1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - zeros][j - ones])
        return dp[-1][-1]
```
* [Medium] 474. Ones and Zeroes

### min ammount
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @functools.lru_cache(None)
        def coinChange(rem):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            min_ = float('inf')
            for coin in coins:
                res = coinChange(rem - coin)
                if res >= 0 and res < min_:
                    min_ = 1 + res
            return -1 if (min_ == float('inf')) else min_

        if amount < 1:
            return 0
        return coinChange(amount)
    
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1
```
* [Medium] [Solution] 322. Coin Change

### Try every sum for each number
```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return True

        # in case total is odd, then there is no way for us to evenly divide the sum
        total = sum(nums)

        if total & 1:
            return False

        total >>= 1

        dp = [False] * (total + 1)
        dp[0] = True

        for num in nums:
            for s in range(total, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]

        return dp[-1]
    
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        sm = sum(nums)
        if sm%2: return False
        target = sm//2

        @functools.lru_cache(None)
        def dfs(i, g1):
            if i == N:
                if g1 == 0:
                    return True
                else:
                    return False
            if dfs(i+1, g1-nums[i]) or dfs(i+1, g1):
                return True
            else:
                return False
```
* [Medium] 416. Partition Equal Subset Sum

### Full Binary Tree
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            # return [rob this node, not rob this node]
            if not node:
                return (0, 0)
            left = helper(node.left)
            right = helper(node.right)
            # if we rob this node, we cannot rob its children
            rob = node.val + left[1] + right[1]
            # else we could choose to either rob its children or not
            not_rob = max(left) + max(right)
            return [rob, not_rob]

        return max(helper(root))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        rob_saved = {}
        not_rob_saved = {}

        def helper(node, parent_robbed):
            if not node:
                return 0

            if parent_robbed:
                if node in rob_saved:
                    return rob_saved[node]
                result = helper(node.left, False) + helper(node.right, False)
                rob_saved[node] = result
                return result
            else:
                if node in not_rob_saved:
                    return not_rob_saved[node]
                rob = node.val + helper(node.left, True) + helper(node.right, True)
                not_rob = helper(node.left, False) + helper(node.right, False)
                result = max(rob, not_rob)
                not_rob_saved[node] = result
                return result

        return helper(root, False)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0

        # reform tree into array-based tree
        tree = []
        graph = {-1: []}
        index = -1
        q = [(root, -1)]
        while q:
            node, parent_index = q.pop(0)
            if node:
                index += 1
                tree.append(node.val)
                graph[index] = []
                graph[parent_index].append(index)
                q.append((node.left, index))
                q.append((node.right, index))

        # represent the maximum start by node i with robbing i
        dp_rob = [0] * (index+1)

        # represent the maximum start by node i without robbing i
        dp_not_rob = [0] * (index+1)

        for i in reversed(range(index+1)):
            if not graph[i]:  # if is leaf
                dp_rob[i] = tree[i]
                dp_not_rob[i] = 0
            else:
                dp_rob[i] = tree[i] + sum(dp_not_rob[child]
                                          for child in graph[i])
                dp_not_rob[i] = sum(max(dp_rob[child], dp_not_rob[child])
                                    for child in graph[i])

        return max(dp_rob[0], dp_not_rob[0])
```
* [Medium] 337. House Robber III

### Simulation, child = (current - 1) // 2
```python
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        A = [[0] * k for k in range(1, 102)]
        A[0][0] = poured
        for r in range(query_row + 1):
            for c in range(r+1):
                q = (A[r][c] - 1.0) / 2.0
                if q > 0:
                    A[r+1][c] += q
                    A[r+1][c+1] += q

        return min(1, A[query_row][query_glass])
```
* [Medium] [Solution] 799. Champagne Tower

### Sorted by age and DP through score
```python
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        z = sorted(zip(ages, scores))
        n = len(z)
        dp = [0] * n
        for i in range(n):
            dp[i] = z[i][1]
            for j in range(i):
                if z[j][1] <= z[i][1]:
                    dp[i] = max(dp[i], dp[j] + z[i][1])

        return max(dp)
```
* [Medium] 1626. Best Team With No Conflicts

### Word Break
```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [False] * N    
        for i in range(N):
            for w in wordDict:
                w_size = len(w)
                if w == s[i - w_size + 1:i + 1] and (dp[i - w_size] or i - w_size == -1):
                    dp[i] = True
        return dp[-1]

import functools
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)

        @functools.lru_cache(None)
        def dfs(i):
            if i == N:
                return True
            rst = False
            for w in wordDict:
                w_size = len(w)
                if i + w_size <= N and s[i:i + w_size] == w:
                    rst = rst | dfs(i + w_size)
            return rst

        return dfs(0)
```
* [Medium] 139. Word Break

### Maximum Length of Subarray With Positive Product
```python
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = pos = neg = 0
        for x in nums: 
            if x > 0: pos, neg = 1 + pos, 1 + neg if neg else 0
            elif x < 0: pos, neg = 1 + neg if neg else 0, 1 + pos
            else: pos = neg = 0 # reset 
            ans = max(ans, pos)
        return ans
```
* [Medium] 1567. Maximum Length of Subarray With Positive Product

### Campus Bikes
```python
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        M, N = len(bikes), len(workers)
        manhattanDist = lambda i,j: abs(workers[i][0]-bikes[j][0])+abs(workers[i][1]-bikes[j][1])
        dist = []
        for i in range(N):
            dist.append([])
            for j in range(M):
                dist[-1].append(manhattanDist(i,j))

        @functools.lru_cache(None)
        def dp(remainingBikes, i):
            if i == N:
                return 0            
            rst = math.inf
            for j in range(len(remainingBikes)):
                rst = min(rst, dist[i][remainingBikes[j]] + dp(remainingBikes[:j] + remainingBikes[j+1:], i+1))
            return rst

        return dp(tuple(range(M)), 0)
```
* [Lock] [Medium] 1066. Campus Bikes II

### 2 state array
```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res1 = [0 for i in range(len(nums))]
        res2 = [0 for i in range(len(nums))]
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if i == 0:
                res1[i] = nums[i]
                res2[i] = nums[i]
            else:
                res1[i] = max(nums[i], nums[i]*res1[i-1], nums[i]*res2[i-1])
                res2[i] = min(nums[i], nums[i]*res1[i-1], nums[i]*res2[i-1])

        return max(max(res1), max(res2))

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max_so_far = min_so_far = nums[0]
        for i in range(1, len(nums)):
            candidates = (nums[i], max_so_far*nums[i], min_so_far*nums[i])
            max_so_far = max(candidates)
            min_so_far = min(candidates)
            ans = max(ans, max_so_far)

        return ans   
```
* [Medium] 152. Maximum Product Subarray

### Longest Fibonacci Subsequence
```python
class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        N = len(A)
        index = {k: i for i, k in enumerate(A)}
        dp = [[2]*N for _ in range(N)]
        ans = 0
        for k in range(N):
            for j in range(k):
                if A[k] - A[j] in index:
                    i = index[A[k] - A[j]]
                    if i < j:
                        dp[j][k] = dp[i][j] + 1
                        ans = max(ans, dp[j][k])
                    
        return ans if ans >=3 else 0
    
class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        N = len(A)
        if N <= 2:
            return N
        index = {v: i for i, v in enumerate(A)}
        ans = 0

        @functools.lru_cache(None)
        def dfs(i, j):
            if (A[i] + A[j]) not in A:
                return 0
            return 1 + dfs(j, index[A[i] + A[j]])

        for i in range(N-2):
            for j in range(i+1, N-1):
                if A[i] + A[j] in index:
                    ans = max(ans, dfs(i, j))

        return ans + 2 if ans >= 1 else 0
```
* [Medium] [Solution] 873. Length of Longest Fibonacci Subsequence

### Only Top-Down DP
```python
from functools import lru_cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
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
* [Medium] [Solution] 877. Stone Game

### Bottom-up
```python
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        for i in range(len(s1) - 1, -1, -1):
            dp[i][len(s2)] = dp[i+1][len(s2)] + ord(s1[i])
        for j in range(len(s2) - 1, -1, -1):
            dp[len(s1)][j] = dp[len(s1)][j+1] + ord(s2[j])

        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s2) - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j] + ord(s1[i]),
                                   dp[i][j+1] + ord(s2[j]))

        return dp[0][0]
```
* [Medium] [Solution] 712. Minimum ASCII Delete Sum for Two Strings

### Unique Paths
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            ans[0][i] = 1
        for i in range(n):
            ans[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                ans[i][j] = ans[i-1][j] + ans[i][j-1]

        return ans[n-1][m-1]  

import functools
class Solution:
    @functools.lru_cache(None)
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1: return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
```
* [Medium] 62. Unique Paths

### Perfect Squares
```python
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0

        dp = [0] * (n+1)
        for i in range(1,n+1):
            dp[i] = min([dp[i - j*j] for j in range(1, int(i**.5)+1)]) + 1
        return dp[n]

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0

        @functools.lru_cache(None)
        def dfs(i):
            if i <= 0:
                return 0
            return min(dfs(i - j**2) + 1 for j in range(int(i**.5), 0, -1))

        return dfs(n)
```
* [Medium] 279. Perfect Squares

### Prefix/Range sum
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
* [Medium] [Solution] 304. Range Sum Query 2D - Immutable

### Floyd Warshall's shortest path
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
* [Medium] 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance

### Profit - 2 Option(Buy/Sell)
```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sell, buy = 0, float('-inf')
        for i in range(len(prices)):
            buy = max(buy, sell - prices[i])
            sell = max(sell, buy + prices[i] - fee)
        return sell
```
* [Medium] [Solution] 714. Best Time to Buy and Sell Stock with Transaction Fee

### Profit - 2 Option(Buy/Sell)
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        if N <=1 :
            return 0
        cash = [0]*N
        cash[1] = max(0, prices[1]-prices[0])
        hold = [float('-inf')] * N
        hold[0] = [-prices[0]]
        hold[1] = max(-prices[0], -prices[1])
        for day in range(2,len(prices)):
            cash[day] = max(cash[day-1], hold[day-1]+prices[day])
            hold[day] = max(hold[day-1], cash[day-2]-prices[day])

        return cash[-1]
```
* [Medium] 309. Best Time to Buy and Sell Stock with Cooldown

### 2 Option (Up/Dow)
```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        up = down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1

        return max(up, down)

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 0: return 0

        @functools.lru_cache(None)
        def dfs(i, isUp):
            if i == N-1: return 1
            if isUp:
                if nums[i+1] > nums[i]:
                    return 1 + dfs(i+1, False)
                else:
                    return dfs(i+1, True)
            else:
                if nums[i+1] < nums[i]:
                    return 1 + dfs(i+1, True)
                else:
                    return dfs(i+1, False)

        return max(dfs(0, True), dfs(0, False))

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 2:
            return N

        prevdiff = nums[1] - nums[0];
        count = 2 if prevdiff != 0 else 1
        for i in range(2, N):
            diff = nums[i] - nums[i - 1]
            if ((diff > 0 and prevdiff <= 0) or (diff < 0 and prevdiff >= 0)):
                count += 1
                prevdiff = diff

        return count
```
* [Medium] [Solution] 376. Wiggle Subsequence

### Only Top-Down
```python
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        @lru_cache(None)
        def isPalindrome(l, r):  # l, r inclusive
            if l >= r: return True
            if s[l] != s[r]: return False
            return isPalindrome(l+1, r-1)
        
        @lru_cache(None)
        def dp(i):  # s[i..n-1]
            if i == n:
                return 0
            ans = math.inf
            for j in range(i, n):
                if (isPalindrome(i, j)):
                    ans = min(ans, dp(j+1) + 1)
            return ans
        
        return dp(0) - 1
```
[Hard] 132. Palindrome Partitioning II

### Digital DP
```python
class Solution:
    def findIntegers(self, num: int) -> int:
        num = bin(num+1)[2:]
        n = len(num)
        fibo = [1, 2]
        for _ in range(n-1):
            fibo.append(fibo[-1] + fibo[-2])
        res = 0
        for i in range(n):
            v = num[i:i+2]
            if v == '11':
                res += fibo[n-i]
                break
            elif v == '10':
                res += fibo[n-i-1]
            elif v == '1':
                res += 1
        return res

class Solution:
    def findIntegers(self, num: int) -> int:
        
        @lru_cache(None)
        def dfs(num, prev):
            if not num or num == "0":
                return 1
            a = str(int(num))
            if a != num:
                # "000xxx" -> "xxx"
                return dfs(a, 0)
            if not prev:
                # fist num can take 1 or 0
                return dfs(num[1:], 1) + dfs("1" * (len(num)-1), 0)
            else:
                # fist num can take only 0 since previous num is 1
                return dfs("1" * (len(num) - 1), 0)
            
        return dfs(bin(num)[2:], 0)
```
* [Hard] [Solution] 600. Non-negative Integers without Consecutive Ones.md

### 2 state
```python
class Solution:
    def numDecodings(self, s: str) -> int:
        M = 10**9 + 7  
        dp = [None] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 9 if s[0] == '*' else 0 if s[0] == '0' else 1;
        for i in range(1, len(s)):
            if s[i] == '*':
                dp[i + 1] = 9 * dp[i]
                if s[i - 1] == '1':
                    dp[i + 1] = (dp[i + 1] + 9 * dp[i - 1]) % M
                elif s[i - 1] == '2':
                    dp[i + 1] = (dp[i + 1] + 6 * dp[i - 1]) % M
                elif s[i - 1] == '*':
                    dp[i + 1] = (dp[i + 1] + 15 * dp[i - 1]) % M
            else:
                dp[i + 1] = dp[i] if s[i] != '0' else 0
                if s[i - 1] == '1':
                    dp[i + 1] = (dp[i + 1] + dp[i - 1]) % M
                elif s[i - 1] == '2' and s[i] <= '6':
                    dp[i + 1] = (dp[i + 1] + dp[i - 1]) % M
                elif s[i - 1] == '*':
                    dp[i + 1] = (dp[i + 1] + (2 if s[i] <= '6' else 1) * dp[i - 1]) % M
                       
        return dp[len(s)] % M

class Solution:
    def numDecodings(self, s: str) -> int:
        M = 10**9 + 7  
        first, second = 1, 9 if s[0] == '*' else 0 if s[0] == '0' else 1
        for i in range(1, len(s)):
            temp = second
            if s[i] == '*':
                second = 9 * second
                if s[i - 1] == '1':
                    second = (second + 9 * first) % M
                elif s[i - 1] == '2':
                    second = (second + 6 * first) % M
                elif s[i - 1] == '*':
                    second = (second + 15 * first) % M
            else:
                second = second if s[i] != '0' else 0
                if s[i - 1] == '1':
                    second = (second + first) % M
                elif s[i - 1] == '2' and s[i] <= '6':
                    second = (second + first) % M
                elif s[i - 1] == '*':
                    second = (second + (2 if s[i] <= '6' else 1) * first) % M
            first = temp
            
        return second
```
* [Hard] [Solution] 639. Decode Ways II.md

### Count
```python
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        d = {
            'a': ['e'],
            'e': ['a', 'i'],
            'i': ['a', 'e', 'o', 'u'],
            'o': ['i', 'u'],
            'u': ['a']
        }
        
        @functools.lru_cache(None)
        def dp(i, c):
            if i == n-1:
                return 1
            return sum([dp(i+1, _) for _ in d[c]])
            
        return sum([dp(0, _) for _ in list(d.keys())]) % MOD
```
* [Hard] 1220. Count Vowels Permutation.md

### Prefix Sum, left and right scan
```python
class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Concept - Just do what the problem is saying, we can 
        # fill our result array with one, now the first requirement
        # is fulfilled and for 2nd requirement, there will be 2 cases
        # 1 - Rating at i is greater than at i-1 --> Forward Pass
        # 2 - Rating at i is greater than i + 1 --> Backward Pass
        
        
        # Condition-1 Fulfilled as we gave 1 candy to everyone
        candies = [1] * len(ratings)
        
        # Calculate the candies needed to fulfill left condition     
        # We drop the 0th element as nothing is located left to it
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        # Calculate the candies needed to fulfill right condition  
        # We drop the last element as nothing is located right to it
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        
        # Take the summation --> Minimum candies
        return sum(candies)

class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans = down = up = 0
        for i in range(len(ratings)):
            if not i or ratings[i-1] < ratings[i]:
                if down: down, up = 0, 1
                up += 1
                ans += up
            elif ratings[i-1] == ratings[i]: 
                down, up = 0, 1
                ans += 1
            else:
                down += 1
                ans += down if down < up else down+1
        return ans
```
* [Hard] [Solution] 135. Candy.md

### Brute Force, Backtracking
```python
import functools
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        M, N = len(s1), len(s2)

        @functools.lru_cache(None)
        def is_Interleave(i, j, k):
            if i == M:
                return s2[j:] == s3[k:]
            if j == N:
                return s1[i:] == s3[k:]
            ans = False
            if s3[k] == s1[i] and is_Interleave(i + 1, j, k + 1) \
               or s3[k] == s2[j] and is_Interleave(i, j + 1, k + 1):
                ans = True
            return ans

        return is_Interleave(0, 0, 0)
    
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        M, N = len(s1), len(s2)
        if len(s3) != M + N:
            return False
        dp = [[False]*(N + 1) for _ in range(M + 1)]
        for i in range(M + 1):
            for j in range(N + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                else:
                    dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1] \
                    or dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]

        return dp[M][N]

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        M, N = len(s1), len(s2)
        if len(s3) != M + N:
            return False
        dp = [False]*(N + 1)
        for i in range(M + 1):
            for j in range(N + 1):
                if i == 0 and j == 0:
                    dp[j] = True
                elif i == 0:
                    dp[j] = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    dp[j] = dp[j] and s1[i - 1] == s3[i + j - 1]
                else:
                    dp[j] = dp[j] and s1[i - 1] == s3[i + j - 1] \
                    or dp[j - 1] and s2[j - 1] == s3[i + j - 1]

        return dp[N]
```
* [Hard] [Solution] 97. Interleaving String

### jump index
```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)

        @functools.lru_cache(None)
        def dp(i):
            if i == N-1:
                return 0
            elif i > N-1 or nums[i] == 0:
                return float('inf')
            return 1 + min(dp(j) for j in range(i + 1, i + nums[i] + 1))

        return dp(0)
```
* [Hard] 45. Jump Game II

### One can win if he/she can force the other one onto a losing state
```python
class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        @lru_cache(maxsize=None)
        def dfs(remain):
            if remain == 0:
                return False

            sqrt_root = int(remain**0.5)
            for i in range(1, sqrt_root+1):
                # if there is any chance to make the opponent lose the game in the next round,
                #  then the current player will win.
                if not dfs(remain - i*i):
                    return True

            return False

        return dfs(n)
    
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False]*(n+1)
        for i in range(1, n+1):
            for k in range(1, int(i**0.5)+1):
                if dp[i-k*k] == False:
                    dp[i] = True
                    break
        return dp[n]

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        squares = [i*i for i in range(int(n**0.5), 0, -1)]

        @functools.lru_cache(None)
        def alice_wins(stones=n, alice_plays=True):
            if not stones: return not alice_plays
            criterion = any if alice_plays else all
            return criterion(alice_wins(stones - move, not alice_plays) for move in squares if stones >= move)

        return alice_wins()
```
* [Hard] 1510. Stone Game IV

### Range Sum, Binary Search
```python
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        def maxSumSubarray(arr):
            sub_s_max = float('-inf')
            s_curr = 0
            prefix_sums = [float('inf')]
            for x in arr:
                bisect.insort(prefix_sums, s_curr)
                s_curr += x
                i = bisect.bisect_left(prefix_sums, s_curr - k)
                sub_s_max = max(sub_s_max, s_curr - prefix_sums[i])
            return sub_s_max
        
        m, n = len(matrix), len(matrix[0])
        for x in range(m):
            for y in range(n - 1):
                matrix[x][y+1] += matrix[x][y]
        res = float('-inf')
        for y1 in range(n):
            for y2 in range(y1, n):
                arr = [matrix[x][y2] - (matrix[x][y1-1] if y1 > 0 else 0) for x in range(m)]
                res = max(res, maxSumSubarray(arr))
        return res
```
* [Hard] 363. Max Sum of Rectangle No Larger Than K

### Brute Force DP, Longest Increasing Subsequence
```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        N = len(nums)
        dp = [0 for _ in range(N)]
        dp[0] = 1
        maxans = 1
        for i in range(1, N):
            maxval = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    maxval = max(maxval, dp[j])
            dp[i] = maxval + 1
            maxans = max(maxans, dp[i])
        return maxans
```
* [Medium] [Solution] 300. Longest Increasing Subsequence

### Longest Common Subarray
```python
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    memo[i+1][j+1] = memo[i][j]+1
        return max(max(row) for row in memo)
```
* [Medium] [Solution] 718. Maximum Length of Repeated Subarray

### Longest Common Subsequence
```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)

        @functools.lru_cache(None)
        def dfs(i, j):
            if i == M or j == N:
                return 0
            if text1[i] == text2[j]:
                return 1 + dfs(i+1, j+1)
            else:
                return max(dfs(i+1, j), dfs(i, j+1))

        return dfs(0, 0)
    
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M = len(text1)
        N = len(text2)
        dp = [[0]*(N+1) for _ in range(M+1)]

        for i in range(1, M+1):
            for j in range(1, N+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[M][N]
```
* [Medium] 1143. Longest Common Subsequence

### Longest Common Subsequence
```python
import functools
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)

        @functools.lru_cache(None)
        def dp(i, j):
            if i == 0 or j == 0:
                return i+j
            elif word1[i-1] == word2[j-1]:
                return dp(i-1, j-1)
            else:
                return 1 + min(dp(i-1, j), dp(i, j-1))

        return dp(M, N)
```
* [Medium] [Solution] 583. Delete Operation for Two Strings

### longest increasing number with count
```python
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1: return N
        lengths = [0] * N #lengths[i] = longest ending in nums[i]
        counts = [1] * N #count[i] = number of longest ending in nums[i]

        for j, num in enumerate(nums):
            for i in range(j):
                if nums[i] < nums[j]:
                    if lengths[i] >= lengths[j]:
                        lengths[j] = 1 + lengths[i]
                        counts[j] = counts[i]
                    elif lengths[i] + 1 == lengths[j]:
                        counts[j] += counts[i]

        longest = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)
```
* [Medium] [Solution] 673. Number of Longest Increasing Subsequence

### Sum of Probability
```python
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:

        @functools.lru_cache(None)
        def dfs(k, r, c):
            if r < 0 or r >= N or c < 0 or c >= N:
                return 0
            if k == 0:
                return 1
            shift = [(-1, -2),
                     (-1, 2),
                     (1, -2),
                     (1, 2),
                     (-2, -1),
                     (-2, 1),
                     (2, -1),
                     (2, 1)
                    ]
            return sum(dfs(k-1, r+i, c+j) for i, j in shift) / 8

        return dfs(K, r, c)

class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        dp = [[0] * N for _ in range(N)]
        dp[r][c] = 1
        for _ in range(K):
            dp2 = [[0] * N for _ in range(N)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for dr, dc in ((2,1),(2,-1),(-2,1),(-2,-1),
                                   (1,2),(1,-2),(-1,2),(-1,-2)):
                        if 0 <= r + dr < N and 0 <= c + dc < N:
                            dp2[r+dr][c+dc] += val / 8.0
            dp = dp2

        return sum(map(sum, dp))
```
* [Medium] [Solution] 688. Knight Probability in Chessboard

### Greedy, Count on every level
```python
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        dp = 0;
        sum_ = 0;
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp += 1
                sum_ += dp
            else:
                dp = 0
        return sum_

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        N = len(A)
        ans = 0

        @functools.lru_cache(None)
        def dfs(i):
            nonlocal ans
            if i < 2: return 0
            rst = 0
            if A[i-1] - A[i-2] == A[i] - A[i-1]:
                rst = 1 + dfs(i-1)
                ans += rst
            else:
                dfs(i-1)
            return rst 

        dfs(N-1)
        return ans
```
* [Medium] [Solution] 413. Arithmetic Slices

### Maximal Square
```python
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        rows, cols = len(matrix), len(matrix[0]) if matrix else 0
        dp = [[0]*(cols + 1) for _ in range(rows + 1)]
        maxsqlen = 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(min(dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1]) + 1
                    maxsqlen = max(maxsqlen, dp[i][j])

        return maxsqlen **2
    
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        R, C = len(matrix), len(matrix[0]) if matrix else 0

        @functools.lru_cache(None)
        def dp(i, j):
            if i < 0 or j < 0:
                return 0, 0

            up = dp(i, j-1)
            upleft = dp(i-1, j-1)
            left = dp(i-1, j)
            minimum = min(up[0], upleft[0], left[0])
            best = max(up[1], upleft[1], left[1])

            if matrix[i][j] == '1':
                return (minimum + 1, max(best, minimum + 1))
            return (0, max(best, 0))

        return dp(R-1, C-1)[1]**2
```
* [Medium] [Solution] 221. Maximal Square

### Dynamic Programming with Binary Search, insertion sort
```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [float('inf') for _ in range(N)]
        length = 0
        for num in nums:
            i = bisect.bisect_left(dp, num)
            dp[i] = num
            if i == length:
                length += 1
        return length
```
* [Medium] [Solution] 300. Longest Increasing Subsequence

### Using Recursion with memoization
```python
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def shopping(needs):
            if memo[tuple(needs)]:
                return memo[tuple(needs)]
            res = dot(needs, price)
            for s in special:
                clone = needs.copy()
                for j in range(len(needs)):
                    diff = clone[j] - s[j]
                    if diff < 0:
                        break
                    clone[j] = diff
                    if j == len(needs)-1:
                        res = min(res, s[j+1] + shopping(clone))
            memo[tuple(needs)] = res
            return res

        def dot(a, b):
            sum_ = 0;
            for i in range(len(a)):
                sum_ += a[i] * b[i]
            return sum_

        memo = collections.defaultdict(int)
        return shopping(needs)
```
* [Medium] [Solution] 638. Shopping Offers

### Dynamic Programming on Subsets of Input
```python
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, rem = divmod(sum(nums), k)
        if rem or max(nums) > target: return False

        @functools.lru_cache(None)
        def search(used, todo):
            if todo == 0:
                return True
            targ = (todo - 1) % target + 1  # maximum value that can be chosen so as to not cross a multiple of target
            return any(search(used | (1<<i), todo - num)
                                 for i, num in enumerate(nums)
                                 if (used >> i) & 1 == 0 and num <= targ)

        return search(0, target * k)
```
* [Medium] [Solution] 698. Partition to K Equal Sum Subsets

### Direction Buffer
```python
class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        banned = {tuple(mine) for mine in mines}
        dp = [[0] * N for _ in range(N)]
        ans = 0
        
        for r in range(N):  # for every row
            count = 0
            for c in range(N):  # from left to right
                count = 0 if (r,c) in banned else count+1
                dp[r][c] = count
            
            count = 0
            for c in range(N-1, -1, -1):  # from right to left
                count = 0 if (r,c) in banned else count+1
                if count < dp[r][c]: dp[r][c] = count
        
        for c in range(N):  # for every column
            count = 0
            for r in range(N):  # from top - bottom
                count = 0 if (r,c) in banned else count+1
                if count < dp[r][c]: dp[r][c] = count
            
            count = 0
            for r in range(N-1, -1, -1):  from bottom to up
                count = 0 if (r, c) in banned else count+1
                if count < dp[r][c]: dp[r][c] = count
                if dp[r][c] > ans: ans = dp[r][c]  # update an
        
        return ans
```
* [Medium] [Solution] 764. Largest Plus Sign

### Counting Bits
```python
class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]*(num+1)
        for i in range(num+1):
            ans[i] = (i&1) + ans[i>>1]
        return ans
    
class Solution:
    def countBits(self, num: int) -> List[int]:

        @functools.lru_cache(None)
        def dfs(n):
            if n == 0:
                return 0
            return (n&1) + dfs(n>>1)

        return [dfs(i) for i in range(num+1)]
```
* [Medium] 338. Counting Bits

### Largest Divisible Subset
```python
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        if len(nums) ==0: return []
        result = [nums[0]]
        dp = [[nums[i]] for i in range(len(nums))]
        for i in range(len(dp)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(dp[j]) + 1 > len(dp[i]):
                        dp[i] = dp[j] + [nums[i]]
            if len(dp[i]) > len(result):
                result = dp[i]
        return result
```
* [Medium] 368. Largest Divisible Subset

### State Combination
```python
class Solution:
    def numTilings(self, N: int) -> int:
        MOD = 10**9 + 7
        A = [0 for i in range(N+1)]
        B = [0 for i in range(N+1)]
        C = [0 for i in range(N+1)]
        A[0] = 1
        for i in range(1, N+1):
            A[i] = (B[i-1] + C[i-1] + A[i-1] + (A[i-2] if i >=2 else 0)) % MOD
            B[i] = (C[i-1] + (A[i-2] if i >=2 else 0)) % MOD
            C[i] = (B[i-1] + (A[i-2] if i >=2 else 0)) % MOD
        return A[-1]
```
* [Medium] 790. Domino and Tromino Tiling

### Swap / not swap
```python
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n1, s1 = 0, 1  # not-swap, swap
        for i in range(1, len(A)):
            n2 = s2 = float("inf")
            if A[i-1] < A[i] and B[i-1] < B[i]:
                n2 = min(n2, n1)  # not swap
                s2 = min(s2, s1 + 1)  # swap
            if A[i-1] < B[i] and B[i-1] < A[i]:
                n2 = min(n2, s1)  # prev swap
                s2 = min(s2, n1 + 1)  # swap

            n1, s1 = n2, s2

        return min(n1, s1)
```
* [Medium] [Solution] 801. Minimum Swaps To Make Sequences Increasing

### Largest Sum of Averages
```python
class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        N = len(A)

        @functools.lru_cache(None)
        def dfs(k, i):
            if i >= N:
                return 0
            if k == 1:
                score = sum(A[i:]) / (N-i)
            else:
                score = max(sum(A[i:j]) / (j-i) + dfs(k-1, j) for j in range(i+1, N-k+2))
            return score

        return dfs(K, 0)
```
* [Medium] [Solution] 813. Largest Sum of Averages

### Falling path
```python
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        while len(A) >= 2:
            row = A.pop()            
            for i in range(len(row)):
                A[-1][i] += min(row[max(0,i-1): min(len(row), i+2)])
        return min(A[0])
```
* [Medium] [Solution] 931. Minimum Falling Path Sum

### Knight move
```python
class Solution:
    def knightDialer(self, N: int) -> int:
        MOD = 10**9 + 7
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
                     [1,7,0],[2,6],[1,3],[2,4]]

        dp = [1] * 10
        for hops in range(N-1):
            dp2 = [0] * 10
            for node, count in enumerate(dp):
                for nei in moves[node]:
                    dp2[nei] += count
                    dp2[nei] %= MOD
            dp = dp2
        return sum(dp) % MOD
```
* [Medium] [Solution] 935. Knight Dialer

### Minimum Cost For Tickets
```python
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N = len(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i): # How much money to do days[i]+
            if i >= N: return 0

            ans = float('inf')
            j = i
            for c, d in zip(costs, durations):
                while j < N and days[j] < days[i] + d:
                    j += 1
                ans = min(ans, dp(j) + c)

            return ans

        return dp(0)
```
* [Medium] [Solution] 983. Minimum Cost For Tickets

### All possible sum
```python
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s = {0}
        for st in stones:
            tmp = set()
            for i in s:
                tmp.add(abs(i + st))
                tmp.add(abs(i - st))
            s = tmp
        return min(s) if len(s) > 0 else 0

    
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        N = len(stones)

        @functools.lru_cache(None)
        def dp(i, s): #arguments are stone index and current sum
            if i == N: #end of array, return the current sum (abs)
                return abs(s)
            return min(dp(i+1, s + stones[i]), dp(i+1, s - stones[i])) #try summing or subtracting each stone value

        return dp(0, 0)
```
* [Medium] 1049. Last Stone Weight II

### Range DP
```python
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        N = len(clips)
        dp = [float('inf') for _ in range(T+1)]
        dp[0] = 0
        for videoLen in range(1, T+1):
            for clipStart, clipEnd in clips:
                if clipStart <= videoLen <= clipEnd:
                    dp[videoLen] = min(dp[videoLen], 1 + dp[clipStart])

        return -1 if dp[T] == float('inf') else dp[T]

class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        N = len(clips)
        clips.sort()

        @functools.lru_cache(None)
        def dp (i, t):
            if t >= T:
                return 0
            rst = float('inf')
            for j in range(i+1, N):
                clipStart = clips[j][0]
                clipEnd = clips[j][1]
                if clipStart <= t <= clipEnd:
                    rst = min(rst, 1 + dp(j, clipEnd))
            return rst

        ans = dp(-1, 0)

        return -1 if ans == float('inf') else ans
```
* [Medium] 1024. Video Stitching

### Circle DP
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1: return nums[0]
        dp, dp2 = [0]*N, [0]*N
        dp[1] = nums[0]
        for i in range(1, N-1):
            dp[i+1] = max(dp[i], dp[i-1] + nums[i])
        dp2[1] = nums[1]
        for i in range(2, N):
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i])

        return max(dp[-1], dp2[-1])

class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 0:
            return 0
        elif N == 1:
            return nums[0]
        elif N == 2:
            return max(nums)

        @functools.lru_cache(None)
        def dfs(i, j):
            if i >= j:
                return 0
            return max(nums[i] + dfs(i+2, j), dfs(i+1, j))

        #rob the first house, can't rob the last house
        return max(dfs(0, N-1), dfs(1, N))
```
* [Medium] 213. House Robber II

### Probability
```python
class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        N = len(prob)

        @functools.lru_cache(None)
        def dp(n, k):
            if k > n or k < 0: return 0
            if n == 0: return 1
            return dp(n-1, k-1)*prob[n-1] + dp(n-1, k)*(1-prob[n-1])

        return dp(N, target)
```
* [Medium] 1230. Toss Strange Coins

### Count
```python
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if  matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1] ,matrix[i-1][j-1]) + 1
        return sum([sum(x) for x in matrix])
```
* [Medium] 1277. Count Square Submatrices with All Ones

### Uncrossed Lines
```python
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        M, N = len(A), len(B)
        dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
        for i in range(1, M+1):
            for j in range(1, N+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        M, N = len(A), len(B)

        @functools.lru_cache(None)
        def dp(i, j):
            if i == M or j == N:
                return 0
            if A[i] == B[j]:
                return dp(i+1, j+1) + 1
            else:
                return max(dp(i+1, j), dp(i, j+1))

        return dp(0, 0)
```
* [Medium] 1035. Uncrossed Lines

### Brute Force
```python
class Solution(object):
    def shortestSuperstring(self, A):
        N = len(A)

        # Populate overlaps
        overlaps = [[0] * N for _ in xrange(N)]
        for i, x in enumerate(A):
            for j, y in enumerate(A):
                if i != j:
                    for ans in xrange(min(len(x), len(y)), -1, -1):
                        if x.endswith(y[:ans]):
                            overlaps[i][j] = ans
                            break

        # dp[mask][i] = most overlap with mask, ending with ith element
        dp = [[0] * N for _ in xrange(1<<N)]
        parent = [[None] * N for _ in xrange(1<<N)]
        for mask in xrange(1, 1 << N):
            for bit in xrange(N):
                if (mask >> bit) & 1:
                    # Let's try to find dp[mask][bit].  Previously, we had
                    # a collection of items represented by pmask.
                    pmask = mask ^ (1 << bit)
                    if pmask == 0: continue
                    for i in xrange(N):
                        if (pmask >> i) & 1:
                            # For each bit i in pmask, calculate the value
                            # if we ended with word i, then added word 'bit'.
                            value = dp[pmask][i] + overlaps[i][bit]
                            if value > dp[mask][bit]:
                                dp[mask][bit] = value
                                parent[mask][bit] = i

        # Answer will have length sum(len(A[i]) for i) - max(dp[-1])
        # Reconstruct answer:

        # Follow parents down backwards path that retains maximum overlap
        perm = []
        mask = (1<<N) - 1
        i = max(xrange(N), key = dp[-1].__getitem__)
        while i is not None:
            perm.append(i)
            mask, i = mask ^ (1<<i), parent[mask][i]

        # Reverse path to get forwards direction; add all remaining words
        perm = perm[::-1]
        seen = [False] * N
        for x in perm:
            seen[x] = True
        perm.extend([i for i in xrange(N) if not seen[i]])

        # Reconstruct answer given perm = word indices in left to right order
        ans = [A[perm[0]]]
        for i in xrange(1, len(perm)):
            overlap = overlaps[perm[i-1]][perm[i]]
            ans.append(A[perm[i]][overlap:])

        return "".join(ans)
```
* [Hard] [Solution] 943. Find the Shortest Superstring

### DP + Binary Search
```python
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        starts = [x for x,y,z in events]

        def bs(idx):
            return bisect_right(starts, idx)

        @lru_cache(None)
        def dp(idx, k):
            if k == 0 or idx >= len(events):
                return 0
            return max(dp(idx+1, k), events[idx][2] + dp(bs(events[idx][1]), k-1))

        return dp(0,k)

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])
        dp, dp2 = [[0, 0]], [[0, 0]]
        for _ in range(k):
            for s, e, v in events:
                i = bisect.bisect(dp, [s]) - 1
                if dp[i][1] + v > dp2[-1][1]:
                    dp2.append([e, dp[i][1] + v])
            dp, dp2 = dp2, [[0, 0]]
        return dp[-1][-1]
```
* [Hard] 1751. Maximum Number of Events That Can Be Attended II.md

### 2 Group DP with bitmask
```python
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        sz1, sz2 = len(cost), len(cost[0])
        min_sz2 = [min([cost[i][j] for i in range(sz1)]) for j in range(sz2)]

        @lru_cache(None)
        def dfs(i: int, mask: int):
            res = 0 if i >= sz1 else float('inf')
            if i >= sz1:
                for j in range(sz2):
                    if mask & (1 << j) == 0:
                        res += min_sz2[j]
            else:
                for j in range(sz2):
                    res = min(res, cost[i][j] + dfs(i + 1, mask | (1 << j)))
            return res

        return dfs(0, 0)
```
* [[[Hard] 1595. Minimum Cost to Connect Two Groups of Points](%5BHard%5D%201595.%20Minimum%20Cost%20to%20Connect%20Two%20Groups%20of%20Points.md)

### Character match
```python
import functools
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @functools.lru_cache(None)
        def dp(i, j):
            if j == len(p):
                ans = i == len(s)
            else:
                first_match = i < len(s) and p[j] in {s[i], '.'}
                if j+1 < len(p) and p[j+1] == '*':
                    ans = dp(i, j+2) or first_match and dp(i+1, j)
                else:
                    ans = first_match and dp(i+1, j+1)
            return ans

        return dp(0, 0)
```
* [Hard] [Solution] 10. Regular Expression Matching

### Coin Change
```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
                
        return dp[-1]

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        
        @functools.lru_cache(None)
        def dp(i, t):
            if (t == amount):
                return 1
            if t > amount or i == N:
                return 0

            return dp(i, t + coins[i]) + dp(i + 1, t)
        
        return dp(0, 0)

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0: return 1
        N = len(coins)
        coins.sort(reverse=True)
        
        @functools.lru_cache(None)
        def dp(i, t):
            if t == amount:
                return 1
            if i >= N or t > amount:
                return 0
            return sum(dp(ni, t + coins[ni]) for ni in range(i, N))
        
        return dp(0, 0)
```
* [Medium] 518. Coin Change 2

### factor dependency
```python
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        N = len(arr)
        arr.sort()
        dp = [1] * N
        index = {x: i for i, x in enumerate(arr)}
        for i, x in enumerate(arr):
            for j in range(i):
                if x % arr[j] == 0: #arr[j] will be left child
                    right = x // arr[j]
                    if right in index:
                        dp[i] += dp[j] * dp[index[right]]
                        dp[i] %= MOD

        return sum(dp) % MOD

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        s_arr, N = set(arr), 10**9 + 7

        @lru_cache(None)
        def dp(num):
            ans = 1
            for cand in s_arr:
                if num % cand == 0 and num//cand in s_arr:
                    ans += dp(cand)*dp(num//cand)
            return ans

        return sum(dp(num) for num in s_arr) % N
```
* [Medium] [Solution] 823. Binary Trees With Factors

### Reamining amount
```python
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        A = [[0] * k for k in range(1, 102)]
        A[0][0] = poured
        for r in range(query_row + 1):
            for c in range(r+1):
                q = (A[r][c] - 1.0) / 2.0
                if q > 0:
                    A[r+1][c] += q
                    A[r+1][c+1] += q

        return min(1, A[query_row][query_glass])
    
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        excess = lambda x: max(0, x-1)

        @lru_cache(None)
        def f(i,j):
            if (i,j) == (0,0): return poured
            if j < 0 or j > i: return 0
            return (excess(f(i-1, j-1)) + excess(f(i-1, j))) / 2

        return min(f(query_row, query_glass),1)
````
* [Medium] [Solution] 799. Champagne Tower

### Row by row
```python
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        @lru_cache(None)
        def dp(row, col1, col2):
            if col1 < 0 or col1 >= n or col2 < 0 or col2 >= n:
                return -inf
            # current cell
            result = 0
            result += grid[row][col1]
            if col1 != col2:
                result += grid[row][col2]
            # transition
            if row != m-1:
                result += max(dp(row+1, new_col1, new_col2)
                              for new_col1 in [col1, col1+1, col1-1]
                              for new_col2 in [col2, col2+1, col2-1])
            return result

        return dp(0, 0, n-1)
    
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[[0]*n for _ in range(n)] for __ in range(m)]

        for row in reversed(range(m)):
            for col1 in range(n):
                for col2 in range(n):
                    result = 0
                    # current cell
                    result += grid[row][col1]
                    if col1 != col2:
                        result += grid[row][col2]
                    # transition
                    if row != m-1:
                        result += max(dp[row+1][new_col1][new_col2]
                                      for new_col1 in [col1, col1+1, col1-1]
                                      for new_col2 in [col2, col2+1, col2-1]
                                      if 0 <= new_col1 < n and 0 <= new_col2 < n)
                    dp[row][col1][col2] = result
        return dp[0][0][n-1]
```
* [Hard] 1463. Cherry Pickup II

### DP Top Down with Preprocessing count
```python
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(words[0]), len(target)
        charAtIndexCnt = collections.defaultdict(int)
        for word in words:
            for i, c in enumerate(word):
                charAtIndexCnt[(c, i)] += 1  # Count the number of character `c` at index `i` of all words

        @lru_cache(None)
        def dp(k, i):
            if i == n:  # Formed a valid target
                return 1
            if k == m:  # Reached to length of words[x] but don't found any result
                return 0
            c = target[i]
            ans = dp(k + 1, i)  # Skip k_th index of words
            if charAtIndexCnt[(c, k)] > 0: # Take k_th index of words if found character `c` at index k_th
                ans += dp(k + 1, i + 1) * charAtIndexCnt[(c, k)]
                ans %= MOD
            return ans

        return dp(0, 0)
```
* [Hard] 1639. Number of Ways to Form a Target String Given a Dictionary

### Best Time to Buy and Sell Stock
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t1_cost, t2_cost = float('inf'), float('inf')
        t1_profit, t2_profit = 0, 0

        for price in prices:
            # the maximum profit if only one transaction is allowed
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price - t1_cost)
            # reinvest the gained profit in the second transaction
            t2_cost = min(t2_cost, price - t1_profit)
            t2_profit = max(t2_profit, price - t2_cost)

        return t2_profit
```
* [Hard] [Solution] 123. Best Time to Buy and Sell Stock III

### Next Array Variation
```python
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        N = len(S)
        nxt = [None] * N
        last = [-1] * 26
        for i in range(N-1, -1, -1):
            last[ord(S[i]) - ord('a')] = i
            nxt[i] = tuple(last)

        windows = [[i, i] for i, c in enumerate(S) if c == T[0]]
        for j in range(1, len(T)):
            letter_index = ord(T[j]) - ord('a')
            windows = [[root, nxt[i+1][letter_index]]
                       for root, i in windows
                       if 0 <= i < N-1 and nxt[i+1][letter_index] >= 0]

        if not windows: return ""
        i, j = min(windows, key = lambda x: x[1]-x[0])
        return S[i: j+1]
```
* [Lock] [Hard] [Solution] 727. Minimum Window Subsequence

### Using 1D Dynamic Programming
```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        M, N = len(s1), len(s2)
        if len(s3) != M + N:
            return False
        dp = [False]*(N + 1)
        for i in range(M + 1):
            for j in range(N + 1):
                if i == 0 and j == 0:
                    dp[j] = True
                elif i == 0:
                    dp[j] = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    dp[j] = dp[j] and s1[i - 1] == s3[i + j - 1]
                else:
                    dp[j] = dp[j] and s1[i - 1] == s3[i + j - 1] \
                    or dp[j - 1] and s2[j - 1] == s3[i + j - 1]
        
        return dp[N]
```
* [Hard] [Solution] 97. Interleaving String

### 1-D Dynamic Programmming
```python
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [0]*(k + 1)
        MOD = 10**9 + 7
        for i in range(1, n+1):
            temp = [0]*(k + 1)
            temp[0] = 1
            for j in range(1, k+1):
                val = (dp[j] + MOD - (dp[j - i] if (j - i) >= 0 else 0)) % MOD
                temp[j] = (temp[j - 1] + val) % MOD
            dp = temp

        return ((dp[k] + MOD - (dp[k - 1] if k > 0 else 0)) % MOD)
```
* [Hard] [Solution] 629. K Inverse Pairs Array

### Dynamic Programming + Counting
```python
class Solution:
    def atMostNGivenDigitSet(self, D: List[str], N: int) -> int:
        S = str(N)
        K = len(S)
        dp = [0] * K + [1]
        # dp[i] = total number of valid integers if N was "N[i:]"

        for i in range(K-1, -1, -1):
            # Compute dp[i]

            for d in D:
                if d < S[i]:
                    dp[i] += len(D) ** (K-i-1)
                elif d == S[i]:
                    dp[i] += dp[i+1]

        return dp[0] + sum(len(D) ** i for i in range(1, K))

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        S = str(n)
        K = len(S)

        def dfs(idx):
            ans = 0
            if idx >= K:
                return 1
            for d in digits:
                if d < S[idx]:          
                    # not need to consider the following digits since all is less than N 
                    ans += len(digits) ** (K - idx - 1)
                elif d == S[idx]:  
                    # compare the following digits to N
                    ans += dfs(idx + 1)
                else:      
                    # not need to consider the following digits since all is more than N 
                    break
            return ans

        return dfs(0) + sum([len(digits) ** i for i in range(1, K)])
```
* [Hard] [Solution] * 902. Numbers At Most N Given Digit Set

### Backtracking DFS
```python
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] % 2 == 0:
                    yield nr, nc

        todo = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val != -1: todo += 1
                if val == 1: sr, sc = r, c
                if val == 2: tr, tc = r, c

        self.ans = 0
        def dfs(r, c, todo):
            todo -= 1
            if todo < 0: return
            if r == tr and c == tc:
                if todo == 0:
                    self.ans += 1
                return

            grid[r][c] = -1
            for nr, nc in neighbors(r, c):
                dfs(nr, nc, todo)
            grid[r][c] = 0

        dfs(sr, sc, todo)
        return self.ans
    
from functools import lru_cache
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def code(r, c):
            return 1 << (r * C + c)

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] % 2 == 0:
                    yield nr, nc

        target = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val % 2 == 0:
                    target |= code(r, c)

                if val == 1:
                    sr, sc = r, c
                if val == 2:
                    tr, tc = r, c

        @lru_cache(None)
        def dp(r, c, todo):
            if r == tr and c == tc:
                return +(todo == 0)

            ans = 0
            for nr, nc in neighbors(r, c):
                if todo & code(nr, nc):
                    ans += dp(nr, nc, todo ^ code(nr, nc))
            return ans

        return dp(sr, sc, target)
```
* [Hard] [Solution] 980. Unique Paths III

### Digit DP
```python
class Solution:
    def atMostNGivenDigitSet(self, D: List[str], N: int) -> int:
        D = list(map(int, D))
        N = list(map(int, str(N)))

        @functools.lru_cache(None)
        def dp(i, isPrefix, isBigger):
            if i == len(N):
                return not isBigger
            if not isPrefix and not isBigger:
                return 1 + len(D) * dp(i + 1, False, False)
            return 1 + sum(dp(i + 1, isPrefix and d == N[i], isBigger or (isPrefix and d > N[i])) for d in D)

        return dp(0, True, False) - 
```
* [Hard] [Solution] * 902. Numbers At Most N Given Digit Set

### How many ways to place P_i with relative rank j
```python
from functools import lru_cache

class Solution:
    def numPermsDISequence(self, S: str) -> int:
        MOD = 10**9 + 7
        N = len(S)

        @lru_cache(None)
        def dp(i, j):
            # How many ways to place P_i with relative rank j?
            if not(0 <= j <= i):
                return 0
            if i == 0:
                return 1
            elif S[i-1] == 'D':
                return (dp(i, j+1) + dp(i-1, j)) % MOD
            else:
                return (dp(i, j-1) + dp(i-1, j-1)) % MOD

        return sum(dp(N, j) for j in range(N+1)) % MOD
```
* [Hard] [Solution] 903. Valid Permutations for DI Sequence

### Ways
```python
class Solution:
    def numMusicPlaylists(self, N, L, K):
        @lru_cache(None)
        def dp(i, j):
            # number of playlists of length i that have exactly j unique songs
            if i == 0:
                return +(j == 0)
            ans = dp(i-1, j-1) * (N-j+1)
            ans += dp(i-1, j) * max(j-K, 0)
            return ans % (10**9+7)

        return dp(L, N)
```
* [Hard] [Solution] 920. Number of Music Playlists

### Prefix + Suffix
```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        set_wordDict = set(wordDict)

        @functools.lru_cache(None)
        def dfs(seq):
            if not seq:
                return []
            rst = []
            if seq in set_wordDict:
                rst.append(seq)
            for i in range(1, len(seq)):
                prefix = seq[:i]
                if prefix in set_wordDict:
                    for sufix in dfs(seq[i:]):
                        rst.append(prefix+' ' + sufix)
            return rst

        ans = dfs(s)
        return ans
```
* [Hard] 140. Word Break II

### n day * k transaction * 2 (buy|sell) state
```python
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        # solve special cases
        if not prices or k==0:
            return 0

        if 2*k > n:
            res = 0
            for i, j in zip(prices[1:], prices[:-1]):
                res += max(0, i - j)
            return res

        # dp[i][used_k][ishold] = balance
        # ishold: 0 nothold, 1 hold
        dp = [[[-math.inf]*2 for _ in range(k+1)] for _ in range(n)]

        # set starting value
        dp[0][0][0] = 0
        dp[0][1][1] = -prices[0]

        # fill the array
        for i in range(1, n):
            for j in range(k+1):
                # transition equation
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
                # you can't hold stock without any transaction
                if j > 0:
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])

        res = max(dp[n-1][j][0] for j in range(k+1))
        return res
```
* [Hard] 188. Best Time to Buy and Sell Stock IV

### KMP
```python
class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:

        def srange(a, b):
            yield from (chr(i) for i in range(ord(a), ord(b)+1))

        def failure(pat): 
            res = [0]
            i, target = 1, 0
            while i < len(pat):
                if pat[i] == pat[target]: 
                    target += 1
                    res += target,
                    i += 1
                elif target: 
                    target = res[target-1] 
                else: 
                    res += 0,
                    i += 1
            return res    

        f = failure(evil)

        @lru_cache(None)
        def dfs(idx, max_matched=0, lb=True, rb=True):
            '''
            idx: current_idx_on_s1_&_s2, 
            max_matched: nxt_idx_to_match_on_evil, 
            lb, rb: is_left_bound, is_right_bound
            '''
            if max_matched == len(evil): return 0 # evil found, break
            if idx == n: return 1 # base case

            l = s1[idx] if lb else 'a' # valid left bound
            r = s2[idx] if rb else 'z' # valid right bound
            candidates = [*srange(l, r)]

            res = 0
            for i, c in enumerate(candidates):
                nxt_matched = max_matched
                while evil[nxt_matched] != c and nxt_matched:
                    nxt_matched = f[nxt_matched - 1]
                res += dfs(idx+1, nxt_matched + (c == evil[nxt_matched]), 
                           lb=(lb and i == 0), rb=(rb and i == len(candidates)-1))
            return res                

        return dfs(0) % (10**9 + 7)
```
* [Hard] 1397. Find All Good Strings

### 3D DP
```python
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:

        @functools.lru_cache(None)
        def dfs(i, largest, accend):
            if i == n: return accend == k
            if accend > k: return 0
            return sum(dfs(i + 1, max(largest, j), accend + (j > largest)) for j in range(1, m + 1))

        if k > m: return 0
        return sum(dfs(1, i, 1) for i in range(1, m + 1)) % (10 ** 9 + 7)
```
* [Hard] 1420. Build Array Where You Can Find The Maximum Exactly K Comparisons

### Rectangle
```python
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if (n == 11 and m == 13) or (n == 13 and m == 11):
            return 6

        @functools.lru_cache(None)
        def dp(i, j):
            if i <= 0 or j <= 0:
                return 0
            rst = float('inf')
            for k in range(1, min(i, j) + 1):
                rst = min(rst, 1 + min(dp(i-k, j) + dp(k, j-k),  # up to up, upright to bottomleft
                                       dp(i-k, k) + dp(i, j-k)))  # bottomleft to upright, left to left
            return rst
                
        return dp(n, m)
```
* [Hard] 1240. Tiling a Rectangle with the Fewest Squares

### 2-Level DP
```python
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        N = len(s)
        
        @lru_cache(None)
        def nchange(i, j):
            res = 0
            while i < j:
                if s[i] != s[j]:
                    res += 1
                i,j = i+1, j-1
            return res

        @lru_cache(None)
        def part(st, k):
            if k == 1: return nchange(st, N-1)
            res = float('inf')
            for i in range(st, N):
                res = min(res, nchange(st, i) + part(i+1, k-1))
            return res
        
        return part(0, k)
```
* [Hard] 1278. Palindrome Partitioning III

### Path DP
```python
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        N = len(hats)
        MOD = 10**9 + 7
        d = collections.defaultdict(list) # mapping : hat -> people 
        for i, hat in enumerate(hats):
            for x in hat: d[x].append(i)

        @lru_cache(None)
        def dp(h, path):
            """Return the number of ways to wear h to last hats among people whose 
            availability is indicated by mask"""
            if bin(path).count("1") == N: return 1 # # set bits = # people 
            if h == 40: return 0                           # if used all hat, 
            ans = dp(h+1, path) 
            for p in d[h+1]:       # loop through all people preferring the hat
                if path & (1 << p): continue # if taken, continue
                path |= 1 << p               # set bit
                ans += dp(h+1, path)
                path ^= 1 << p               # reset bit
            return ans

        return dp(0, 0) % MOD
```
* [Hard] 1434. Number of Ways to Wear Different Hats to Each Other

### Sort DP Bottom-Up
```python
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        h = mat[0][:]
        for row in mat[1:]:
            h = sorted([i+j for i in row for j in h])[:k]
        return h[k-1]
```
* [Hard] 1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows

### Prefix Sum
```python
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        R, C, MOD = len(pizza), len(pizza[0]), 10 ** 9 + 7
        preSum = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R - 1, -1, -1):
            for c in range(C - 1, -1, -1):
                preSum[r][c] = preSum[r][c + 1] + preSum[r + 1][c] - preSum[r + 1][c + 1] + (pizza[r][c] == 'A')

        @lru_cache(None)
        def dp(kk, r, c):
            if preSum[r][c] == 0: return 0
            if kk == 0: return 1
            ans = 0
            # cut horizontally
            for nr in range(r + 1, R):
                if preSum[r][c] - preSum[nr][c] > 0:
                    ans = (ans + dp(kk - 1, nr, c)) % MOD
            # cut vertically                    
            for nc in range(c + 1, C):
                if preSum[r][c] - preSum[r][nc] > 0:
                    ans = (ans + dp(kk - 1, r, nc)) % MOD
            return ans

        return dp(k - 1, 0, 0)
```
* [Hard] 1444. Number of Ways of Cutting a Pizza

### Dungeon Game
```python
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon or not dungeon[0]: return 0
        M, N = len(dungeon), len(dungeon[0])
        dp = [[0]*N for _ in range(M)]
        for i in range(M-1,-1,-1):
            for j in range(N-1,-1,-1):
                if i == M-1 and j == N-1:
                    dp[i][j] = max(1, 1 - dungeon[i][j])
                elif i == M-1:
                    dp[i][j] = max(1, dp[i][j+1] - dungeon[i][j])
                elif j == N-1:
                    dp[i][j] = max(1, dp[i+1][j] - dungeon[i][j])                
                else:
                    dp[i][j] = max(1, min(dp[i][j + 1],dp[i + 1][j]) - dungeon[i][j])

        return dp[0][0]

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        # returns minimum possible amount of health required at position (i, j)
        def calculate(i, j):
            if i == m or j == n:
                return float('inf')
            elif i == m-1 and j == n-1:
                return max(1,  1 - dungeon[i][j])
            elif (i, j) in memory:
                return memory[i, j]
            down = calculate(i+1, j) # min health required to go down and survive
            right = calculate(i, j+1) # min health required to go right and survive
            cur = min(max(down - dungeon[i][j], 1), max(right - dungeon[i][j], 1))
            memory[i, j] = cur
            return cur
        memory = {}
        return calculate(0, 0)
```
* [Hard] 174. Dungeon Game

## Math <a name="math"></a>
---
### brute force
```python
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        prime = [True]*n
        prime[0] = prime[1] = False
        for i in range(2, int(n**0.5)+1):
            if prime[i]:
                prime[i*i: n: i] = [False] * len(prime[i*i: n: i])
        return sum(prime)
```
* [Easy] 204. Count Primes

### Logartihmic Bounds
```python
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:

        a = bound if x == 1 else int(log(bound, x))
        b = bound if y == 1 else int(log(bound, y))

        powerful_integers = set([])

        for i in range(a + 1):
            for j in range(b + 1):

                value = x**i + y**j

                if value <= bound:
                    powerful_integers.add(value)

                if y == 1:
                    break

            if x == 1:
                break

        return list(powerful_integers)
```
* [Easy] [Solution] 970. Powerful Integers

### Greedy
```python
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while n%3 == 0:
            n = n/3
        return True if n == 1 else False
```
* [Easy] 326. Power of Three

### Simulation
```python
class Solution:
    def numberOfSteps (self, num: int) -> int:
        ans = 0
        while num > 0:
            if num%2:
                num -= 1
            else:
                num //= 2
            ans += 1

        return ans
```
* [Easy] 1342. Number of Steps to Reduce a Number to Zero

### Conclude possible case
```python
class Solution:
    def check(self, nums: List[int]) -> bool:
        return sum(a > b for a, b in zip(nums, nums[1:] + nums[:1])) <= 1
```
* [Easy] 1752. Check if Array Is Sorted and Rotated

### Count of even of odd
```pyth0on
class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        odd = even = 0
        for c in chips:
            if not c %2:
                even += 1
            else:
                odd += 1
        return min(odd, even)
```
* [Easy] 1217. Play with Chips

### Base Conversion
```python
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        base = ord('A') - 1
        return sum((ord(v)-base)*26**i for i,v in enumerate(s[::-1]))
```
* [Easy] 171. Excel Sheet Column Number

### Power of Four
```python
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        temp = bin(num).split('1')
        return num > 0 and len(temp) == 2 and not len(temp[-1]) % 2
```
* [Easy] [Solution] 342. Power of Four

### Digital Root
```python
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9
        
class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0
```
* [Easy] [Solution] 258. Add Digits

### Binary Search
```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        lo, hi = 1, num
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            val = mid ** 2
            if val == num: return True
            elif val < num: lo = mid + 1
            else: hi = mid - 1
        return False
```
* [Easy] 367. Valid Perfect Square

### Increase number
```python
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums)-len(nums)*min(nums)
```
* [Easy] 453. Minimum Moves to Equal Array Elements

### Hamming Distance
```python
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count("1")
```
* [Easy] 461. Hamming Distance

### Perfect Number
```python
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 0:
            return False
        sum_ = 0
        for i in range(1, int(num**.5) + 1):
            if num % i == 0:
                sum_ += i
                if i**2 != num:
                    sum_ += num / i
        return sum_ - num == num
```
* [Easy] [Solution] 507. Perfect Number

### Rectangle Overlap
```python
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        def intersect(p_left, p_right, q_left, q_right):
            return min(p_right, q_right) > max(p_left, q_left)
        return (intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and # width > 0
                intersect(rec1[1], rec1[3], rec2[1], rec2[3]))    # height > 0
```
* [Easy] [Solution] 836. Rectangle Overlap

### Binary Gap
```python
class Solution:
    def binaryGap(self, N: int) -> int:
        last = None
        ans = 0
        for i in range(32):
            if (N >> i) & 1:
                if last is not None:
                    ans = max(ans, i - last)
                last = i
        return ans
```
* [Easy] [Solution] 868. Binary Gap

### Projection
```python
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ans = sum(map(max, grid))  # x-z plane
        ans += sum(map(max, zip(*grid)))  # y-z plane
        ans += sum(v > 0 for row in grid for v in row)  # x-y plane
        return ans
```
* [Easy] [Solution] 883. Projection Area of 3D Shapes

### Square by Square
```python
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        N = len(grid)

        ans = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    ans += 2
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r,c+1)):
                        if 0 <= nr < N and 0 <= nc < N:
                            nval = grid[nr][nc]
                        else:
                            nval = 0

                        ans += max(grid[r][c] - nval, 0)

        return ans
```
* [Easy] [Solution] 892. Surface Area of 3D Shapes

### GCD
```python
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from functools import reduce
        vals = collections.Counter(deck).values()
        return reduce(math.gcd, vals) >= 2
```
* [Easy] [Solution] 914. X of a Kind in a Deck of Cards

### Smallest Range
```python
class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        return max(0, max(A) - min(A) - 2*K)
```
* [Easy] [Solution] 908. Smallest Range I

### Ad-Hoc
```python
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        lo, hi = 0, len(S)
        ans = []
        for x in S:
            if x == 'I':
                ans.append(lo)
                lo += 1
            else:
                ans.append(hi)
                hi -= 1

        return ans + [lo]
```
* [Easy] [Solution] 942. DI String Match

### Brute Force
```python
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        ans = -1
        for h1, h2, m1, m2 in itertools.permutations(A):
            hours = 10 * h1 + h2
            mins = 10 * m1 + m2
            time = 60 * hours + mins
            if 0 <= hours < 24 and 0 <= mins < 60 and time > ans:
                ans = time

        return "{:02}:{:02}".format(*divmod(ans, 60)) if ans >= 0 else ""
```
* [Easy] [Solution] 949. Largest Time for Given Digits

### Largest Perimeter Triangle
```python
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        for i in range(len(A) - 3, -1, -1):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0
```
* [Easy] [Solution] 976. Largest Perimeter Triangle

### Odd and even
```python
class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        def dfs(lst):
            if len(lst) <= 2:
                return lst
            return dfs(lst[::2]) + dfs(lst[1::2])
        
        return dfs([_ for _ in range(1,N+1)])
```
* [Medium] 932. Beautiful Array.md

### Maximum
```python
class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))
```
* [Medium] 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers

### Area sum
```python
class Solution:
    def minOperations(self, n: int) -> int:
        return (n+1)*(n-1)//4 if n%2 else n*n//4

class Solution:
    def minOperations(self, n: int) -> int:
        last = 2*(n-1) + 1
        mid = (last+1)//2
        if n%2:
            return (last-mid) * ((n+1)//2) // 2
        else:
            return (1 + last-mid) * n//2 // 2
```
* [Medium] 1551. Minimum Operations to Make Array Equal

### Hash Map
```python
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        rm = ((1000, 'M'), 
              (900, 'CM'),
              (500, 'D'), 
              (400, 'CD'), 
              (100, 'C'), 
              (90, 'XC'), 
              (50, 'L'), 
              (40, 'XL'), 
              (10, 'X'), 
              (9, 'IX'), 
              (5, 'V'), 
              (4, 'IV'), 
              (1, 'I'))
        for i, m in enumerate(rm):
            q, _ = divmod(num, m[0])
            ans += m[1] * q
            num -= q * m[0]
        return ans
```
* [Medium] 12. Integer to Roman

### Transform to select 2k points from n+k-1
```python
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        return math.comb(n + k - 1, k * 2) % (10**9 + 7)
```
* [Medium] 1621. Number of Sets of K Non-Overlapping Line Segments

### Factor
```python
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for factor in range(1, n + 1):
            if n % factor == 0:
                k -= 1
                if k == 0:
                    return factor
        return -1
```
* [Medium] 1492. The kth Factor of n

### Checking Loop
```python
class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        remainder = 0
        for length_N in range(1,K+1):
            remainder = (remainder*10+1) % K
            if remainder == 0:
                return length_N
        return -1
```
* [Medium] 1015. Smallest Integer Divisible by K

### GCD
```python
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g = math.gcd(p,q)
        return 2 if not p//g % 2 else q//g % 2
```
* [Medium] 858. Mirror Reflection

### Task Scheduler
```python
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        d = collections.Counter(tasks)
        counts = d.values()
        longest = max(counts)
        ans = (longest - 1) * (n + 1)
        for count in counts:
            ans += count == longest and 1 or 0
        return max(len(tasks), ans)
```
* [Medium] [Solution] 621. Task Scheduler

### Smallest Range
```python
class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        mi, ma = A[0], A[-1]
        ans = ma - mi
        for i in range(len(A) - 1):
            a, b = A[i], A[i+1]
            ans = min(ans, max(ma-K, a+K) - min(mi+K, b-K))
        return ans
```
* [Medium] [Solution] 910. Smallest Range II

### Greedy
```python
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        ans = 0
        while Y > X:
            ans += 1
            if Y%2: Y += 1
            else: Y //= 2

        return ans + X-Y
```
* [Medium] [Solution] 991. Broken Calculator

### Permutation Sequence
```python
class Solution:    
    def getPermutation(self, n: int, k: int) -> str:
        rst, k, nums = '', k-1, list(range(1, n+1))
        for i in range(n, 0, -1):
            ind, k = divmod(k, math.factorial(i-1))
            rst += str(nums[ind])
            del nums[ind]
        return rst
```
* [Medium] 60. Permutation Sequence

### Single Number
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return int((3*sum(set(nums)) - sum(nums)) // 2)
```
* [Medium] 137. Single Number II

### Prime Factor
```python
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglyNumbers = [1]
        p2 = p3 = p5 = 0

        while len(uglyNumbers) < n:
            #If a value lesser than latest was already added, try finding next least value.
            while uglyNumbers[p2]*2 <= uglyNumbers[-1]:
                p2 += 1

            while uglyNumbers[p3]*3 <= uglyNumbers[-1]:
                p3 += 1

            while uglyNumbers[p5]*5 <= uglyNumbers[-1]:
                p5 += 1

            nextVal = min(uglyNumbers[p2]*2, uglyNumbers[p3]*3, uglyNumbers[p5]*5)
            uglyNumbers.append(nextVal)

        return uglyNumbers[-1]

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n < 1: return 
        k = [1] * n
        p2 = p3 = p5 = 0
        for i in range(1, n):
            k[i] = min(k[p2] * 2, k[p3] * 3, k[p5] * 5)
            #cannot use elif, becaude case '6' forward two pointer at the same time, '30' forward all pointer
            if k[i] == k[p2] * 2: p2 += 1
            if k[i] == k[p3] * 3: p3 += 1
            if k[i] == k[p5] * 5: p5 += 1
        return k[-1]

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        Set = {2,3,5}
        q = [2,3,5]
        heapq.heapify(q)
        cur = 1
        for i in range(2, n+1):
            cur = heapq.heappop(q)
            for x in [2*cur, 3*cur, 5*cur]:
                if x not in Set:
                    Set.add(x)
                    heapq.heappush(q, x)
        return cur
```
* [Medium] 264. Ugly Number II

### Pow(x, n)
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            x = 1/x
            n = -n
        
        ans = 1
        while n > 0:
            if n % 2 == 1: # current exponent is odd
                ans = ans * x
                x = x * x
                n = (n-1) / 2
            else: # current exponent is even
                x = x * x
                n = n / 2

        return ans

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        if n < 0:
            x = 1/x
            n = -n

        ans = 1
        if n %2 == 1:
            ans = x * self.myPow(x*x, (n-1)/2)
        else:
            ans = self.myPow(x*x, n/2)

        return ans
```
* [Medium] 50. Pow(x, n)

### GCD
```python
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z == 0:
            return True
        if x+y < z:
            return  False
        return z % math.gcd(x, y) == 0
```
* [Medium] 365. Water and Jug Problem

### Hash Table Buffer
```python
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        ans2step, step2ans = collections.defaultdict(int), collections.defaultdict(int)
        b = int("".join(map(str,b)))
        ans = 1
        for step in range(min(1338, b)):
            ans = ans*a % 1337
            if ans in ans2step:
                loop_length = step - ans2step[ans]
                rest = (b - step - 1) % loop_length
                return step2ans[ans2step[ans]+rest]
            ans2step[ans] = step
            step2ans[step] = ans
        return ans
```
* [Medium] 372. Super Pow

### Digit
```python
class Solution:
    def findNthDigit(self, n: int) -> int:
        s, d = 0, 0
        while s < n:
            s += (d+1)*9*10**d
            d += 1
        n -= s-d*9*10**(d-1)
        r, q = n % d, 10**(d-1) + n//d
        return str(q)[r-1] if r > 0 else str(q-1)[-1]
```
* [Medium] 400. Nth Digit

### Medium
```python
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid = nums[len(nums)//2]       
        return sum(abs(n - mid) for n in nums)
```
* [Medium] 462. Minimum Moves to Equal Array Elements II

### Prefix Sum difference
```python
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cumsum = [0]
        for n in nums:
            cumsum.append(cumsum[-1]+n)
        record = {}
        for a,b in zip(cumsum[:-1],cumsum[1:]):  # subarry need at least 2 elements
            b = b%k if k else b
            a = a%k if k else a
            if b in record:
                return True
            record[a] = 1 
        return False
```
* [Medium] 523. Continuous Subarray Sum

### Complex Number
```python
class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        A = [int(x) for x in a.replace('i','').split('+')]
        B = [int(x) for x in b.replace('i','').split('+')]
        return '{}+{}i'.format((A[0]*B[0] - A[1]*B[1]), (A[0]*B[1] + A[1]*B[0]))
```
*[[Medium] 537. Complex Number Multiplication](%5BMedium%5D%20537.%20Complex%20Number%20Multiplication.md)

### Division
```python
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0])+'/'+str(nums[1])
        return str(nums[0]) + '/(' + '/'.join(list(map(str,nums[1:]))) + ')'
```
* [Medium] 553. Optimal Division

### Circle
```python
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
        self.MAX_AREA = math.pi * self.radius**2

    def randPoint(self) -> List[float]:
        r = (random.uniform(0, self.MAX_AREA) / math.pi) ** 0.5
        theta = random.uniform(0, 2 * math.pi)
        return [self.x_center + r * math.cos(theta), self.y_center + r * math.sin(theta)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
```
* [Medium] 478. Generate Random Point in a Circle

### Factor
```python
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        res = [1, num + 1]
        for a in range(1, int((num+2)**0.5) + 1):
            if (num + 2) % a == 0:
                res = [a, (num + 2) // a]
            if (num + 1) % a == 0:
                res = [a, (num + 1) // a]
        return res
```
* [Medium] 1362. Closest Divisors

### Construction
```python
class Solution(object):
    def constructArray(self, n, k):
        ans = list(range(1, n - k))
        for i in range(k+1):
            if i % 2 == 0:
                ans.append(n-k + i//2)
            else:
                ans.append(n - i//2)

        return ans
```
* [Medium] [Solution] 667. Beautiful Arrangement II

### Sort and map 4 points to plane
```python
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        p = sorted([p1, p2, p3, p4])
        dist = lambda i, j: (p[i][0] - p[j][0])**2 + (p[i][1] - p[j][1])**2
        return dist(0, 1) != 0 and dist(0, 1) == dist(1, 3) == dist(3, 2) == dist(2, 0) and dist(0, 3) == dist(1, 2)
```
* [Medium] [Solution] 593. Valid Square

### Reach a Number
```python
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        step, pos=0, 0
        while pos < target or (pos-target)%2 != 0:
            step += 1
            pos += step
            
        return step
```
* [Medium] [Solution] 754. Reach a Number

### Count
```python
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        if len(answers) == 0:
            return 0
        d = {}  # similar rabit -> current rabit
        count = 0
        for num in answers:
            # If there's no other rabit that has the same color,
            # the rabbit is one kind of its own
            if num == 0:
                count += 1
            else:
                # For a rabbit that has n rabbits similar to it, 
                # the minimum of rabbit there are is n + 1
                if num not in d:
                    d[num] = 1
                    count += (num + 1)
                else:
                    d[num] += 1
                    # If the number of similar rabbits is canceled out,
                    # we remove it from the hash table
                    if d[num] > num:
                        del d[num]
        return count
```
* [Medium] 781. Rabbits in Forest

### Distance
```python
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        t1 = abs(target[0]) + abs(target[1])
        t2 = 40000
        for ghost in ghosts:
            t2 = min(t2, (abs(target[0]-ghost[0]) + abs(target[1] -ghost[1])))
```
* [Medium] 789. Escape The Ghosts

### Prime Palindrome
```python
class Solution:
    def primePalindrome(self, N: int) -> int:
        def is_prime(n):
            return n > 1 and all(n % d for d in range(2, int(n**.5) + 1))

        def reverse(x):
            ans = 0
            while x:
                ans = 10 * ans + x % 10
                x //= 10
            return ans

        while True:
            if N == reverse(N) and is_prime(N):
                return N
            N += 1
            if 10**7 < N < 10**8:
                N = 10**8
```
* [Medium] [Solution] 866. Prime Palindrome

### Counting, search from candidate answer
```python
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        count = collections.Counter(str(N))
        return any(count == collections.Counter(str(1 << b))
                   for b in range(31))
```
* [Medium] [Solution] 869. Reordered Power of 2

### Walk in a Spiral
```python
class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        ans = [(r0, c0)]
        if R * C == 1: return ans

        # For walk length k = 1, 3, 5 ...
        for k in xrange(1, 2*(R+C), 2):

            # For direction (dr, dc) = east, south, west, north;
            # and walk length dk...
            for dr, dc, dk in ((0, 1, k), (1, 0, k), (0, -1, k+1), (-1, 0, k+1)):

                # For each of dk units in the current direction ...
                for _ in xrange(dk):

                    # Step in that direction
                    r0 += dr
                    c0 += dc

                    # If on the grid ...
                    if 0 <= r0 < R and 0 <= c0 < C:
                        ans.append((r0, c0))
                        if len(ans) == R * C:
                            return ans
```
* [Medium] [Solution] 885. Spiral Matrix III

### Clumsy Factorial
```python
class Solution:
    def clumsy(self, N: int) -> int:
        tmp = 0
        ans = 0
        for i, n in enumerate(range(N,0,-1)):
            if i%4 == 0:
                tmp = n
            elif i%4 == 1:
                tmp *= n
            elif i%4 == 2:
                tmp //= n
            elif i%4 == 3:
                if i == 3:
                    ans = tmp + n
                else:
                    ans += -tmp + n
                tmp = 0
            if n == 1 and tmp > 0:
                if i < 3:
                    ans = tmp
                else:
                    ans -= tmp
        return ans
```
* [Medium] 1006. Clumsy Factorial

### Sliding Window
```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return len({s[i:i + k] for i in range(len(s) - k + 1)}) == 2 ** k
```
* [Medium] 1461. Check If a String Contains All Binary Codes of Size K

### Clock Angle
```python
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Degree covered by hour hand (hour area + minutes area)
        h = (hour%12 * 30) + (minutes/60 * 30)

        # Degree covered by minute hand (Each minute = 6 degree)
        m = minutes * 6

        # Absolute angle between them
        angle = abs(m - h)

        # If the angle is obtuse (>180), convert it to acute (0<=x<=180)
        if angle > 180:
            angle = 360.0 - angle

        return (angle)
```
* [Medium] 1344. Angle Between Hands of a Clock

### shrink program space
```python
class Solution:
    def superpalindromesInRange(self, L: str, R: str) -> int:
        L, R = int(L), int(R)
        MAGIC = 100000

        def reverse(x):
            ans = 0
            while x:
                ans = 10 * ans + x % 10
                x //= 10
            return ans

        def is_palindrome(x):
            return x == reverse(x)

        ans = 0

        # count odd length
        for k in range(MAGIC):
            s = str(k)  # Eg. s = '1234'
            t = s + s[-2::-1]  # t = '1234321'
            v = int(t) ** 2
            if v > R: break
            if v >= L and is_palindrome(v):
                ans += 1

        # count even length
        for k in range(MAGIC):
            s = str(k)  # Eg. s = '1234'
            t = s + s[::-1]  # t = '12344321'
            v = int(t) ** 2
            if v > R: break
            if v >= L and is_palindrome(v):
                ans += 1

        return ans
```
* [Hard] [Solution] 906. Super Palindromes

### Greedy with combination
```python
class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        m, n, ans = destination[0], destination[1], ""
        for i in range(m+n):
            if k == 1:  #no options left
                ans += "H"*n + "V"*m
                break

            if k <= math.comb(m+n-1, m):
                n -= 1
                ans += "H"
            else:
                ans += "V"
                k -= math.comb(m+n-1, m)
                m -= 1

        return ans
```
* [Hard] 1643. Kth Smallest Instructions

### Moving Average
```python
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        S = sum(machines)
        N = len(machines)
        if S % N!=0:
            return -1
        ave = S // N
        sumneed = 0
        res = 0
        for m in machines:
            sumneed += m-ave
            res = max(res,abs(sumneed), m-ave)

        return res
```
* [Hard] 517. Super Washing Machines

### Combination
```python
class Solution:
    def countOrders(self, n: int) -> int:
        return (math.factorial(n * 2) >> n) % (10**9 + 7)  # 2n!/2^n
```
* [Hard] 1359. Count All Valid Pickup and Delivery Options

### (rounds+1)\*\*x >= n
```python
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        pigs, rounds = 0, minutesToTest//minutesToDie
        while (rounds+1)**pigs < buckets:
            pigs += 1

        return pigs
```
* [Hard] 458. Poor Pigs

### Sum of Subsequence Widths
```python
class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        MOD = 10**9 + 7
        N = len(A)
        A.sort()

        pow2 = [1]
        for i in range(1, N):
            pow2.append(pow2[-1] * 2 % MOD)

        ans = 0
        for i, x in enumerate(A):
            ans = (ans + (pow2[i] - pow2[N-1-i]) * x) % MOD
        return ans
```
* [Hard] [Solution] 891. Sum of Subsequence Widths

### Dynamic Programming with Binary Search
```python
class Solution(object):
    def superEggDrop(self, K, N):
        memo = {}
        def dp(k, n):
            if (k, n) not in memo:
                if n == 0:
                    ans = 0
                elif k == 1:
                    ans = n
                else:
                    lo, hi = 1, n
                    # keep a gap of 2 X values to manually check later
                    while lo + 1 < hi:
                        x = (lo + hi) / 2
                        t1 = dp(k-1, x-1)
                        t2 = dp(k, n-x)

                        if t1 < t2:
                            lo = x
                        elif t1 > t2:
                            hi = x
                        else:
                            lo = hi = x

                    ans = 1 + min(max(dp(k-1, x-1), dp(k, n-x))
                                  for x in (lo, hi))

                memo[k, n] = ans
            return memo[k, n]

        return dp(K, N)
```
* [Hard] [Solution] 887. Super Egg Drop

### LCM
```python
class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        from fractions import gcd
        MOD = 10**9 + 7
        L = A / gcd(A,B) * B

        def magic_below_x(x):
            # How many magical numbers are <= x?
            return x // A + x // B - x // L

        lo = 0
        hi = N * min(A, B)
        while lo < hi:
            mi = (lo + hi) // 2
            if magic_below_x(mi) < N:
                lo = mi + 1
            else:
                hi = mi

        return lo % MOD
```
* [Hard] [Solution] 878. Nth Magical Number

### Power
```python
class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        MOD = 10**9 + 7
        N = len(A)
        A.sort()

        pow2 = [1]
        for i in range(1, N):
            pow2.append(pow2[-1] * 2 % MOD)

        ans = 0
        for i, x in enumerate(A):
            ans = (ans + (pow2[i] - pow2[N-1-i]) * x) % MOD
        return ans
```
* [Hard] [Solution] 891. Sum of Subsequence Widths

### Equal Ones
```python
class Solution:
    def threeEqualParts(self, A: List[int]) -> List[int]:
        IMP = [-1, -1]

        S = sum(A)
        if S % 3: return IMP
        T = S / 3
        if T == 0:
            return [0, len(A) - 1]

        breaks = []
        su = 0
        for i, x in enumerate(A):
            if x:
                su += x
                if su in {1, T+1, 2*T+1}:
                    breaks.append(i)
                if su in {T, 2*T, 3*T}:
                    breaks.append(i)

        i1, j1, i2, j2, i3, j3 = breaks

        # The array is in the form W [i1, j1] X [i2, j2] Y [i3, j3] Z
        # where [i1, j1] is a block of 1s, etc.
        if not(A[i1:j1+1] == A[i2:j2+1] == A[i3:j3+1]):
            return [-1,-1]

        # x, y, z: the number of zeros after part 1, 2, 3
        x = i2 - j1 - 1
        y = i3 - j2 - 1
        z = len(A) - j3 - 1

        if x < z or y < z: return IMP
        j1 += z
        j2 += z
        return [j1, j2+1]
```
* [Hard] [Solution] 927. Three Equal Parts

### Gradient Descent
```python
class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        #euclidean distance 
        fn = lambda x, y: sum(sqrt((x-xx)**2 + (y-yy)**2) for xx, yy in positions)
        #centroid as starting point
        x = sum(x for x, _ in positions)/len(positions)
        y = sum(y for _, y in positions)/len(positions)

        ans = fn(x, y)
        chg = 100 #change since 0 <= positions[i][0], positions[i][1] <= 100
        while chg > 1e-6: #accuracy within 1e-5
            zoom = True
            for dx, dy in (-1, 0), (0, -1), (0, 1), (1, 0):
                xx = x + chg * dx
                yy = y + chg * dy
                dd = fn(xx, yy)
                if dd < ans: 
                    ans = dd 
                    x, y = xx, yy
                    zoom = False 
                    break 
            if zoom: chg /= 2
        return ans 
```
* [Hard] 1515. Best Position for a Service Centre

## String <a name="string"></a>
---
### KMP
```python
class Solution:
    def build_lps(self, pattern):
        """ Helper function for strStr.
        Returns longest proper suffix array for string pattern.
        Each lps_array[i] is the length of the longest proper prefix
        which is equal to suffix for pattern ending at character i.
        Proper means that whole string cannot be prefix or suffix.

        Time complexity: O(m). Space complexity: O(1), where
        m is the length of the pattern, space used for lps array isn't included.
        """
        m = len(pattern)
        lps_array = [0] * m
        i, j = 1, 0  # start from the 2nd character in pattern
        while i < m:
            if pattern[i] == pattern[j]:
                lps_array[i] = j + 1
                j += 1
                i += 1
            else:
                if j > 0:
                    j = lps_array[j - 1]
                else:
                    lps_array[i] = 0
                    i += 1
        return lps_array

    def strStr(self, text, pattern):
        """ Returns index of 1st occurence of pattern in text.
        Returns -1 if pattern is not in the text.
        Knuth–Morris–Pratt algorithm.
        Time complexity: O(n + m). Space complexity: O(m).
        """
        # special cases
        if not text and not pattern:
            return 0
        elif not pattern:
            return 0

        # build longest proper suffix array for pattern
        lps_array = self.build_lps(pattern)

        n, m = len(text), len(pattern)
        i, j = 0, 0
        while i < n:
            # current characters match, move to the next characters
            if text[i] == pattern[j]:
                i += 1
                j += 1
            # current characters don't match
            else:
                if j > 0:  # try start with previous longest prefix
                    j = lps_array[j - 1]
                # 1st character of pattern doesn't match character in text
                # go to the next character in text
                else:
                    i += 1

            # whole pattern matches text, match is found
            if j == m:
                return i - m

        # no match was found
        return -1
```
### Math
```python
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 2 - (s == s[::-1]) - (s == "")
```
* [Easy] 1332. Remove Palindromic Subsequences

### Sort
```python
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return words == sorted(words, key= lambda word: [order.index(c) for c in word])
```
* [Easy] [Solution] 953. Verifying an Alien Dictionary

### product
```python
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        return set(map(''.join, itertools.product(*zip(S.lower(), S.upper()))))
```
* [Easy] 784. Letter Case Permutation

### string concatenate
```python
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)
```
* [Easy] 1662. Check If Two String Arrays are Equivalent

### Enumerate Cases
```python
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False
        if A == B:
            seen = set()
            for a in A:
                if a in seen:
                    return True
                seen.add(a)
            return False
        else:
            pairs = []
            for a, b in zip(A, B):
                if a != b:
                    pairs.append((a, b))
                if len(pairs) >= 3: return False
            return len(pairs) == 2 and pairs[0] == pairs[1][::-1]
```
* [Easy] [Solution] 859. Buddy Strings

### split
```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])
```
* [Easy] 58. Length of Last Word

### Read N Characters Given Read4
```python
"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        copied_chars = 0
        read_chars = 4
        buf4 = [''] * 4

        while copied_chars < n and read_chars == 4:
            read_chars = read4(buf4)

            for i in range(read_chars):
                if copied_chars == n:
                    return copied_chars
                buf[copied_chars] = buf4[i]
                copied_chars += 1

        return copied_chars
```
* [Lock] [Easy] [Solution] 157. Read N Characters Given Read4

### KMP
```python
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        N = len(A)
        if N != len(B): return False
        if N == 0: return True

        #Compute shift table
        shifts = [1] * (N+1)
        left = -1
        for right in range(N):
            while left >= 0 and B[left] != B[right]:
                left -= shifts[left]
            shifts[right + 1] = right - left
            left += 1

        #Find match of B in A+A
        match_len = 0
        for char in A+A:
            while match_len >= 0 and B[match_len] != char:
                match_len -= shifts[match_len]

            match_len += 1
            if match_len == N:
                return True

        return False
```
* [Easy] [Solution] 796. Rotate String

### Goat Latin
```python
class Solution:
    def toGoatLatin(self, S: str) -> str:
        def convert(word):
            if word[0] not in 'aeiouAEIOU':
                word = word[1:] + word[:1]
            return word + 'ma'

        return " ".join(convert(word) + 'a' * i
                        for i, word in enumerate(S.split(), 1))
```
* [Easy] [Solution] 824. Goat Latin

### Rolling Hash
```python
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        MOD = 10**9 + 7
        P = 113
        Pinv = pow(P, MOD-2, MOD)

        hb = 0
        power = 1
        for x in B:
            code = ord(x) - 96
            hb = (hb + power * code) % MOD
            power = power * P % MOD

        ha = 0
        power = 1
        for x in A:
            code = ord(x) - 96
            ha = (ha + power * code) % MOD
            power = power * P % MOD

        if ha == hb and A == B: return True
        for i, x in enumerate(A):
            code = ord(x) - 96
            ha += power * code
            ha -= code
            ha *= Pinv
            ha %= MOD
            if ha == hb and A[i+1:] + A[:i+1] == B:
                return True
        return False
```
* [Easy] [Solution] 796. Rotate String

### Read and Write Heads
```python
class Solution:
    def compress(self, chars: List[str]) -> int:
        anchor = write = 0
        for read, c in enumerate(chars):
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write
```
* [Easy] [Solution] 443. String Compression

### Plus One
```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int, str(int(''.join(map(str, digits))) + 1)))
```
* [Easy] 66. Plus One

### Add Binary
```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num_a = int(a, 2)
        num_b = int(b, 2)
        return bin(num_a+num_b)[2:]
```
* [Easy] 67. Add Binary

### Reverse Bits
```python
class Solution:
    def reverseBits(self, n):
        return int('{:032b}'.format(n)[::-1], 2)
```
* [Easy] 190. Reverse Bits

### Valid Palindrome
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filter_str = [*filter(lambda c:c.isdigit() or c.isalpha(), s.lower())]  # list(filter(lambda c:c.isdigit() or c.isalpha(), s.lower()))
        return filter_str[::-1] == filter_str
```
* [Easy] [Solution] 125. Valid Palindrome

### Repeated Substring Pattern
```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]
```
* [Easy] 459. Repeated Substring Pattern

### Reverse String
```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
```
* [Easy] [Solution] 344. Reverse String

### Two Pointers
```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i , j = 0, len(s) - 1

        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                c1 = s[i:j]
                c2 = s[i+1:j+1]

                if c1 == c1[::-1] or c2 == c2[::-1]:  # checking the candidate is palindrome or not
                    return True
                else:
                    return False
        return True
```
* [Easy] [Solution] 680. Valid Palindrome II

### Ad-Hoc
```python
class Solution(object):
    def repeatedStringMatch(self, A, B):
        q = (len(B) - 1) // len(A) + 1
        for i in range(2):
            if B in A * (q+i): return q+i
        return -1
```
* [Easy] [Solution] 686. Repeated String Match

### Linear Scan
```python
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1

        return ans + min(prev, cur)
```
* [Easy] [Solution] 696. Count Binary Substrings

### Enumerate Cases
```python
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False
        if A == B:
            seen = set()
            for a in A:
                if a in seen:
                    return True
                seen.add(a)
            return False
        else:
            pairs = []
            for a, b in zip(A, B):
                if a != b:
                    pairs.append((a, b))
                if len(pairs) >= 3: return False
            return len(pairs) == 2 and pairs[0] == pairs[1][::-1]
```
* [Easy] [Solution] 859. Buddy Strings

### Stack of Letters
```python
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters = [c for c in S if c.isalpha()]
        ans = []
        for c in S:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)
```
* [Easy] [Solution] 917. Reverse Only Letters

### Custom Sort
```python
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def f(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key = f)
```
* [Easy] [Solution] 937. Reorder Data in Log Files

### Cartesian Product, Brute force all combination
```python
class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        def make(frag):
            N = len(frag)
            for d in range(1, N+1):
                left = frag[:d]
                right = frag[d:]
                if ((not left.startswith('0') or left == '0')
                        and (not right.endswith('0'))):
                    yield left + ('.' if d != N else '') + right

        S = S[1:-1]
        return ["({}, {})".format(*cand)
                for i in range(1, len(S))
                for cand in itertools.product(make(S[:i]), make(S[i:]))]
```
* [Medium] [Solution] 816. Ambiguous Coordinates

### Work Backwards
```python
class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        size = 0
        # Find size = length of decoded string
        for c in S:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1

        for c in reversed(S):
            K %= size
            if K == 0 and c.isalpha():
                return c

            if c.isdigit():
                size /= int(c)
            else:
                size -= 1
```
* [Medium] [Solution] 880. Decoded String at Index

### GCD
```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2: return str1
        if len(str2) > len(str1): return self.gcdOfStrings(str2, str1)
        if str1[:len(str2)] == str2: return self.gcdOfStrings(str1[len(str2):], str2)  # x - y (also need to check the prefix str match)
        return "" # original gcd alway has a solution (at least '1')
```
* [Easy] 1071. Greatest Common Divisor of Strings

### Binary
```python
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return int(''.join(bin(i)[2 :] for i in range(1, n + 1)), 2) % (10 ** 9 + 7)
```
* [Medium] 1680. Concatenation of Consecutive Binary Numbers

### same set and frequency
```python
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values())
```
* [Medium] 1657. Determine if Two Strings Are Close

### Simulation
```python
class Solution:
    def nextClosestTime(self, time: str) -> str:
        cur = 60 * int(time[:2]) + int(time[3:])
        allowed = {int(x) for x in time if x != ':'}
        while True:
            cur = (cur + 1) % (24 * 60)
            if all(digit in allowed
                    for block in divmod(cur, 60)
                    for digit in divmod(block, 10)):
                return "{:02d}:{:02d}".format(*divmod(cur, 60))
```
* [Lock] [Medium] [Solution] 681. Next Closest Time

### Binary search in string time range
```python
class LogSystem:

    def __init__(self):
        self.data = []
        self.map = {}
        
    def put(self, id: int, timestamp: str) -> None:
        bisect.insort(self.data, timestamp)
        self.map[timestamp] = id

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        low, high = '0000:00:00:00:00:00', '9999:99:99:99:99:99'
        i = {'Year':4, 'Month':7, 'Day':10, 'Hour':13, 'Minute':16, 'Second':19}[gra]
        s = s[:i] + low[i:]
        e = e[:i] + high[i:]
        j = bisect_left(self.data, s)
        k = bisect_right(self.data, e)
        return list(map(self.map.get, self.data[j:k]))

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)
```
* [Lock] [Medium] [Solution] 635. Design Log Storage System

### Split Concatenated Strings
```python
class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        def getMaxStr(s: str) -> str:
            i, j = 0, len(s)-1
            while i < j:
                if s[i] < s[j]: return s[::-1]
                if s[i] > s[j]: return s
                i += 1
                j -= 1
            return s

        for i in range(len(strs)): 
            strs[i] = getMaxStr(strs[i])

        concatenated = ''.join(strs)
        exclusives = [''] * len(strs)
        for i in range(len(strs)):
            exclusives[i] = concatenated[len(strs[i]):]
            concatenated = concatenated[len(strs[i]):] + strs[i]

        output = ''
        for i, s in enumerate(strs):
            sr = s[::-1]
            for j in range(len(s)+1):
                output = max(output, s[j:]+exclusives[i]+s[:j], sr[j:]+exclusives[i]+sr[:j])

        return output
```
* [Lock] [Medium] [Solution] 555. Split Concatenated Strings

### Brute Force
```python
class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        N = len(s)
        mask = [False] * N
        for i in range(N):
            prefix = s[i:]
            for word in dict:
                if prefix.startswith(word):
                    for j in range(i, min(i+len(word), N)):
                        mask[j] = True

        ans = []
        for incl, grp in itertools.groupby(zip(s, mask), lambda z: z[1]):
            if incl: ans.append("<b>")
            ans.append("".join(z[0] for z in grp))
            if incl: ans.append("</b>")
        return "".join(ans)
```
* [Lock] [Medium] [Solution] 616. Add Bold Tag in String

### Reverse the Whole String and Then Reverse Each Word
```python
class Solution:
    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1
            
    def reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = end = 0
        
        while start < n:
            # go to the end of the word
            while end < n and l[end] != ' ':
                end += 1
            # reverse the word
            self.reverse(l, start, end - 1)
            # move to the next word
            start = end + 1
            end += 1
            
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # reverse the whole string
        self.reverse(s, 0, len(s) - 1)
        
        # reverse each word
        self.reverse_each_word(s)
```
* [Lock] [Medium] [Solution] 186. Reverse Words in a String II

### Visit by Row
```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for _ in range(numRows)]
        curRow = 0
        goingDown = False
        ret = []
        for c in s:
            rows[curRow].append(c)
            if numRows == 1: continue
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1
        ret = ''.join([c for r in rows for c in r])
        return ret
```
* [Medium] [Solution] 6. ZigZag Conversion

### Brute Force all combination
```python
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0: return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans
```
* [Medium] [Solution] 22. Generate Parentheses

### Stack
```python
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0] #The score of the current frame

        for x in S:
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)

        return stack.pop()
```
* [Medium] [Solution] 856. Score of Parentheses

### Reverse Words
```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])  #first split then reverse and then join to form new string
```
* [Medium] 151. Reverse Words in a String

### Stack, previous operator
```python
class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        pre_op = '+'
        s += '#'
        stack = []
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c == ' ': continue
            else:
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    operant = stack.pop()
                    stack.append((operant*num))
                elif pre_op == '/':
                    operant = stack.pop()
                    stack.append(int(operant/num))
                num = 0
                pre_op = c
        return sum(stack)
```
* [Medium] 227. Basic Calculator II

### Manacher's Algorithm
```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        def manachers(S):
            A = '+_' + '_'.join(S) + '_-'
            Z = [0] * len(A)
            center = right = 0
            for i in range(1, len(A) - 1):
                if i < right:
                    Z[i] = min(right - i, Z[2 * center - i])
                while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                    Z[i] += 1
                if i + Z[i] > right:
                    center, right = i, i + Z[i]
            return Z

        return sum((v+1)//2 for v in manachers(s))
```
* [Medium] [Solution] 647. Palindromic Substrings

### Next Greater Element
```python
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n == 0:
            return -1

        nums = list(str(n))
        ln = len(nums)
        i = ln-1
        # find the first non increasing sequence from the right
        while i > 0:
            if nums[i-1] < nums[i]:
                break
            i -= 1

        #this is the number to be replaced as it is smaller
        # than any other element on the right of it
        i -= 1  

        if i < 0:
            return -1

        # look for the min largest number greater than nums[i]
        # and swap it and sort the rest
        temp = ln-1
        while temp > i:
            if nums[i] < nums[temp]:
                break
            temp -= 1

        nums[i], nums[temp] = nums[temp], nums[i]

        #sort rest of the stuff from [i+1, ln-1]
        nums[i+1:] = sorted(nums[i+1:]) 
        res = int("".join(nums))
        return  res if (res > n and res <= (2**31-1)) else -1
```
* [Medium] 556. Next Greater Element III

### Heap
```python
class Solution:
    def reorganizeString(self, S: str) -> str:
        pq = [(-S.count(x), x) for x in set(S)]
        heapq.heapify(pq)
        if any(-nc > (len(S) + 1) / 2 for nc, x in pq):
            return ""

        ans = []
        while len(pq) >= 2:
            nct1, ch1 = heapq.heappop(pq)
            nct2, ch2 = heapq.heappop(pq)
            ans.extend([ch1, ch2])
            if nct1 + 1: heapq.heappush(pq, (nct1 + 1, ch1))
            if nct2 + 1: heapq.heappush(pq, (nct2 + 1, ch2))

        return "".join(ans) + (pq[0][1] if pq else '')
```
* [Medium] [Solution] 767. Reorganize String

### Run Length Encoding
```python
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def RLE(S):
            return zip(*[(k, len(list(grp)))
                         for k, grp in itertools.groupby(S)])

        R, count = RLE(S)
        ans = 0
        for word in words:
            R2, count2 = RLE(word)
            if R2 != R: continue
            ans += all(c1 >= max(c2, 3) or c1 == c2
                       for c1, c2 in zip(count, count2))

        return ans
```
* [Medium] [Solution] 809. Expressive Words

### Cartesian Product
```python
class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        def make(frag):
            N = len(frag)
            for d in range(1, N+1):
                left = frag[:d]
                right = frag[d:]
                if ((not left.startswith('0') or left == '0')
                        and (not right.endswith('0'))):
                    yield left + ('.' if d != N else '') + right

        S = S[1:-1]
        return ["({}, {})".format(*cand)
                for i in range(1, len(S))
                for cand in itertools.product(make(S[:i]), make(S[i:]))]
```
* [Medium] [Solution] 816. Ambiguous Coordinates

### Counting
```python
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        def count(A):
            ans = [0] * 52
            for i, letter in enumerate(A):
                ans[ord(letter) - ord('a') + 26 * (i%2)] += 1
            return tuple(ans)

        return len({count(word) for word in A})
```
* [Easy] [Solution] 893. Groups of Special-Equivalent Strings

### Prefix Sum
```python
class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        ans = []
        X = sum(shifts) % 26
        for i, c in enumerate(S):
            index = ord(c) - ord('a')
            ans.append(chr(ord('a') + (index + X) % 26))
            X = (X - shifts[i]) % 26

        return "".join(ans)
```
* [Medium] [Solution] 848. Shifting Letters

### Hash Table
```python
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            P = {}
            for x, y in zip(pattern, word):
                if P.setdefault(x, y) != y:
                    return False
            return len(set(P.values())) == len(P.values())

        return filter(match, words)
```
* [Medium] [Solution] 890. Find and Replace Pattern

### HashMap, map candidate and answer to the same entry
```python
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(word):
            return "".join('*' if c in 'aeiou' else c
                           for c in word)

        words_perfect = set(wordlist)
        words_cap = {}
        words_vow = {}

        for word in wordlist:
            wordlow = word.lower()
            words_cap.setdefault(wordlow, word)
            words_vow.setdefault(devowel(wordlow), word)

        def solve(query):
            if query in words_perfect:
                return query

            queryL = query.lower()
            if queryL in words_cap:
                return words_cap[queryL]

            queryLV = devowel(queryL)
            if queryLV in words_vow:
                return words_vow[queryLV]
            return ""

        return map(solve, queries)
```
* [Medium] [Solution] 966. Vowel Spellchecker

### break string, stack
```python
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        stack = [s]
        ans = 0
        while stack:
            string = stack.pop()
            for char in set(string):
                if string.count(char) < k:
                    stack.extend(substring for substring in string.split(char))
                    break
            else:
                ans = max(ans, len(string))
        return ans
```
* [Medium] 395. Longest Substring with At Least K Repeating Characters

### string match
```python
class Solution:
    def isNumber(self, s: str) -> bool:
        def is_integer(s):
            return s.isdigit() or len(s) > 0 and s[0] in "+-" and s[1:].isdigit()

        def is_decimal(s):
            parts = s.split(".")
            if len(parts) != 2: return False
            if is_integer(parts[0]) and parts[1].isdigit(): return True
            if parts[0] in ["","+","-"] and parts[1].isdigit(): return True
            if is_integer(parts[0]) and not parts[1]: return True
            return False

        s = s.lower()
        parts = s.split("e")
        if len(parts) > 2: return False
        if not is_integer(parts[0]) and not is_decimal(parts[0]): return False
        return True if len(parts) == 1 else is_integer(parts[1])
```
* [Hard] 65. Valid Number

### Math
```python
class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        if K == 1:
            return min(S[i:] + S[:i] for i in range(len(S)))
        return "".join(sorted(S))
```
* [Hard] [Solution] 899. Orderly Queue

### Edit Distance
```python
import functools
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)

        @functools.lru_cache(None)
        def dp(i, j):
            if i == M: return N - j
            if j == N: return M - i
            if word1[i] == word2[j]:
                return dp(i+1, j+1)           # Nothing to do 
            else:
                return min( dp(i+1, j)+1,     # Word1[i] Insert
                            dp(i, j+1)+1,     # Word1[i] Delete
                            dp(i+1, j+1)+1 )  # Word1[i] Replace 

        return dp(0, 0)
```
* [Hard] 72. Edit Distance

## Tree <a name="tree"></a>
---
### DFS
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        node = TreeNode(nums[len(nums)//2])
        node.left = self.sortedArrayToBST(nums[:len(nums)//2])
        node.right = self.sortedArrayToBST(nums[len(nums)//2 + 1:])
        return node
```
* [Easy] 108. Convert Sorted Array to Binary Search Tree.md

### DFS
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def trim(node):
            if not node:
                return None
            elif node.val > R:
                return trim(node.left)
            elif node.val < L:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)
```
* [Easy] [Solution] 669. Trim a Binary Search Tree

### DFS
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.isBalanced = True

        def height(root):
            if not root:
                return 0

            left = height(root.left)
            right = height(root.right)
            if self.isBalanced:
                self.isBalanced = abs(left - right) < 2 

            return 1 + max(left, right)


        height(root)
        return self.isBalanced
```
* [Easy] 110. Balanced Binary Tree

### Traversal with Relinking
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right
```
* [Easy] [Solution] 897. Increasing Order Search Tree

### DFS/BFS
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif root.left == None and root.right == None:
            return 1
        else:
             return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        q = [[root, 1]] if root else []
        depth = 0
        while q:
            node, d = q.pop(0)
            depth = max(depth, d)
            for c in [node.left, node.right]:
                if c:
                    q += [[c, d+1]]

        return depth
```
* [Easy] 104. Maximum Depth of Binary Tree

### DFS, Yield
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(node, previous):
            if not node.left and not node.right:
                yield 2*previous + node.val

            if node.left:
                yield from dfs(node.left, 2*previous + node.val)

            if node.right:
                yield from dfs(node.right, 2*previous + node.val)

        return sum(dfs(root, 0))
```
* [Easy] 1022. Sum of Root To Leaf Binary Numbers

### DFS
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root
```
* [Easy] [Solution] 226. Invert Binary Tree

### In-Order with extra pointer
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is not None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root
```
* [Easy] [Solution] 538. Convert BST to Greater Tree

### Range Sum
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)

        self.ans = 0
        dfs(root)
        return self.ans
```
* [Easy] [Solution] 938. Range Sum of BST

### DFS
```python
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        parent = {}
        def dfs(node, par=None, depth=0):
            if node:
                parent[node.val] = (par, depth)
                dfs(node.left, node.val, depth + 1)
                dfs(node.right, node.val, depth + 1)

        dfs(root)
        x_parent, x_depth = parent[x]
        y_parent, y_depth = parent[y]
        return True if x_parent != y_parent and x_depth == y_depth else False 
```
* [Easy] [Solution] 993. Cousins in Binary Tree

### BFS
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        level = [root]
        while level:
            ans += [[node.val for node in level if node]]
            level = [c for node in level if node for c in [node.left, node.right] if c]
        return ans[::-1]
```
* [Easy] 107. Binary Tree Level Order Traversal II

### DFS
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None

        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)
```
* [Easy] 700. Search in a Binary Search Tree

### DFS
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root == None:
            return []
        
        ans = []
        def dfs(node, path_sum, path):
            nonlocal ans
            if not node:
                return False
            if node.val == path_sum and not node.left and not node.right:
                ans += [path]
                return
            else:
                if node.left:
                    dfs(node.left, path_sum-node.val, path + [node.left.val])
                if node.right:
                    dfs(node.right, path_sum-node.val, path + [node.right.val])
            return
        
        dfs(root, sum, [root.val])
        return ans
```
* [Medium] 113. Path Sum II

### Postorder
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        def contains_one(node: TreeNode) -> bool:
            if not node: 
                return False
            
            # Check if any node in the left subtree contains a 1.
            left_contains_one = contains_one(node.left)
            
            # Check if any node in the right subtree contains a 1.
            right_contains_one = contains_one(node.right)
            
            # If the left subtree does not contain a 1, prune the subtree.
            if not left_contains_one: 
                node.left = None
                
            # If the right subtree does not contain a 1, prune the subtree.
            if not right_contains_one: 
                node.right = None
            
            # Return True if the current node or its left or right subtree contains a 1.
            return node.val or left_contains_one or right_contains_one

        # Return the pruned tree if the tree contains a 1, otherwise return None.
        return root if contains_one(root) else None
```
* [Medium] 814. Binary Tree Pruning

### Postorder, parent pointer
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        # Variable to store LCA node.
        self.ans = None
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurse_tree(current_node):
            
            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # Stack for tree traversal
        stack = [root]

        # Dictionary for parent pointers
        parent = {root: None}

        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:

            node = stack.pop()

            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Ancestors set() for node p.
        ancestors = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q
```
* [Medium] [Solution] 236. Lowest Common Ancestor of a Binary Tree.md

### DFS
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root
```
* [[Medium] 105. Construct Binary Tree from Preorder and Inorder Traversa

### Post-Order
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    prev = None
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return 

        stack = [root]
        while stack:
            node = stack.pop()
            if node.right is not None:
                stack.append(node.right)    
            if node.left is not None:
                stack.append(node.left)
            if stack:
                node.right = stack[-1]
            node.left = None
```
* [Medium] 114. Flatten Binary Tree to Linked List

### Pre-order
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.flipped = []
        self.i = 0

        def dfs(node):
            if node:
                if node.val != voyage[self.i]:
                    self.flipped = [-1]
                    return
                self.i += 1

                if (self.i < len(voyage) and
                        node.left and node.left.val != voyage[self.i]):
                    self.flipped.append(node.val)
                    dfs(node.right)
                    dfs(node.left)
                else:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        if self.flipped and self.flipped[0] == -1:
            self.flipped = [-1]
        return self.flipped
```
* [Medium] [Solution] 971. Flip Binary Tree To Match Preorder Traversal

### Pre-order
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node, low, high):    
            if not node: return True       
            if node.val >= high or node.val <= low: return False      
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float('-inf'), float('inf'))
```
* [Medium] 98. Validate Binary Search Tree

### Linked-List Walk through every level
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root
        while node:
            curr = dummy = Node(0)
            while node:
                if node.left:
                    curr.next = node.left
                    curr = curr.next
                if node.right:
                    curr.next = node.right
                    curr = curr.next
                node = node.next
            node = dummy.next

        return root
```
* [Medium] 117. Populating Next Right Pointers in Each Node II

### DFS, Queue
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        def dfs(node):
            nonlocal res
            if not node:
                res += ['null']
                return 
            res += [str(node.val)]
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        res = ','.join(res)
        return res

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        q = collections.deque(data.split(','))
        def dfs(data_list):
            if data_list[0] == 'null':
                data_list.popleft()
                return None
            node = TreeNode(int(data_list[0]))
            data_list.popleft()
            node.left = dfs(data_list)
            node.right = dfs(data_list)
            return node

        root = dfs(q)    
        return root
```
* [Medium] 449. Serialize and Deserialize BST

### DFS
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        else:
            if root.val > val:
                root.left = self.insertIntoBST(root.left, val)
            else:
                root.right = self.insertIntoBST(root.right, val)
            return root
```
* [Medium] 701. Insert into a Binary Search Tree

### All Elements in Two Binary Search Tree
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(root):
            if not root: return []
            return dfs(root.left) + [root.val] + dfs(root.right)

        nums1, nums2 = dfs(root1), dfs(root2)
        i = j = 0
        ans = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1

        return ans + (nums1[i:] if i < len(nums1) else nums2[j:])
```
* [Medium] 1305. All Elements in Two Binary Search Trees

### Binary Tree Inorder Traversa
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return

        ans = []
        ans += self.inorderTraversal(root.left) if root.left else []
        ans += [root.val]
        ans += self.inorderTraversal(root.right) if root.right else []
        return ans
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res
```
* [Medium] [Solution] 94. Binary Tree Inorder Traversal

### Kth Smallest
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        seq = []
        
        def dfs(node, n):
            nonlocal seq
            if not node:
                return
            dfs(node.left, n)
            seq += [node.val]
            if n == 1:
                return
            else:
                n -= 1
            dfs(node.right, n)
        
        dfs(root, k)
        return seq[k-1]
```
* [Medium] [Solution] 230. Kth Smallest Element in a BST

### DFS
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return 0 if not root else 1 + self.countNodes(root.left) + self.countNodes(root.right)
```
* [Medium] 222. Count Complete Tree Nodes

### DFS
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if preorder:
            val = preorder[0]
            root = TreeNode(val)
            i = 1
            while i < len(preorder) and preorder[i] < val:
                i += 1
            root.left = self.bstFromPreorder(preorder[1:i])
            root.right = self.bstFromPreorder(preorder[i:])
            return root
```
* [Medium] 1008. Construct Binary Search Tree from Preorder Traversal

### Post-Order
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, direction):
            nonlocal res
            if not node:
                return 0
            left = dfs(node.left,'left')
            right = dfs(node.right,'right')
            res = max(res, left+1, right+1)
            return right+1 if direction == 'left' else left+1

        if not root:
            return 0
        dfs(root,'left')
        dfs(root,'right')

        return res-1
```
* [Medium] 1372. Longest ZigZag Path in a Binary Tree

### Unique Binary Search Trees
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import functools
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        @functools.lru_cache(None)
        def dfs(l, r):   # split between [l, r)
            if l == r:
                return [None]  # list contain None object
            rst = []
            for i in range(l, r):
                for lchild in dfs(l, i):
                    for rchild in dfs(i+1, r):
                        root = TreeNode(i+1)   # +1 to convert the index to the actual value
                        root.left = lchild
                        root.right = rchild
                        rst.append(root)
            return rst

        return dfs(0, n) if n else []
```
* [Medium] 95. Unique Binary Search Trees II

### Unique Binary Search Trees
```python
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        arr = [0]*(n+1)
        arr[0] = 1
        arr[1] = 1
        arr[2] = 2
        for i in range(3,n+1):
            for j in range(i):
                arr[i] += arr[j]*arr[i-1-j]
        return arr[-1]
    
import functools
class Solution:

    @functools.lru_cache(None)
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        elif n == 2:
            return 2
        rst = 0
        for i in range(n):
            rst += self.numTrees(i) * self.numTrees(n - i - 1)
        return rst
```
* [Medium] 96. Unique Binary Search Trees

### Preorder
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node, total):
            nonlocal ans
            if not node.left and not node.right:
               ans += total
            
            if node.left:
                dfs(node.left, total*10 + node.left.val)
            if node.right:
                dfs(node.right, total*10 + node.right.val)
            return
            
        if not root:
            return 0
        dfs(root, root.val)
        return ans
```
* [Medium] 129. Sum Root to Leaf Numbers

### DFS with pre node pointer
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def inorder(node):
            if not node: return
            inorder(node.left)
            #spot node which is out of order
            #the first appearing swaped node must be greater than the next node 
            if not self.first and node.val < self.pre.val: self.first = self.pre
            #the second appearing swaped node must be smaller than the pre node
            if self.first and node.val < self.pre.val: self.second = node
            self.pre = node
            inorder(node.right)

        self.pre, self.first, self.second = TreeNode(-float('inf')), None, None
        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
```
* [Hard] 99. Recover Binary Search Tree

## Hash Table <a name='ht'></a>
---
### Step-by-step build Hash Table
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        for i in range(len(nums)):
            if target-nums[i] in sum_dict:
                return [i, sum_dict[target-nums[i]]]
            else:
                sum_dict[nums[i]] = i
```
* [Easy] [Solution] 1. Two Sum.md

### Character Mapping with Dictionary
```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        mapping_s_t = {}
        mapping_t_s = {}
        
        for c1, c2 in zip(s, t):
            
            # Case 1: No mapping exists in either of the dictionaries
            if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
                mapping_s_t[c1] = c2
                mapping_t_s[c2] = c1
            
            # Case 2: Ether mapping doesn't exist in one of the dictionaries or Mapping exists and
            # it doesn't match in either of the dictionaries or both            
            elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
                return False
            
        return True
```
* [Easy] 205. Isomorphic Strings.md

### Counter
```python
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        cnt = collections.Counter(A)
        for k in sorted(cnt, reverse=True):
            if cnt[k] == 1:
                return k
        return -1
```
* [Lock] [Easy] 1133. Largest Unique Number

### Count set size
```python
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        return min(len(set(candies)), len(candies) // 2)
```
* [Easy] [Solution] 575. Distribute Candies

### Greedy, Hash Table
```python
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0    
        for i in range(0, len(s)):
            result +=  roman_dict[s[i]]
            if i>=1 and roman_dict[s[i]]>roman_dict[s[i-1]]:
                result -= 2*roman_dict[s[i-1]]
        return result
```
* [Easy] 13. Roman to Integer

### Counter
```python
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return collections.Counter(s) == collections.Counter(t)
```
* [Easy] [Solution] 242. Valid Anagram

### Counter
```python
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        seen_d = collections.Counter(nums)        # prep dict { elem: times_seen }

        # find 2 harmomious keys in seen_d with max times_seen for both of them
        max_seen = 0
        for k in seen_d:
            if k + 1 in seen_d:
                max_seen = max(max_seen, seen_d[k] + seen_d[k + 1])
        return max_seen
```
* [Easy] [Solution] 594. Longest Harmonious Subsequence

### Hash Table
```python
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mp = {x[0]: x for x in pieces}
        i = 0
        while i < len(arr): 
            if (x := arr[i]) not in mp or mp[x] != arr[i:i+len(mp[x])]: return False 
            i += len(mp[x])
        return True
```
* [Easy] 1640. Check Array Formation Through Concatenation

### Hash Set
```python
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]

        seen = {"".join(MORSE[ord(c) - ord('a')] for c in word) for word in words}

        return len(seen)
```
* [Easy] [Solution] 804. Unique Morse Code Words

### Candidate value hash
```python
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = []
        dic = {}
        for num in nums:
            if num in dic:
                res.append((dic[num],num))          
            dic[num+k] = num
        return len(set(res))
```
* [Easy] 532. K-diff Pairs in an Array

### Two Counter
```python
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cow_count = sum(dict(collections.Counter(secret) & collections.Counter(guess)).values())
        bull_count = len(["_" for letter_secret, letter_guess in zip(secret, guess) if letter_secret == letter_guess])
        return '{}A{}B'.format(bull_count, cow_count - bull_count)
```
* [Easy] 299. Bulls and Cows

### Word Pattern
```python
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        d = {}
        word = str.split()
        if len(word) != len(pattern): return False
        for i in range(len(pattern)):
            if not d.get(pattern[i], None):
                if word[i] in d.values():
                    return False
                d[pattern[i]] = word[i]
            else:
                if d[pattern[i]] != word[i]:
                    return False
        return True
```
* [Easy] 290. Word Pattern

### Fizz Buzz
```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # ans list
        ans = []

        # Dictionary to store all fizzbuzz mappings
        fizz_buzz_dict = {3 : "Fizz", 5 : "Buzz"}

        for num in range(1,n+1):

            num_ans_str = ""

            for key in fizz_buzz_dict.keys():

                # If the num is divisible by key,
                # then add the corresponding string mapping to current num_ans_str
                if num % key == 0:
                    num_ans_str += fizz_buzz_dict[key]

            if not num_ans_str:
                num_ans_str = str(num)

            # Append the current answer str to the ans list
            ans.append(num_ans_str)  

        return ans
```
* [Easy] [Solution] 412. Fizz Buzz

### Left and Right Index
```python
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans
```
* [Easy] [Solution] 697. Degree of an Array

### Counter
```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return len(collections.Counter(ransomNote) - collections.Counter(magazine)) == 0
```
* [Easy] 383. Ransom Note

### Counter
```python
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """            
        # build hash map : character and how often it appears
        count = collections.Counter(s)

        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
```
* [Easy] [Solution] 387. First Unique Character in a String

### Counter with order
```python
class Solution:
    def customSortString(self, order: str, str: str) -> str:
        cnt, ans = Counter(str), ""
        for c in order:
            if c in cnt:
                ans += c*cnt[c]
                cnt.pop(c)
                
        return ans + "".join(c*cnt[c] for c in cnt) 
```
* [Medium] 791. Custom Sort String.md

### Categorize by Count
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
            
        return ans.values()
```
* [Medium] [Solution] 49. Group Anagrams

### Key-value pair
```python
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for path in paths:
            values = path.split(' ')
            for i in range(1, len(values)):
                name_cont = values[i].split('(')
                name_cont[1] = name_cont[1].replace(')', '')
                d[name_cont[1]].append(values[0] + '/' + name_cont[0])
        res = []
        for k in d.keys():
            if len(d[k]) > 1:
                res.append(d[k])
        return res
```
* [Medium] [Solution] 609. Find Duplicate File in System

### Set
```python
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        A, B = map(set, zip(*paths))
        return (B - A).pop()
```
* [Easy] 1436. Destination City

### Set
```python
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = s.lower()[:len(s)//2]
        b = s.lower()[len(s)//2:]
        return collections.Counter(c in 'aeiou' for c in a) == collections.Counter(c in 'aeiou' for c in b)
```
* [Easy] 1704. Determine if String Halves Are Alike

### Counter
```python
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        R = len(wall)
        counter = collections.Counter()
        for row in wall:
            pos = 0
            for width in row[:-1]:
                pos += width
                counter[pos] += 1
        return R - counter.most_common(1)[0][1] if counter else R
```
* [Medium] 554. Brick Wall

### feature set Hash Table
```python
class Solution:
    def originalDigits(self, s: str) -> str:
        names = [('zero','z','0'),('two','w','2'),('four','u','4'),('six','x','6'),('eight','g','8'),('one','o','1'),('three','t','3'),\
                 ('five','f','5'),('seven','s','7'),('nine','i','9')]
        result = []
        cnt = collections.Counter(s)
        for name in names:
            count = cnt[name[1]]
            if not count: continue
            for c in name[0]: cnt[c] -= count
            result.append(name[2]*count)
        return ''.join(sorted(result))
```
* [Medium] 423. Reconstruct Original Digits from English

### 2 hash table
```python
class UndergroundSystem:

    def __init__(self):
        self.check = {}
        self.time = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        prevstation, prevt = self.check[id]
        time = t-prevt
        if (prevstation,stationName) in self.time:
            totaltime,stationN = self.time[(prevstation,stationName)]
            self.time[(prevstation,stationName)] = (totaltime+time,stationN+1)
        else:
            self.time[(prevstation,stationName)] = (time,1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totaltime,stationN = self.time[(startStation,endStation)]
        return totaltime/stationN


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
```
* [Medium] 1396. Design Underground System

### Hash table to counter
```python
class Codec:
    def __init__(self):
        self.url_map = {}
        self.count = 1

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if self.url_map.get(longUrl):
            return
        self.url_map[self.count] = longUrl
        self.count += 1

        return self.count - 1

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.url_map[int(shortUrl)]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
```
* [Medium] 535. Encode and Decode TinyURL

### Counter
```python
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = Counter(nums)
        ans = 0
        for key in d.keys():
            if key * 2 == k:
                ans += d[key] // 2
            elif d[k - key] > 0:
                mi = min(d[key], d[k - key])
                d[key] -= mi     
                d[k - key] -= mi
                ans += mi
        return ans
```
* [Medium] 1679. Max Number of K-Sum Pairs

### Frequency Table
```python
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        ans = 0
        freq = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)): 
                key = nums[i] * nums[j]
                ans += freq.get(key, 0)
                freq[key] = 1 + freq.get(key, 0)
        return 8*ans
```
* [Medium] 1726. Tuple with Same Product

### Hash Table Counter
```python
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        total_sum = 0
        cache = collections.defaultdict(int)
        for i in C:
            for j in D:
                key = i + j
                cache[key] += 1
        for i in A:
            for j in B:
                key = 0 - i - j
                if key in cache:
                    total_sum += cache[key]
        return total_sum
```
* [Medium] 454. 4Sum II

### Hash Key = Pattern sequence
```python
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        table = {}
        ret = []
        for index, num in enumerate(s):
            pattern = s[index:index+10]            
            if pattern in table:
                ret.append(pattern)
            else:
                table[pattern] = index
        return list(set(ret))
```
* [Medium] 187. Repeated DNA Sequences

### Prefix sum Hash Table index
```python
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        need = sum(nums) % p
        dp = {0: -1}
        cur = 0
        res = n = len(nums)
        for i, a in enumerate(nums):
            cur = (cur + a) % p
            dp[cur] = i
            if (cur - need) % p in dp:
                res = min(res, i - dp[(cur - need) % p])
        return res if res < n else -1
```
* [Medium] 1590. Make Sum Divisible by P

### Top K Frequent Elements
```python
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        return [el for el, c in count.most_common(k)]

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        unique = list(count.keys())

        def partition(left, right, pivot_index) -> int:
            pivot_frequency = count[unique[pivot_index]]
            # 1. move pivot to end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]  

            # 2. move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]  

            return store_index

        def quickselect(left, right, k_smallest) -> None:
            """
            Sort a list within left..right till kth less frequent element
            takes its place. 
            """
            # base case: the list contains only one element
            if left == right: 
                return

            # select a random pivot_index
            pivot_index = random.randint(left, right)     

            # find the pivot position in a sorted list   
            pivot_index = partition(left, right, pivot_index)

            # if the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return 
            # go left
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            # go right
            else:
                quickselect(pivot_index + 1, right, k_smallest)

        n = len(unique) 
        # kth top frequent element is (n - k)th less frequent.
        # Do a partial sort: from less frequent to the most frequent, till
        # (n - k)th less frequent element takes its place (n - k) in a sorted array. 
        # All element on the left are less frequent.
        # All the elements on the right are more frequent.  
        quickselect(0, n - 1, n - k)
        # Return top k frequent elements
        return unique[n - k:]
```
* [Medium] [Solution] 347. Top K Frequent Elements

### Contiguous Array
```python
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0: -1}  # count of 1: index
        ans, count = 0, 0
        for i in range(len(nums)):
            count += 1 if nums[i] == 1 else -1
            if count in d:
                ans = max(ans, i - d[count])
            else:
                d[count] = i
        return ans
```
* [Medium] [Solution] 525. Contiguous Array

### Simulation, cache
```python
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def nextday(cells):
            return [int(i > 0 and i < 7 and cells[i-1] == cells[i+1])
                    for i in range(8)]

        seen = {}
        while N > 0:
            c = tuple(cells)
            if c in seen:
                N %= seen[c] - N
            seen[c] = N

            if N >= 1:
                N -= 1
                cells = nextday(cells)

        return cells
```
* [Medium] [Solution] 957. Prison Cells After N Days

### 3Sum
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic = collections.defaultdict(int)
        soln = []

        #creates a dictionary and counts the array
        for x in nums:
            dic[x] += 1

        #gets a list of keys and the length
        keys = list(dic.keys())
        length_k = len(keys)

        #for each key
        for i in range(length_k):
            x = keys[i]

            # case: [x, x, -2*x]
            #if the negative sum exists, add it to the solution
            if dic[x]>1:
                if -2*x in dic:
                    soln.append([x, x,-2*x])

            # case: [x, y, -(x+y)
            for j in range(i+1,length_k):
                y = keys[j]
                #ensures we dont double count
                if -(x+y) in dic and -(x+y) not in [x,y]:
                    soln.append([x, y, -(x+y)])

        #special case of 0
        if 0 in dic:
            if dic[0] == 2:
                soln.remove([0,0,0])

        #returns unique solution sets
        soln=[list(x) for x in set(tuple(sorted(x)) for x in soln)]

        return soln
```
* [Medium] 15. 3Sum

### OrderedDict
```python
class LRUCache:

    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.lru_cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        key = str(key)
        if(key not in self.lru_cache):
            return -1
        value = self.lru_cache[key]
        del self.lru_cache[key]
        self.lru_cache[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        key = str(key)
        if key not in self.lru_cache:
            if len(self.lru_cache) < self.max_capacity:
                self.lru_cache[key] = value
            else:
                self.lru_cache.popitem(last=False)
                self.lru_cache[key] = value
        else:
            del self.lru_cache[key]
            self.lru_cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```
* [Medium] 146. LRU Cache

### Generalized Neighbors
```python
class MagicDictionary:

    def _genneighbors(self, word):
        for i in range(len(word)):
            yield word[:i] + '*' + word[i+1:]

    def buildDict(self, words):
        self.words = set(words)
        self.count = collections.Counter(nei for word in words
                                        for nei in self._genneighbors(word))

    def search(self, word):
        return any(self.count[nei] > 1 or
                   self.count[nei] == 1 and word not in self.words
                   for nei in self._genneighbors(word))


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
```
* [Medium] [Solution] 676. Implement Magic Dictionary

### Random
```python
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.list = []


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dic:
            return False
        self.list.append(val)
        self.dic[val] = len(self.list) - 1
        return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dic:
            return False
        if self.dic[val] == len(self.list) - 1:
            del self.dic[val]
        else:
            idx = self.dic[val] 
            self.list[idx] = self.list[-1]
            self.dic[self.list[idx]] = idx
            del self.dic[val]
        self.list.pop()
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.list[random.randint(0, len(self.list) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```
* [Medium] 380. Insert Delete GetRandom O(1)

### Boyer-Moore Voting Algorithm
```python
if not nums:
            return []

        # 1st pass
        count1, count2, candidate1, candidate2 = 0, 0, None, None
        for n in nums:
            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 += 1
            elif count2 == 0:
                candidate2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        # 2nd pass
        result = []
        for c in [candidate1, candidate2]:
            if nums.count(c) > len(nums)//3:
                result.append(c)

        return result
```
* [Medium] 229. Majority Element II

### Vote
```python
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        count = {v: [0] * len(votes[0]) for v in votes[0]}  # {team1: [rank1_count, rank2_count, ...]}
        for a in votes:
            for i, v in enumerate(a):
                count[v][i] -= 1
        return ''.join(sorted(votes[0], key=lambda v: count[v] + [v]))
```
* [Medium] 1366. Rank Teams by Votes

### Happen again
```python
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        d, n, r = {0: -1}, 0, 0
        for i, c in enumerate(s):
            if c in vowels:
                n ^= vowels[c]
            if n not in d:
                d[n] = i
            else:
                r = max(r, i - d[n])
        return r
```
* [Medium] 1371. Find the Longest Substring Containing Vowels in Even Counts

### Prefix Sum
```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_cnt = collections.defaultdict(int)
        sum_cnt[0] = 1
        cum_sum, cnt = 0, 0
        for i in range(len(nums)):
            cum_sum += nums[i]                       
            cnt += sum_cnt[cum_sum-k]
            sum_cnt[cum_sum] += 1    

        return cnt
```
* [Medium] [Solution] 560. Subarray Sum Equals K

### Binary Search with Rolling Hash
```python
class Solution:
    def search(self, L: int, a: int, modulus: int, n: int, nums: List[int]) -> str:
        """
        Rabin-Karp with polynomial rolling hash.
        Search a substring of given length
        that occurs at least 2 times.
        @return start position if the substring exits and -1 otherwise.
        """
        # compute the hash of string S[:L]
        h = 0
        for i in range(L):
            h = (h * a + nums[i]) % modulus

        # already seen hashes of strings of length L
        seen = {h} 
        # const value to be used often : a**L % modulus
        aL = pow(a, L, modulus) 
        for start in range(1, n - L + 1):
            # compute rolling hash in O(1) time
            h = (h * a - nums[start - 1] * aL + nums[start + L - 1]) % modulus
            if h in seen:
                return start
            seen.add(h)
        return -1

    def longestRepeatingSubstring(self, S: str) -> int:
        n = len(S)
        # convert string to array of integers
        # to implement constant time slice
        nums = [ord(S[i]) - ord('a') for i in range(n)]
        # base value for the rolling hash function
        a = 26
        # modulus value for the rolling hash function to avoid overflow
        modulus = 2**24

        # binary search, L = repeating string length
        left, right = 1, n
        while left <= right:
            L = left + (right - left) // 2
            if self.search(L, a, modulus, n, nums) != -1:
                left = L + 1
            else:
                right = L - 1

        return left - 1
```
* [Lock] [Medium] [Solution] 1062. Longest Repeating Substring

### Binary Search with Rolling Hash
```python
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        P, MOD = 113, 10**9 + 7
        Pinv = pow(P, MOD-2, MOD)
        def check(guess):
            def rolling(A, length):
                if length == 0:
                    yield 0, 0
                    return

                h, power = 0, 1
                for i, x in enumerate(A):
                    h = (h + x * power) % MOD
                    if i < length - 1:
                        power = (power * P) % MOD
                    else:
                        yield h, i - (length - 1)
                        h = (h - A[i - (length - 1)]) * Pinv % MOD

            hashes = collections.defaultdict(list)
            for ha, start in rolling(A, guess):
                hashes[ha].append(start)
            for ha, start in rolling(B, guess):
                iarr = hashes.get(ha, [])
                if any(A[i:i+guess] == B[start:start+guess] for i in iarr):
                    return True
            return False

        lo, hi = 0, min(len(A), len(B)) + 1
        while lo < hi:
            mi = (lo + hi) // 2
            if check(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo - 1
```
* [Medium] [Solution] 718. Maximum Length of Repeated Subarray

### palindrome
```python
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        dicts = {}
        for i, word in enumerate(words):
            dicts[word[::-1]] = i
        
        def isPalindrome(s):
            return s == s[::-1]
        
        res = set()
        for i, word in enumerate(words):
            for j in range(len(word) + 1):  # to cover the case of empty string 
                left = word[:j]
                right = word[j:]
                # case 1: e.g. ["abcd","dcba"], ["lls","s"], ["sssll","lls"]
                if isPalindrome(left) and (right in dicts) and (i!=dicts[right]):
                    res.add((dicts[right], i))
                # case 2: E.G. ["a", ""]
                if isPalindrome(right) and (left in dicts) and (i!=dicts[left]):
                    res.add((i, dicts[left]))
        return res
```
[Hard] 336. Palindrome Pairs

### Substring Rolling Hash
```python
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        some_strings = set()
        for j in range(len(text)):
            for i in range(j):
                if text.startswith(text[i:j], j):
                    some_strings.add(text[i:j])
        return len(some_strings)
```
* [Hard] 1316. Distinct Echo Substrings

### Brute Force
```python
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        for word in words:
            i = -1
            for c in word:
                i = s.find(c, i+1)
                if i < 0:
                    break
            if i >= 0:
                ans += 1
        return ans
```
* [Medium] 792. Number of Matching Subsequences

### Delta Hash Table Counter
```python
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        A_points, B_points, d = [], [], collections.defaultdict(int)

        # Filter points having 1 for each matrix respectively.
        for r in range(len(A)):
            for c in range(len(A[0])):
                if A[r][c]:
                    A_points.append((r, c))

                if B[r][c]:
                    B_points.append((r, c))

        # For every point in filtered A, calculate the
        # linear transformation vector with all points of filtered B
        # count the number of the pairs that have the same transformation vector
        for r_a, c_a in A_points:
            for r_b, c_b in B_points:
                d[(r_b - r_a, c_b - c_a)] += 1

        return max(d.values() or [0])
```
* [Medium] [Solution] 835. Image Overlap

### HashSet and Intelligent Sequence Building
```python
class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
```
* [Hard] [Solution] 128. Longest Consecutive Sequence

### Reverse location list
```python
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        #places: this stores the indices of every digit from 0 to 9
        places = defaultdict(list)
        for i in reversed(range(len(s))):
            key = int(s[i])
            places[key].append(i)

        for e in t: #we loop over t and check every digit
            key = int(e) #current digit
            if not places[key]: #digit is not in s, return False
                return False 
            i = places[key][-1] #location of current digit
            for j in range(key): #only loop over digits smaller than current digit
                if places[j]: #there is a digit smaller than current digit, return false
                    if places[j][-1] < i: 
                        return False
            places[key].pop()

        return True
```
* [Hard] 1585. Check If String Is Transformable With Substring Sort Operations


## Depth-first Search <a name="dfs"></a>
---
### Pre-Order
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.ans = []
        def dfs(node):
            if not node:
                return
            self.ans.append(node.val)
            for c in node.children:
                dfs(c)
        dfs(root)
        return self.ans
    
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        stack = root and [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            stack.extend([c for c in node.children[::-1] if c])
        return ans
```
* [Easy] 589. N-ary Tree Preorder Traversal

### Post-Order
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            diff = abs(left - right)
            self.ans += diff
            return node.val + left + right

        dfs(root)
        return self.ans
```
* [Easy] [Solution] 563. Binary Tree Tilt

### Sum of Left Leaves
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None: 
            return 0

        def is_leaf(node):
            return node is not None and node.left is None and node.right is None

        stack = [root]
        total = 0
        while stack:
            sub_root = stack.pop()
            # Check if the left node is a leaf node.
            if is_leaf(sub_root.left):
                total += sub_root.left.val
            # If the right node exists, put it on the stack.
            if sub_root.right is not None:
                stack.append(sub_root.right)
            # If the left node exists, put it on the stack.
            if sub_root.left is not None:
                stack.append(sub_root.left)

        return total
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        def process_subtree(subtree, is_left):

            # Base case: If this subtree is empty, return 0
            if subtree is None:
                return 0

            # Base case: This is a leaf node.
            if subtree.left is None and subtree.right is None:
                return subtree.val if is_left else 0

            # Recursive case: return result of adding the left and right subtrees.
            return process_subtree(subtree.left, True) + process_subtree(subtree.right, False)

        return process_subtree(root, False)
```
* [Easy] 404. Sum of Left Leaves

### DFS
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)
```
* [Easy] [Solution] 100. Same Tree

### island
```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        R, C = len(grid), len(grid[0])

        def neighbours(r, c):
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        def dfs(r, c):
            grid[r][c] = '0'
            for nr, nc in neighbours(r, c):
                if grid[nr][nc] == '1':
                    dfs(nr, nc)

        island = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    island += 1
                    dfs(r, c)

        return island

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def is_island(x, y):
            if x >= len(grid) or x < 0:
                return False
            if y >= len(grid[0]) or y < 0 :
                return False
            if grid[x][y] == '0':
                return False
            return True
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                else:
                    queue = collections.deque([(i, j)])
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in delta:
                            new_x, new_y = x + dx, y + dy
                            if is_island(new_x, new_y):
                                queue.append((new_x, new_y))
                                grid[new_x][new_y] = '0'
                    ans += 1 
        return ans
```
[Medium] 200. Number of Islands.md

### search max area
```python
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        seen = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                   and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 
                    + area(r-1, c) 
                    + area(r+1, c) 
                    + area(r, c-1) 
                    + area(r, c+1))

        return max(area(r, c)
                  for r in range(len(grid))
                  for c in range(len(grid[0])))
    
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        seen = set()
        ans = 0
        for r0, row in enumerate(grid):
            for c0, val in enumerate(row):
                if val and (r0, c0) not in seen:
                    shape = 0
                    stack = [(r0, c0)]
                    seen.add((r0, c0))
                    while stack:
                        r, c = stack.pop()
                        shape += 1
                        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) 
                                and grid[nr][nc] and (nr, nc) not in seen):
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    ans = max(ans, shape)
        return ans
```
* [Medium] [Solution] 695. Max Area of Island

### Search map, fix one axes and move forward the other
```python
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        def search(matrix, rows, cols):
            if rows >= len(matrix) or cols < 0:
                return False
            upper_right = matrix[rows][cols]
            if upper_right > target:
                return search(matrix, rows, cols - 1)
            elif upper_right < target:
                return search(matrix, rows + 1, cols)
            else:
                return True
        return search(matrix, 0, len(matrix[0]) - 1)
```
* [Medium] 240. Search a 2D Matrix II

### DFS + Greedy
```python
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        if word1 >= word2 > '':
            return word1[0] + self.largestMerge(word1[1:], word2)
        if word2 >= word1 > '':
            return word2[0] + self.largestMerge(word1, word2[1:])
        return word1 + word2

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ans = ''
        while word1 and word2:
            if word1 > word2:
                ans += word1[0]
                word1 = word1[1:]
            else:
                ans += word2[0]
                word2 = word2[1:]
        ans += word1
        ans += word2
        return ans
```
* [Medium] 1754. Largest Merge Of Two Strings

### Flood Fill
```python
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)

        dfs(sr, sc)
        return image
```
* [Easy] [Solution] 733. Flood Fill

### DFS
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return
        if target == original:
            return cloned
        return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)
```
* [Medium] 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree

### Count Preorder Traversal
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        count = 0

        stack = [(root, 0) ]
        while stack:
            node, path = stack.pop()
            if node is not None:
                # compute occurences of each digit 
                # in the corresponding register
                path = path ^ (1 << node.val)
                # if it's a leaf, check if the path is pseudo-palindromic
                if node.left is None and node.right is None:
                    # check if at most one digit has an odd frequency
                    if path & (path - 1) == 0:
                        count += 1
                else:
                    stack.append((node.right, path))
                    stack.append((node.left, path))

        return count

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        def preorder(node, path):
            nonlocal count
            if node:
                # compute occurences of each digit 
                # in the corresponding register
                path = path ^ (1 << node.val)
                # if it's a leaf, check if the path is pseudo-palindromic
                if node.left is None and node.right is None:
                    # check if at most one digit has an odd frequency
                    if path & (path - 1) == 0:
                        count += 1
                else:                    
                    preorder(node.left, path)
                    preorder(node.right, path) 

        count = 0
        preorder(root, 0)
        return count
```
* [Medium] 1457. Pseudo-Palindromic Paths in a Binary Tree

### Return tupple
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        # The result of a subtree is:
        # Result.node: the largest depth node that is equal to or
        #              an ancestor of all the deepest nodes of this subtree.
        # Result.dist: the number of nodes in the path from the root
        #              of this subtree, to the deepest node in this subtree.
        Result = collections.namedtuple("Result", ("node", "dist"))
        def dfs(node):
            # Return the result of the subtree at this node.
            if not node: return Result(None, 0)
            L, R = dfs(node.left), dfs(node.right)
            if L.dist > R.dist: return Result(L.node, L.dist + 1)
            if L.dist < R.dist: return Result(R.node, R.dist + 1)
            return Result(node, L.dist + 1)

        return dfs(root).node
```
* [Medium] [Solution] 865. Smallest Subtree with all the Deepest Nodes

### Spiral
```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for _ in range(n)]
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        def dfs(x, y, d, k):
            ans[x][y] = k
            nx, ny = x+dx[d], y+dy[d]
            if 0 <= nx < n and  0 <= ny < n and ans[nx][ny] == 0:
                dfs(nx, ny, d, k+1)
            else:
                d = (d+1)%4
                nx, ny = x+dx[d], y+dy[d]
                if 0 <= nx < n and  0 <= ny < n and ans[nx][ny] == 0:
                    dfs(nx, ny, d, k+1)
            
        dfs(0, 0, 0, 1)
        return ans
```
* [Medium] 59. Spiral Matrix II

### Maximum Minus Minimum, Postorder with current max and min as parameter and return as answer
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0

        def helper(node, cur_max, cur_min):
            # if encounter leaves, return the max-min along the path
            if not node:
                return cur_max - cur_min
            # else, update max and min
            # and return the max of left and right subtrees
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            left = helper(node.left, cur_max, cur_min)
            right = helper(node.right, cur_max, cur_min)
            return max(left, right)

        return helper(root, root.val, root.val)
```
* [Medium] 1026. Maximum Difference Between Node and Ancestor

### Seen node hash table
```python
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
* [Medium] 133. Clone Graph

### First neighbor
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
* [Medium] 399. Evaluate Division

### Delete Node in a BST
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMin(self, node):
        if node is None:
            return
        while node.left:
            node = node.left
        return node

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return
        if root.val == key:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            temp = self.findMin(root.right)
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
```
* [Medium] * 450. Delete Node in a BST

### The Maze
```python
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        R, C = len(maze), len(maze[0])
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, seen):
            if r == destination[0] and c == destination[1]:
                return True
            seen.add((r, c))
            for dr, dc in d:
                nr, nc = r+dr, c+dc
                while 0 <= nr < R and 0 <= nc < C and maze[nr][nc] == 0:
                    nr, nc = nr+dr, nc+dc
                nr, nc = nr-dr, nc-dc
                if (nr, nc) not in seen:
                    if dfs(nr, nc, seen):
                        return True
            return False

        return dfs(start[0], start[1], set())
```
* [Lock] [Medium] [Solution] 490. The Maze

### DFS, BFS
```python
class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return [i for i in range(10)]

        ans = []
        def DFS(N, num):
            # base case
            if N == 0:
                return ans.append(num)

            tail_digit = num % 10
            # using set() to avoid duplicates when K == 0
            next_digits = set([tail_digit + K, tail_digit - K])

            for next_digit in next_digits:
                if 0 <= next_digit < 10: 
                    new_num = num * 10 + next_digit
                    DFS(N-1, new_num)

        for num in range(1, 10):
            DFS(N-1, num)

        return list(ans)
    
class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return [i for i in range(10)]

        # initialize the queue with candidates for the first level
        queue = [digit for digit in range(1, 10)]

        for level in range(N-1):
            next_queue = []
            for num in queue:
                tail_digit = num % 10
                # using set() to avoid duplicates when K == 0
                next_digits = set([tail_digit + K, tail_digit - K])

                for next_digit in next_digits:
                    if 0 <= next_digit < 10: 
                        new_num = num * 10 + next_digit
                        next_queue.append(new_num)
            # start the next level
            queue = next_queue

        return queue
```
* [Medium] [Solution] 967. Numbers With Same Consecutive Differences

### Prefix Sum
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def pathSum(self, root: TreeNode, sum: int) -> int:
        target = sum
        prev_sum = collections.defaultdict(int)
        prev_sum[0] = 1
        cnt = 0

        def dfs(node, curr_sum):
            nonlocal cnt, prev_sum
            if node is not None:
                curr_sum += node.val
                cnt += prev_sum[curr_sum - target]
                prev_sum[curr_sum] += 1

                dfs(node.left, curr_sum)
                dfs(node.right, curr_sum)
                prev_sum[curr_sum] -= 1

        dfs(root, 0)
        return cnt
```
* [Medium] [Solution] 437. Path Sum III

### Hash Table + Preorder
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        left = {}
        def dfs(node, depth = 0, pos = 0):
            if node:
                left.setdefault(depth, pos)
                self.ans = max(self.ans, pos - left[depth] + 1)
                dfs(node.left, depth + 1, pos * 2)
                dfs(node.right, depth + 1, pos * 2 + 1)

        dfs(root)
        return self.ans
```
* [Medium] [Solution] 662. Maximum Width of Binary Tree

### step by step try dfs cycle
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
* [Medium] [Solution] 684. Redundant Connection

### Stack
```python
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]
        #At the beginning, we have a todo list "stack" of keys to use.
        #'seen' represents at some point we have entered this room.
        while stack:  #While we have keys...
            node = stack.pop() # get the next key 'node'
            for nei in rooms[node]: # For every key in room # 'node'...
                if not seen[nei]: # ... that hasn't been used yet
                    seen[nei] = True # mark that we've entered the room
                    stack.append(nei) # add the key to the todo list
        return all(seen) # Return true iff we've visited every room
```
* [Medium] [Solution] 841. Keys and Rooms

### Store Locations
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        seen = collections.defaultdict(
                  lambda: collections.defaultdict(list))

        def dfs(node, x=0, y=0):
            if node:
                seen[x][y].append(node)
                dfs(node.left, x-1, y+1)
                dfs(node.right, x+1, y+1)

        dfs(root)
        ans = []

        for x in sorted(seen):
            report = []
            for y in sorted(seen[x]):
                report.extend(sorted(node.val for node in seen[x][y]))
            ans.append(report)

        return ans
```
* [Medium] [Solution] 987. Vertical Order Traversal of a Binary Tree

### DFS, BFS
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
* [Medium] [Solution] 934. Shortest Bridge

### Cycle
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
* [Medium] 207. Course Schedule

### Reconstruct Itinerary
```python
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        for departure, arrival in tickets:
             graph[departure].append(arrival)

        for airport in graph:
            graph[airport].sort()

        total = len(tickets) + 1

        def dfs(ticket, way):
            if len(way) == total:
                return way

            for i in range(len(graph[ticket])):
                if graph[ticket][i] == None:
                    continue

                arrival = graph[ticket][i]
                graph[ticket][i] = None

                reconstruction = dfs(arrival, way + [arrival])
                if reconstruction:
                    return reconstruction

                graph[ticket][i] = arrival

        return dfs('JFK', ['JFK'])
```
* [Medium] 332. Reconstruct Itinerary

### All Path
```python
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)
        ans = []

        def dfs(node, path):
            if node == N-1:
                ans.append(path)
            else:
                for nei in graph[node]:
                    dfs(nei, path+[nei])
        
        dfs(0, [0])
        return ans
```
* [Medium] 797. All Paths From Source to Target

### inorder to postorder
```python
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            ind = inorder.index(postorder.pop())
            root = TreeNode(inorder[ind])
            root.right = self.buildTree(inorder[ind+1:], postorder)
            root.left = self.buildTree(inorder[:ind], postorder)
            return root
```
* [Medium] 106. Construct Binary Tree from Inorder and Postorder Traversal

### Connected Component
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
            seen[i] = True
            for j in g[i]:
                if not seen[j]:
                    dfs(j)
        
        for i in range(n):
            if not seen[i]:
                num_connected_components += 1
                dfs(i)
        
        return num_connected_components - 1
```
* [Medium] 1319. Number of Operations to Make Network Connected

### 2*DFS
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
* [Medium] 1343. Maximum Product of Splitted Binary Tree

### Level DFS
```python
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        T = collections.defaultdict(set)
        for u, v, w in allowed:
            T[u, v].add(w)

        #Comments can be used to cache intermediate results
        #seen = set()
        def solve(A):
            if len(A) == 1: return True
            #if A in seen: return False
            #seen.add(A)
            return any(solve(cand) for cand in build(A, []))

        def build(A, ans, i = 0):
            if i + 1 == len(A):
                yield "".join(ans)
            else:
                for w in T[A[i], A[i+1]]:
                    ans.append(w)
                    for result in build(A, ans, i+1):
                        yield result
                    ans.pop()

        return solve(bottom)
```
* [Medium] [Solution] 756. Pyramid Transition Matrix

### DFS to find equal and sort
```python
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def dfs(i):
            visited.add(i)
            char.append(s[i])
            idx.append(i)
            for j in g[i]:
                if j not in visited:
                    dfs(j)

        if not pairs or not pairs[0]:
            return s

        S = list(s)
        visited = set()
        g = [[] for _ in range(len(s))]
        for i, j in pairs:
            g[i].append(j)
            g[j].append(i)

        for i in range(len(s)):
            if i not in visited:
                char = []
                idx = []
                dfs(i)
                char = sorted(char)
                idx = sorted(idx)
                for k in range(len(idx)):
                    S[idx[k]] = char[k]

        return ''.join(S)
```
* [Medium] 1202. Smallest String With Swaps

### Reverse graph
```python
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.res = 0    
        roads = set()
        graph = collections.defaultdict(list)
        for u, v in connections:
            roads.add((u, v))
            graph[v].append(u)
            graph[u].append(v)

        def dfs(u, parent):
            self.res += (parent, u) in roads
            for v in graph[u]:
                if v == parent:
                    continue
                dfs(v, u)

        dfs(0, -1)
        return self.res
```
* [Medium] 1466. Reorder Routes to Make All Paths Lead to the City Zero

### Counter, Post-Order
```python
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def dfs(node: int, parent: int):
            cnt = Counter()
            cnt[labels[node]] += 1 
            for child in g.get(node, []):
                if child != parent:
                    cnt += dfs(child, node)
            ans[node] = cnt[labels[node]]
            return cnt

        g, ans = defaultdict(list), [0] * n
        for a, b in edges:
            g[a] += [b]
            g[b] += [a]
        dfs(0, -1)
        return ans
````
* [Medium] 1519. Number of Nodes in the Sub-Tree With the Same Label

### Counter, Post-Order
```python
Runtime: 224 ms
Memory Usage: 15.2 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans
            if not node:
                return collections.Counter()
            if not node.left and not node.right:
                return collections.Counter([0])
            lcount = dfs(node.left)
            rcount = dfs(node.right)
            for ld, ln in lcount.items():
                for rd, rn in rcount.items():
                    if ld+rd+2 <= distance:
                        ans += ln*rn
            return Counter({d+1: n for d, n in (lcount + rcount).items()})

        dfs(root)
        return ans
```
* [Medium] 1530. Number of Good Leaf Nodes Pairs

### Color neighbor component
```python
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < N and 0 <= nc < N:
                    yield nr, nc

        def dfs(r, c, index):
            ans = 1
            grid[r][c] = index
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    ans += dfs(nr, nc, index)
            return ans

        area = {}
        index = 2
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    area[index] = dfs(r, c, index)
                    index += 1

        ans = max(area.values() or [0])
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    seen = {grid[nr][nc] for nr, nc in neighbors(r, c) if grid[nr][nc] > 1}
                    ans = max(ans, 1 + sum(area[i] for i in seen))
        return ans
```
* [Hard] [Solution] 827. Making A Large Island

### Tarjan's algorithm
```python
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = {} # graph as adjacency list 
        for u, v in connections: 
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)

        def dfs(x, p, step): 
            """Traverse the graph and collect bridges using Tarjan's algo."""
            disc[x] = low[x] = step
            for xx in graph.get(x, []): 
                if disc[xx] == inf: 
                    step += 1
                    dfs(xx, x, step)
                    low[x] = min(low[x], low[xx])
                    if low[xx] > disc[x]: ans.append([x, xx]) # bridge
                elif xx != p: low[x] = min(low[x], disc[xx])

        ans = []
        low = [inf]*n
        disc = [inf]*n

        dfs(0, -1, 0)
        return ans
```
* [Hard] 1192. Critical Connections in a Network

**Template 1: (Postorder)**
```python
ans = ...
def dfs(...):
    if not ...:
        return
    ...
    res = ...
    ... = dfs(...)
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
    seen[j] = True
    for j in g[i]:
        if not seen[j]:  
            dfs(j)
for i in range(N):
    if not seen[i]:
        num_connected_components += 1
        dfs(i)

return num_connected_components        
```

* [Medium] 1110. Delete Nodes And Return Forest

## Binary Search <a name="bs"></a>
---
### Binary Search
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
* [Easy] [Solution] 704. Binary Search

### Closest Binary Search Tree Value
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            closest = min(root.val, closest, key = lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest
```
* [Lock] [Easy] [Solution] 270. Closest Binary Search Tree Value

### Binary Search to leftmost - increase one side
```python
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):  # >=
                right = mid
            else:  # <
                left = mid + 1
        return left
```
* [Easy] [Solution] 278. First Bad Version

### Insert Position
```python
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return bisect.bisect_left(nums, target)
```
* [Easy] 35. Search Insert Position

### Arranging Coins
```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            k = (right + left) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            if n < curr:
                right = k - 1
            else:
                left = k + 1
        return right
```
* [Easy] [Solution] 441. Arranging Coins

### search interval
```python
class MyCalendar:

    def __init__(self):
        self.booking = []

    def book(self, start: int, end: int) -> bool:
        left = 0
        right = len(self.booking) - 1
        while left <= right:
            mid = (left + right) // 2
            a, b = self.booking[mid]
            if end > a >= start or b > start >= a:
                return False
            if end <= a:
                right = mid - 1
            elif b <= start:
                left = mid + 1
                
        self.booking.insert(left, (start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
```
* [Medium] [Solution] 729. My Calendar I.md

### Inorder Simulation
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def findSize(self, head):
        ptr = head
        c = 0
        while ptr:
            ptr = ptr.next
            c += 1
        return c

    def sortedListToBST(self, head: ListNode) -> TreeNode:        

        # Get the size of the linked list first
        size = self.findSize(head)

        # Recursively form a BST out of linked list from l --> r
        def convert(l, r):
            nonlocal head

            # Invalid case
            if l > r:
                return None

            mid = (l + r) // 2

            # First step of simulated inorder traversal. Recursively form
            # the left half
            left = convert(l, mid - 1)

            # Once left half is traversed, process the current node
            node = TreeNode(head.val)   
            node.left = left

            # Maintain the invariance mentioned in the algorithm
            head = head.next

            # Recurse on the right hand side and form BST out of them
            node.right = convert(mid + 1, r)
            return node
        return convert(0, size - 1)
```
* [Medium] [Solution] 109. Convert Sorted List to Binary Search Tree

### search boundary
```python
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = bisect.bisect_left(nums, target)  # Find left index
        if start >= len(nums): return [-1, -1]
        end = bisect.bisect_right(nums, target)  # Find right index
        if (end == 0 and nums[end] != target) or target != nums[end-1]: return [-1, -1]
        return [start, end-1]  # bisect_right returns the position after the last occurrence of our target. So we return end -1
```
* [Medium] [Solution] 34. Find First and Last Position of Element in Sorted Array

### Binary Search
```python
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if sum((a - 1) // mid for a in nums) > maxOperations:
                left = mid + 1
            else:
                right = mid
        return left
```
* [Medium] 1760. Minimum Limit of Balls in a Bag

### Binary Search without diplicate
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        ans = -1
        
        while left <= right:
            mid = left + (right - left) // 2

            if target == nums[mid]:
                ans = mid
                break
            elif (nums[left] <= target < nums[mid] or
                    target <= nums[mid] < nums[left] or
                    nums[mid] < nums[left] <= target):
                right = mid - 1
            else:
                left = mid + 1

        return ans

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(left, right, target):
            if left > right:
                return -1
            
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid            
            elif (nums[left] <= target < nums[mid] or
                    target <= nums[mid] < nums[left] or
                    nums[mid] < nums[left] <= target):
                return binary_search(left, mid-1, target)
            else:
                return binary_search(mid+1, right, target)        
            
        return binary_search(0, len(nums)-1, target)
```
* [Medium] 33. Search in Rotated Sorted Array

### Binary Search with duplicate
```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        N = len(nums)
        if N == 0: return False
        end = N - 1
        start = 0

        # returns true if we can reduce the search space in current binary search space
        def isBinarySearchHelpful(start, element):
            return nums[start] != element

        # returns true if element exists in first array, false if it exists in second
        def existsInFirst(start, element):
            return nums[start] <= element
        
        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return True

            if not isBinarySearchHelpful(start, nums[mid]):
                start += 1
                continue
            # which array does pivot belong to.
            pivotArray = existsInFirst(start, nums[mid])

            # which array does target belong to.
            targetArray = existsInFirst(start, target)
            if pivotArray ^ targetArray: # If pivot and target exist in different sorted arrays, recall that xor is true when both operands are distinct
                if pivotArray:
                    start = mid + 1 # pivot in the first, target in the second
                else:
                    end = mid - 1 # target in the first, pivot in the second
            else: # If pivot and target exist in same sorted array
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1

        return False

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums: return False

        def dfs(left, right):
            if left >= right: return False
            mid = left + (right - left) // 2
            if nums[mid] == target: return True
            if nums[mid] == nums[left] and nums[left] == nums[right - 1]:
                return dfs(left, mid) or dfs(mid + 1, right)
            if nums[mid] >= nums[left]:                
                return dfs(left, mid) if nums[left] <= target < nums[mid] else dfs(mid + 1, right)
            else:
                return dfs(mid + 1, right) if nums[mid] < target <= nums[right - 1] else dfs(left, mid)
        
        return dfs(0, len(nums))

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def dfs(beg, end):
            if end - beg <= 1: return target in nums[beg: end+1]
            
            mid = (beg + end)//2
            if nums[mid] > nums[end]:   # eg. 3,4,5,6,7,1,2
                if nums[end] < target <= nums[mid]:
                    return dfs(beg, mid)
                else:
                    return dfs(mid + 1, end)
            elif nums[mid] < nums[end]: # eg. 6,7,1,2,3,4,5
                if nums[mid] < target <= nums[end]:
                    return dfs(mid + 1, end)
                else:
                    return dfs(beg, mid)
            else:
                return dfs(mid+1, end) or dfs(beg, mid)
    
        return dfs(0, len(nums)-1)
```
* [Medium] 81. Search in Rotated Sorted Array II

### Fix upper bound and increase lower bound
```python
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo, hi = 1, max(nums)
        def check(n):
            s = 0
            for x in nums:
                s += math.ceil(x / n)
            return s <= threshold

        while lo < hi:
            mi = lo + (hi - lo) // 2
            if check(mi):
                hi = mi
            else:
                lo = mi + 1

        return lo
```
* [Medium] 1283. Find the Smallest Divisor Given a Threshold

### search row head then column
```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        R, C = len(matrix), len(matrix[0])
        if C == 0: return False
        row = bisect.bisect_left(list(zip(*matrix))[0], target)
        if row < R and matrix[row][0] == target:
            return True
        row -= 1
        col = bisect.bisect_left(matrix[row], target)
        if col == C:
            return False
        elif matrix[row][col] == target:
            return True
        else:
            return False
```
* [Medium] 74. Search a 2D Matrix

### Greedy, Binary Search
```python
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        h = collections.defaultdict(list)
        for i, ch in enumerate(source):
            h[ch].append(i)        
        i, j = -1, 0
        count = 1
        while j < len(target):
            if target[j] not in h:
                return -1
            idx = bisect.bisect(h[target[j]], i) 
            if idx == len(h[target[j]]):
                i = -1
                count += 1
                continue
            i = h[target[j]][idx]
            j += 1
        return count
```
* [Lock] [Medium] 1055. Shortest Way to Form String

### Random
```python
class Solution:

    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] += w[i-1]
        self.w = w  # prefix sum

    def pickIndex(self) -> int:
        ranint = random.randint(1, self.w[-1])
        return bisect.bisect_left(self.w, ranint)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
```
* [Medium] 528. Random Pick with Weight

### Binary Search to leftmost - increase one side
```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        b, e = 0, len(nums) - 1
        while b < e:
            m = (b + e) // 2
            if m % 2 == 1 and nums[m - 1] == nums[m]:
                b = m + 1
            elif  m % 2 == 0 and nums[m + 1] == nums[m]:
                b = m + 2
            else:
                e = m
        return nums[b]
```
* [Medium] 540. Single Element in a Sorted Array

### pivort as first element
```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # If the list has just one element then return that element.
        if len(nums) == 1:
            return nums[0]

        # left pointer
        left = 0
        # right pointer
        right = len(nums) - 1

        # if the last element is greater than the first element then there is no rotation.
        # e.g. 1 < 2 < 3 < 4 < 5 < 7. Already sorted array.
        # Hence the smallest element is first element. A[0]
        if nums[right] > nums[0]:
            return nums[0]

        # Binary search way
        while right >= left:
            # Find the mid element
            mid = left + (right - left) // 2
            # if the mid element is greater than its next element then mid+1 element is the smallest
            # This point would be the point of change. From higher to lower value.
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # if the mid element is lesser than its previous element then mid element is the smallest
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            # if the mid elements value is greater than the 0th element this means
            # the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]
            if nums[mid] > nums[0]:
                left = mid + 1
            # if nums[0] is greater than the mid value then this means the smallest value is somewhere to the left
            else:
                right = mid - 1
```
* [Medium] [Solution] 153. Find Minimum in Rotated Sorted Array

### Sort, Binary Search, insert
```python
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # sort increasing in first dimension and decreasing on second
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        def lis(nums):
            dp = []
            for i in range(len(nums)):
                idx = bisect_left(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
            return len(dp)
        # extract the second dimension and run the LIS
        return lis([e[1] for e in envelopes])
```
* [Hard] 354. Russian Doll Envelopes

### Rotated Sorted Array, dupliczated
```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        mid = 0
        while left < right:
            mid = left + (right - left) // 2;           
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1

        return nums[left]
```
* [Hard] 154. Find Minimum in Rotated Sorted Array II

### Binary search to edge condition
```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1

        return l
```
* [Medium] [Solution] 162. Find Peak Element

### H-Index
```python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        left, right = 0, N-1
        ans = 0
        while right >= left:
            mid = left + (right - left) // 2
            if citations[mid] >= N - mid:
                ans = max(ans, N - mid)
                right = mid -1 
            else:
                left = mid + 1

        return ans
```
* [Medium] 275. H-Index II

### Max to sum 
```python
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def cannot_split(max_wgt):
            s = 0
            days = 1
            for w in weights:
                s += w
                if s > max_wgt:
                    s = w
                    days += 1
            return days > D

        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if cannot_split(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo
```
* [Medium] 1011. Capacity To Ship Packages Within D Days

### 0 to max
```python
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def getSum(val):
            total = 0
            for i in range(n):
                total += arr[i] if arr[i] <= val else val
            return total

        lo, hi, n = 0, max(arr), len(arr)
        diff = collections.defaultdict(set)
        while lo <= hi:
            mi = (lo+hi) // 2
            total = getSum(mi)
            # store the absolute differences
            diff[abs(total - target)].add(mi)
            if total < target:
                lo = mi + 1
            elif total > target:
                hi = mi - 1
            else:
                break

        # Find the lowest diff
        cand = diff[sorted(diff.keys())[0]]

        # Return the minimum value among candidates
        return sorted(cand)[0]
```
* [Medium] 1300. Sum of Mutated Array Closest to Target

### Range Sum Search
```python
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        #build prefix sum 
        prefix = [[0]*(n+1) for _ in range(m+1)]

        for i, j in itertools.product(range(m), range(n)):
            prefix[i+1][j+1] = prefix[i+1][j] + prefix[i][j+1] - prefix[i][j] + mat[i][j]

        def below(k): 
            """reture true if there is such a sub-matrix of length k"""
            for i, j in itertools.product(range(m+1-k), range(n+1-k)):
                if prefix[i+k][j+k] - prefix[i][j+k] - prefix[i+k][j] + prefix[i][j] <= threshold: return True
            return False 

        #binary search
        max_square = 0
        lo, hi = 1, min(m, n)
        while lo <= hi: 
            mi = lo + (hi - lo)//2
            if below(mi):
                max_square = max(max_square, mi)
                lo = mi + 1
            else:
                hi = mi - 1

        return max_square
```
* [Medium] 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold

### Time series search
```python
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay): return -1
        left, right = 1, max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            flow = bouq = 0
            for a in bloomDay:
                flow = 0 if a > mid else flow + 1
                if flow >= k:
                    flow = 0
                    bouq += 1
                    if bouq == m: break
            if bouq == m:
                right = mid
            else:
                left = mid + 1
        return left
```
* [Medium] 1482. Minimum Number of Days to Make m Bouquets

### 2D Binary Search
```python
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        R, C = binaryMatrix.dimensions()
        leftmost_col = -1
        
        def dfs(r, c):
            nonlocal leftmost_col
            if r >= R or c < 0:
                return
            if binaryMatrix.get(r,c) == 1:
                leftmost_col = c
                dfs(r, c-1)
            else:
                dfs(r+1, c)
        
        dfs(0, C-1)
        return leftmost_col
```
* [Medium] 30day. Leftmost Column with at Least a One

### Rabin-Karp Algorithm
```python
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        
        def RabinKarp(M, q):
            if M == 0: return True
            h, t, d = (1<<(8*M-8))%q, 0, 256
            dic = defaultdict(list)
            for i in range(M): 
                t = (d * t + ord(S[i]))% q
            dic[t].append(i-M+1)
            for i in range(len(S) - M):
                t = (d*(t-ord(S[i])*h) + ord(S[i + M]))% q
                for j in dic[t]:
                    if S[i+1:i+M+1] == S[j:j+M]:
                        return (True, S[j:j+M])
                dic[t].append(i+1)
            return (False, "")
        
        beg, end = 0, len(S)
        q = (1<<31) - 1 
        Found = ""
        while beg + 1 < end:
            mid = (beg + end)//2
            isFound, candidate = RabinKarp(mid, q)
            if isFound:
                beg, Found = mid, candidate
            else:
                end = mid

        return Found
```
* [Hard] 1044. Longest Duplicate Substring

### Binary Search + Sliding Window
```python
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def possible(guess):
            #Is there k or more pairs with distance <= guess?
            count = left = 0
            for right, x in enumerate(nums):
                while x - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k

        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mi = (lo + hi) // 2
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1

        return lo
```
* [Hard] [Solution] 719. Find K-th Smallest Pair Distance

### Search index range
```python
class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.loc = collections.defaultdict(list)
        for i, n in enumerate(arr):
            self.loc[n].append(i)    
        self.nums = sorted(self.loc.keys(), key = lambda n: len(self.loc[n]), reverse=True)

    def query(self, left: int, right: int, threshold: int) -> int:
        for n in self.nums:
            if len(self.loc[n]) < threshold: return -1
            l, r = bisect.bisect_left(self.loc[n], left), bisect.bisect_right(self.loc[n], right)
            if r - l >= threshold: return n
        return -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
```
* [Hard] 1157. Online Majority Element In Subarray

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

* [Hard] 1231. Divide Chocolate
* [Medium] 1201. Ugly Number III
* [Medium] [Solution] 875. Koko Eating Bananas

## Greedy <a name="greedy"></a>
---
### character conversion
```python
class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ''
        for c in s:
            if c.isalpha() and ord(c) < ord('a'):
                ans += chr(ord('a')+ord(c)-ord('A')) 
            else:
                ans += c
        return ans
```
* [Easy] 709. To Lower Case

### Max Profit
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = sys.maxsize
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i]-min_price > max_profit:
                max_profit = prices[i]-min_price
        return max_profit
```
* [Easy] [Solution] 121. Best Time to Buy and Sell Stock

### Greedy
```python
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        i = 1
        ans = [0]*num_people
        i = 1
        while candies-i > 0:
            ans[(i-1)%num_people] += i
            candies -= i
            i += 1
        ans[(i-1)%num_people] += candies
        return ans
```
* [Easy] [Solution] 1103. Distribute Candies to People

### Greedy
```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        for v in collections.Counter(s).values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans
```
* [Easy] [Solution] 409. Longest Palindrome

### Append leftmost and rightmost element
```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        tmp =[0] + flowerbed +[0]

        index = 1 

        while index< len(tmp)-1:
            if tmp[index-1]== 0 and tmp[index]==0 and tmp[index+1]==0:
                n -= 1
                index += 1 
            index += 1
        return n <= 0
```
* [Easy] [Solution] 605. Can Place Flowers

### frequency
```python
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        N = len(arr)
        cnt = collections.Counter(arr)
        ans = cur = 0
        for _, c in cnt.most_common():
            if cur < N//2:
                cur += c
                ans += 1
            else:
                break
        return ans
```
* [Medium] 1338. Reduce Array Size to The Half.md

### Heap to record smallest
```python
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights) - 1):
            d = heights[i + 1] - heights[i]
            if d > 0:
                heapq.heappush(heap, d)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i
        return len(heights) - 1
```
* [Medium] 1642. Furthest Building You Can Reach

### global != local inversion
```python
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        for idx, value in enumerate(A):
            if abs(idx - value) > 1:
                return False
        return True
```
* [Medium] 775. Global and Local Inversions

### construct string from base to remaining
```python
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = ''
        i = 0
        while i < n:
            if k > (n-i-1)*26:
                r = k - (n-i-1)*26
                ans += chr(96+r)
                ans += 'z'*(n-i-1)
                break
            else:
                k -= 1
                ans += 'a'
            i += 1
        return ans
```
* [Medium] 1663. Smallest String With A Given Numeric Value

### One Pass + Count
```python
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # initialize the counter of zeros to k
        # to pass the first 1 in nums
        count = k
        
        for num in nums:
            # if the current integer is 1
            if num == 1:
                # check that number of zeros in-between 1s
                # is greater than or equal to k
                if count < k:
                    return False
                # reinitialize counter
                count = 0
            # if the current integer is 0
            else:
                # increase the counter
                count += 1
                
        return True
```
* [Medium] 1437. Check If All 1's Are at Least Length K Places Away

### Two Pointers, greedy from back
```python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people) - 1
        ans = 0
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return ans
```
* [Medium] [Solution] 881. Boats to Save People

### Focus on some patter
```python
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        a = 'a'
        b = 'b'
        if x < y:
            x, y = y, x
            a, b = b, a
        seen = Counter()
        ans = 0
        for c in s + 'x':
            if c in 'ab':
                if c == b and 0 < seen[a]:
                    ans += x
                    seen[a] -= 1
                else:
                    seen[c] += 1
            else:
                ans += y * min(seen[a], seen[b])
                seen = Counter()

        return ans
```
* [Medium] 1717. Maximum Score From Removing Substrings

### Sort then greedy add rectangle area arithmetic sum
```python
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True) # inventory high to low 
        inventory += [0]
        ans = 0
        k = 1
        for i in range(len(inventory)-1): 
            if inventory[i] > inventory[i+1]: 
                if k*(inventory[i] - inventory[i+1]) < orders: 
                    ans += k*(inventory[i] + inventory[i+1] + 1)*(inventory[i] - inventory[i+1])//2 # arithmic sum 
                    orders -= k*(inventory[i] - inventory[i+1])
                else: 
                    q, r = divmod(orders, k)
                    ans += k*(2*inventory[i] - q + 1) * q//2 + r*(inventory[i] - q)
                    return ans % 1_000_000_007
            k += 1
```
* [Medium] 1648. Sell Diminishing-Valued Colored Balls

### Sort then lost min and gain max
```python
class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        deque = collections.deque(tokens)
        ans = bns = 0
        while deque and (P >= deque[0] or bns):
            while deque and P >= deque[0]:
                P -= deque.popleft()
                bns += 1
            ans = max(ans, bns)

            if deque and bns:
                P += deque.pop()
                bns -= 1

        return ans
```
* [Medium] [Solution] 948. Bag of Tokens

### Split Two Strings to Make Palindrome
```python
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        i, j = 0, len(a) - 1
        while i < j and a[i] == b[j]:
            i, j = i + 1, j - 1
        s1, s2 = a[i:j + 1], b[i:j + 1]

        i, j = 0, len(a) - 1
        while i < j and b[i] == a[j]:
            i, j = i + 1, j - 1
        s3, s4 = a[i:j + 1], b[i:j + 1]

        return any(s == s[::-1] for s in (s1,s2,s3,s4))
```
* [Medium] 1616. Split Two Strings to Make Palindrome

### Sort by end and filter by start
```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        prev_end = float('inf')
        ans = 0
        for start, end in sorted(points, key=lambda x: x[1]):
            if start <= prev_end <= end:
                continue
            else:
                prev_end = end
                ans += 1
        return ans
```
* [Medium] 452. Minimum Number of Arrows to Burst Balloons

### First match
```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if (sum(gas) - sum(cost) < 0):
            return -1

        gas_tank, start_index = 0, 0

        for i in range(len(gas)):
            gas_tank += gas[i] - cost[i]

            if gas_tank < 0:
                start_index = i+1
                gas_tank = 0

        return start_index
```
* [Medium] 134. Gas Station

### zip_longest
```python
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        for v1, v2 in itertools.zip_longest(version1.split('.'), version2.split('.')):
            v1 = int(v1) if v1 else 0
            v2 = int(v2) if v2 else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0
```
* [Medium] 165. Compare Version Numbers

### Greedy over sorted intervals
```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        prev_end = intervals[0][1]
        ans = 0
        for start, end in intervals[1:]:
            if prev_end > start:
                ans += 1
            else:
                prev_end = end
        return ans

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: 
            return 0
        N = len(intervals)
        intervals.sort(key=lambda x: x[0])
        prev_end = intervals[0][1]
        count = 0
        for start, end in intervals[1:]:
            if start < prev_end <= end:
                count += 1
            elif prev_end > end:
                count += 1
                prev_end = end
            else:
                prev_end = end

        return count
```
* [Medium] [Solution] 435. Non-overlapping Intervals

### Greedy check expected position
```python
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums: return False
        mi, mi2 = nums[0], float('inf')
        for num in nums[1:]:
            if num <= mi:
                mi = num
            elif num <= mi2:
                mi2 = num
            else:
                return True
        return False
```
* [Medium] 334. Increasing Triplet Subsequence

### 1-bit and 2-bit Characters
```python
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        parity = bits.pop()
        while bits and bits.pop(): parity ^= 1
        return parity == 0
```
* [Easy] [Solution] 717. 1-bit and 2-bit Characters

### Logical Deduction with Caching
```python
class Solution:

    @lru_cache(maxsize=None)
    def cachedKnows(self, a, b):
        return knows(a, b)

    def findCelebrity(self, n: int) -> int:
        self.n = n
        celebrity_candidate = 0
        for i in range(1, n):
            if self.cachedKnows(celebrity_candidate, i):
                celebrity_candidate = i
        if self.is_celebrity(celebrity_candidate):
            return celebrity_candidate
        return -1

    def is_celebrity(self, i):
        for j in range(self.n):
            if i == j: continue
            if knows(i, j) or not knows(j, i):
                return False
        return True
```
* [Lock] [Medium] [Solution] 277. Find the Celebrity

### Range Caching
```python
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        result = [0] * length

        # просто обозначим в каждой ячейке что делать с последующими, начиная от этой
        for idx_start, idx_end, inc in updates:
            result[idx_start] += inc
            if idx_end + 1 < length:
                result[idx_end + 1] -= inc

        # посчитаем все разом
        for idx in range(1, length):
            result[idx] += result[idx - 1]

        return result
```
* [Lock] [Medium] [Solution] 370. Range Addition

### Overlap interval Sum
```python
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        n = len(timeSeries)
        if n == 0:
            return 0

        total = 0
        for i in range(n - 1):
            total += min(timeSeries[i + 1] - timeSeries[i], duration)
        return total + duration
```
* [Medium] [Solution] 495. Teemo Attacking

### Profit
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
* [Medium] [Solution] 714. Best Time to Buy and Sell Stock with Transaction Fee

### Hash table, Sort and remaining
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
* [Medium] [Solution] 870. Advantage Shuffle

### Last index
```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_pos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i
        return last_pos == 0
```
* [Medium] [Solution] 55. Jump Game

### Maximum Swap
```python
class Solution:
    def maximumSwap(self, num: int) -> int:
        A = list(map(int, str(num)))
        last = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for d in range(9, x, -1):
                if last.get(d, None) != None and last.get(d, None) > i:
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int("".join(map(str, A)))
        return num
```
* [Medium] [Solution] 670. Maximum Swap

### Doubled Pairs
```python
class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        count = collections.Counter(A)
        for x in sorted(A, key = abs):
            if count[x] == 0: continue
            if count[2*x] == 0: return False
            count[x] -= 1
            count[2*x] -= 1

        return True
```
* [Medium] [Solution] 954. Array of Doubled Pairs

### Valid Parenthesis
```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0  # [lower, upper bound]
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if hi < 0: break
            lo = max(lo, 0)

        return lo == 0
```
* [Medium] [Solution] 678. Valid Parenthesis String

### Post-Order
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.ans = 0
        covered = {None}

        def dfs(node, par = None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if (par is None and node not in covered or
                        node.left not in covered or node.right not in covered):
                    self.ans += 1
                    covered.update({node, par, node.left, node.right})

        dfs(root)
        return self.ans
```
* [Hard] [Solution] 968. Binary Tree Cameras

### Prefix Sum
```python
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        res = total = 0
        satisfaction.sort()
        while satisfaction and satisfaction[-1] + total > 0:
            total += satisfaction.pop()
            res += total
            
        return res
```
* [Hard] 1402. Reducing Dishes

### Prefix Sum
```python
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix = {0: -1}
        best_till = [math.inf] * len(arr)
        ans = best = math.inf
        for i, curr in enumerate(itertools.accumulate(arr)):
            if curr - target in prefix:
                end = prefix[curr - target]
                if end > -1:
                    ans = min(ans, i - end + best_till[end])
                best = min(best, i - end)
            best_till[i] = best
            prefix[curr] = i
        return -1 if ans == math.inf else ans
```
* [Medium] 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum

### Substring Range Overlay
```python
class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        tmp = {c: [s.index(c), s.rindex(c)+1] for c in set(s)}
        # find all the correct boundries
        pairs = []
        for c in set(s):
            l = tmpl = s.index(c)
            r = tmpr = s.rindex(c) + 1
            while True:
                t = set(s[tmpl:tmpr])
                for k in t:
                    tmpl = min(tmpl, tmp[k][0])
                    tmpr = max(tmpr, tmp[k][1])
                if (tmpl, tmpr) == (l, r):
                    break
                l, r = tmpl, tmpr
            pairs.append([l, r])

        # greedy find the optimal solution
        # similar to find the maximum number of meetings
        pairs.sort(key=lambda x: x[1])
        res, last = [], 0
        for b, e in pairs:
            if b >= last:
                res.append(s[b:e])
                last = e
        return res
```
* [Medium] 1520. Maximum Number of Non-Overlapping Substrings

### Odd sum subarray
```python
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        count = [1, 0]
        cur = res = 0
        for a in arr:
            cur ^= a & 1
            res += count[1 - cur]
            count[cur] += 1
        return res % (10**9 + 7)
```
* [Medium] 1524. Number of Sub-arrays With Odd Sum

### Minimum Swaps
```python
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def count(arr):
            ans = 0
            for i in range(n-1, -1, -1):
                if arr[i] == 0:
                    ans += 1
                else:
                    break
            return ans

        arr = [count(row) for row in grid]
        ans = 0
        for i in range(n):
            target = n - i - 1
            if arr[i] >= target:
                continue
            flag = False
            for j in range(i+1, n):
                if arr[j] >= target:
                    flag = True
                    ans += (j - i)
                    arr[i+1:j+1] = arr[i:j]
                    break
            if not flag:
                return -1

        return ans
```
* [Medium] 1536. Minimum Swaps to Arrange a Binary Grid

### Greedy, Work Backwards
```python
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        ns = len(stamp)        
        stamp_patterns = []
        # Step - 1:
        # we need to collect all possible stamp patters, like
        # 'abcde'
        # 'abcd*'
        # '*bcde'
        # 'abc**'
        # '**cde'
        # 'ab***'
        # '*bc**'
        # '**cd*'
        # '***de'
        # ‘****e’ and etc
        for window_size in range(1, ns + 1):
            for i in range(ns - window_size + 1):
                curr = '*' * i + stamp[i:i + window_size] + '*' * (ns - window_size - i)
                stamp_patterns.append(curr)
        stamp_patterns.append('*' * ns)

        res = []
        nt = len(target)
        # Step - 2
        # '*****' is our final target
        while target != '*' * nt:
            old_target = target
            # greedy, keep replace current target string with possible patter
            for pattern in stamp_patterns:
                inx = target.find(pattern)
                if inx != -1:
                    target = target[:inx] + '*' * ns + target[inx + ns:]
                    res.append(inx)
            if old_target == target:
                return []

        return res[::-1]
```
* [Hard] [Solution] 936. Stamping The Sequence

### Greedy add with count and visited
```python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        N = len(s)
        cnt = collections.Counter(s)
        visited = collections.defaultdict(int)
        ans = "0"
        for i in range(N):
            cnt[s[i]] -= 1
            if visited[s[i]]: continue
            while s[i] < ans[-1] and cnt[ans[-1]]:
                visited[ans[-1]] = 0
                ans = ans[:-1]
            ans += s[i]
            visited[s[i]] = 1

        return ans[1:]
```
* [Hard] 316. Remove Duplicate Letters

### Minimum Number of Increments
```python
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = pre = 0
        for a in target:
            res += max(a - pre, 0)
            pre = a
        return res
```
* [Hard] 1526. Minimum Number of Increments on Subarrays to Form a Target Array

**Template 1:**
```python
ans = []
A.sort()
for i in ragen(len(A)):
    if /* max profit */:
        ans += ...
        
return ans
```

* [Medium] [Solution] 767. Reorganize String
* [Medium] [Solution] 738. Monotone Increasing Digits
* [Easy] [Solution] 874. Walking Robot Simulation
* [Medium] * 1111. Maximum Nesting Depth of Two Valid Parentheses Strings

## Breadth-first Search <a name="bfs"></a>
---
### Level-Order
```python
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        level = [root]
        while level:
            ans += [sum([node.val for node in level])/len(level)]
            level = [c for node in level if node for c in [node.left, node.right] if c]
        return ans
```
* [Easy] [Solution] 637. Average of Levels in Binary Tree

### Minimum Depth
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        q = collections.deque()
        q.append((root,1))

        while q:
            node, level = q.popleft()
            if not node.left and not node.right:
                return level

            for node in [node.left, node.right]:
                if node:
                    q.append((node, level+1))
                    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None: 
            return 0
        if root.left == None and root.right == None: # Reach leaf node
            return 1
        if root.left == None:
            return self.minDepth(root.right) + 1
        if root.right == None:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
```
* [Easy] 111. Minimum Depth of Binary Tree

### expand from answer 
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
* [Medium] [Solution] 542. 01 Matrix

### Level order
```python
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(code):
            for i in range(4):
                x = int(code[i])
                for diff in (-1, 1):
                    y = (x + diff + 10) % 10
                    yield code[:i] + str(y) + code[i + 1:]

        deadSet = set(deadends)
        if "0000" in deadSet: return -1
        q = deque(["0000"])
        steps = 0
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == target:
                    return steps
                for nei in neighbors(curr):
                    if nei in deadSet: continue
                    deadSet.add(nei)  # Marked as visited
                    q.append(nei)
            steps += 1

        return -1
```
* [Medium] 752. Open the Lock

### Level order
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = [root] if root else None
        ans = []
        while q:
            nq = []
            cur = []
            for node in q:
                cur += [node.val]
                for c in [node.left, node.right]:
                    if c:
                        nq += [c]
            ans += [cur]
            q = nq
        return ans
```
* [Medium] 102. Binary Tree Level Order Traversal

### Level order
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        l = [root]
        while l:
            pre, l = l, [child for p in l for child in [p.left, p.right] if child]
        return sum(node.val for node in pre)
```
* [Medium] 1302. Deepest Leaves Sum

### BFS
```python
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        depth = 1
        level = [root] if root else []
        if d == 1:
            new_node = TreeNode(v)
            new_node.left = root
            root = new_node
        else:
            while level:
                if depth + 1 == d:
                    for node in level:
                        if node:
                            new_node = TreeNode(v)
                            if node.left:
                                new_node.left = node.left
                            node.left = new_node

                            new_node = TreeNode(v)
                            if node.right:
                                new_node.right = node.right
                            node.right = new_node
                    break
                else:
                    next_level = [c for node in level if node for c in [node.left , node.right]]
                level = next_level
                depth += 1

        return root
```
* [Medium] [Solution] 623. Add One Row to Tree

### Search grid
```python
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return -1
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1  

        R, C = len(grid), len(grid[0])
        q = collections.deque([(0,0, 1)])
        grid[0][0] = 1

        def neighbours(r, c):
            for nr, nc in [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)]:
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        while q:
            r, c, step = q.popleft()
            if r == R-1 and c == C-1:
                return step
            for nr, nc in neighbours(r, c):
                if not grid[nr][nc]:
                    grid[nr][nc] = 1
                    q.append((nr, nc, step+1))
        return -1
```
* [Medium] 1091. Shortest Path in Binary Matrix

### BFS
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        level = root and [root]
        while level:
            ans.append([node for node in level][-1].val)
            level = [c for node in level for c in [node.left, node.right] if c]
        return ans
```
* [Medium] [Solution] 199. Binary Tree Right Side View

### Jump to index
```python
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        q = [start]

        while q:
            node = q.pop(0)
            # check if reach zero
            if arr[node] == 0:
                return True
            if arr[node] < 0:
                continue

            # check available next steps            
            for i in [node + arr[node], node - arr[node]]:
                if 0 <= i < n:
                    q.append(i)

            # mark as visited
            arr[node] = -arr[node]

        return False
    
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if 0 <= start < len(arr) and arr[start] >= 0:
            if arr[start] == 0:
                return True

            arr[start] = -arr[start]
            return self.canReach(arr, start+arr[start]) or self.canReach(arr, start-arr[start])

        return False
```
* [Medium] 1306. Jump Game III

### Jump to home
```python
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        max_val = max([x]+forbidden) + a + b
        jumps = [0] + [math.inf]*(max_val)
        for pos in forbidden: 
            jumps[pos] = -1
        stack = deque([0])
        while stack:
            pos=stack.popleft()
            if pos + a <= max_val and jumps[pos+a] > jumps[pos]+1:
                stack.append(pos+a)
                jumps[pos+a] = jumps[pos]+1
            if pos-b > 0 and jumps[pos-b] > jumps[pos]+1:
                jumps[pos-b] = jumps[pos]+1
                if pos-b+a <= max_val and jumps[pos-b+a] > jumps[pos]+2:  # It cannot jump backward twice in a row.
                    stack.append(pos-b+a)
                    jumps[pos-b+a] = jumps[pos]+2

        return jumps[x] if jumps[x] < math.inf else -1
```
* [Medium] 1654. Minimum Jumps to Reach Home

### Level-order
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = [root] if root else []
        while q:
            nq = []
            n = len(q)
            for i in range(len(q)):
                if i != n-1:
                    q[i].next = q[i+1]
                if q[i].left:
                    nq += [q[i].left, q[i].right]
            q = nq

        return root
```
* [Medium] 116. Populating Next Right Pointers in Each Node

### Topological Sorting, BFS from leaf to centroid
```python
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        # base cases
        if n <= 2:
            return [i for i in range(n)]

        # Build the graph with the adjacency list
        neighbors = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        # Initialize the first layer of leaves
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        # Trim the leaves until reaching the centroids
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            # remove the current leaves along with the edges
            while leaves:
                leaf = leaves.pop()
                for neighbor in neighbors[leaf]:
                    neighbors[neighbor].remove(leaf)
                    if len(neighbors[neighbor]) == 1:
                        new_leaves.append(neighbor)

            # prepare for the next round
            leaves = new_leaves

        # The remaining nodes are the centroids of the graph
        return leaves
```
* [Medium] 310. Minimum Height Trees

### BFS with seen
```python
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        dq, seen, smallest = deque([s]), {s}, s
        while dq:
            cur = dq.popleft()
            if smallest > cur:
                smallest = cur
            addA = list(cur)    
            for i, c in enumerate(addA):
                if i % 2 == 1:
                    addA[i] = str((int(c) + a) % 10)
            addA = ''.join(addA)        
            if addA not in seen:
                seen.add(addA);
                dq.append(addA)
            rotate = cur[-b :] + cur[: -b]
            if rotate not in seen:
                seen.add(rotate)
                dq.append(rotate)
        return smallest
    
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        rec = set()

        def dfs(s):
            if s in rec:
                return           
            rec.add(s)
            dfs(s[-b:] + s[:-b])
            dfs("".join([str((int(c) + a * (i % 2)) % 10) for i, c in enumerate(s)]))

        dfs(s)
        return min(rec)
```
* [Medium] 1625. Lexicographically Smallest String After Applying Operations

### Bidirectional BFS
```python
class Solution:
    def __init__(self):
        self.length = 0
        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        self.all_combo_dict = collections.defaultdict(list)

    def visitWordNode(self, queue, visited, others_visited):
        current_word, level = queue.popleft()
        for i in range(self.length):
            # Intermediate words for current word
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]

            # Next states are all the words which share the same intermediate state.
            for word in self.all_combo_dict[intermediate_word]:
                # If the intermediate state/word has already been visited from the
                # other parallel traversal this means we have found the answer.
                if word in others_visited:
                    return level + others_visited[word]
                if word not in visited:
                    # Save the level as the value of the dictionary, to save number of hops.
                    visited[word] = level + 1
                    queue.append((word, level + 1))
        return None

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        self.length = len(beginWord)

        for word in wordList:
            for i in range(self.length):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                self.all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


        # Queues for birdirectional BFS
        queue_begin = collections.deque([(beginWord, 1)]) # BFS starting from beginWord
        queue_end = collections.deque([(endWord, 1)]) # BFS starting from endWord

        # Visited to make sure we don't repeat processing same word
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}
        ans = None

        # We do a birdirectional search starting one pointer from begin
        # word and one pointer from end word. Hopping one by one.
        while queue_begin and queue_end:

            # One hop from begin word
            ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            if ans:
                return ans
            # One hop from end word
            ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0
```
* [Medium] [Solution] 127. Word Ladder

### BFS
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
* [Medium] [Solution] 994. Rotting Oranges

### Level order
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
* [Medium] 429. N-ary Tree Level Order Traversal

### Level order
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        level = root and [root]
        ans = []
        forward = True
        while level:
            if forward:
                ans.append([node.val for node in level])
            else:
                ans.append([node.val for node in level[::-1]])
            level = [c for node in level for c in [node.left, node.right] if c]
            forward = not forward

        return ans
```
* [Medium] 103. Binary Tree Zigzag Level Order Traversal

### Surrounded Regions
```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        R, C = len(board), len(board[0])
        q = collections.deque()
        for c in range(C):
            q.append((0, c))
            q.append((R - 1, c))
        for r in range(R):
            q.append((r, 0))
            q.append((r, C - 1))
        while q:
            r, c = q.popleft()
            if 0 <= r < R and 0 <= c < C and board[r][c] == "O":
                # modify the value from O to N
                board[r][c] = "*"
                # append the surrouding cells to queue.
                q.append((r, c+1))
                q.append((r, c-1))
                q.append((r-1, c))
                q.append((r+1, c))  
        for i in range(R):
            for j in range(C):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "*":
                    board[i][j] = "O"
```
* [Medium] 130. Surrounded Regions

### Bipartite, Hash Table as visited group
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
* [Medium] 785. Is Graph Bipartite?

### Bipartite
```python
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        colored = collections.defaultdict(int)

        def dfs(node, color):
            colored[node] = color
            for nei in graph[node]:
                if nei in colored:
                    if colored[nei] == colored[node]:
                        return False
                else:  # Adj nodes to be color inverted.
                    if not dfs(nei, -color):
                        return False
            return True

        for v in graph:
            if v not in colored:
                if not dfs(v, 1):
                    return False
        return True
```
* [Medium] [Solution] 886. Possible Bipartition

### Matrix
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
* [Medium] 529. Minesweeper

### 2 Direction
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
        return ans`
```
* [Medium] * 1129. Shortest Path with Alternating Colors

### BFS, level-order with decreasing candidate set
```python
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        if beginWord == endWord:
            return [beginWord]

        g = collections.defaultdict(list)
        N = len(beginWord)
        wordList.append(beginWord)
        for w in wordList:
            for i in range(N):
                wildcast = w[:i] + '*' + w[i+1:]
                g[wildcast].append(w)
                
        path_dict = collections.defaultdict(list)
        path_dict[beginWord] = [[beginWord]]
        level = {beginWord}
        while level:
            next_level = set()
            new_path_dict = collections.defaultdict(list)
            for cur in level:
                wordSet.discard(cur)
                for i in range(N):
                    wildcast = cur[:i] + '*' + cur[i+1:]
                    for nei in g[wildcast]:
                        if nei in wordSet:
                            next_level.add(nei)
                            for pre_path in path_dict[cur]:
                                new_path_dict[nei].append(pre_path+[nei])
            if endWord in new_path_dict:
                return new_path_dict[endWord]
            level = next_level
            path_dict = new_path_dict
        return []
```
* [Hard] 126. Word Ladder II

### Topological Sort
```python
class Solution:

    WHITE = 1
    GRAY = 2
    BLACK = 3

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create the adjacency list representation of the graph
        adj_list = defaultdict(list)

        # A pair [a, b] in the input represents edge from b --> a
        for dest, src in prerequisites:
            adj_list[src].append(dest)

        topological_sorted_order = []
        is_possible = True

        # By default all vertces are WHITE
        color = {k: Solution.WHITE for k in range(numCourses)}
        def dfs(node):
            nonlocal is_possible

            # Don't recurse further if we found a cycle already
            if not is_possible:
                return

            # Start the recursion
            color[node] = Solution.GRAY

            # Traverse on neighboring vertices
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == Solution.WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == Solution.GRAY:
                         # An edge to a GRAY vertex represents a cycle
                        is_possible = False

            # Recursion ends. We mark it as black
            color[node] = Solution.BLACK
            topological_sorted_order.append(node)

        for vertex in range(numCourses):
            # If the node is unprocessed, then call dfs on it.
            if color[vertex] == Solution.WHITE:
                dfs(vertex)

        return topological_sorted_order[::-1] if is_possible else [] 

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        indegree = [0] * numCourses
        ans = []

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        q = collections.deque([i for i in range(numCourses) if indegree[i] == 0])
        while q:
            pre = q.popleft()
            ans.append(pre)
            for course in graph[pre]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)

        return ans if len(ans) == numCourses else []

class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Prepare the graph
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)

            # Record each node's in-degree
            indegree[dest] = indegree.get(dest, 0) + 1

        # Queue for maintainig list of nodes that have 0 in-degree
        zero_indegree_queue = deque([k for k in range(numCourses) if k not in indegree])

        topological_sorted_order = []

        # Until there are nodes in the Q
        while zero_indegree_queue:

            # Pop one node with 0 in-degree
            vertex = zero_indegree_queue.popleft()
            topological_sorted_order.append(vertex)

            # Reduce in-degree for all the neighbors
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1

                    # Add neighbor to Q if in-degree becomes 0
                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)

        return topological_sorted_order if len(topological_sorted_order) == numCourses else []
```
* [Medium] [Solution] 210. Course Schedule II

### Topological Sort
```python
class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        indeg = [0]*N
        g = collections.defaultdict(list)
        for X, Y in relations:
            g[X-1] += [Y-1]
            indeg[Y-1] += 1
        q = [(i, 1) for i, _ in enumerate(indeg) if _ == 0]
        ans = [0]*N
        while q:
            u, semester = q.pop()
            ans[u] = 1
            if all(ans):
                return semester
            for v in g[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.insert(0, (v, semester+1))

        return -1
```
* [Lock] [Hard] 1136. Parallel Courses

### Minimum Genetic Mutation
```python
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank, queue = set(bank) ,[[start,0]]
        if end not in bank: return -1
        while queue:
            current_word, steps = queue. pop(0)
            if current_word == end: return steps
            for i in range(len(current_word)):
                for letter in ["A","C","G","T"]:
                    if letter != current_word[i]:
                        temp = current_word[:i] + letter + current_word[i+1:]
                        if temp in bank:
                            queue.append([temp, steps+1])
                            bank.remove(temp)
        return -1
```
* [Medium] 433. Minimum Genetic Mutation

### BFS with visited
```python
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curs = [0]  # store current layers
        visited = {0}
        step = 0

        # when current layer exists
        while curs:
            nex = []

            # iterate the layer
            for node in curs:
                # check if reached end
                if node == n-1:
                    return step

                # check same value
                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)

                # clear the list to prevent redundant search
                graph[arr[node]].clear()

                # check neighbors
                for child in [node-1, node+1]:
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.append(child)

            curs = nex
            step += 1

        return -1
```
* [Hard] 1345. Jump Game IV

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
            seen[el] = True
            q.append(nei)
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
                seen.add((r, c))
                q.append((nr, nc))
    step += 1
return -1
```

**Template 4:**
```python
N = ...
g = collections.defaultdict(list)
indeg = [0]*N
for src, dst in XXX:
    g[src] += [dst]
    indeg[dst] += 1
q = collections.deque([i for i, v in enumerate(indeg) if v == 0])
ans = []
while q:
    src = q.popleft()
    ans += [src]
    for dst in g[src]:
        indeg[dst] -= 1
        if indeg[dst] == 0:
            q += [dst]

return ans if len(ans) == N else []
```

## Two Pointers <a name="tp"></a>
---
### walk backward
```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        for i in range(m+n-1, -1, -1):
            if p1 < 0 or p2 < 0: break
            if nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
              
        while p2 >= 0:
            nums1[i] = nums2[p2]
            i -= 1
            p2 -= 1
```
* [Easy] 88. Merge Sorted Array

### Two Pointers
```python
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        N = len(A)
        # i, j: negative, positive parts
        j = 0
        while j < N and A[j] < 0:
            j += 1
        i = j - 1

        ans = []
        while 0 <= i and j < N:
            if A[i]**2 < A[j]**2:
                ans.append(A[i]**2)
                i -= 1
            else:
                ans.append(A[j]**2)
                j += 1

        while i >= 0:
            ans.append(A[i]**2)
            i -= 1
        while j < N:
            ans.append(A[j]**2)
            j += 1

        return ans
```
* [Easy] [Solution] 977. Squares of a Sorted Array

### Sort Array By Parity
```python
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1
        while True:
            while i < j and not A[i] & 1: i += 1
            while i < j and A[j] & 1: j -= 1
            if i < j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
            else:
                break
        return A
```
* [Easy] [Solution] 922. Sort Array By Parity

### Cycle, slow/fast start from head
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
* [Easy] [Solution] 141. Linked List Cycle

### Is Subsequence
```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        j = 0
        for i in range(len(t)):
            if t[i] == s[j]:
                j += 1
            if j == len(s):
                return True
        return False
```
* [Easy] 392. Is Subsequence

### fix one and slide over the other two
```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while (lo < hi):
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
        return target - diff
```
* [Medium] 16. 3Sum Closest.md

### Sorted candidate pointer
```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if nums == None or len(nums) == 0:
            return nums
        N = len(nums)
        nums.sort()
        ans = []
        for i in range(N-3):
            for j in range(i+1, N-2):
                t = target - nums[i] -  nums[j]
                min_sum = nums[j+1] + nums[j+2]
                max_sum = nums[-1] + nums[-2]
                if t < min_sum or t > max_sum:
                    continue
                left = j+1
                right = N-1
                while left < right:
                    cur = nums[left] + nums[right]
                    if cur == t:
                        ans += [[nums[i], nums[j], nums[left], nums[right]]]
                        left += 1
                        right -= 1
                    elif cur < t:
                        left += 1
                    else:
                        right -= 1
        ans = set([tuple(x) for x in ans])
        return ans
```
* [Medium] 18. 4Sum.md

### Greedy add
```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # left pointer and right pointer
        i, j = 0, len(arr)-1
        while j-i+1 != k:
            # will stop once we have k elements
            # else keep shifting pointers towards minimum difference
            left_diff = abs(arr[i] - x)
            right_diff = abs(arr[j] - x)
            if left_diff > right_diff:
                i += 1
            else:
                j -= 1
        return arr[i:j+1]
```
* [Medium] 658. Find K Closest Elements.md

### Greedy add, parallel viewpoint
```python
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        start = 0
        last = -1
        count = 0
        for i in range(len(nums)):
            if nums[i] > right:
                start = i + 1
            else:
                if nums[i] >= left:
                    last = i
                if last >= start:
                    count += last - start + 1

        return count
```
* [Medium] 795. Number of Subarrays with Bounded Maximum

### Greedy, Two Pointers, iterate based on two pointer value
```python
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, res = 0, len(height)-1, 0
        while left < right:
            area = (right-left) * min(height[right], height[left])
            res = max(res, area)
            if height[right] < height[left]: right-=1  
            else: left+=1
        return res
```
* [Medium] [Solution] 11. Container With Most Water

### first decreasing element from right
```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # first decreasing element from right
        i = len(nums) - 2
        while (i >= 0 and nums[i+1] <= nums[i]):
            i -= 1

        # nums[j] = element just greater than nums[i]
        if i >= 0:
            j = len(nums)-1
            while (j >= 0 and nums[j] <= nums[i]):
                j -= 1

            # swap nums[i], nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # reverse nums[i+1],...
        nums[i+1:] = nums[i+1:][::-1]
```
* [Medium] [Solution] 31. Next Permutation

### Greedy Increase and assign
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        i = 1
        for j in range(2, len(nums)):
            if (nums[i-1] != nums[j]) or (nums[i] != nums[j]):
                i += 1        
            nums[i] = nums[j]   
        return i+1
```
* [Medium] 80. Remove Duplicates from Sorted Array II

### Greedy increase then rebase
```python
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        N = len(nums)
        i, j = 0, 0
        ans = []
        while i < N:
            while j + 1 < N and nums[j + 1] == nums[j] + 1:
                j += 1
            if i != j:
                ans.append('{}->{}'.format(nums[i], nums[j]))
            else:
                ans .append('{}'.format(str(nums[i])))
            j = j + 1
            i = j

        return ans
```
* [Medium] 228. Summary Ranges

### Shortest Subarray to be Removed to Make Array Sorted
```python
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        N = len(arr)
        left, right = 0, N - 1
        while left + 1 < N and arr[left] <= arr[left + 1]:
            left += 1
        if left == N - 1: 
            return 0
        while right > left and arr[right - 1] <= arr[right]:
            right -= 1
        ans = min(N - left - 1, right)
        i, j = 0, right
        while i <= left and j < N:
            if arr[j] >= arr[i]:
                ans = min(ans, j - i - 1)
                i += 1
            else:
                j += 1
        return ans
```
* [Medium] 1574. Shortest Subarray to be Removed to Make Array Sorted

### Contains Duplicate
```python
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        N = len(nums)
        if t == 0 and len(nums) == len(set(nums)):
            # Quick response for special case on t = 0
            # t = 0 requires at last one pair of duplicate elements
            return False
        for i, cur_val in enumerate(nums):
            for j in range(i+1, i+k+1):
                if j >= N:
                    # avoid index out of boundary
                    break
                if abs(cur_val - nums[j]) <= t:
                    # hit: 
                    # i != j, | i-j | <= k
                    # | nums[i] - nums[j] | <= t
                    return True

        return False
```
* [Medium] 220. Contains Duplicate III

### Cycle entrance
```python
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare
```
* [Medium] [Solution] 287. Find the Duplicate Number

### Sliding window, Two Pointers, iterate right pointer
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
* [Medium] [Solution] 713. Subarray Product Less Than K

### Greedy, Two Pointers, iterate left pointer
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
* [Medium] [Solution] 763. Partition Labels

### Two Pointers, iterate left and right pointer
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
* [Medium] [Solution] 838. Push Dominoes

### Two Pointers, iterate left and right pointer with yield
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
* [Easy] [Solution] 844. Backspace String Compare

### Three pointer
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
* [Medium] [Solution] 923. 3Sum With Multiplicity

### Group into Blocks
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
* [Easy] [Solution] 925. Long Pressed Name

### Three pointer
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
* [Medium] [Solution] 930. Binary Subarrays With Sum

### Two Pointers, Counter
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
* [Medium] [Solution] 904. Fruit Into Baskets

### Interval intersection
```python
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j, res = 0, 0, []
        la, lb = len(A), len(B)
        while i < la and j < lb:
            if A[i][1] >= B[j][0] and A[i][0] <= B[j][1]:
                res += [[max(A[i][0], B[j][0]), min(A[i][1], B[j][1])]]
            if A[i][1] >= B[j][1]:
                j += 1
            else:
                i += 1
        return res
```
* [Medium] [Solution] 986. Interval List Intersections

### Sort Colors
```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left,right = 0 , 0

        # move all 0's to the left
        while right < len(nums):
            if nums[right] != 0:
                right += 1
                continue
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right += 1

        right = left
        # move all 1' to the left
        while right < len(nums):
            if nums[right] != 1:
                right += 1
                continue
            nums[left],nums[right] = nums[right], nums[left]
            left += 1
            right += 1
```
* [Medium] 75. Sort Colors

### Four pointers
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
* [Medium] 1248. Count Number of Nice Subarrays

### Number of Subsequences
```python
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        mod = 10**9 + 7
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += pow(2, r - l, mod)
                l += 1
        return res % mod
```
* [Medium] 1498. Number of Subsequences That Satisfy the Given Sum Condition

### left right and current pointer
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1;
        ans = 0
        left_max, right_max = 0, 0
        while left < right: 
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += (left_max - height[left])
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += (right_max - height[right])
                right -= 1
        return ans
```
* [Hard] [Solution] 42. Trapping Rain Water

### Maximum Score of 2 increasing path
```python
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        i, j, n, m = 0, 0, len(nums1), len(nums2)
        a, b, res, mod = 0, 0, 0, 10**9 + 7
        while i < n or j < m:
            if i < n and (j == m or nums1[i] < nums2[j]):
                a += nums1[i]
                i += 1
            elif j < m and (i == n or nums1[i] > nums2[j]):
                b += nums2[j]
                j += 1
            else:
                res += max(a, b) + nums1[i]
                i += 1
                j += 1
                a, b = 0, 0
        return (res + max(a, b)) % mod
```
* [Hard] 1537. Get the Maximum Score

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

**Template 4: (Two Pointers, Binary Search)**
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

## Stack <a name="stack"></a>
---
### Greedy add
```python
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for c in S:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
                
        return ''.join(stack)
```
* [Easy] 1047. Remove All Adjacent Duplicates In String.md

### Mapping
```python
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack
```
* [Easy] [Solution] 20. Valid Parentheses

### PreOrder
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

### InOrder
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
### PostOrder
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

### Valid Parentheses
```python
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack
```
* [Easy] [Solution] 20. Valid Parentheses

### 2 element stack: key and count
```python
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['#', 0]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return ''.join(c * k for c, k in stack)
```
* [Medium] 1209. Remove All Adjacent Duplicates in String II

### Greedy
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
* [Medium] [Solution] 946. Validate Stack Sequences

### index-element stack
```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return
        stack = []
        for i, token in enumerate(s):
            if token == ")" and stack and stack[-1][1] == "(":
                stack.pop()
            elif token in ('(',')'):
                stack.append((i,token))     # Trick is to append index and token both to stack. All unmatched/extra brackets will be 
                                            # left on stack which have to be removed from given string.
            else:
                continue
        s = list(s)
        while stack:
            index = stack.pop()[0]
            s.pop(index)                # Remove unmatched from string.
            #s[:] = s[:index] + s[index+1:]

        return ''.join(s)
```
* [Medium] 1249. Minimum Remove to Make Valid Parentheses

### path
```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path_split = path.split("/")
        for subdir in path_split:
            if subdir == "." or len(subdir) == 0:
                continue
            elif subdir == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(subdir)

        return "/"+"/".join(stack)
```
* [Medium] 71. Simplify Path

### Controlled Recursion
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):

        # Stack for the recursion simulation
        self.stack = []

        # Remember that the algorithm starts with a call to the helper function
        # with the root node as the input
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):

        # For a given node, add all the elements in the leftmost branch of the tree
        # under it to the stack.
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:

        # Node at the top of the stack is the next smallest element
        topmost_node = self.stack.pop()

        # Need to maintain the invariant. If the node has a right child, call the
        # helper function for the right child
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```
* [Medium] [Solution] 173. Binary Search Tree Iterator

### Monotonic Stack
```python
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        stk = []
        for i, n in enumerate(nums):
            while stk and stk[-1] > n and len(stk) + N - i > k:
                stk.pop()
            if len(stk) < k:    
                stk.append(n)
        return stk 
```
* [Medium] 1673. Find the Most Competitive Subsequence

### Fix one direction and use decreasing stack to filter element in the other side
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
* [Medium] [Solution] 456. 132 Pattern

### Keep append and pop smaller with different direction
```python
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for new in asteroids:
            while ans and new < 0 < ans[-1]:
                if ans[-1] < -new:
                    ans.pop()
                    continue
                elif ans[-1] == -new:
                    ans.pop()
                break
            else:
                ans.append(new)
        return ans
```
* [Medium] [Solution] 735. Asteroid Collision

### Find Permutation
```python
class Solution:
    def findPermutation(self, s: str) -> List[int]:
        N = len(s)
        res = [0]*(N+1)
        stack = []
        j = 0
        for i in range(1, N+1):
            if s[i - 1] == 'I':
                stack += [i]
                while stack:
                    res[j] = stack.pop()
                    j += 1
            else:
                stack += [i]
        stack += [N+1]
        while stack:
            res[j] = stack.pop()
            j += 1
            
        return res
```
* [Lock] [Medium] [Solution] 484. Find Permutation

### Stack, Hash Table
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
* [Medium] 150. Evaluate Reverse Polish Notation

### 2 element Stack
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
* [![Medium] 394. Decode String](!%5BMedium%5D%20394.%20Decode%20String.md)

### Preprocessing, stack maintain variance from right
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
* [Medium] [Solution] 456. 132 Pattern

### Weighted stack
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
* [Medium] [Solution] 901. Online Stock Span

### Maintain Stack of Minimums
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
* [Medium] [Solution] 907. Sum of Subarray Minimums

### Decreasing stack
```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"

        result = []
        for c in num:
            while k > 0 and result and result[-1] > c:
                result.pop()
                k -= 1
            result.append(c)
        if k > 0:
            result = result[:-k]
        ans = "".join(result)
        return ans.lstrip("0") or "0"
```
* [Medium] 402. Remove K Digits

### Greedy, Stack simulation
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
* [Medium] [Solution] 946. Validate Stack Sequences

### Heap
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
* [Medium] 1130. Minimum Cost Tree From Leaf Values

### Increment stack
```python
class CustomStack:

    def __init__(self, maxSize: int):
        self.n = maxSize
        self.stack = []
        self.inc = [0] * maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.n:
            self.stack.append(x)

    def pop(self) -> int:
        i = len(self.stack) - 1
        if i < 0:
            return -1
        inc = self.inc[i]
        self.inc[i] = 0
        if i: self.inc[i - 1] += inc
        return self.stack.pop() + inc


    def increment(self, k: int, val: int) -> None:
        i = min(k, len(self.stack)) - 1
        if i >= 0:
            self.inc[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
```
* [Medium] 1381. Design a Stack With Increment Operation

### index stack
```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxans = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack += [i]
            else:
                stack.pop()
                if not stack:
                    stack += [i]
                else:
                    maxans = max(maxans, i - stack[-1])

        return maxans
```
* [Hard] [Solution] 32. Longest Valid Parentheses

### Two Stack, operator stack + operation stack
```python
class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return None

        def higher(o1, o2):
            if o1 == '/' or o1 == '*':
                return (o2 == '+' or o2 == '-' or o2 =='(' )
            else: 
                return o2 == '('

        stN = []
        stO = []
        num = 0
        dictO = {'+' : lambda a, b: a+b,
                '-': lambda a, b: b-a,
                 '/': lambda a, b: b //a,
                "*": lambda a, b: a*b,}
        have_num = False
        for i, val in enumerate(s):
            if val.isnumeric():
                num  = num * 10 + int(val)
                have_num = True
            if (not val.isnumeric() and val != ' '):
                if have_num:
                    stN.append(num)
                    num = 0
                    have_num = False
                if val == '(':
                    stO.append(val)
                elif val == ')':
                    while stO[-1] != '(':
                        stN.append(dictO[stO.pop(-1)](stN.pop(-1), stN.pop(-1)))
                    stO.pop()
                else:
                    while stO and not higher(val, stO[-1]):
                        stN.append(dictO[stO.pop(-1)](stN.pop(-1), stN.pop(-1)))
                    stO.append(val)

        if have_num:
            stN.append(num)
        while stO:
            stN.append(dictO[stO.pop(-1)](stN.pop(-1), stN.pop(-1)))
        return stN.pop()
```
* [Lock] [Hard] 772. Basic Calculator III

### stack maintain first and second hightest value index
```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, max_area = [-1], 0
        for i, h in enumerate(heights + [-1]):
            while stack and stack[-1] >= 0 and h <= heights[stack[-1]]:
                max_area = max(heights[stack.pop()] * (i - stack[-1] - 1), max_area)
            stack.append(i)
        return max_area
```
* [Hard] 84. Largest Rectangle in Histogram

### Index Stack
```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxans = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack += [i]
            else:
                stack.pop()
                if not stack:
                    stack += [i]
                else:
                    maxans = max(maxans, i - stack[-1])

        return maxans
```
* [Hard] [Solution] 32. Longest Valid Parentheses

### Next Greater Element
```python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [None] * N
        stack = []
        for i in range(2*N -1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i % N]:
                stack.pop()
            res[i % N] = -1 if not stack else nums[stack[-1]]
            stack.append(i % N)

        return res
```
* [Medium] [Solution] 503. Next Greater Element II

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

* [Medium] [Solution] 636. Exclusive Time of Functions

## Backtracking <a name="backtracking"></a>
---
### DFS
```python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.s = []

        def dfs(lst):
            for node in lst:
                if node.isInteger():
                    self.s += [node.getInteger()]
                else:
                    dfs(node.getList())

        dfs(nestedList)

    def next(self) -> int:
        return self.s.pop(0)

    def hasNext(self) -> bool:
         return self.s

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
```
* [Medium] 341. Flatten Nested List Iterator

### count
```python
class Solution:
    def countVowelStrings(self, n: int) -> int:

        @lru_cache(None)
        def dp(n, i):
            if n == 0: return 1  # Found a valid answer
            if i == 5:  return 0  # Reach to length of vowels [a, e, i, o, u]
            ans = dp(n, i + 1)  # Skip vowels[i]
            ans += dp(n - 1, i)  # Include vowels[i]
            return ans

        return dp(n, 0)
```
* [Medium] 1641. Count Sorted Vowel Strings

### more smaller current more larger result
```python
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        arr = [0]*(2*n-1)     # the array we want to put numbers. 0 means no number has been put here
        i = 0                 # current index to put a number                
        vi = [False] * (n+1)  # check if we have used that number

        # backtracking
        def dfs(arr, i, vi):
            # if we already fill the array successfully, return True
            if i >= (2*n-1):
                return True

            # try each number from n to 1
            for x in range(n, 0, -1):
                # two cases:
                # x > 1, we check two places. Mind index out of bound here.
                # x = 1, we only check one place
                # arr[i] == 0 means index i is not occupied
                if (x > 1 and ((not (arr[i] == 0 and (i+x < 2*n-1) and arr[i+x] == 0)) or vi[x]))  \
                    or (x == 1 and (arr[i] != 0 or vi[x])):
                    continue

                # if it can be placed, then place it
                if x > 1:
                    arr[i] = x
                    arr[i+x] = x
                else:
                    arr[i] = x
                vi[x] = True

                # find the next available place
                nexti = i+1
                while nexti < 2*n-1 and arr[nexti]:
                    nexti += 1

                # place the next one
                if dfs(arr, nexti, vi):
                    # if it success, it is already the lexicographically largest one, we don't search anymore
                    return True

                # backtracking... restore the state
                if x > 1:
                    arr[i] = 0
                    arr[i+x] = 0
                else:
                    arr[i] = 0
                vi[x] = False

            # we could not find a solution, return False
            return False

        dfs(arr, i, vi)
        return arr
```
* [Medium] 1718. Construct the Lexicographically Largest Valid Sequence

### Backtracking
```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:    
        def backtrack(s, candidate):
            if not s: res.append(candidate[:]); return
            for i in range(1, len(s)+1):
                #equal to s[:i] == s[:i][::-1]
                if s[:i] == s[i-1::-1]:
                    candidate.append(s[:i])
                    backtrack(s[i:], candidate)
                    candidate.pop()
        res = []
        backtrack(s, [])

        return res
```
* [Medium] 131. Palindrome Partitioning

### Backtracking with Groups of Numbers
```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                # make a deep copy of the resulting permutation,
                # since the permutation would be backtracked later.
                results.append(list(comb))
                return

            for num in counter:
                if counter[num] > 0:
                    # add this number into the current combination
                    comb.append(num)
                    counter[num] -= 1
                    # continue the exploration
                    backtrack(comb, counter)
                    # revert the choice for the next exploration
                    comb.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))

        return results
```
* [Medium] 47. Permutations II

### Android Unlock Patterns
```python
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:

        # I.e. to move from 1->3, 2 must be chosen earlier.
        reach_conditions = {
            # 4 corners: 1, 3, 7, 9 to reach another corner.
            (1,3): 2, (1,7): 4, (1,9): 5,            
            (3,1): 2, (3,7): 5, (3,9): 6,
            (7,1): 4, (7,3): 5, (7,9): 8,
            (9,1): 5, (9,3): 6, (9,7): 8,

            # 2, 4, 6, 8 can reach anywhere except its opposite side, which need to cross 5.
            (4,6): 5, (6,4): 5, (2,8): 5, (8,2): 5
        }

        def backtrack(chosen):
            count = 0

            for i in range(1, 10):
                if i in chosen:
                    continue

                # If not first time (empty chosen), subject to the condition above
                if chosen:
                    move = (chosen[-1], i)
                    if move in reach_conditions and reach_conditions[move] not in chosen:
                        continue

                chosen.append(i)

                # Valid pattern
                if len(chosen) >= m and len(chosen) <= n:
                    count += 1

                # Can add more
                if len(chosen) < n:
                    count += backtrack(chosen)

                chosen.pop()
            return count

        return backtrack([])
```
* [Lock] [Medium] [Solution] 351. Android Unlock Patterns

### Backtracking, path
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        res = []
        candidates.sort()
        
        def dfs(total, index, path, res):
            if total < 0:
                return
            if total == 0:
                res.append(path)
                return
            for i in range(index, N):
                dfs(total-candidates[i], i, path+[candidates[i]], res)

        dfs(target, 0, [], res)
        return res
```
* [Medium] 39. Combination Sum

### Backtracking, next_start wtih path
```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []
        def backtrack(remain, comb, next_start):
            if remain == 0 and len(comb) == k:
                # make a copy of current combination
                results.append(list(comb))
                return
            elif remain < 0 or len(comb) == k:
                # exceed the scope, no need to explore further.
                return

            # Iterate through the reduced list of candidates.
            for i in range(next_start, 9):
                comb.append(i+1)
                backtrack(remain-i-1, comb, i+1)
                # backtrack the current choice
                comb.pop()

        backtrack(n, [], 0)

        return results
```
* [Medium] 216. Combination Sum III

### Combination, Hash Table
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
* [Medium] [Solution] 17. Letter Combinations of a Phone Number

### Combination
```python
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.c = characters
        self.n = combinationLength
        self.i = 0
        self.ans = []
        self.permute(0, '')

    def permute(self, index, path):
        if len(path) == self.n:
            self.ans.append(path)
            return
        else:
            for i in range(index, len(self.c)):
                self.permute(i + 1, path + self.c[i])

    def next(self) -> str:
        ans = self.ans[self.i]
        self.i += 1
        return ans

    def hasNext(self) -> bool:
        return self.i < len(self.ans)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.n = n = len(characters)
        self.k = k = combinationLength
        self.chars = characters

        # generate first bitmask 1(k)0(n - k)
        self.b = (1 << n) - (1 << n - k)

    def next(self) -> str:
        # convert bitmasks into combinations
        # 111 --> "abc", 000 --> ""
        # 110 --> "ab", 101 --> "ac", 011 --> "bc"
        curr = [self.chars[j] for j in range(self.n) if self.b & (1 << self.n - j - 1)]

        # generate next bitmask
        self.b -= 1
        while self.b > 0 and bin(self.b).count('1') != self.k:
            self.b -= 1

        return ''.join(curr)

    def hasNext(self) -> bool:
        return self.b > 0


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```
* [Medium] 1286. Iterator for Combination

### Permutation
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
* [Medium] 46. Permutations

### Subset
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
        return output
```
* [Medium] [Solution] 78. Subsets

### Recursion
```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return set(tuple(el) for el in output)
```
* [Medium] 90. Subsets II

### Ccount
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
* [Medium] [Solution] 526. Beautiful Arrangement

### Partition
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
* [Medium] [Solution] 842. Split Array into Fibonacci Sequence

### Word Search
```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        N = len(word)
        v = [[0 for _ in range(C)] for _ in range(R)]

        def neighbours(r, c):
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc
                    
        def dfs(r, c, index):
            v[r][c] = True
            index += 1
            if index == N:
                return True
            for nr, nc in neighbours(r, c):
                if not v[nr][nc] and board[nr][nc] == word[index]:
                    if dfs(nr, nc, index):
                        return True
            v[r][c] = False
            return False

        ans = False
        for i in range(R):
            if word[0] in board[i]:
                for j in range(C):
                    if word[0] == board[i][j]:
                        ans = dfs(i, j, 0)
                        if ans:
                            return True
                        else:
                            continue
        return ans
```
* [Medium] 79. Word Search

### Taken not-taken to balnce
```python
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        N = len(requests)
        
        def dfs(buildings, currentIndex):
            if currentIndex == N:
                return 0 if min(buildings) == 0 and max(buildings) == 0  else -999999
            source, destination = requests[currentIndex]
            buildings[source] -= 1
            buildings[destination] += 1
            taken = 1 + dfs(buildings, currentIndex+1)
            buildings[source] += 1
            buildings[destination] -= 1
            not_taken = dfs(buildings, currentIndex+1)
            result = max(taken, not_taken)
            return result

        buildings = [0 for _ in range(n)]
        return dfs(buildings, 0)
```
### Try all combination path
```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queens = []
        grid = [['.' for i1 in range(n)] for i2 in range(n)]
        solution = []

        def isValid(location):
            row, col = location
            for queen in queens:
                x, y = queen
                if abs(row - x) == abs(col - y):
                    return False
                if row == x or col == y:
                    return False
            return True

        def solve(col):
            if col >= n:
                solution.append([''.join(row) for row in grid])
                return

            for r in range(n):
                if isValid((r, col)):
                    grid[r][col] = 'Q'
                    queens.append((r, col))
                    solve(col + 1)
                    grid[r][col] = '.'
                    queens.remove((r, col))

        solve(0)
        return solution
```
* [Hard] 51. N-Queens

### Try all combination count
```python
class Solution:
    def totalNQueens(self, n: int) -> int:
        queens = []
        solution = []
        ans = 0

        def isValid(location):
            row, col = location
            for queen in queens:
                x, y = queen
                if abs(row - x) == abs(col - y):
                    return False
                if row == x or col == y:
                    return False
            return True

        def solve(col):
            nonlocal ans
            if col >= n:
                return 1
            rst = 0
            for r in range(n):
                if isValid((r, col)):
                    queens.append((r, col))
                    rst += solve(col + 1)
                    queens.remove((r, col))
            return rst

        return solve(0)
```
* [Hard] 52. N-Queens II

### Spiral Backtracking
```python
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(cell = (0, 0), d = 0):
            visited.add(cell)
            robot.clean()
            # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
            for i in range(4):
                new_d = (d + i) % 4
                new_cell = (cell[0] + directions[new_d][0], \
                            cell[1] + directions[new_d][1])

                if not new_cell in visited and robot.move():
                    backtrack(new_cell, new_d)
                    go_back()
                # turn the robot following chosen direction : clockwise
                robot.turnRight()

        # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        backtrack()
```
* [Lock] [Hard] [Solution] 489. Robot Room Cleaner

### Sort before backtracking
```python
class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        c = Counter(nums)
        m = len(quantity)
        # we only need at most m different numbers, so we choose the ones which are most abundant
        left = sorted(c.values())[-m:]

        # If the customer with most quantity required can't be fulfilled, we don't need to go further and answer will be false
        quantity.sort(reverse=True)

        def func(left, quantity, customer):
            if customer == m:
                return True

            for i in range(len(left)):
                if left[i] >= quantity[customer]:
                    left[i] -= quantity[customer]
                    if func(left, quantity, customer+1):
                        return True
                    left[i] += quantity[customer]
            return False

        return func(left, quantity, 0)
```
* [Hard] 1655. Distribute Repeating Integers

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

## Bit Manipulation <a name="bm"></a>
---
### A + ~A = 2**N - 1
```python
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return 2 ** (len(bin(N))-2)-1 - N
```
* [Easy] 1009. Complement of Base 10 Integer

### Power of Two
```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        while n >= 2:
            n, r = divmod(n, 2)
            if r:
                return False

        return True
```
* [Easy] 231. Power of Two

### Number Complement
```python
class Solution:
    def findComplement(self, num: int) -> int:
         return int(''.join(chr(ord('0') + ord('1') - ord(ch)) for ch in bin(num)[2:]),2)
```
* [Easy] 476. Number Complement

### Ascii to hash value
```python
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        if not words: return 0
        N = len(words)
        ans, hashword = 0, [0] * N 
        for i in range(N):
            for j in words[i]:
                hashword[i] |= 1 << (ord(j) - ord('a'))
        for i in range(N):
            for j in range(i+1, N):
                if not (hashword[i] & hashword[j]): 
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans
```
* [Medium] 318. Maximum Product of Word Lengths

### division simulation
```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = (dividend < 0) != (divisor < 0)
        divisor, dividend = abs(divisor), abs(dividend)

        quotient = 0
        the_sum = divisor

        while the_sum <= dividend:
            current_quotient = 1
            while (the_sum << 1) <= dividend:
                the_sum <<= 1
                current_quotient <<= 1            
            dividend -= the_sum
            the_sum = divisor
            quotient += current_quotient

        return min(2**31 -1, max(-quotient if is_negative else quotient, -2**31))
```
* [Medium] 29. Divide Two Integers

### Common Prefix
```python
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        k = 0
        while n != m:
            n >>= 1
            m >>= 1
            k += 1
            
        return n << k
```
* [Medium] 201. Bitwise AND of Numbers Range

### Bitmap
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
* [Medium] [Solution] 78. Subsets

### Next highest 1 bit: n & (n-1))
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
* [Easy] [Solution] 191. Number of 1 Bits

### a xor a = 0, a xor 0 = a
```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for c in s: ans ^= ord(c)
        for c in t: ans ^= ord(c)
        return chr(ans)
```
* [Easy] 389. Find the Difference

### a xor a = 0, a xor 0 = a
```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
```
* [Easy] [Solution] 268. Missing Number

### a xor b xor c = b xor c xor a
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # xor all numbers, so the duplicates are cancelled
        x = functools.reduce(operator.xor, nums)

        # find the bit that is set in x.
        bit = 0
        for i in range(32):
            if x & (1<<i):
                bit = i
                break

        # let the answer be first and second.
        # let first is the number that has the bit set.
        # second does not have the bit set, because x=first^second has the bit set.  
        # now xor all numbers in nums with the bit set.
        # all duplicates will be cancelled
        # only first will remain. second will not be included, as second does not have the bit set.
        first = 0
        for a in nums:
            if a & (1<<bit):
                first ^= a

        # now x=first^second, therefore second = a^first
        second = first^x
        return [first, second]
```
* [Medium] 260. Single Number III

### Bitmask
```python
class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        # Number of bytes in the current UTF-8 character
        n_bytes = 0

        # Mask to check if the most significant bit (8th bit from the left) is set or not
        mask1 = 1 << 7

        # Mask to check if the second most significant bit is set or not
        mask2 = 1 << 6
        for num in data:

            # Get the number of set most significant bits in the byte if
            # this is the starting byte of an UTF-8 character.
            mask = 1 << 7
            if n_bytes == 0:
                while mask & num:
                    n_bytes += 1
                    mask = mask >> 1

                # 1 byte characters
                if n_bytes == 0:
                    continue

                # Invalid scenarios according to the rules of the problem.
                if n_bytes == 1 or n_bytes > 4:
                    return False
            else:

                # If this byte is a part of an existing UTF-8 character, then we
                # simply have to look at the two most significant bits and we make
                # use of the masks we defined before.
                if not (num & mask1 and not (num & mask2)):
                    return False
            n_bytes -= 1
        return n_bytes == 0
```
* [Medium] [Solution] 393. UTF-8 Validation

### Direct
```python
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(bin(x).count('1') in primes
                   for x in range(L, R+1))
```
* [Easy] [Solution] 762. Prime Number of Set Bits in Binary Representation

### Frontier Set, DP Bottom-Up
```python
class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        ans = set()
        cur = {0}
        for x in A:
            cur = {x | y for y in cur} | {x}
            ans |= cur
        return len(ans)
```
* [Medium] [Solution] 898. Bitwise ORs of Subarrays

### Math
```python
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        max1 = max2 = max3 = max4 = float('-inf')
        min1 = min2 = min3 = min4 = float('inf')

        for i in range(len(arr1)):
            tmp1 = arr1[i] - arr2[i] - i
            max1 = max(max1 , tmp1)
            min1 = min(min1 , tmp1)

            tmp2 = arr1[i] + arr2[i] - i
            max2 = max(max2 , tmp2)
            min2 = min(min2 , tmp2)

            tmp3 = arr1[i] + arr2[i] + i
            max3 = max(max3 , tmp3)
            min3 = min(min3 , tmp3)


            tmp4 = arr1[i] - arr2[i] + i
            max4 = max(max4 , tmp4)
            min4 = min(min4 , tmp4)

        return max((max1 - min1), (max2 - min2),(max3 - min3),(max4 - min4))
```
* [Medium] 1131. Maximum of Absolute Value Expression

### g(n) = "1" + f(n)
```python
class Solution:
    def encode(self, num: int) -> str:
        return bin(num + 1)[3:]
```
* [Medium] 1256. Encode Number

### Prefix Sum, Left-right range
```python
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        N = 26
        S = len(s) + 1
        ints = list(map(lambda c: ord(c) - ord('a'), s))

        dp = [0] * S
        for i in range(1, S):
            dp[i] = dp[i-1] ^ (1 << ints[i-1])

        ones = lambda x: bin(x).count('1')
        return [
            ones(dp[r+1] ^ dp[l]) >> 1 <= k
            for l, r, k in queries
        ]
```
* [[Medium] 1177. Can Make Palindrome from Substring](%5BMedium%5D%201177.%20Can%20Make%20Palindrome%20from%20Substring.md

### expand from internal
```python
class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [i ^ (i >> 1) for i in range(2**n)]

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        def recursion(n):
            if n == 1:
                return ['0','1']
            else:
                return ['0' + i for i in recursion(n - 1)] + ['1' + i for i in recursion(n - 1)[::-1]]
            
        return [int(i,2) for i in recursion(n)]
```
[Medium] 89. Gray Code.md
---
**Template 1: (Negative binary, 2's complement representation)**
```python
def twosComplement (value, bitLength) :
    return bin(value & (2**bitLength - 1))[2:]
```
**Template 2: (Gray code)**
```python
def binaryToGray(self, n: int) -> int:
    return n ^ (n >> 1)
```


## Sort <a name="sort"></a>
---
### Greedy most profit
```python
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        A = sorted(boxTypes, key = lambda x:x[1] , reverse = True)
        res = 0
        for i in range(len(A)):
            if truckSize - A[i][0] >= 0:
                res += A[i][0] * A[i][1]
                truckSize = truckSize - A[i][0]
            else:
                res += truckSize * A[i][1]
                break
        return res
```
*  [Lock] [Easy] [Solution] 1710. Maximum Units on a Truck

### Counting Sort
```python
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        S = -1
        count = [0] * 1001
        for i in A:
            count[i] += 1
        lo, hi = 0, 1000
        while lo < hi:
            if lo + hi >= K or count[hi] == 0:
                hi -= 1
            else:
                if count[lo] > 0 if lo < hi else 1:
                    S = max(S, lo + hi)
                lo += 1
        return S
```
* [Lock] [Easy] [Solution] 1099. Two Sum Less Than K

### Shortest Unsorted Continuous Subarray
```python
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums) # returns the another sorted copy     
        start = 0
        end = len(nums)-1
        while start <= end and sorted_nums[start] == nums[start]:
            start += 1
        while end >= 0 and sorted_nums[end] == nums[end]:
            end -= 1

        return 0 if start > end else end - start + 1
```
* [Easy] [Solution] 581. Shortest Unsorted Continuous Subarray

### Two City Scheduling
```python
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        return sum([x[0] if i < len(costs)//2 else x[1] for i, x in enumerate(sorted(costs,key=lambda x: x[0]-x[1]))])
```
* [Easy] 1029. Two City Scheduling

### Max horizontal length * max vertical length = max area
```python
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        dy, dx = max(horizontalCuts[0], h - horizontalCuts[-1]), max(verticalCuts[0], w - verticalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            dy = max(dy, horizontalCuts[i] - horizontalCuts[i - 1])
        for i in range(1, len(verticalCuts)):
            dx = max(dx, verticalCuts[i] - verticalCuts[i - 1])
        return dx * dy % (10**9 + 7)
```
* [Medium] 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

### recursive filter
```python
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = list() 
        products.sort()
        for i in range(1, len(searchWord)+1):
            products = list(filter(lambda x: x.startswith(searchWord[:i]), products))
            result.append(products[:3])
        return result
```
* [Medium] 1268. Search Suggestions System

### Quick sort
```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[k-1]
        b = 0
        a = nums[-1]
        for i in range( len(nums)-1):
            if nums[i] < a:
                nums[i], nums[b] = nums[b], nums[i]
                b += 1
        nums[-1], nums[b] = nums[b], nums[-1]
        if len(nums)-b == k:
            return nums[b]
        elif k > len(nums)-b:
            return self.findKthLargest(nums[:b], k-len(nums)+b)
        else:
            return self.findKthLargest(nums[b+1:], k)
```
* [Medium] 215. Kth Largest Element in an Array

### Covered Interval
```python
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = right = 0
        for i, j in sorted(intervals, key=lambda a: [a[0], -a[1]]):
            res += j > right
            right = max(right, j)
        return res
```
* [Medium] 1288. Remove Covered Intervals

### Bucket Sort
```python
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamp = [0] * 1001
        for trip in trips:
            timestamp[trip[1]] += trip[0]
            timestamp[trip[2]] -= trip[0]

        used_capacity = 0
        for passenger_change in timestamp:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False

        return True
    
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamp = []
        for trip in trips:
            timestamp.append([trip[1], trip[0]])
            timestamp.append([trip[2], -trip[0]])

        timestamp.sort()

        used_capacity = 0
        for time, passenger_change in timestamp:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False

        return True
```
* [Medium] 1094. Car Pooling

### Sort by start, search by end interval
```python
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        N = len(intervals)
        d = {}
        start_idx = {start:i for i, (start, _) in enumerate(intervals)}
        sorted_start = sorted(start for start, _ in intervals)
        for i, (start, end) in enumerate(intervals):
            idx = bisect.bisect_left(sorted_start, end)  # search every end in every sorted_start
            d.setdefault(start, start_idx[sorted_start[idx]] if idx != N else -1)

        return list(map(lambda x: d[x[0]], intervals))
```
* [Medium] 436. Find Right Interval

### Sort interval
```python
class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1].end = max(merged[-1].end, interval.end)

        return merged
```
* [Medium] [Solution] 56. Merge Intervals

### Greedy over start and end pointer
```python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # If there are no meetings, we don't need any rooms.
        if not intervals:
            return 0

        used_rooms = 0

        # Separate out the start and the end timings and sort them individually.
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)

        # The two pointers in the algorithm: e_ptr and s_ptr.
        end_pointer = 0
        start_pointer = 0

        # Until all the meetings have been processed
        while start_pointer < L:
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                # Free up a room and increment the end_pointer.
                used_rooms -= 1
                end_pointer += 1

            # We do this irrespective of whether a room frees up or not.
            # If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
            # remain the same in that case. If no room was free, then this would increase used_rooms
            used_rooms += 1    
            start_pointer += 1   

        return used_rooms

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])  # or heapq.heappush(free_rooms)

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)
```
* [Lock] [Medium] [Solution] 253. Meeting Rooms II

### Sorting via Custom Comparator
```python
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
```
* [Medium] [Solution] 179. Largest Number

### Heap with string iterator
```python
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        heap = []
        for word in d:
            heapq.heappush(heap, (-len(word), word))
        while heap:
            _, word = heapq.heappop(heap)
            it = iter(s)  # maintain string order
            if all(c in it for c in word):
                return word
        return ""
```
* [Medium] [Solution] 524. Longest Word in Dictionary through Deleting

### H-Index
```python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if citations == []:
            return 0
        citations = sorted(citations,reverse=True)
        for i in range(len(citations)):
            if i >= citations[i]:
                return i
        return len(citations)
```
* [Medium] 274. H-Index

### Partition
```python
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse=True)
        mid=len(nums)//2
        nums[::2], nums[1::2] = nums[mid:], nums[:mid]

        return nums
```
* [Medium] 324. Wiggle Sort II

### insertion sort
```python
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        ans = []
        for p in people:
            ans.insert(p[1], p)

        return ans
```
* [Medium] 406. Queue Reconstruction by Height

### Count
```python
class Solution:
    def frequencySort(self, s: str) -> str:
        ans = []
        count = collections.Counter(s)
        for el, c in count.most_common():
            ans += [el] * c

        return ''.join(ans)
```
* [Medium] 451. Sort Characters By Frequency

### Hash Table with pointer
```python
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        N = len(barcodes)
        ans = [0]*N
        i = 0
        for k,v in collections.Counter(barcodes).most_common():
            for _ in range(v):
                ans[i] = k
                i += 2
                if i >= N:
                    i = 1
                    
        return ans
```
* [Medium] 1054. Distant Barcodes

### Hash Table buffer
```python
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        R, C = len(mat), len(mat[0])
        d = collections.defaultdict(list)
        for r in range(R):
            for c in range(C):
                d[r - c].append(mat[r][c])
        for k in d:
            d[k].sort(reverse=1)
        for r in range(R):
            for c in range(C):
                mat[r][c] = d[r - c].pop()
        return mat
```
* [Medium] 1329. Sort the Matrix Diagonally

### Bucket Sort
```python
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        ## RC ##
        ## APPROACH : BUCKET SORT ##
        ## LOGIC ##
        ## 1. lets say we have number from 1 to 10 like, 1,1.1,1.2,2.4,3.5,3.7,4,....10 (not in the same order)
        ## 2. we create n - 1 buckets, why n-1 ? (b1 -> [1-2] b2-> [2-3] b3->[3-4] ...so on 9 buckets)
        ## 3. we can say size of each bucket will be (10 - 1) // 9 i.e 1 ==> (maximum - mimimum) // (length - 1)
        ## 3. Instead of storing all the elements in the buckets, we store minvalue of that bucket and maximum value of that bucket
        ## 4. Maximum Gap can be Case 1: gap between min and max in the bucket itself (or) Case 2: Gap between bucket1 max and bucket2 and so on..

        ## TIME COMPLEXITY : O(N) ##
        ## SPACE COMPLEXITY : O(N) ##

        if len(nums) < 2 or min(nums) == max(nums):
            return 0
        minimum, maximum = min(nums), max(nums)
        size = ( maximum - minimum )//(len(nums) - 1) or 1
        buckets = [[None, None] for _ in range((maximum-minimum)//size + 1)]
        for num in nums:
            # getting the bucket number in which it falls into
            bucket = buckets[(num - minimum)//size]
            bucket[0] = num if bucket[0] is None else min(bucket[0], num)
            bucket[1] = num if bucket[1] is None else max(bucket[1], num)
        buckets = [bucket for bucket in buckets if bucket[0] is not None]
        return max(buckets[i][0]-buckets[i-1][1] for i in range(1, len(buckets)))
```
* [Hard] [Solution] 164. Maximum Gap

### value to correct index, bucket sort
```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        i = 0
        while i < N:
            if nums[i] <= 0 or nums[i] > N:
                i += 1
                continue
            j = nums[i]
            if nums[j-1] != nums[i]:
                nums[j-1], nums[i] = nums[i], nums[j-1]
            else:
                i += 1

        for i in range(N):
            if i + 1 != nums[i]:
                return i + 1
        return N + 1
```
* [Hard] 41. First Missing Positive

### DP Bottom-Up, Greedy, Binary Search
```python
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            i = bisect.bisect(dp, [s + 1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]
```
* [Hard] 1235. Maximum Profit in Job Scheduling

## Linked List <a name="ll"></a>
---
### fast and slow pointer
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        slow = fast = head
        prev = None

        #Reverse the list until it's mid point

        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        if fast and not fast.next:
            slow = slow.next

        while prev and slow:
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next

        return True
```
* [Easy] 234. Palindrome Linked List

### interaction
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        pa = headA
        pb = headB
        while pa is not pb:
            pa = headB if not pa else pa.next
            pb = headA if not pb else pb.next
        return pa
```
* [Easy] [Solution] 160. Intersection of Two Linked Lists

### Linked List
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        current = None
        head = None
        while l1 and l2:
            if l1.val <= l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next
            if current == None:
                current = node
                head = current
            else:
                current.next = node
                current = current.next
        if head == None:
            head = l1 or l2
            current = head
        else:
            current.next = l1 or l2
        return head
```
* [Easy] 21. Merge Two Sorted Lists

### Binary Representation
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head:
            ans = ans * 2 + head.val
            head = head.next
        return ans
```
* [Easy] 1290. Convert Binary Number in a Linked List to Integer

### Delete Node
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
```
* [Easy] [Solution] 237. Delete Node in a Linked List

###  Remove Linked List Elements
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        tmp = dummy
        while dummy.next:
            if dummy.next.val == val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
            
        return tmp.next
```
* [Easy] 203. Remove Linked List Elements

### Two pointer, runner and walker
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        walker = runner = head
        for _ in range(k - 1):
            runner = runner.next
        first, runner = runner, runner.next
        while runner:
            walker = walker.next
            runner = runner.next
        walker.val, first.val = first.val, walker.val
        return head
```
* [Medium] 1721. Swapping Nodes in a Linked List

### Linked List, Greedy
```python
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self.val = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.val is None: self.val = self.it.next()
        return self.val

    def next(self):
        """
        :rtype: int
        """
        if self.val: 
            tmp, self.val = self.val, None
            return tmp
        return self.it.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.val is not None or self.it.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
```
* [Medium] 284. Peeking Iterator

### Greedy, stack
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        s = []
        dup = 0
        while head:
            if not s:
                s += [head]
            else:
                if s[-1].val == head.val:
                    dup = 1
                elif s[-1].val < head.val:
                    if dup:
                        s.pop()
                    dup = 0
                    s += [head]
                    if len(s) >= 2:
                        s[-2].next = s[-1]
            head = head.next
            if not head and dup:
                s.pop()
                if s:
                    s[-1].next = None

        return s[0] if s else None
```
* [Medium] 82. Remove Duplicates from Sorted List II

### Number to string stack
```pyghon
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = 0
        while l1 != None:
            cur = cur*10 + l1.val
            l1 = l1.next
        n1 = cur
        cur = 0
        while l2:
            cur = cur*10 + l2.val
            l2 = l2.next
        n2 = cur
        s = list(str(n1+n2))
        dummy = cur = ListNode(-1)
        while s:
            cur.next = ListNode(s[0])
            cur = cur.next
            s.pop(0)
        return dummy.next 
```
* [Medium] 445. Add Two Numbers II

### cycle entrance
```python
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next: 
            return
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow: 
                break
        if fast != slow: 
            return
        start = head
        meet = slow
        while meet != start:
            meet = meet.next
            start = start.next

        return start
```
* [Medium] 142. Linked List Cycle II

### Rotate List
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        n = 0
        while dummy.next:
            dummy = dummy.next
            n += 1
        if n == 0: return None
        r = n - k%n
        dummy.next = head
        while r > 0:
            dummy = dummy.next
            r -= 1
        nh = dummy.next
        dummy.next = None
        return nh
```
* [Medium] 61. Rotate List

### Reorder List
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return 

        # find the middle of linked list [Problem 876]
        # in 1->2->3->4->5->6 find 4 
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

        # reverse the second part of the list [Problem 206]
        # convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
        # reverse the second half in-place
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next       

        # merge two sorted linked lists [Problem 21]
        # merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
```
* [Medium] 143. Reorder List

### 2 Step Unit
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head: return
        odd, even, = head, head.next
        evenHead = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead

        return head
```
* [Medium] [Solution] 328. Odd Even Linked List

### Elementary Math, Three Pointers
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode(-1)
        current_position = dummy_head
        carry = 0
        while l1 or l2 or carry:
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            carry, new_value = divmod(l1_value + l2_value + carry, 10)
            current_position.next = ListNode(new_value)
            current_position = current_position.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy_head.next
```
* [Medium] [Solution] 2. Add Two Numbers

### Insertion srot, Linked List
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        while prev.next and prev.next.next:
            # incremental number
            if prev.next.val <= prev.next.next.val:
                prev = prev.next
            else:
                cur = prev.next.next
                prev.next.next = cur.next
                tmp = dummy

                # insert node
                while tmp.next.val <= cur.val:
                    tmp = tmp.next
                cur.next = tmp.next
                tmp.next = cur
        return dummy.next
```
* [Medium] 147. Insertion Sort List

### Merge sort, Linked List
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(h1, h2):
            cur = dummy = ListNode(-1)
            while h1 and h2:
                if h1.val < h2.val:
                    cur.next, h1 = h1, h1.next
                else:
                    cur.next, h2 = h2, h2.next
                cur = cur.next
            cur.next = h1 or h2
            return dummy.next
        
        if not head or not head.next: return head
        pres = slow = fast = head
        while fast and fast.next:
            pres = slow
            slow = slow.next
            fast = fast.next.next
        pres.next = None  #cut off in the middle
        first = self.sortList(head)
        second = self.sortList(slow)
        return merge(first, second)
```
* [Medium] 148. Sort List

### Two Pointers
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = second = dummy
        # Advances first pointer so that the gap between first and second is n nodes apart
        for i in range(1, n+2):
            first = first.next
        # Move first to the end, maintaining the gap
        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next
```
* [Medium] [Solution] 19. Remove Nth Node From End of List

### Group reverse
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = prev = start = end = ListNode(-1)
        dummy.next = head
        cur = head
        cnt = k
        while end:
            end = end.next
            cnt -= 1
            if cnt == -1:
                while cur != end:
                    nxt = cur.next
                    cur.next = prev
                    prev = cur
                    cur = nxt
                cnt = k-1
                start.next.next = end
                start_nxt = start.next
                start.next = prev
                start = start_nxt
        
        return dummy.next
```
* [Hard] 25. Reverse Nodes in k-Group

### Merge with Divide And Conquer, Merge Sort
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        hq = [(l.val, idx) for idx, l in enumerate(lists) if l]
        heapq.heapify(hq)
        head = cur = ListNode(None)
        while hq:
            val, idx = heapq.heappop(hq)
            cur.next = ListNode(val)
            cur = cur.next
            node = lists[idx] = lists[idx].next
            if node:
                heapq.heappush(hq, (node.val, idx))
        return head.next
```
* [Hard] [Solution] 23. Merge k Sorted Lists

### Post-Order
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        first = head
        sec = head.next
        first.next = self.swapPairs(sec.next)
        sec.next = first
        return sec
```
* [Medium] 24. Swap Nodes in Pairs

### Two Pointers
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        # before and after are the two pointers used to create two list
        # before_head and after_head are used to save the heads of the two lists.
        # All of these are initialized with the dummy nodes created.
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            # If the original list node is lesser than the given x,
            # assign it to the before list.
            if head.val < x:
                before.next = head
                before = before.next
            else:
                # If the original list node is greater or equal to the given x,
                # assign it to the after list.
                after.next = head
                after = after.next

            # move ahead in the original list
            head = head.next

        # Last node of "after" list would also be ending node of the reformed list
        after.next = None
        # Once all the nodes are correctly assigned to the two lists,
        # combine them to form a single list which would be returned.
        before.next = after_head.next

        return before_head.next
```
* [Medium] [Solution] 86. Partition List

### Iterative
```python
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        # Empty list
        if not head:
            return None

        # Move the two pointers until they reach the proper starting point
        # in the list.
        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1

        # The two pointers that will fix the final connections.
        tail, con = cur, prev

        # Iteratively reverse the nodes until n becomes 0.
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1

        # Adjust the final connections as explained in the algorithm
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head
```
* [![Medium] [Solution] 92. Reverse Linked List II](!%5BMedium%5D%20%5BSolution%5D%2092.%20Reverse%20Linked%20List%20II.md)

### Inorder Simulation
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def findSize(self, head):
        ptr = head
        c = 0
        while ptr:
            ptr = ptr.next
            c += 1
        return c
        
    def sortedListToBST(self, head: ListNode) -> TreeNode:        
        
        # Get the size of the linked list first
        size = self.findSize(head)

        # Recursively form a BST out of linked list from l --> r
        def convert(l, r):
            nonlocal head

            # Invalid case
            if l > r:
                return None

            mid = (l + r) // 2

            # First step of simulated inorder traversal. Recursively form
            # the left half
            left = convert(l, mid - 1)

            # Once left half is traversed, process the current node
            node = TreeNode(head.val)   
            node.left = left

            # Maintain the invariance mentioned in the algorithm
            head = head.next

            # Recurse on the right hand side and form BST out of them
            node.right = convert(mid + 1, r)
            return node
        return convert(0, size - 1)
```
* [Medium] [Solution] 109. Convert Sorted List to Binary Search Tree

### Hash Table pointer
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        copy_dict = {}
        cur = head
        while cur:
            copy_dict[cur] = Node(cur.val, None, None)
            cur = cur.next

        cur = head
        while cur:
            if cur.next:
                copy_dict[cur].next = copy_dict[cur.next]
            if cur.random:
                copy_dict[cur].random = copy_dict[cur.random]
            cur = cur.next

        return copy_dict[head]
```
* [Medium] 138. Copy List with Random Pointer

### Split Input List
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        ans = []
        length = 0

        cur = root
        while cur:
            length += 1
            cur = cur.next

        part_size, remainder = divmod(length, k)

        cur = root
        for i in range(k):
            dummy = ListNode(0)
            node = dummy
            for j in range(part_size + (i < remainder)):
                node.next = ListNode(cur.val)
                node = node.next              
                cur = cur.next

            ans.append(dummy.next)

        return ans
```
* [Medium] [Solution] 725. Split Linked List in Parts

### Grouping
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        Gset = set(G)
        cur = head
        ans = 0
        while cur:
            if (cur.val in Gset and
                    getattr(cur.next, 'val', None) not in Gset):
                ans += 1
            cur = cur.next

        return ans
```
* [Medium] [Solution] 817. Linked List Components

### Stack
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack = []
        cur = head
        while cur:
            while stack and cur.val > stack[-1].val:
                node = stack.pop()
                node.val = cur.val
            stack.append(cur)
            cur = cur.next

        for node in stack:
            node.val = 0

        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next

        return res
```
* [Medium] 1019. Next Greater Node In Linked List

### Prefix Sum
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        prefix_sum = 0
        seen = {prefix_sum: dummy}
        
        while head:
            prefix_sum += head.val

            # remove elements in zero sum
            if prefix_sum in seen:           
                k, v = seen.popitem()
                while k != prefix_sum:
                    k, v = seen.popitem()
                seen[k] = v
            else:
                # add non zero-sum elements
                seen[prefix_sum] = head
            
            head = head.next
        
        # rebuild the linkedlist
        ret = dummy
        for i, k in enumerate(seen):
            if i > 0:
                ret.next = seen[k]
                ret = ret.next
        
        ret.next = None
        
        return dummy.next
```
* [Medium] 1171. Remove Zero Sum Consecutive Nodes from Linked List

### Iterative, Recursive
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        node = head
        children = []  # stack
        prev = None
        while node:
            node.prev = prev
            if node.child:
                if node.next:
                    children.append(node.next)
                node.next = node.child
                node.child = None
                prev = node
                node = node.next
            elif node.next:
                prev = node
                node = node.next
            else:
                if children:
                    node.next = children.pop()
                    prev = node
                    node = node.next
                else:
                    prev = node    
                    node=node.next
        return head
    
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        p = head
        while p != None and p.child == None:
            p = p.next

        if p == None:
            return head
        down = self.flatten(p.child)
        right = self.flatten(p.next)
        p.next = down
        down.prev = p
        p.child = None
        while p.next != None:
            p = p.next

        p.next = right
        if right != None:
            right.prev = p

        return head
```
* [Medium] 430. Flatten a Multilevel Doubly Linked List

**Template 1:**
```python
dummy = listNode(-1)
dummy.next = head
while head:
    ...
    head = head.next
return dummy.next
```

## Heap <a name="heap"></a>
---
### Greedy add
```
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if len(res) < k:
                    heapq.heappush(res, -matrix[i][j]) 
                else:
                    heapq.heappushpop(res, -matrix[i][j])
        return -(res[0])
```
* [Medium] 378. Kth Smallest Element in a Sorted Matrix.md

### Greedy, backward sliding window
```python
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        pq = [] # max heap 
        for i in reversed(range(len(nums))): 
            while pq and pq[0][1] - i > k: heappop(pq)
            ans = nums[i] - pq[0][0] if pq else nums[i]
            heappush(pq, (-ans, i))
        return ans
```
[Medium] 1696. Jump Game VI.md

### Greedy Max Heap
```python
class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        heap = [(-i-j, i, j) for i,j in zip(aliceValues,bobValues)] #max heap
        AScore = 0
        BScore = 0
        heapq.heapify(heap)
        turn = "A"
        while heap:
            _, ascore, bscore = heapq.heappop(heap)
            if turn == "A":
                AScore += ascore
                turn = "B"
            else:
                BScore += bscore
                turn = "A"
        if AScore == BScore : return 0
        return 1 if AScore > BScore else  -1
```
* [Medium] 1686. Stone Game VI

### Greedy push to/pop from Heap with max profit
```python
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights) - 1):
            d = heights[i + 1] - heights[i]
            if d > 0:
                heapq.heappush(heap, d)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i
        return len(heights) - 1
```
* [Medium] 1642. Furthest Building You Can Reach

### Count
```python
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums)   
        return heapq.nlargest(k, count.keys(), key=count.get) 
```
* [Medium] [Solution] 347. Top K Frequent Elements

### Consecutive Subsequences
```python
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        d = collections.defaultdict(list)
        for e in nums:
            if d[e-1]: # there is sequence ending with e-1
                minLen = heapq.heappop(d[e-1]) # the shortest sequence
                heapq.heappush(d[e], minLen+1)
            else:
                heapq.heappush(d[e], 1) # create a new sequence
        for h in d.values():
            for hl in h:
                if hl < 3:
                    return False
                
        return True
```
* [Medium] [Solution] 659. Split Array into Consecutive Subsequences

### Frequency
```python
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
```
* [Medium] [Solution] 692. Top K Frequent Words

### Dijkstra's Algorithm
```python
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dist = [[float('inf')] * n for _ in range(m)]
        minHeap = []
        minHeap.append((0, 0, 0))  # distance, row, col
        DIR = [0, 1, 0, -1, 0]
        while minHeap:
            d, r, c = heappop(minHeap)
            if r == m - 1 and c == n - 1:
                return d  # Reach to bottom right
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                if 0 <= nr < m and 0 <= nc < n:
                    newDist = max(d, abs(heights[nr][nc] - heights[r][c]))
                    if dist[nr][nc] > newDist:
                        dist[nr][nc] = newDist
                        heappush(minHeap, (dist[nr][nc], nr, nc))
```
* [Medium] 1631. Path With Minimum Effort

### Dijkstra's Algorithm
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
* [Medium] [Solution] 743. Network Delay Time

### Dijkstra's Algorithm
```python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dic = collections.defaultdict(list)
        for s, d, p in flights:
            dic[s].append([d, p])
        q = [[0, src, 0]]
        while q:
            price, s, hop = heapq.heappop(q)
            if s == dst:
                return price
            if hop > K: continue
            for nd, np in dic[s]:
                heapq.heappush(q, [price + np, nd, hop + 1])
        return -1
```
* [Medium] 787. Cheapest Flights Within K Stops

### Minimum Spanning Tree
```python
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        N = len(points)
        g = collections.defaultdict(list)
        for i in range(N):
            for j in range(i+1, N):
                d = manhattan(points[i], points[j])
                g[i].append((d, j))
                g[j].append((d, i))
        cnt, ans, visited, heap = 1, 0, [0] * N, g[0]
        visited[0] = 1
        heapq.heapify(heap)
        while heap:
            d, j = heapq.heappop(heap)
            if not visited[j]:
                visited[j], cnt, ans = 1, cnt+1, ans+d
                for record in g[j]: heapq.heappush(heap, record)
            if cnt >= N: break        
        return ans
```
* [Medium] 1584. Min Cost to Connect All Points

### Greedy with Heap
```python
class Solution:
    def reorganizeString(self, S: str) -> str:
        pq = [(-S.count(x), x) for x in set(S)]
        heapq.heapify(pq)
        if any(-nc > (len(S) + 1) / 2 for nc, x in pq):
            return ""

        ans = []
        while len(pq) >= 2:
            nct1, ch1 = heapq.heappop(pq)
            nct2, ch2 = heapq.heappop(pq)
            ans.extend([ch1, ch2])
            if nct1 + 1: heapq.heappush(pq, (nct1 + 1, ch1))
            if nct2 + 1: heapq.heappush(pq, (nct2 + 1, ch2))

        return "".join(ans) + (pq[0][1] if pq else '')
```
* [Medium] [Solution] 767. Reorganize String

### nsmallest
```python
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return heapq.nsmallest(K, points, key= lambda x: x[0]**2 + x[1]**2)
```
* [Medium] [Solution] 973. K Closest Points to Origin

### Two Heaps, Min and Max Heap
```python
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lo = []  // max heap
        self.hi = []  // min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -self.lo[0])
        heapq.heappop(self.lo)
        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -self.hi[0])
            heapq.heappop(self.hi)

    def findMedian(self) -> float:
        return -self.lo[0] if len(self.lo) > len(self.hi) else (-self.lo[0] + self.hi[0]) * .5


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```
* [Hard] [Solution] 295. Find Median from Data Stream.md

### Dijkstra's Algorithm
```python
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # not sure whether anyone else find this one easier than the cheapest flight
        n = len(grid)
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]

        q = [(grid[0][0], 0, 0)]
        best = {}
        while q:
            elev, x0, y0 = heapq.heappop(q)
            best[(x0, y0)] = elev
            if (x0, y0) == (n-1, n-1): return elev
            for dx, dy in dirs:
                nx, ny = x0 + dx, y0 + dy
                if n > nx >= 0 and n > ny >= 0 and max(elev, grid[nx][ny]) < best.get((nx, ny), float('inf')):
                    heapq.heappush(q,(max(elev, grid[nx][ny]), nx, ny))
                    best[(nx, ny)] = max(elev, grid[nx][ny])
```
* [Hard] 778. Swim in Rising Water

### Sort by efficiency, and greedy over max speed with heap
```python
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        modulo = 10 ** 9 + 7

        # build tuples of (efficiency, speed)
        candidates = zip(efficiency, speed)
        # sort the candidates by their efficiencies
        candidates = sorted(candidates, key=lambda t:t[0], reverse=True)

        speed_heap = []
        speed_sum, perf = 0, 0
        for curr_efficiency, curr_speed in candidates:
            # maintain a heap for the fastest (k-1) speeds
            if len(speed_heap) > k-1:
                speed_sum -= heapq.heappop(speed_heap)
            heapq.heappush(speed_heap, curr_speed)

            # calcuslate the maximum performance with the current member as the least efficient one in the team
            speed_sum += curr_speed
            perf = max(perf, speed_sum * curr_efficiency)

        return perf % modulo
```
* [Hard] 1383. Maximum Performance of a Team

### think backward
```python
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        target = [-x for x in target]
        heapq.heapify(target)

        while -target[0] > 1:
            num = -heapq.heappop(target)
            rest_sum = total - num
            if num < rest_sum or not rest_sum or (not num % rest_sum and rest_sum != 1):
                return False
            num %= rest_sum
            total = num + rest_sum 
            heapq.heappush(target, -num)
        return True  
```
* [Hard] 1354. Construct Target Array With Multiple Sums

### Greedy with max heap
```python
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap, time = [], 0
        for t, end in sorted(courses, key=lambda x: x[1]):
            time += t
            heapq.heappush(heap, -t)
            if time > end:
                nt = heapq.heappop(heap)
                time += nt
        return len(heap)
```
* [Hard] [Solution] 630. Course Schedule III

### Unify and solve by one method
```python
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = list(set(-(x * 2 if x & 1 else x) for x in nums))
        heapify(heap)
        ma, mi = -heap[0], -max(heap)
        ans = ma - mi
        while heap[0] % 2 == 0:
            x = heappop(heap) // 2
            heappush(heap, x)
            ma, mi = -heap[0], min(mi, -x)
            ans = min(ans, ma - mi)
        return ans
```
* [Hard] 1675. Minimize Deviation in Array

### Sort and step-by-step count from smallest/highest
```python
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        from fractions import Fraction
        workers = sorted((Fraction(w, q), q, w)
                         for q, w in zip(quality, wage))

        ans = float('inf')
        pool = []
        sumq = 0
        for ratio, q, w in workers:
            heapq.heappush(pool, -q)
            sumq += q

            if len(pool) > K:
                sumq += heapq.heappop(pool)

            if len(pool) == K:
                ans = min(ans, ratio * sumq)

        return float(ans)
```
* [Hard] [Solution] 857. Minimum Cost to Hire K Workers

### Max Heap Frequency
```python
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        if a != 0:
            heappush(max_heap, (-a, 'a'))
        if b != 0:
            heappush(max_heap, (-b, 'b'))
        if c != 0:
            heappush(max_heap, (-c, 'c'))
        s = []
        while max_heap:
            first, char1 = heappop(max_heap) # char with most rest numbers
            if len(s) >= 2 and s[-1] == s[-2] == char1: # check whether this char is the same with previous two
                if not max_heap: # if there is no other choice, just return
                    return ''.join(s)
                second, char2 = heappop(max_heap) # char with second most rest numbers
                s.append(char2)
                second += 1 # count minus one, because the second here is negative, thus add 1
                if second != 0: # only if there is rest number count, add it back to heap
                    heappush(max_heap, (second, char2))
                heappush(max_heap, (first, char1)) # also need to put this part back to heap
                continue
                
            #  situation that this char can be directly added to answer
            s.append(char1)
            first += 1
            if first != 0:
                heappush(max_heap, (first, char1))
        return ''.join(s)
```
* [Medium] 1405. Longest Happy String

### Nearest Future Location Heap
```python
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        seen = set()
        closest = []
        locs = collections.defaultdict(collections.deque)
        for i, lake in enumerate(rains):
            locs[lake].append(i)
        ret = []
        for lake in rains:
            if lake in seen:
                return []
            if not lake:
                # get closest that's already seen
                if not closest:
                    # there's nothing filled that will be filled again later
                    ret.append(1) 
                    continue
                nxt = heapq.heappop(closest)
                ret.append(rains[nxt])
                seen.remove(rains[nxt])
            else:
                seen.add(lake)
                l = locs[lake]
                l.popleft()
                if l:
                    nxt = l[0]
                    heapq.heappush(closest, nxt)
                ret.append(-1)
        return ret
```
* [Medium] 1488. Avoid Flood in The City

### 3 Heap, busy -> available -> busy heap
```python
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        busy_jobs = []  # heap (job_end_time, node) to free up the nodes quickly
        after = [] # heap (nodes) free after current server
        before = list(range(k))  # heap (nodes) to use for loopback
        requests_handled = [0] * k

        for i, (arrvl, ld) in enumerate(zip(arrival, load)):
            server_id = i % k
            if server_id == 0:  # loopback
                after = before
                before = []

            while busy_jobs and busy_jobs[0][0] <= arrvl:
                freed_node = heapq.heappop(busy_jobs)[1]
                if freed_node < server_id: heapq.heappush(before, freed_node)
                else: heapq.heappush(after, freed_node)

            use_queue = after if after else before
            if not use_queue: continue  # request dropped
            using_node = heapq.heappop(use_queue)
            requests_handled[using_node] += 1
            heapq.heappush(busy_jobs, (arrvl + ld, using_node))

        maxreqs = max(requests_handled)
        return [i for i, handled in enumerate(requests_handled) if handled == maxreqs]
```
* [Hard] 1606. Find Servers That Handled Most Number of Requests

### Greedy with Max-Heap
```python
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pq = []  # A maxheap is simulated using negative values
        stations.append((target, float('inf')))

        ans = prev = 0
        tank = startFuel
        for location, capacity in stations:
            tank -= location - prev
            while pq and tank < 0:  # must refuel in past
                tank += -heapq.heappop(pq)
                ans += 1
            if tank < 0: return -1
            heapq.heappush(pq, -capacity)
            prev = location

        return ans
```
* [Hard] [Solution] 871. Minimum Number of Refueling Stops

### Points of Interest + Dijkstra
```python
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        R, C = len(grid), len(grid[0])

        # The points of interest
        location = {v: (r, c)
                    for r, row in enumerate(grid)
                    for c, v in enumerate(row)
                    if v not in '.#'}

        def neighbors(r, c):
            for cr, cc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= cr < R and 0 <= cc < C:
                    yield cr, cc

        # The distance from source to each point of interest
        def bfs_from(source):
            r, c = location[source]
            seen = [[False] * C for _ in range(R)]
            seen[r][c] = True
            queue = collections.deque([(r, c, 0)])
            dist = {}
            while queue:
                r, c, d = queue.popleft()
                if source != grid[r][c] != '.':
                    dist[grid[r][c]] = d
                    continue # Stop walking from here if we reach a point of interest
                for cr, cc in neighbors(r, c):
                    if grid[cr][cc] != '#' and not seen[cr][cc]:
                        seen[cr][cc] = True
                        queue.append((cr, cc, d+1))
            return dist        

        dists = {place: bfs_from(place) for place in location}
        target_state = 2 ** sum(p.islower() for p in location) - 1

        #Dijkstra
        pq = [(0, '@', 0)]
        final_dist = collections.defaultdict(lambda: float('inf'))
        final_dist['@', 0] = 0
        while pq:
            d, place, state = heapq.heappop(pq)
            if final_dist[place, state] < d: continue
            if state == target_state: return d
            for destination, d2 in dists[place].items():
                state2 = state
                if destination.islower(): #key
                    state2 |= (1 << (ord(destination) - ord('a')))
                elif destination.isupper(): #lock
                    if not(state & (1 << (ord(destination) - ord('A')))): #no key
                        continue

                if d + d2 < final_dist[destination, state2]:
                    final_dist[destination, state2] = d + d2
                    heapq.heappush(pq, (d+d2, destination, state2))

        return -1
```
* [Hard] [Solution] 864. Shortest Path to Get All Keys

### Scan X axis, and heapify Y axis
```python
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """ https://leetcode.com/problems/the-skyline-problem/
        General approach: scan the X positions where anything happened, maintaining a heap
        of active buildings and noting when the max height changes.
        """
        if not buildings:
            return []

        # left and right edges are where all the action happens, so collect these.
        # These will look like {x position: [height of each building starting or ending here]}
        building_left_edges = collections.defaultdict(list)
        building_right_edges = collections.defaultdict(list)
        for building in buildings:
            left_index, right_index, height = building
            building_left_edges[left_index].append(height)
            building_right_edges[right_index].append(height)

        x_positions_of_interest = sorted(
            set(building_left_edges.keys()).union(building_right_edges.keys())
        )

        # Heap will contain heights of all buildings present at the current x value.
        # Heights will be stored as negative values since heapq only supports min heaps,
        # and at any point we want the maximum height.
        active_buildings_heap = []
        last_skyline_height = 0
        skyline = []
        for x in x_positions_of_interest:
            for height in building_left_edges[x]:
                heapq.heappush(active_buildings_heap, -height)
            if building_right_edges[x]:
                for height in building_right_edges[x]:
                    active_buildings_heap.remove(-height)
                heapq.heapify(active_buildings_heap)

            skyline_here = -active_buildings_heap[0] if active_buildings_heap else 0

            if skyline_here != last_skyline_height:
                last_skyline_height = skyline_here
                skyline.append((x, skyline_here))

        return skyline
```
* [Hard] 218. The Skyline Problem

### Minimum Time
```python
class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        pq = []
        for block in blocks:
            heapq.heappush(pq, block)
        while len(pq) > 1:
            heapq.heappop(pq)
            heapq.heappush(pq, heapq.heappop(pq)+split)

        return heapq.heappop(pq)
```
* [Hard] 1199. Minimum Time to Build Blocks

### A*
```python
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        R, C = len(forest), len(forest[0])
        trees = sorted((v, r, c) for r, row in enumerate(forest)
                       for c, v in enumerate(row) if v > 1)
        sr = sc = ans = 0

        def astar(sr, sc, tr, tc):
            heap = [(0, 0, sr, sc)]
            cost = {(sr, sc): 0}
            while heap:
                f, g, r, c = heapq.heappop(heap)
                if r == tr and c == tc: return g
                for nr, nc in ((r-1,c), (r+1,c), (r,c-1), (r,c+1)):
                    if 0 <= nr < R and 0 <= nc < C and forest[nr][nc]:
                        ncost = g + 1 + abs(nr - tr) + abs(nc - tc)
                        if ncost < cost.get((nr, nc), 9999):
                            cost[nr, nc] = ncost
                            heapq.heappush(heap, (ncost, g+1, nr, nc))
            return -1

        for _, tr, tc in trees:
            d = astar(sr, sc, tr, tc)
            if d < 0: return -1
            ans += d
            sr, sc = tr, tc
        return ans
```
* [Hard] [Solution] 675. Cut Off Trees for Golf Event

**Template 1:**
```python
ans = ...
hq = [(...)]
while hq:
    ... = heapq.heappop(hq)
    ...
    ans = ...
    heapq.heappush(hq, ...)
    
return ans
```

**Template 2:**
```python
sortedXXX = sorted(...)
hq = []
for ... in sortedXXX:
    while ...:
        heapq.heappush(hq, sortedXXX...)
    if ...:
        ans += heapq.heappop(hq)

return ans
```

## Union Find <a name="uf"></a>
---
### Path Compression
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
* [Medium] [Solution] 684. Redundant Connection

### Region
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
Solution 1: (DFS, Graph)
```
* [Medium] [Solution] 959. Regions Cut By Slashes

### Eqaulity
```python
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if x not in G:
                G[x] = x
                return x
            while G[x]!=x:
                x = G[x]
            return x
        
        def union(x,y):
            xp,yp = find(x), find(y)
            if xp!=yp:
                G[yp] = xp
        
        G = {}
        for e in equations:
            if e[1:3]=="==":
                union(e[0],e[3])
        for e in equations:
            if e[1:3]=="!=":
                if find(e[0])==find(e[3]):
                    return False
        return True
```
* [Medium] [Solution] 990. Satisfiability of Equality Equations

### Union-Find equal elements
```python
class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        rank = [0] * (m + n)
        d = collections.defaultdict(list)
        for i in range(n):
            for j in range(m):
                d[matrix[i][j]].append([i, j])

        def find(i):
            if p[i] != i:
                p[i] = find(p[i])
            return p[i]

        for a in sorted(d):
            p = list(range(m + n))
            rank2 = rank[:]
            for i, j in d[a]:
                i, j = find(i), find(j + n)
                p[i] = j
                rank2[j] = max(rank2[i], rank2[j])
            for i, j in d[a]:
                rank[i] = rank[j + n] = matrix[i][j] = rank2[find(i)] + 1
        return matrix
```
* [Hard] 1632. Rank Transform of a Matrix.md

### Reverse Time and Union-Find
```python
class DSU:
    def __init__(self, R, C):
        #R * C is the source, and isn't a grid square
        self.par = [_ for _ in range(R*C + 1)]
        self.rnk = [0] * (R*C + 1)
        self.sz = [1] * (R*C + 1)

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr: return
        if self.rnk[xr] < self.rnk[yr]:
            xr, yr = yr, xr
        if self.rnk[xr] == self.rnk[yr]:
            self.rnk[xr] += 1

        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]

    def size(self, x):
        return self.sz[self.find(x)]

    def top(self):
        # Size of component at ephemeral "source" node at index R*C,
        # minus 1 to not count the source itself in the size
        return self.size(len(self.sz) - 1) - 1

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        R, C = len(grid), len(grid[0])
        def index(r, c):
            return r * C + c

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        A = [row[:] for row in grid]
        for i, j in hits:
            A[i][j] = 0

        dsu = DSU(R, C)
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                if val:
                    i = index(r, c)
                    if r == 0:
                        dsu.union(i, R*C)
                    if r and A[r-1][c]:
                        dsu.union(i, index(r-1, c))
                    if c and A[r][c-1]:
                        dsu.union(i, index(r, c-1))

        ans = []
        for r, c in reversed(hits):
            pre_roof = dsu.top()
            if grid[r][c] == 0:
                ans.append(0)
            else:
                i = index(r, c)
                for nr, nc in neighbors(r, c):
                    if A[nr][nc]:
                        dsu.union(i, index(nr, nc))
                if r == 0:
                    dsu.union(i, R*C)
                A[r][c] = 1
                ans.append(max(0, dsu.top() - pre_roof - 1))
        return ans[::-1]
```
* [Hard] [Solution] 803. Bricks Falling When Hit

### Coloring
```python
class DSU:
    def __init__(self, N):
        self.p = [_ for _ in range(N)]
        self.sz = [1] * N

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr
        self.sz[yr] += self.sz[xr]

class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        dsu = DSU(len(graph))

        for j, row in enumerate(graph):
            for i in range(j):
                if row[i]:
                    dsu.union(i, j)

        count = collections.Counter(dsu.find(u) for u in initial)
        ans = (-1, min(initial))
        for node in initial:
            root = dsu.find(node)
            if count[root] == 1:  # unique color
                if dsu.sz[root] > ans[0]:
                    ans = dsu.sz[root], node
                elif dsu.sz[root] == ans[0] and node < ans[1]:
                    ans = dsu.sz[root], node

        return ans[1]
```

* [Hard] [Solution] 924. Minimize Malware Spread

### Count common factor
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
    def largestComponentSize(self, A: List[int]) -> int:
        B = []
        for x in A:
            facs = []
            d = 2
            while d * d <= x:
                if x % d == 0:
                    while x % d == 0:
                        x /= d
                    facs.append(d)
                d += 1

            if x > 1 or not facs:
                facs.append(x)
            B.append(facs)

        primes = list({p for facs in B for p in facs})
        prime_to_index = {p: i for i, p in enumerate(primes)}

        dsu = DSU(len(primes))
        for facs in B:
            for x in facs:
                dsu.union(prime_to_index[facs[0]], prime_to_index[x])

        count = collections.Counter(dsu.find(prime_to_index[facs[0]]) for facs in B)
        return max(count.values())
```
* [Hard] [Solution] 952. Largest Component Size by Common Factor

### Remove Max Number of Edges to Keep Graph Fully Traversable
```python
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        # Union find
        def find(i):
            if i != root[i]:
                root[i] = find(root[i])
            return root[i]

        def uni(x, y):
            x, y = find(x), find(y)
            if x == y: return 0
            root[x] = y
            return 1

        res = e1 = e2 = 0

        # Alice and Bob
        root = list(range(n + 1))
        for t, i, j in edges:
            if t == 3:
                if uni(i, j):
                    e1 += 1
                    e2 += 1
                else:
                    res += 1
        root0 = root[:]

        # only Alice
        for t, i, j in edges:
            if t == 1:
                if uni(i, j):
                    e1 += 1
                else:
                    res += 1

        # only Bob
        root = root0
        for t, i, j in edges:
            if t == 2:
                if uni(i, j):
                    e2 += 1
                else:
                    res += 1

        return res if e1 == e2 == n - 1 else -1
```
* [Hard] 1579. Remove Max Number of Edges to Keep Graph Fully Traversable

**Template 1:**
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
class Solution:
    def is_cycle(self, ...):
        dsu = DSN(N)
        for ...:
            if is dsu.union(..., ...):
                return True
```

**Template 2:**
```python
class DSU:
    def __init__(self, N):
        self.p = [_ for _ in range(N)]
        self.sz = [1] * N

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr
        self.sz[yr] += self.sz[xr]
        
    def size(self, x):
        return self.sz[self.find(x)]
        
class Solution:
    def ...(self, XXX):
        N = ...
        dsu = DSN(N)
        for ... in XXX:
            dus.union(..., ...)
        max_component_size = max(dsu.sz)
        for ... in XXX:
            component_size[...] = dsu.size(...)
        n_component = len({dsu.find(...) for ... in XXX})
        # n_component = sum(dsu.find(x) == x for x in range(N))
```

## Sliding Window <a name="sw"></a>
---
### maximum subarray
```python
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target, size, win_sum, lo = sum(nums) - x, -1, 0, -1
        for hi, num in enumerate(nums):
            win_sum += num
            while lo + 1< len(nums) and win_sum > target:
                lo += 1
                win_sum -= nums[lo]
            if win_sum == target:
                size = max(size, hi - lo)
        return -1 if size < 0 else len(nums) - size
```
* [Medium] 1658. Minimum Operations to Reduce X to Zero

### Sliding window with cumulative sum
```python
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = float('-inf')
        cur = 0
        # sliding window; current value = [i, j]
        seen = set()
        i = 0
        for j in range(len(nums)):
            while nums[j] in seen:
                cur -= nums[i]
                seen.remove(nums[i])
                i += 1
            seen.add(nums[j])
            cur += nums[j]
            ans = max(ans, cur)
            
        return ans
```
* [Medium] 1695. Maximum Erasure Value

### Mono queue
```python
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        best = [float('-inf')] * n
        best[0] = nums[0]
        dec = collections.deque([0])
        
        for i in range(1, n):
            # lazy deletion
            while dec and dec[0] < i - k:
                dec.popleft()
            # calculate the best score up until i
            best[i] = best[dec[0]] + nums[i]
            # maintain the mono dec deque
            while dec and best[dec[-1]] <= best[i]:
                dec.pop()
            dec.append(i)
            
        return best[-1]
```
* [Medium] 1696. Jump Game VI

### Sliding over candidate
```python
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        len_low = len(str(low))
        len_high = len(str(high))
        digits = '123456789'
        ans = []
        for win_len in range(len_low, len_high + 1):
            for i in range(10-win_len):
                if low <= int(digits[i:i + win_len]) <= high:
                    ans.append(int(digits[i:i + win_len]))
        return ans
```
* [Medium] 1291. Sequential Digits

### Group All 1's Together
```python
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        window = data.count(1)
        ans = c = data[:window].count(0)
        for i in range(window, len(data)):
            c += not data[i]
            c -= not data[i-window]
            ans = min(ans, c)
        return ans
```
* [Lock] [Medium] 1151. Minimum Swaps to Group All 1's Together

### Greedy slide left and right index
```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = [None] * 128

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]

            index = chars[ord(r)]
            if index != None and index >= left and index < right:
                left = index + 1

            res = max(res, right - left + 1)

            chars[ord(r)] = right
            right += 1
        return res
```
* [Medium] [Solution] 3. Longest Substring Without Repeating Characters

### Counter
```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pattern_counter = collections.Counter(p)
        running_counter = collections.Counter()
        len_p = len(p)
        result = []

        for i in range(len(s)):
            
            # If index  >= length of the pattern.
            # then decrement the count of the (i - len_p)th character to remove it from 
            # the current (sliding) window.
            if i >= len_p:
                if running_counter[s[i - len_p]] == 1:
                    del running_counter[s[i  - len_p]]
                else:
                    running_counter[s[i - len_p]] -= 1
            
            # Default: just increment the count of the current character.
            running_counter[s[i]] += 1
            
            # At any time, if running_counter == pattern_counter then append the result.
            if running_counter == pattern_counter:
                result.append(i - len_p + 1)

        return result
```
* [Medium] 438. Find All Anagrams in a String

### Counter
```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        M, N = len(s1), len(s2)
        t = collections.Counter(s1)
        w = collections.Counter(s2[:M - 1])
        for i in range(M-1, N):
            w[s2[i]] += 1
            if w == t: 
                return True
            w[s2[i - M + 1]] -= 1
            if w[s2[i - M + 1]] == 0 : 
                del w[s2[i - M + 1]]

        return False
```
* [Medium] 567. Permutation in String

### Greedy Left index pointer
```python
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        N = len(A)
        ans = 1
        anchor = 0

        for i in range(1, N):
            c = A[i-1] - A[i]
            if not c:
                anchor = i
            elif i == N-1 or not c * (A[i] - A[i+1]) < 0:
                ans = max(ans, i - anchor + 1)
                anchor = i
        return ans
```
* [Medium] [Solution] 978. Longest Turbulent Subarray

### Greedy append
```python
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        zeroes = 0
        left, right = 0, 0
        ans = 0
        while right < len(A):
            if A[right] == 0:
                zeroes += 1
            while zeroes > K:
                if A[left] == 0:
                    zeroes -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans
```
* [Medium] 1004. Max Consecutive Ones III

### Sliding over left, right end
```python
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints)
        s = sum(cardPoints)
        min_ = cur = sum(cardPoints[:N-k])
        i = 0
        for j in range(N-k, N):
            cur += cardPoints[j]
            cur -= cardPoints[i]
            min_ = min(min_, cur)
            i += 1
        return s - min_
```
* [Medium] 1423. Maximum Points You Can Obtain from Cards

### slide right and try best to shrink the window from left
```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = collections.Counter(t)

        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)

        # left and right pointer
        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):

            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                l += 1    

            # Keep expanding the window once we are done contracting.
            r += 1    
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
```
* [Hard] [Solution] 76. Minimum Window Substring

### 2 Sliding window
```python
Runtime: 780 ms
Memory Usage: 15.9 MB
class Window:
    def __init__(self):
        self.count = collections.Counter()
        self.nonzero = 0

    def add(self, x):
        self.count[x] += 1
        if self.count[x] == 1:
            self.nonzero += 1

    def remove(self, x):
        self.count[x] -= 1
        if self.count[x] == 0:
            self.nonzero -= 1

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        window1 = Window()
        window2 = Window()
        ans = left1 = left2 = 0

        for right, x in enumerate(A):
            window1.add(x)
            window2.add(x)

            while window1.nonzero > K:
                window1.remove(A[left1])
                left1 += 1

            while window2.nonzero >= K:
                window2.remove(A[left2])
                left2 += 1

            ans += left2 - left1

        return ans
```
* [Hard] [Solution] 992. Subarrays with K Different Integers

### Greedy + Events
```python
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        N = len(A)
        hint = [0] * N
        ans = flip = 0

        # When we flip a subarray like A[i], A[i+1], ..., A[i+K-1]
        # we can instead flip our current writing state, and put a hint at
        # position i+K to flip back our writing state.
        for i, x in enumerate(A):
            flip ^= hint[i]
            if x ^ flip == 0:  # If we must flip the subarray starting here...
                ans += 1  # We're flipping the subarray from A[i] to A[i+K-1]
                if i+K > N: return -1  # If we can't flip the entire subarray, its impossible
                flip ^= 1  
                if i+K < N: hint[i + K] ^= 1

        return ans
```
* [Hard] [Solution] 995. Minimum Number of K Consecutive Bit Flips

### Horizontal 1D Prefix Sum
```python
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        r, c = len(matrix), len(matrix[0])

        # compute 2D prefix sum
        ps = [[0] * (c + 1) for _ in range(r + 1)]
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                ps[i][j] = ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1] + matrix[i - 1][j - 1]

        count = 0
        # reduce 2D problem to 1D one
        # by fixing two rows r1 and r2 and 
        # computing 1D prefix sum for all matrices using [r1..r2] rows
        for r1 in range(1, r + 1):
            for r2 in range(r1, r + 1):
                h = defaultdict(int)
                h[0] = 1

                for col in range(1, c + 1):
                    # current 1D prefix sum  
                    curr_sum = ps[r2][col] - ps[r1 - 1][col]

                    # add subarrays which sum up to (curr_sum - target)
                    count += h[curr_sum - target]

                    # save current prefix sum
                    h[curr_sum] += 1

        return count
```
* [Hard] 1074. Number of Submatrices That Sum to Target

### inverse sliding window
```python
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = i = 0
        count = {c: 0 for c in 'abc'}
        for j in range(len(s)):
            count[s[j]] += 1
            while all(count.values()):
                count[s[i]] -= 1
                i += 1
            res += i
        return res
```
* [Medium] 1358. Number of Substrings Containing All Three Characters

### Min Max Queue
```python
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_deque, max_deque = deque(), deque()
        l = r = 0
        ans = 0
        while r < len(nums):
            while min_deque and nums[r] <= nums[min_deque[-1]]:
                min_deque.pop()
            while max_deque and nums[r] >= nums[max_deque[-1]]:
                max_deque.pop()
            min_deque.append(r)
            max_deque.append(r)
            
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                l += 1
                if l > min_deque[0]:
                    min_deque.popleft()
                if l > max_deque[0]:
                    max_deque.popleft()
            
            ans = max(ans, r - l + 1)
            r += 1
                
        return ans
```
* [Medium] 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

### Longest Subarray of 1's
```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = sum = lo = 0
        for hi, num in enumerate(nums):
            sum += num
            while lo < hi and sum < hi - lo:
                sum -= nums[lo]
                lo += 1
            ans = max(ans, hi - lo)
        return ans 
```
* [Medium] 1493. Longest Subarray of 1's After Deleting One Element

**Template 1:**
```python
i = 0
for j in range(N):
    if OOO:
        XXX += 1
    while XXX > K:
        i += 1
    max = j - i + 1
```

## Divide and Conquer <a name="dc"></a>
---
### Merge Sort, Postorder
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) >1: 
            mid = len(nums)//2 #Finding the mid of the array 
            L = nums[:mid] # Dividing the array elements  
            R = nums[mid:] # into 2 halves 

            self.sortArray(L) # Sorting the first half 
            self.sortArray(R) # Sorting the second half 

            i = j = k = 0

            # Copy data to temp arrays L[] and R[] 
            while i < len(L) and j < len(R): 
                if L[i] < R[j]: 
                    nums[k] = L[i] 
                    i+=1
                else: 
                    nums[k] = R[j] 
                    j+=1
                k+=1

            # Checking if any element was left 
            while i < len(L): 
                nums[k] = L[i] 
                i+=1
                k+=1

            while j < len(R): 
                nums[k] = R[j] 
                j+=1
                k+=1

        return nums
```
* [Medium] 912. Sort an Array

### Quick Sort, Preorder
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def partition(arr,low,high): 
            i = ( low-1 )         # index of smaller element 
            pivot = arr[high]     # pivot 
            for j in range(low , high): 
                if   arr[j] <= pivot:
                    i = i+1 
                    arr[i],arr[j] = arr[j],arr[i] 
            arr[i+1],arr[high] = arr[high],arr[i+1] 
            return ( i+1 ) 
        
        def quickSort(arr, low, high): 
            if low < high:
                pi = partition(arr,low,high) 
                quickSort(arr, low, pi-1) 
                quickSort(arr, pi+1, high)
            return arr
            
        return quickSort(nums, 0, len(nums)-1)
```
* [Medium] 912. Sort an Array

### Iterate over response
```python
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit(): return [int(input)]
        rst, tmp = [], 0
        for i in range(len(input)):
            if input[i] in '+-*':
                a, b = input[:i], input[i+1:]
                l, r = self.diffWaysToCompute(a), self.diffWaysToCompute(b)
                for p in l: 
                    for q in r:
                        if input[i] == '+': tmp = p + q
                        elif input[i] == '-': tmp = p - q
                        else: tmp = p * q
                        rst.append(tmp)
        return rst
```
* [Medium] 241. Different Ways to Add Parentheses

### DP - Top-down
```python
import functools
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums_ext = [1] + [num for num in nums if num != 0] + [1]
        N = len(nums_ext) - 2
        
        @functools.lru_cache(None)
        def dfs(lower, upper):
            max_coins = 0
            for i in range(lower, upper+1):
                coins = nums_ext[lower-1] * nums_ext[i] * nums_ext[upper+1]
                coins += dfs(lower, i-1)
                coins += dfs(i+1, upper)
                if coins > max_coins:
                    max_coins = coins
            return max_coins

        return dfs(1, N)
    
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [num for num in nums if num > 0] + [1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]

        for length in range(1, n-1):
            for left in range(0, n-1-length):
                right = left + length + 1
                for i in range(left+1, right):
                    dp[left][right] = max(dp[left][right], 
                                          nums[left]*nums[i]*nums[right] +
                                          dp[left][i] + dp[i][right])

        return dp[0][n-1]
```
* [Hard] 312. Burst Balloons

### Backtracking
```python
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        N = len(num)
        answers = []
        def recurse(index, prev_operand, current_operand, value, string):

            # Done processing all the digits in num
            if index == N:

                # If the final value == target expected AND
                # no operand is left unprocessed
                if value == target and current_operand == 0:
                    answers.append("".join(string[1:]))
                return

            # Extending the current operand by one digit
            current_operand = current_operand*10 + int(num[index])
            str_op = str(current_operand)

            # To avoid cases where we have 1 + 05 or 1 * 05 since 05 won't be a
            # valid operand. Hence this check
            if current_operand > 0:

                # NO OP recursion
                recurse(index + 1, prev_operand, current_operand, value, string)

            # ADDITION
            string.append('+'); string.append(str_op)
            recurse(index + 1, current_operand, 0, value + current_operand, string)
            string.pop();string.pop()

            # Can subtract or multiply only if there are some previous operands
            if string:

                # SUBTRACTION
                string.append('-'); string.append(str_op)
                recurse(index + 1, -current_operand, 0, value - current_operand, string)
                string.pop();string.pop()

                # MULTIPLICATION
                string.append('*'); string.append(str_op)
                recurse(index + 1, current_operand * prev_operand, 0, value - prev_operand + (current_operand * prev_operand), string)
                string.pop();string.pop()
        recurse(0, 0, 0, 0, [])    
        return answers
```
* [Hard] [Solution] 282. Expression Add Operators

### Binay Search Tree
```python
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if preorder:
            val = preorder[0]
            root = TreeNode(val)
            i = 1
            while i < len(preorder) and preorder[i] < val:
                i += 1
            root.left = self.bstFromPreorder(preorder[1:i])
            root.right = self.bstFromPreorder(preorder[i:])
            return root
```
* [Medium] 1008. Construct Binary Search Tree from Preorder Traversal

### Modified merge sort
```python
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(start, mid, end):
            n1 = (mid - start + 1)
            n2 = (end - mid)
            L = nums[start:start + n1]
            R = nums[mid + 1:mid + 1 +n2]
            i, j = 0, 0
            for k in range(start, end+1):
                if j >= n2 or (i < n1 and L[i] <= R[j]):
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1

        def mergesort_and_count(start, end):
            if start < end:
                mid = (start + end) // 2;
                count = mergesort_and_count(start, mid) + mergesort_and_count(mid + 1, end)
                j = mid + 1;
                for i in range(start, mid+1):
                    while j <= end and nums[i] > nums[j] * 2:
                        j += 1
                    count += j - (mid + 1)
                merge(start, mid, end)
                return count
            else:
                return 0

        return mergesort_and_count(0, len(nums) - 1)
```
* [Hard] [Solution] 493. Reverse Pairs

### Prefix Sum with merge sort
```python
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        N = len(nums)
        cumSum = [0]
        for i in range(N):
            cumSum.append(cumSum[-1]+nums[i])
        ans = 0
        # inclusive
        def mergesort(l, r):
            if l == r:
                return 0
            mid = (l+r) // 2
            cnt = mergesort(l, mid) + mergesort(mid+1, r)

            i = j = mid+1
            # O(n)
            for left in cumSum[l:mid+1]:
                while i <= r and cumSum[i] - left < lower:
                    i += 1
                while j <= r and cumSum[j] - left <= upper:
                    j += 1
                cnt += j-i

            cumSum[l:r+1] = sorted(cumSum[l:r+1])
            return cnt

        return mergesort(0, N)
```
* [Hard] 327. Count of Range Sum

## Trie <a name="trie"></a>
---
### Trie + Depth-First Search
```python
import functools
class Solution:
    def longestWord(self, words: List[str]) -> str:
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for i, word in enumerate(words):
            functools.reduce(dict.__getitem__, word, trie)[END] = i

        stack = list(trie.values())
        ans = ""
        while stack:
            cur = stack.pop()
            if END in cur:
                word = words[cur[END]]
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                stack.extend([cur[letter] for letter in cur if letter != END])

        return ans
```
* [Easy] [Solution] 720. Longest Word in Dictionary

### Implementation
```python
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        t = self.trie
        for c in word:
            # if c not in t:
            #     t[c] = {}
            # t = t[c]
            t = t.setdefault(c, {})
        t['#'] = word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        t = self.trie
        for c in word:
            if c not in t:
                return False
            t = t[c]
        return '#' in t

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        t = self.trie
        for c in prefix:
            if c not in t:
                return False
            t = t[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```
* [Medium] [Solution] 208. Implement Trie (Prefix Tree)

### Add and Search Word
```python
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie

        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]
        node['@'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def search_in_node(word, node) -> bool:
            for i, ch in enumerate(word):
                if not ch in node:
                    # if the current character is '.'
                    # check all possible nodes at this level
                    if ch == '.':
                        for x in node:
                            if x != '@' and search_in_node(word[i + 1:], node[x]):
                                return True
                    # if no nodes lead to answer
                    # or the current character != '.'
                    return False
                # if the character is found
                # go down to the next level in trie
                else:
                    node = node[ch]
            return '@' in node

        return search_in_node(word, self.trie)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```
* [Medium] [Solution] 211. Add and Search Word - Data structure design

### Node
```python
class TrieNode(object):
    __slots__ = 'children', 'score'
    def __init__(self):
        self.children = {}
        self.score = 0

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        cur = self.root
        cur.score += delta
        for char in key:
            cur = cur.children.setdefault(char, TrieNode())
            cur.score += delta


    def sum(self, prefix: str) -> int:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return cur.score


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
```
* [Medium] [Solution] 677. Map Sum Pairs

### python typical
```python
import functools
class Solution:
    def replaceWords(self, roots: List[str], sentence: str) -> str:
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for root in roots:
            functools.reduce(dict.__getitem__, root, trie)[END] = root

        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur or END in cur: break
                cur = cur[letter]
            return cur.get(END, word)

        return " ".join(map(replace, sentence.split()))
```
* [Medium] [Solution] 648. Replace Words

### Bit
```python
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        # need to know the largest binary representation
        # bin prepends '0b', ignore
        L = len(bin(max(nums))) - 2

        # preprocess step - left-pad zeros to ensure each number has L bits
        # (x >> i) & 1 produces the bit at position i for number x
        # x's value is moved right by i bits, we & 1 to produce 0 or 1
        # e.g., if L = 5, then 3 = [0, 0, 0, 1, 1], so the steps to get there are:
        # (3 >> 4) & 1 = 0
        # (3 >> 3) & 1 = 0
        # (3 >> 2) & 1 = 0
        # (3 >> 1) & 1 = 1
        # (3 >> 0) & 1 = 1
        nums_bits = [[(x >> i) & 1 for i in reversed(range(L))] for x in nums]
        root = {}
        # build the trie
        for num, bits in zip(nums, nums_bits):
            node = root
            for bit in bits:
                node = node.setdefault(bit, {})
            node["#"] = num

        max_xor = 0
        for num, bits in zip(nums, nums_bits):
            node = root
            # we want to find the node that will produce the largest XOR with num
            for bit in bits:
                # our goal is to find the opposite bit, e.g. bit = 0, we want 1
                # this is our goal because we want as many 1's as possible
                toggled_bit = 1 - bit
                if toggled_bit in node:
                    node = node[toggled_bit]
                else:
                    node = node[bit]
            # we're at a leaf node, now we can do the XOR computation
            max_xor = max(max_xor, node["#"] ^ num)


        return max_xor
```
* [Medium] 421. Maximum XOR of Two Numbers in an Array

### Trie of Suffix Wrapped Words
```python
Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()

        for weight, word in enumerate(words):
            word += '#'
            for i in range(len(word)):
                cur = self.trie
                cur[WEIGHT] = weight
                for j in range(i, 2 * len(word) - 1):
                    cur = cur[word[j % len(word)]]
                    cur[WEIGHT] = weight

    def f(self, prefix: str, suffix: str) -> int:
        cur = self.trie
        for letter in suffix + '#' + prefix:
            if letter not in cur:
                return -1
            cur = cur[letter]
        return cur[WEIGHT]


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
```
* [Hard] [Solution] 745. Prefix and Suffix Search

### Stream of Characters
```python
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.stream = deque([])

        for word in set(words):
            node = self.trie       
            for ch in word[::-1]:
                if not ch in node:
                    node[ch] = {}
                node = node[ch]
            node['#'] = word

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)

        node = self.trie
        for ch in self.stream:
            if '#' in node:
                return True
            if not ch in node:
                return False
            node = node[ch]
        return '#' in node


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
```
* [Hard] 1032. Stream of Characters


### DFS aloong trie
```python
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R, C = len(board), len(board[0])
        ans = []

        def neighbours(r, c):
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        def dfs(r, c, node, path):
            letter = board[r][c]
            board[r][c] = ''
            node = node[letter]
            if '#' in node:
                ans.append(path)
                del node['#']
            for nr, nc in neighbours(r, c):
                if board[nr][nc] != '' and board[nr][nc] in node:
                    dfs(nr, nc, node, path + board[nr][nc])
            board[r][c] = letter

        trie = {}
        for word in words:
            t = trie
            for c in word + '#':
                t = t.setdefault(c, {})
        for r in range(R):
            for c in range(C):
                if board[r][c] in trie:
                    dfs(r, c, trie, board[r][c])

        return ans
```
* [Hard] 212. Word Search II

### Trie of Suffix Wrapped Words
```python
Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()

        for weight, word in enumerate(words):
            word += '#'
            for i in range(len(word)):
                cur = self.trie
                cur[WEIGHT] = weight
                for j in range(i, 2 * len(word) - 1):
                    cur = cur[word[j % len(word)]]
                    cur[WEIGHT] = weight
            
    def f(self, prefix: str, suffix: str) -> int:
        cur = self.trie
        for letter in suffix + '#' + prefix:
            if letter not in cur:
                return -1
            cur = cur[letter]
        return cur[WEIGHT]


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
```
* [Hard] [Solution] 745. Prefix and Suffix Search

**Template 1:**
```python
Trie = lambda: collections.defaultdict(Trie)
trie = Trie()
END = True

for i, XXX in enumerate(XXXs):
    functools.reduce(dict.__getitem__, XXX, trie)[END] = i

ans = ...
for XXX in XXXs:
    cur = trie
    for OOO in XXX:
        if OOO not in cur or END in cur:
            return False
        cur = cur[OOO]
    ... = cur.get(END, ...)
    ans ...
return ans
```

**Template 2:**
```python
trie = {}
for XXX in XXXs:
    t = trie
    for OOO in XXX + '#':
        t = t.setdefault(c, {})
```

## Recursion <a name="recursion"></a>
---
### Tree
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0

        def arrow_length(node):
            if not node: return 0
            left_length = arrow_length(node.left)
            right_length = arrow_length(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans
```
* [Easy] [Solution] 687. Longest Univalue Path

### Search by Constructing Subset Sums
```python
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, rem = divmod(sum(nums), k)
        if rem: return False

        def search(groups):
            if not nums: return True
            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if search(groups): return True
                    groups[i] -= v
                if not group: break
            nums.append(v)
            return False

        nums.sort()
        if nums[-1] > target: return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        return search([0] * k)
```
* [Medium] [Solution] 698. Partition to K Equal Sum Subsets

### DP Top-down, Tree
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    memo = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N not in Solution.memo:
            ans = []
            for x in range(N):
                y = N - 1 - x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        bns = TreeNode(0)
                        bns.left = left
                        bns.right = right
                        ans.append(bns)
            Solution.memo[N] = ans

        return Solution.memo[N]
```
* [Medium] [Solution] 894. All Possible Full Binary Trees

## Segment Tree <a name="st"></a>
---
### Range Sum, array to tree simulation
```python
class NumArray:

    def __init__(self, nums: List[int]):
        self.N = len(nums)
        if self.N > 0:
            self.tree = [0] * 2*self.N
            self.buildTree(nums)
    
    def buildTree(self, nums):
        j = 0
        for i in range(self.N, 2*self.N):
            self.tree[i] = nums[j]
            j += 1
        for i in range(self.N-1, 0, -1):
            self.tree[i] = self.tree[i*2] + self.tree[i*2 + 1]

    def update(self, index: int, val: int) -> None:
        pos = index + self.N
        self.tree[pos] = val
        while pos > 0:
            left = pos
            right = pos
            if pos % 2 == 0:
                right = pos + 1
            else:
                left = pos - 1
            # parent is updated after child is updated
            self.tree[pos // 2] = self.tree[left] + self.tree[right]
            pos //= 2

    def sumRange(self, left: int, right: int) -> int:
        # get leaf with value 'i'
        left += self.N;
        # get leaf with value 'j'
        right += self.N;
        rst = 0
        while left <= right:
            if (left % 2) == 1:
                rst += self.tree[left]
                left += 1
            if (right % 2) == 0:
                rst += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
            
        return rst


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
```
* [Medium] [Solution] 307. Range Sum Query - Mutable

### Maintain Sorted Disjoint Intervals
```python
class RangeModule:

    def __init__(self):
        self.ranges = []

    def _bounds(self, left, right):
        i, j = 0, len(self.ranges) - 1
        for d in (100, 10, 1):  # The total number of calls to addRange in a single test case is at most 1000
            while i + d - 1 < len(self.ranges) and self.ranges[i+d-1][1] < left:
                i += d
            while j >= d - 1 and self.ranges[j-d+1][0] > right:
                j -= d
        return i, j

    def addRange(self, left: int, right: int) -> None:
        i, j = self._bounds(left, right)
        if i <= j:
            left = min(left, self.ranges[i][0])
            right = max(right, self.ranges[j][1])
        self.ranges[i:j+1] = [(left, right)]

    def queryRange(self, left: int, right: int) -> bool:
        i = bisect.bisect_left(self.ranges, (left, float('inf')))
        if i: i -= 1
        return (bool(self.ranges) and
                self.ranges[i][0] <= left and
                right <= self.ranges[i][1])

    def removeRange(self, left: int, right: int) -> None:
        i, j = self._bounds(left, right)
        merge = []
        for k in range(i, j+1):
            if self.ranges[k][0] < left:
                merge.append((self.ranges[k][0], left))
            if right < self.ranges[k][1]:
                merge.append((right, self.ranges[k][1]))
        self.ranges[i:j+1] = merge


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
```
* [Hard] [Solution] 715. Range Module

### Boundary Count
```python
class MyCalendarThree:

    def __init__(self):
        self.delta = collections.Counter()

    def book(self, start: int, end: int) -> int:
        self.delta[start] += 1
        self.delta[end] -= 1

        active = ans = 0
        for x in sorted(self.delta):
            active += self.delta[x]
            if active > ans: ans = active

        return ans


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
```
* [Hard] [Solution] 732. My Calendar III

### Segment Tree with Lazy Propagation
```python
class SegmentTree(object):
    def __init__(self, N, update_fn, query_fn):
        self.N = N
        self.H = 1
        while 1 << self.H < N:
            self.H += 1

        self.update_fn = update_fn
        self.query_fn = query_fn
        self.tree = [0] * (2 * N)
        self.lazy = [0] * N

    def _apply(self, x, val):
        self.tree[x] = self.update_fn(self.tree[x], val)
        if x < self.N:
            self.lazy[x] = self.update_fn(self.lazy[x], val)

    def _pull(self, x):
        while x > 1:
            x //= 2
            self.tree[x] = self.query_fn(self.tree[x*2], self.tree[x*2 + 1])
            self.tree[x] = self.update_fn(self.tree[x], self.lazy[x])

    def _push(self, x):
        for h in range(self.H, 0, -1):
            y = x >> h
            if self.lazy[y]:
                self._apply(y * 2, self.lazy[y])
                self._apply(y * 2+ 1, self.lazy[y])
                self.lazy[y] = 0

    def update(self, L, R, h):
        L += self.N
        R += self.N
        L0, R0 = L, R
        while L <= R:
            if L & 1:
                self._apply(L, h)
                L += 1
            if R & 1 == 0:
                self._apply(R, h)
                R -= 1
            L //= 2; R //= 2
        self._pull(L0)
        self._pull(R0)

    def query(self, L, R):
        L += self.N
        R += self.N
        self._push(L); self._push(R)
        ans = 0
        while L <= R:
            if L & 1:
                ans = self.query_fn(ans, self.tree[L])
                L += 1
            if R & 1 == 0:
                ans = self.query_fn(ans, self.tree[R])
                R -= 1
            L //= 2; R //= 2
        return ans

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        #Coordinate Compression
        coords = set()
        for left, size in positions:
            coords.add(left)
            coords.add(left + size - 1)
        index = {x: i for i, x in enumerate(sorted(coords))}

        tree = SegmentTree(len(index), max, max)
        best = 0
        ans = []
        for left, size in positions:
            L, R = index[left], index[left + size - 1]
            h = tree.query(L, R) + size
            tree.update(L, R, h)
            best = max(best, h)
            ans.append(best)

        return ans
```
* [Hard] [Solution] 699. Falling Squares

### Segment Tree
```python
class Node(object):
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.total = self.count = 0
        self._left = self._right = None

    @property
    def mid(self):
        return (self.start + self.end) // 2

    @property
    def left(self):
        self._left = self._left or Node(self.start, self.mid)
        return self._left

    @property
    def right(self):
        self._right = self._right or Node(self.mid, self.end)
        return self._right

    def update(self, i, j, val):
        if i >= j: return 0
        if self.start == i and self.end == j:
            self.count += val
        else:
            self.left.update(i, min(self.mid, j), val)
            self.right.update(max(self.mid, i), j, val)

        if self.count > 0:
            self.total = X[self.end] - X[self.start]
        else:
            self.total = self.left.total + self.right.total

        return self.total

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        OPEN, CLOSE = 1, -1
        events = []
        global X
        X = set()
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, OPEN, x1, x2))
            events.append((y2, CLOSE, x1, x2))
            X.add(x1)
            X.add(x2)
        events.sort()

        X = sorted(X)
        Xi = {x: i for i, x in enumerate(X)}

        active = Node(0, len(X) - 1)
        ans = 0
        cur_x_sum = 0
        cur_y = events[0][0]

        for y, typ, x1, x2 in events:
            ans += cur_x_sum * (y - cur_y)
            cur_x_sum = active.update(Xi[x1], Xi[x2], typ)
            cur_y = y

        return ans % (10**9 + 7)
```
* [Hard] [Solution] 850. Rectangle Area II

### Binary Search, Insertion Sort
```python
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        sortedNums = [nums[-1]]
        ans = [0 for _ in range(len(nums))]
        for i in range(len(nums) -2, -1, -1):
            index = bisect.bisect_left(sortedNums, nums[i])
            ans[i] = index
            sortedNums.insert(index, nums[i])
        return ans
```
* [Hard] 315. Count of Smaller Numbers After Self

## Ordered Map <a name="om"></a>
---
### Maintain Sorted Positions
```python
class ExamRoom:

    def __init__(self, N: int):
        self.N = N
        self.students = []

    def seat(self) -> int:
        # Let's determine student, the position of the next
        # student to sit down.
        if not self.students:
            student = 0
        else:
            # Tenatively, dist is the distance to the closest student,
            # which is achieved by sitting in the position 'student'.
            # We start by considering the left-most seat.
            dist, student = self.students[0], 0
            for i, s in enumerate(self.students):
                if i:
                    prev = self.students[i-1]
                    # For each pair of adjacent students in positions (prev, s),
                    # d is the distance to the closest student;
                    # achieved at position prev + d.
                    d = (s - prev) // 2
                    if d > dist:
                        dist, student = d, prev + d

            # Considering the right-most seat.
            d = self.N - 1 - self.students[-1]
            if d > dist:
                student = self.N - 1

        # Add the student to our sorted list of positions.
        bisect.insort(self.students, student)
        return student

    def leave(self, p: int) -> None:
        self.students.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
```
* [Medium] [Solution] 855. Exam Room

### Maintain Sorted Intervals
```python
class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._X = []

    def addNum(self, val: int) -> None:
        idx = bisect.bisect(self._X, [val])
        if idx == 0 or self._X[idx-1][1] + 1 < val:  # new interval
            l_idx = idx
            l_val = val
        else:  # extend interval
            l_idx = idx-1
            l_val = self._X[idx-1][0]

        if idx == len(self._X) or self._X[idx][0]-1 > val:  # new interval
            r_idx = idx
            r_val = max(val, self._X[idx-1][1] if idx > 0 else -float('inf'))
        else:  # extend interval
            r_idx = idx+1
            r_val = self._X[idx][1]

        self._X[l_idx:r_idx] = [[l_val, r_val]]

    def getIntervals(self) -> List[List[int]]:
        return self._X


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
```
* [Hard] 352. Data Stream as Disjoint Intervals

### Monotonic Stack
```python
class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        N = len(A)

        def make(B):
            ans = [None] * N
            stack = []  # invariant: stack is decreasing
            for i in B:
                while stack and i > stack[-1]:
                    ans[stack.pop()] = i
                stack.append(i)
            return ans

        B = sorted(range(N), key = lambda i: A[i])
        oddnext = make(B)
        B.sort(key = lambda i: -A[i])
        evennext = make(B)

        odd = [False] * N
        even = [False] * N
        odd[N-1] = even[N-1] = True

        for i in range(N-2, -1, -1):
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]

        return sum(odd)
```
* [Hard] [Solution] 975. Odd Even Jump

## Queue <a name="queue"></a>
---
### Recent Calls
```python
class RecentCounter:

    def __init__(self):
        self.q = collections.deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t-3000:
            self.q.popleft()
        return len(self.q)
```
* [Easy] [Solution] 933. Number of Recent Calls

### head, tail pointer, size and filled
```python
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.size = k
        self.filled = 0
        self.q = [0]*self.size
        self.head = self.tail = None

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            # no elements yet
            if self.head is None and self.tail is None:
                self.head = self.tail = 0

            else: # some elements
                self.tail = (self.tail+1) % self.size
            self.q[self.tail] = value    
            self.filled += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = (self.head+1)% self.size
        self.filled -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.q[self.head] if not self.isEmpty() else -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.q[self.tail] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.filled == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.filled == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
```
* [Medium] 622. Design Circular Queue

### Sliding Window
```python
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        N = len(A)
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        #Want smallest y-x with Py - Px >= K
        ans = N+1 # N+1 is impossible
        monoq = collections.deque() #opt(y) candidates, represented as indices of P
        for y, Py in enumerate(P):
            #Want opt(y) = largest x with Px <= Py - K
            while monoq and Py <= P[monoq[-1]]:
                monoq.pop()

            while monoq and Py - P[monoq[0]] >= K:
                ans = min(ans, y - monoq.popleft())

            monoq.append(y)

        return ans if ans < N+1 else -1
```
* [Hard] [Solution] 862. Shortest Subarray with Sum at Least K

### Decreasing deque index
```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq, n, ans = deque([0]), len(nums), []

        for i in range (n):
            while deq and deq[0] <= i - k:
                deq.popleft()
            while deq and nums[i] >= nums[deq[-1]] :
                deq.pop()
            deq.append(i)

            ans.append(nums[deq[0]])

        return ans[k-1:]
```
* [Hard] 239. Sliding Window Maximum

## Minimax <a name="minimax"></a>
---
### Math
```python
class Solution:
    def canWinNim(self, n: int) -> bool:
        return (n % 4 != 0)
```
* [Easy] [Solution] 292. Nim Game

### Winner/Looser
```python
import functools
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @functools.lru_cache(None)
        def dfs(s, e):
            if s == e:
                return nums[s]
            a = nums[s] - dfs(s+1, e)
            b = nums[e] - dfs(s, e-1)
            return max(a, b)

        return dfs(0, len(nums)-1) >= 0
```
* [Medium] [Solution] 486. Predict the Winner

### Minimax cost
```python
import functools
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @functools.lru_cache(None)
        def dfs(a, b) -> int:
            if b <= a:
                return 0
            global_min = float('inf')
            for k in range(a, b + 1):
                local_max = k + max(dfs(a, k - 1), dfs(k + 1, b))
                global_min = min(global_min, local_max)
            return global_min

        return dfs(1, n)
```
* [Medium] 375. Guess Number Higher or Lower II

### Minimax with Heuristic
```python
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        N = len(wordlist)
        self.H = [[sum(a==b for a,b in zip(wordlist[i], wordlist[j]))
                   for j in range(N)] for i in range(N)]

        possible, path = range(N), ()
        while possible:
            guess = self.solve(possible, path)
            matches = master.guess(wordlist[guess])
            if matches == len(wordlist[0]): return
            possible = [j for j in possible if self.H[guess][j] == matches]
            path = path + (guess,)

    def solve(self, possible, path = ()):
        if len(possible) <= 2: return possible[0]

        ansgrp, ansguess = possible, None
        for guess, row in enumerate(self.H):
            if guess not in path:
                groups = [[] for _ in range(7)]
                for j in possible:
                    if j != guess:
                        groups[row[j]].append(j)
                maxgroup = max(groups, key = len)
                if len(maxgroup) < len(ansgrp):
                    ansgrp, ansguess = maxgroup, guess

        return ansguess
```
* [Hard] [Solution] 843. Guess the Word

### Minimax / Percolate from Resolved States
```python
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        N = len(graph)

        # What nodes could play their turn to
        # arrive at node (m, c, t) ?
        def parents(m, c, t):
            if t == 2:
                for m2 in graph[m]:
                    yield m2, c, 3-t
            else:
                for c2 in graph[c]:
                    if c2:
                        yield m, c2, 3-t

        DRAW, MOUSE, CAT = 0, 1, 2
        color = collections.defaultdict(int)

        # degree[node] : the number of neutral children of this node
        degree = {}
        for m in range(N):
            for c in range(N):
                degree[m,c,1] = len(graph[m])
                degree[m,c,2] = len(graph[c]) - (0 in graph[c])

        # enqueued : all nodes that are colored
        queue = collections.deque([])
        for i in range(N):
            for t in range(1, 3):
                color[0, i, t] = MOUSE
                queue.append((0, i, t, MOUSE))
                if i > 0:
                    color[i, i, t] = CAT
                    queue.append((i, i, t, CAT))

        # percolate
        while queue:
            # for nodes that are colored :
            i, j, t, c = queue.popleft()
            # for every parent of this node i, j, t :
            for i2, j2, t2 in parents(i, j, t):
                # if this parent is not colored :
                if color[i2, j2, t2] is DRAW:
                    # if the parent can make a winning move (ie. mouse to MOUSE), do so
                    if t2 == c: # winning move
                        color[i2, j2, t2] = c
                        queue.append((i2, j2, t2, c))
                    # else, this parent has degree[parent]--, and enqueue if all children
                    # of this parent are colored as losing moves
                    else:
                        degree[i2, j2, t2] -= 1
                        if degree[i2, j2, t2] == 0:
                            color[i2, j2, t2] = 3 - t2
                            queue.append((i2, j2, t2, 3 - t2))

        return color[1, 2, 1]
```
* [Hard] [Solution] 913. Cat and Mouse

**Template 1:**
```python
import functools
@functools.lru_cache(None)
def dfs(i, j):
    if j == i:
        return
    global_min = float('inf')
    for k in range(i, j+1):
        local_max = k... + max(dfs(i, k), dfs(k+1, j))
        global_min = min(global_min, local_max)
    return global_min

return dfs(0, N-1)
```

## Line Sweep <a name="ls"></a>
---
### Prefix Sum, Sort
```python
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        count = [0] * (n + 1)
        for i, j in requests:
            count[i] += 1
            count[j + 1] -= 1
        for i in range(1, n + 1):
            count[i] += count[i - 1]
        res = 0
        for v, c in zip(sorted(count[:-1]), sorted(nums)):
            res += v * c
        return res % (10**9 + 7)
```
* [Medium] 1589. Maximum Sum Obtained of Any Permutation

### Greedy
```python
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = right = 0
        for i, j in sorted(intervals, key=lambda a: [a[0], -a[1]]):
            res += j > right
            right = max(right, j)
        return res
```
* [Medium] 1288. Remove Covered Intervals

### Line Sweep
```python
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        # Populate events
        OPEN, CLOSE = 0, 1
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, OPEN, x1, x2))
            events.append((y2, CLOSE, x1, x2))
        events.sort()

        def query():
            ans = 0
            cur = -1
            for x1, x2 in active:
                cur = max(cur, x1)
                ans += max(0, x2 - cur)
                cur = max(cur, x2)
            return ans

        active = []
        cur_y = events[0][0]
        ans = 0
        for y, typ, x1, x2 in events:
            # For all vertical ground covered, update answer
            ans += query() * (y - cur_y)

            # Update active intervals
            if typ is OPEN:
                active.append((x1, x2))
                active.sort()
            else:    
                active.remove((x1, x2))

            cur_y = y

        return ans % (10**9 + 7)
```
* [Hard] [Solution] 850. Rectangle Area II

## Random <a name="random"></a>
---
### Reservoir Sampling
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        scope = 1
        chosen_value = 0
        curr = self.head

        while curr:
            # decide whether to include the element in reservoir
            if random.random() < 1 / scope:
                chosen_value = curr.val
            # move on to the next node
            curr = curr.next
            scope += 1
        return chosen_value
```
* [Medium] 382. Linked List Random Node

### Rejection Sampling, Utilizing out-of-range samples
```python
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        a, b, idx = 0, 0, 0
        while True:
            a = rand7()
            b = rand7()
            idx = b + (a - 1) * 7
            if idx <= 40:
                return 1 + (idx - 1) % 10
            a = idx - 40
            b = rand7()
            # get uniform dist from 1 - 63
            idx = b + (a - 1) * 7
            if idx <= 60:
                return 1 + (idx - 1) % 10
            a = idx - 60
            b = rand7()
            # get uniform dist from 1 - 21
            idx = b + (a - 1) * 7
            if idx <= 20:
                return 1 + (idx - 1) % 10
```
* [Medium] [Solution] 470. Implement Rand10() Using Rand7()

### Fisher-Yates Algorithm
```python
class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.original = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.array = self.original
        self.original = self.original[:]
        return self.array

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
```
* [Medium] [Solution] 384. Shuffle an Array

### 2D area, Prefix Sum, Binary Search
```python
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        # number of points in each rectangle
        self.counts = [(x2 - x1 + 1) * (y2 - y1 + 1) 
                       for x1, y1, x2, y2 in rects]

        # accumulated (prefix) count of points
        self.accumulate_counts = []
        accumulated = 0
        for count in self.counts:
            accumulated += count
            self.accumulate_counts.append(accumulated)
        
        self.total = self.accumulate_counts[-1]

    def pick(self) -> List[int]:
        # rand is in [1, n], including both ends
        rand = random.randint(1, self.total)

        # find rightmost index with value <= rand
        # e.g., for accumulate_count of [2, 5, 8], with rand inputs range [1, 8]
        # there are 3 groups {1,2 | 3,4,5 | 6,7,8}, corresponding to index [0, 1, 2] respectively
        rect_index = bisect.bisect_left(self.accumulate_counts, rand)

        # use rand to find point_index, too
        point_index = rand - self.accumulate_counts[rect_index] + self.counts[rect_index] - 1
        x1, y1, x2, y2 = self.rects[rect_index]
        i, j = divmod(point_index, y2 - y1 + 1)
        return [x1 + i, y1 + j]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
```
* [Medium] 497. Random Point in Non-overlapping Rectangles

### Reservoir Sampling
```python
class Solution:

    def __init__(self, nums: List[int]):
        self.num = nums

    def pick(self, target: int) -> int:
        rst, count = None, 0
        for i in range(len(self.num)):
            if self.num[i] != target: continue
            count += 1
            if random.randint(1, count) == count: rst = i
        return rst

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
```
* [Medium] 398. Random Pick Index

### Blacklist range
```python
class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.N = N
        self.translate_table = {}
        self.blacklist = set(blacklist)

        swap_index = N-1
        for b in self.blacklist:
            if b < N-len(self.blacklist):
                while swap_index in self.blacklist:
                    swap_index -= 1
                self.translate_table[b] = swap_index
                swap_index -= 1

    def pick(self) -> int:
        rand_index = random.randint(0, self.N-len(self.blacklist)-1)
        return self.translate_table.get(rand_index, rand_index)

# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
```
* [Hard] 710. Random Pick with Blacklist

## Topological Sort <a name="ts"></a>
---
### 2-D matrix
```python
import functools
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        R, C = len(matrix), len(matrix[0])
        
        @functools.lru_cache(None)
        def dfs(r, c):
            val = matrix[r][c]
            return 1 + max(dfs(r-1, c) if r and val < matrix[r-1][c] else 0,
                            dfs(r+1, c) if r < R-1 and val < matrix[r+1][c] else 0,
                            dfs(r, c-1) if c and val < matrix[r][c-1] else 0,
                            dfs(r, c+1) if c < C-1 and val < matrix[r][c+1] else 0)
        
        res = 0
        for r in range(R):
            for c in range(C):
                res = max(dfs(r, c), res)
        
        return res
```
* [Hard] 329. Longest Increasing Path in a Matrix

### 2 Level Topological Sort
```python
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # DFS For Topological Sort
        def dfs(x, pre_list, visit_state, order):
            if visit_state[x] == -1:
                return False
            if visit_state[x] == 1:
                return True
            visit_state[x] = -1
            no_cycles = True
            for p in pre_list[x]:
                no_cycles &= dfs(p, pre_list, visit_state, order)
            visit_state[x] = 1
            order.append(x)
            return no_cycles

        # First make items that are on their own to group[item] = item
        # and make the items that are in the same group to have a group[item] of their leader,
        # where the leader is the item of the group that has min index
        group_translation = {}
        group_table = collections.defaultdict(list)
        for i in range(n):
            if group[i] == -1:
                group[i] = i
            else:
                if not group[i] in group_translation:
                    group_translation[group[i]] = i
                group[i] = group_translation[group[i]]
            group_table[group[i]].append(i)

        # Go through beforeItems, if the item is in the same group, add to inner_pre
        # if the item is in another group, add a pre to the outer_pre
        outer_pre = collections.defaultdict(list)
        inner_pre = collections.defaultdict(list)
        for i in range(n):
            current_group = group[i]
            for b in beforeItems[i]:
                b_group = group[b]
                if b_group == current_group:
                    inner_pre[i].append(b)
                else:
                    outer_pre[current_group].append(b_group)

        # Do topological sort on groups and get a group_order
        group_order = []
        visit_state = collections.defaultdict(int)
        no_group_cycles = True
        for g in group_table:
            if not no_group_cycles:
                return []
            no_group_cycles &= dfs(g, outer_pre, visit_state, group_order)

        # Finally we iterate through each group and do topological sort on the items in the same group
        # and add to result
        result = []
        for g in group_order:
            inner_order = []
            visit_state = collections.defaultdict(int)
            no_inner_cycles = True
            for item in group_table[g]:
                if not no_inner_cycles:
                    return []
                no_inner_cycles &= dfs(item, inner_pre, visit_state, inner_order)
            result += inner_order
        return result
```
* [Hard] 1203. Sort Items by Groups Respecting Dependencies

## Brainteaser <a name="brainteaser"></a>
---
### State
```python
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n**.5)
```
* [Medium] 319. Bulb Switcher

### Probability
```python
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1 if n == 1 else 0.5
```
* [Medium] 1227. Airplane Seat Assignment Probability

### Last Moment
```python
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(max(left or [0]), n - min(right or [n]), 0)
```
* [Medium] 1503. Last Moment Before All Ants Fall Out of a Plank

## Geometry <a name="geometry"></a>
---
### Square by Square
```python
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        N = len(grid)

        ans = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    ans += 2
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r,c+1)):
                        if 0 <= nr < N and 0 <= nc < N:
                            nval = grid[nr][nc]
                        else:
                            nval = 0

                        ans += max(grid[r][c] - nval, 0)

        return ans
```
* [Easy] [Solution] 892. Surface Area of 3D Shapes

### Straight line
```python
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (u, v), (p, q) = coordinates[: 2]
        return all((x - u) * (y - q) == (x - p) * (y - v) for x, y in coordinates)
```
* [Easy] 1232. Check If It Is a Straight Line

### Iterate Centers
```python
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        points = [complex(*z) for z in points]
        seen = collections.defaultdict(list)
        for P, Q in itertools.combinations(points, 2):
            center = (P + Q) / 2
            radius = abs(center - P)
            seen[center, radius].append(P)

        ans = float("inf")
        for (center, radius), candidates in seen.items():
            for P, Q in itertools.combinations(candidates, 2):
                ans = min(ans, abs(P - Q) * abs(P - (2*center - Q)))

        return ans if ans < float("inf") else 0
```
* [Medium] [Solution] 963. Minimum Area Rectangle II

### Overlap
```python
class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        corners = [(x1,y1), (x2,y1), (x2,y2), (x1, y2)]
        for (x, y) in corners:
            if (x_center - x)**2 + (y_center - y)**2 <= radius**2:
                return True

        for x in [x1, x2]:
            if x_center - radius <= x <= x_center + radius and y2 - y_center >= 0 and y1 - y_center <= 0:
                return True
        for y in [y1, y2]:
            if y_center - radius <= y <= y_center + radius and x2 - x_center >= 0 and x1 - x_center <= 0:
                return True

        if x1 <= x_center <= x2 and y1 <= y_center <= y2:
            return True
        return False 
```
* [Medium] 1401. Circle and Rectangle Overlapping

### Monotone Chain
```python
class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        if len(points) <= 3:
            return points

        def is_turn_left(p1, p2, p3):
            return cross_product(direction(p1, p2), direction(p1, p3)) > 0

        def direction(x, y):
            return [y[0] - x[0], y[1] - x[1]]

        def cross_product(x, y):
            return x[0] * y[1] - x[1] * y[0]

        points.sort()
        stack = [points[0], points[1]]

        for p in points[2:]:
            while len(stack) >= 2 and is_turn_left(stack[-2], stack[-1], p):
                stack.pop()
            stack.append(p)   
        for p in reversed(points[:-1]):
            while len(stack) >= 2 and is_turn_left(stack[-2], stack[-1], p):
                stack.pop()
            stack.append(p)
        stack.pop()

        return stack
```
* [Hard] [Solution] 587. Erect the Fence

## Regular Expression <a name="re"></a>
---
### Detect Capital
```python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return re.fullmatch(r"[A-Z]*|.[a-z]*", word)
```
* [Easy] [Solution] 520. Detect Capital

### Using regex for spliting
```python
class Solution:
    def solveEquation(self, equation: str) -> str:
        def coeff(x):
            if len(x) > 1 and x[len(x) - 2] >= '0' and x[len(x) - 2] <= '9':
                return x.replace('x', '')
            return x.replace('x', '1')

        lr = equation.split('=')
        for x in re.split(r"(?=\+)|(?=-)", lr[1]):
            if x.find('x') >= 0:
                lhs -= int(coeff(x))
            else:
                rhs += int(x) if x != '' else 0
        if (lhs == 0):
            if (rhs == 0):
                return "Infinite solutions";
            else:
                return "No solution";
        else:
            return 'x={}'.format(rhs // lhs)
```
* [Medium] [Solution] 640. Solve the Equation

### match
```python
class Solution:
    def validIPAddress(self, IP: str) -> str:
        pattern_ipv4 = r"^((25[0-5]|2[0-4]\d|1\d{0,2}|\d|[1-9]\d)\.){3}(25[0-5]|2[0-4]\d|1\d{0,2}|\d|[1-9]\d)$"
        pattern_ipv6 = r"^(?i)(([0-9a-f]{1,4}|0):){7}([0-9a-f]{1,4}|0)$"
        if re.match(pattern_ipv4, IP):
            return 'IPv4'
        if re.match(pattern_ipv6, IP):
            return 'IPv6'
        return 'Neither'
```
* [Medium] 468. Validate IP Address

### Decode
```python
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        parse = re.findall(r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)", formula)
        stack = [collections.Counter()]
        for name, m1, left_open, right_open, m2 in parse:
            if name:
                stack[-1][name] += int(m1 or 1)
            if left_open:
                stack.append(collections.Counter())
            if right_open:
                top = stack.pop()
                for k in top:
                    stack[-1][k] += top[k] * int(m2 or 1)

        return "".join(name + (str(stack[-1][name]) if stack[-1][name] > 1 else '')
                       for name in sorted(stack[-1]))
```
* [Hard] [Solution] 726. Number of Atoms
