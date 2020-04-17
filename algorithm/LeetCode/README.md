
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
1. [30-Day LeetCoding Challenge](#30day)
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
* `re.split(pattern, string, maxsplit=0, flags=0)`
* `re.findall(pattern, string, flags=0)`

### datetime

* `datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)`

    * ex. datetime.datetime(2011, 11, 4, 0, 0) --> datetime.fromisoformat('2011-11-04T00:05:23')
* `datetime.strftime(format)`

    * ex. dt.strftime("%A, %d. %B %Y %I:%M%p") --> 'Tuesday, 21. November 2006 04:30PM'
* `datetime.strptime(date_string, format)`

    * ex. datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M") --> datetime.datetime(2006, 11, 21, 16, 30)

## 30-Day LeetCoding Challenge <a name="30day"></a>
---
* [[Easy] [Solution] 136. Single Number](%5BEasy%5D%20%5BSolution%5D%20136.%20Single%20Number.md)
* [[Easy] 202. Happy Number](%5BEasy%5D%20202.%20Happy%20Number.md)
* [[Easy] 53. Maximum Subarray](%5BEasy%5D%2053.%20Maximum%20Subarray.md)
* [[Easy] [Solution] 283. Move Zeroes](%5BEasy%5D%20%5BSolution%5D%20283.%20Move%20Zeroes.md)
* [[Easy] [Solution] 122. Best Time to Buy and Sell Stock II](%5BEasy%5D%20%5BSolution%5D%20122.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock%20II.md)
* [[Medium] [Solution] 49. Group Anagrams](%5BMedium%5D%20%5BSolution%5D%2049.%20Group%20Anagrams.md)
* [[Easy] [Solution] 876. Middle of the Linked List](%5BEasy%5D%20%5BSolution%5D%20876.%20Middle%20of%20the%20Linked%20List.md)
* [[Easy] [Solution] 844. Backspace String Compare](%5BEasy%5D%20%5BSolution%5D%20844.%20Backspace%20String%20Compare.md)
* [[Easy] 155. Min Stack](%5BEasy%5D%20155.%20Min%20Stack.md)
* [[Easy] [Solution] 543. Diameter of Binary Tree](%5BEasy%5D%20%5BSolution%5D%20543.%20Diameter%20of%20Binary%20Tree.md)
* [[Easy] 1046. Last Stone Weight](%5BEasy%5D%201046.%20Last%20Stone%20Weight.md)
* [[Medium] [Solution] 525. Contiguous Array](%5BMedium%5D%20%5BSolution%5D%20525.%20Contiguous%20Array.md)
* [[Medium] [Solution] 238. Product of Array Except Self](%5BMedium%5D%20%5BSolution%5D%20238.%20Product%20of%20Array%20Except%20Self.md)
* [[Medium] [Solution] 678. Valid Parenthesis String](%5BMedium%5D%20%5BSolution%5D%20678.%20Valid%20Parenthesis%20String.md)
* [[Medium] 200. Number of Islands](%5BMedium%5D%20200.%20Number%20of%20Islands.md)

## Array <a name="array"></a>
---
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
```
* [[Easy] [Solution] 832. Flipping an Image](%5BEasy%5D%20%5BSolution%5D%20832.%20Flipping%20an%20Image.md)

### Rotate Array
```python
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums.reverse()
        nums[:k] = nums[:k][::-1]
        nums[k:len(nums)] = nums[k:len(nums)][::-1]
```
* [[Easy] [Solution] 189. Rotate Array](%5BEasy%5D%20%5BSolution%5D%20189.%20Rotate%20Array.md)

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
* [[Easy] [Solution] 169. Majority Element](%5BEasy%5D%20%5BSolution%5D%20169.%20Majority%20Element.md)

### Using division and modulus
```python
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        R = len(nums)
        C = len(nums[0])
        if R == 0 or r*c != R*C:
            return nums
        res = [[0 for _ in range(c)] for _ in range(r)]
        count = 0
        for i in range(R):
            for j in range(C):
                res[count//c][count%c] = nums[i][j]
                count += 1

        return res
```
* [[Easy] [Solution] 566. Reshape the Matrix](%5BEasy%5D%20%5BSolution%5D%20566.%20Reshape%20the%20Matrix.md)

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
* [[Easy] [Solution] 665. Non-decreasing Array](%5BEasy%5D%20%5BSolution%5D%20665.%20Non-decreasing%20Array.md)

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
* [[Easy] [Solution] 724. Find Pivot Index](%5BEasy%5D%20%5BSolution%5D%20724.%20Find%20Pivot%20Index.md)

### Compare With Top-Left Neighbor
```python
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))
```
* [[Easy] [Solution] 766. Toeplitz Matrix](%5BEasy%5D%20%5BSolution%5D%20766.%20Toeplitz%20Matrix.md)

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
* [[Easy] [Solution] 840. Magic Squares In Grid](%5BEasy%5D%20%5BSolution%5D%20840.%20Magic%20Squares%20In%20Grid.md)

### Copy Directly
```python
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return zip(*A)
```
* [[Easy] [Solution] 867. Transpose Matrix](%5BEasy%5D%20%5BSolution%5D%20867.%20Transpose%20Matrix.md)

### Greatest Common Divisor
```python
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from functools import reduce
        vals = collections.Counter(deck).values()
        return reduce(math.gcd, vals) >= 2
```
* [[Easy] [Solution] 914. X of a Kind in a Deck of Cards](%5BEasy%5D%20%5BSolution%5D%20914.%20X%20of%20a%20Kind%20in%20a%20Deck%20of%20Cards.md)

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
* [[Easy] [Solution] 896. Monotonic Array](%5BEasy%5D%20%5BSolution%5D%20896.%20Monotonic%20Array.md)

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
* [[Easy] [Solution] 985. Sum of Even Numbers After Queries](%5BEasy%5D%20%5BSolution%5D%20985.%20Sum%20of%20Even%20Numbers%20After%20Queries.md)

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
* [[Easy] 1252. Cells with Odd Values in a Matrix](%5BEasy%5D%201252.%20Cells%20with%20Odd%20Values%20in%20a%20Matrix.md)

### Linear Scan
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
* [[Medium] [Solution] 611. Valid Triangle Number](%5BMedium%5D%20%5BSolution%5D%20611.%20Valid%20Triangle%20Number.md)

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
* [[Medium] [Solution] 565. Array Nesting](%5BMedium%5D%20%5BSolution%5D%20565.%20Array%20Nesting.md)

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
* [[Medium] [Solution] 238. Product of Array Except Self](%5BMedium%5D%20%5BSolution%5D%20238.%20Product%20of%20Array%20Except%20Self.md)

### O(1) Space, Efficient Solution
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
* [[Medium] [Solution] 73. Set Matrix Zeroes](%5BMedium%5D%20%5BSolution%5D%2073.%20Set%20Matrix%20Zeroes.md)

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
* [[Medium] [Solution] 729. My Calendar I](%5BMedium%5D%20%5BSolution%5D%20729.%20My%20Calendar%20I.md)

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
* [[Medium] [Solution] 825. Friends Of Appropriate Ages](%5BMedium%5D%20%5BSolution%5D%20825.%20Friends%20Of%20Appropriate%20Ages.md)

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
* [[Medium] [Solution] 900. RLE Iterator](%5BMedium%5D%20%5BSolution%5D%20900.%20RLE%20Iterator.md)

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
* [[Medium] [Solution] 915. Partition Array into Disjoint Intervals](%5BMedium%5D%20%5BSolution%5D%20915.%20Partition%20Array%20into%20Disjoint%20Intervals.md)

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
* [[Medium] [Solution] 918. Maximum Sum Circular Subarray](%5BMedium%5D%20%5BSolution%5D%20918.%20Maximum%20Sum%20Circular%20Subarray.md)

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
* [[Medium] [Solution] 926. Flip String to Monotone Increasing](%5BMedium%5D%20%5BSolution%5D%20926.%20Flip%20String%20to%20Monotone%20Increasing.md)

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
* [[Medium] [Solution] 945. Minimum Increment to Make Array Unique](%5BMedium%5D%20%5BSolution%5D%20945.%20Minimum%20Increment%20to%20Make%20Array%20Unique.md)

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
* [[Medium] [Solution] 950. Reveal Cards In Increasing Order](%5BMedium%5D%20%5BSolution%5D%20950.%20Reveal%20Cards%20In%20Increasing%20Order.md)

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
* [[Medium] [Solution] 962. Maximum Width Ramp](%5BMedium%5D%20%5BSolution%5D%20962.%20Maximum%20Width%20Ramp.md)

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
* [[Medium] [Solution] 969. Pancake Sorting](%5BMedium%5D%20%5BSolution%5D%20969.%20Pancake%20Sorting.md)

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
* [[Medium] [Solution] 974. Subarray Sums Divisible by K](%5BMedium%5D%20%5BSolution%5D%20974.%20Subarray%20Sums%20Divisible%20by%20K.md)

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
* [[Medium] 1109. Corporate Flight Bookings](%5BMedium%5D%201109.%20Corporate%20Flight%20Bookings.md)

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
* [[Medium] [Solution] 5. Longest Palindromic Substring](%5BMedium%5D%20%5BSolution%5D%205.%20Longest%20Palindromic%20Substring.md)

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
* [[Hard] [Solution] 689. Maximum Sum of 3 Non-Overlapping Subarrays](%5BHard%5D%20%5BSolution%5D%20689.%20Maximum%20Sum%20of%203%20Non-Overlapping%20Subarrays.md)

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
* [[Hard] [Solution] 768. Max Chunks To Make Sorted II](%5BHard%5D%20%5BSolution%5D%20768.%20Max%20Chunks%20To%20Make%20Sorted%20II.md)

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
* [[Hard] 1330. Reverse Subarray To Maximize Array Value](%5BHard%5D%201330.%20Reverse%20Subarray%20To%20Maximize%20Array%20Value.md)

## Dynamic Programming <a name="dp"></a>
---
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
```
* [[Easy] [Solution] 746. Min Cost Climbing Stairs](%5BEasy%5D%20%5BSolution%5D%20746.%20Min%20Cost%20Climbing%20Stairs.md)

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
```
* [[Medium] 152. Maximum Product Subarray](%5BMedium%5D%20152.%20Maximum%20Product%20Subarray.md)

### Longest Fibonacci Subsequence
```python
class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        index = {x: i for i, x in enumerate(A)}
        longest = collections.defaultdict(lambda: 2)

        ans = 0
        for k, z in enumerate(A):
            for j in range(k):
                i = index.get(z - A[j], None)
                if i is not None and i < j:
                    cand = longest[j, k] = longest[i, j] + 1
                    ans = max(ans, cand)

        return ans if ans >= 3 else 0
```
* [[Medium] [Solution] 873. Length of Longest Fibonacci Subsequence](%5BMedium%5D%20%5BSolution%5D%20873.%20Length%20of%20Longest%20Fibonacci%20Subsequence.md)

### Top-down
```python
import functools
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @functools.lru_cache(None)
        def dfs(i, j):
            if i == j:
                return piles[i]
            a = piles[i] - dfs(i+1, j)
            b = piles[j] - dfs(i, j-1)
            return max(a, b)

        return dfs(0, len(piles)-1) >= 0
```
* [[Medium] [Solution] 877. Stone Game](%5BMedium%5D%20%5BSolution%5D%20877.%20Stone%20Game.md)

### Bottom-up
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
* [[Medium] [Solution] 712. Minimum ASCII Delete Sum for Two Strings](%5BMedium%5D%20%5BSolution%5D%20712.%20Minimum%20ASCII%20Delete%20Sum%20for%20Two%20Strings.md)

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
* [[Medium] [Solution] 304. Range Sum Query 2D - Immutable](%5BMedium%5D%20%5BSolution%5D%20304.%20Range%20Sum%20Query%202D%20-%20Immutable.md)

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
* [[Medium] 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance](%5BMedium%5D%201334.%20Find%20the%20City%20With%20the%20Smallest%20Number%20of%20Neighbors%20at%20a%20Threshold%20Distance.md)

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
* [[Medium] [Solution] 714. Best Time to Buy and Sell Stock with Transaction Fee](%5BMedium%5D%20%5BSolution%5D%20714.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock%20with%20Transaction%20Fee.md)

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
```
* [[Medium] [Solution] 376. Wiggle Subsequence](%5BMedium%5D%20%5BSolution%5D%20376.%20Wiggle%20Subsequence.md)

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
* [[Hard] 363. Max Sum of Rectangle No Larger Than K](%5BHard%5D%20363.%20Max%20Sum%20of%20Rectangle%20No%20Larger%20Than%20K.md)

### Longest Increasing Subsequence
```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 0: return 0
        memo = [[-1]*N for _ in range(N+1)]
        ans = 0

        def dfs(previndex, curpos):
            if curpos == N:
                return 0
            if memo[previndex + 1][curpos] >= 0:
                return memo[previndex + 1][curpos]
            taken = 0
            if previndex < 0 or nums[curpos] > nums[previndex]:
                taken = 1 + dfs(curpos, curpos + 1)
            nottaken = dfs(previndex, curpos + 1)
            memo[previndex + 1][curpos] = max(taken, nottaken)
            return memo[previndex + 1][curpos]

        return dfs(-1, 0)
    
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
* [[Medium] [Solution] 300. Longest Increasing Subsequence](%5BMedium%5D%20%5BSolution%5D%20300.%20Longest%20Increasing%20Subsequence.md)

### Longest Common Subarray
```python
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        M, N = len(A), len(B)
        ans = 0
        mem = {}
        
        @functools.lru_cache(None)
        def dfs(i, j):
            nonlocal ans
            if i == 0 or j == 0:
                return 0
            else:
                rst = 0
                if A[i-1] == B[j-1]:
                    rst = 1 + dfs(i - 1, j - 1)
                decrease_i = dfs(i - 1, j)
                decrease_j = dfs(i, j - 1)
                ans = max(ans, rst, decrease_i, decrease_j)
                return rst

        dfs(M, N)
        return ans

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    memo[i+1][j+1] = memo[i][j]+1
        return max(max(row) for row in memo)
```
* [[Medium] [Solution] 718. Maximum Length of Repeated Subarray](%5BMedium%5D%20%5BSolution%5D%20718.%20Maximum%20Length%20of%20Repeated%20Subarray.md)

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
* [[Medium] 1143. Longest Common Subsequence](%5BMedium%5D%201143.%20Longest%20Common%20Subsequence.md)

### longest number
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
* [[Medium] [Solution] 673. Number of Longest Increasing Subsequence](%5BMedium%5D%20%5BSolution%5D%20673.%20Number%20of%20Longest%20Increasing%20Subsequence.md)

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
* [[Medium] [Solution] 688. Knight Probability in Chessboard](%5BMedium%5D%20%5BSolution%5D%20688.%20Knight%20Probability%20in%20Chessboard.md)

### Count on every level
```python
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
* [[Medium] [Solution] 413. Arithmetic Slices](%5BMedium%5D%20%5BSolution%5D%20413.%20Arithmetic%20Slices.md)

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
```
* [[Medium] [Solution] 221. Maximal Square](%5BMedium%5D%20%5BSolution%5D%20221.%20Maximal%20Square.md)

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
* [[Medium] [Solution] 300. Longest Increasing Subsequence](%5BMedium%5D%20%5BSolution%5D%20300.%20Longest%20Increasing%20Subsequence.md)

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
* [[Medium] [Solution] 638. Shopping Offers](%5BMedium%5D%20%5BSolution%5D%20638.%20Shopping%20Offers.md)

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
* [[Medium] [Solution] 698. Partition to K Equal Sum Subsets](%5BMedium%5D%20%5BSolution%5D%20698.%20Partition%20to%20K%20Equal%20Sum%20Subsets.md)

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
* [[Medium] [Solution] 764. Largest Plus Sign](%5BMedium%5D%20%5BSolution%5D%20764.%20Largest%20Plus%20Sign.md)

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
* [[Medium] 790. Domino and Tromino Tiling](%5BMedium%5D%20790.%20Domino%20and%20Tromino%20Tiling.md)

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
* [[Medium] [Solution] 801. Minimum Swaps To Make Sequences Increasing](%5BMedium%5D%20%5BSolution%5D%20801.%20Minimum%20Swaps%20To%20Make%20Sequences%20Increasing.md)

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
* [[Medium] [Solution] 813. Largest Sum of Averages](%5BMedium%5D%20%5BSolution%5D%20813.%20Largest%20Sum%20of%20Averages.md)

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
* [[Medium] [Solution] 931. Minimum Falling Path Sum](%5BMedium%5D%20%5BSolution%5D%20931.%20Minimum%20Falling%20Path%20Sum.md)

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
* [[Medium] [Solution] 935. Knight Dialer](%5BMedium%5D%20%5BSolution%5D%20935.%20Knight%20Dialer.md)

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
* [[Medium] [Solution] 983. Minimum Cost For Tickets](%5BMedium%5D%20%5BSolution%5D%20983.%20Minimum%20Cost%20For%20Tickets.md)

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
* [[Hard] [Solution] 10. Regular Expression Matching](%5BHard%5D%20%5BSolution%5D%2010.%20Regular%20Expression%20Matching.md)

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
* [[Hard] [Solution] 97. Interleaving String](%5BHard%5D%20%5BSolution%5D%2097.%20Interleaving%20String.md)

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
* [[Hard] [Solution] 629. K Inverse Pairs Array](%5BHard%5D%20%5BSolution%5D%20629.%20K%20Inverse%20Pairs%20Array.md)

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
```
* [[Hard] [Solution] 902. Numbers At Most N Given Digit Set](%5BHard%5D%20%5BSolution%5D%20902.%20Numbers%20At%20Most%20N%20Given%20Digit%20Set.md)

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
* [[Hard] [Solution] 903. Valid Permutations for DI Sequence](%5BHard%5D%20%5BSolution%5D%20903.%20Valid%20Permutations%20for%20DI%20Sequence.md)

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
* [[Hard] [Solution] 920. Number of Music Playlists](%5BHard%5D%20%5BSolution%5D%20920.%20Number%20of%20Music%20Playlists.md)

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
* [[Hard] 140. Word Break II](%5BHard%5D%20140.%20Word%20Break%20II.md)

### k state
```python
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0
        n = len(prices)

        #PRECHECK if 2*k >= n  that means we just need to count everyday's profit no need to DP 
        if 2*k >= n:
            res = 0
            for i in range(1, n):
                res += max(prices[i] - prices[i-1], 0)
            return res

        #dp status of buy and sell, only need One-Dimention
        bsk = [0 for i in range(2*k)]   #buy_1 sell_1 buy_2 sell_2 ==> buy_k sell_k (k times)
        for b in range(2*k):
            if b%2 == 0:
                bsk[b] = -prices[0]

        for i in range(1, n):
            bsk[0] = max(bsk[0], -prices[i])
            #for buys
            for j in range(2, 2*k, 2):
                bsk[j] = max(bsk[j-1]-prices[i], bsk[j])
            #for sells
            for o in range(1, 2*k, 2):
                bsk[o] = max(bsk[o-1]+prices[i], bsk[o])
        return bsk[2*k-1]
```
* [[Hard] 188. Best Time to Buy and Sell Stock IV](%5BHard%5D%20188.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock%20IV.md)

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
* [[Hard] 1397. Find All Good Strings](%5BHard%5D%201397.%20Find%20All%20Good%20Strings.md)

## Math <a name="math"></a>
---
### Combination
```python
class Solution:
    def countOrders(self, n: int) -> int:
        return (math.factorial(n * 2) >> n) % (10**9 + 7)  # 2n!/2^n
```
* [[Hard] 1359. Count All Valid Pickup and Delivery Options](%5BHard%5D%201359.%20Count%20All%20Valid%20Pickup%20and%20Delivery%20Options.md)

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
* [[Medium] 1362. Closest Divisors](%5BMedium%5D%201362.%20Closest%20Divisors.md)

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
* [[Medium] [Solution] 667. Beautiful Arrangement II](%5BMedium%5D%20%5BSolution%5D%20667.%20Beautiful%20Arrangement%20II.md)

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
* [[Hard] [Solution] 891. Sum of Subsequence Widths](%5BHard%5D%20%5BSolution%5D%20891.%20Sum%20of%20Subsequence%20Widths.md)

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
* [[Hard] [Solution] 887. Super Egg Drop](%5BHard%5D%20%5BSolution%5D%20887.%20Super%20Egg%20Drop.md)

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

## Tree <a name='tree'></a>
---
### Binary Search Tree
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
* [[Easy] [Solution] 538. Convert BST to Greater Tree](%5BEasy%5D%20%5BSolution%5D%20538.%20Convert%20BST%20to%20Greater%20Tree.md)

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
* [[Medium] 1372. Longest ZigZag Path in a Binary Tree](%5BMedium%5D%201372.%20Longest%20ZigZag%20Path%20in%20a%20Binary%20Tree.md)

## Hash Table <a name='ht'></a>
---
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
* [[Easy] [Solution] 697. Degree of an Array](%5BEasy%5D%20%5BSolution%5D%20697.%20Degree%20of%20an%20Array.md)

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
* [[Medium] [Solution] 676. Implement Magic Dictionary](%5BMedium%5D%20%5BSolution%5D%20676.%20Implement%20Magic%20Dictionary.md)

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
* [[Medium] 1366. Rank Teams by Votes](%5BMedium%5D%201366.%20Rank%20Teams%20by%20Votes.md)

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
* [[Medium] 1371. Find the Longest Substring Containing Vowels in Even Counts](%5BMedium%5D%201371.%20Find%20the%20Longest%20Substring%20Containing%20Vowels%20in%20Even%20Counts.md)

### Prefix Sum
```python
class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_cnt = collections.defaultdict(int)
        sum_cnt[0] = 1
        cur_sum = 0
        cnt = 0

        for i in range(len(nums)):
            cur_sum += nums[i]                        

            if cur_sum-k in sum_cnt:
                cnt += sum_cnt[cur_sum-k]

            sum_cnt[cur_sum] += 1    

        return cnt
```
* [[Medium] [Solution] 560. Subarray Sum Equals K](%5BMedium%5D%20%5BSolution%5D%20560.%20Subarray%20Sum%20Equals%20K.md)

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
* [[Medium] [Solution] 718. Maximum Length of Repeated Subarray](%5BMedium%5D%20%5BSolution%5D%20718.%20Maximum%20Length%20of%20Repeated%20Subarray.md)

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
* [[Hard] 1316. Distinct Echo Substrings](%5BHard%5D%201316.%20Distinct%20Echo%20Substrings.md)

### Subsequence Rolling Hash
```python
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        word_dict = collections.defaultdict(list)
        count = 0

        for word in words:
            word_dict[word[0]].append(word)            

        for char in S:
            words_expecting_char = word_dict[char]
            word_dict[char] = []
            for word in words_expecting_char:
                if len(word) == 1:
                    # Finished subsequence! 
                    count += 1
                else:
                    word_dict[word[1]].append(word[1:])

        return count
```
* [[Medium] 792. Number of Matching Subsequences](%5BMedium%5D%20792.%20Number%20of%20Matching%20Subsequences.md)

### Count by Delta
```python
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        N = len(A)
        count = collections.Counter()
        for i, row in enumerate(A):
            for j, v in enumerate(row):
                if v:
                    for i2, row2 in enumerate(B):
                        for j2, v2 in enumerate(row2):
                            if v2:
                                count[i-i2, j-j2] += 1

        return max(count.values() or [0])
```
* [[Medium] [Solution] 835. Image Overlap](%5BMedium%5D%20%5BSolution%5D%20835.%20Image%20Overlap.md)

## Depth-first Search <a name="dfs"></a>
---
### Redundant Connection
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
* [[Medium] [Solution] 684. Redundant Connection](%5BMedium%5D%20%5BSolution%5D%20684.%20Redundant%20Connection.md)

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
* [[Medium] [Solution] 841. Keys and Rooms](%5BMedium%5D%20%5BSolution%5D%20841.%20Keys%20and%20Rooms.md)

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
* [[Medium] [Solution] 934. Shortest Bridge](%5BMedium%5D%20%5BSolution%5D%20934.%20Shortest%20Bridge.md)

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
* [[Medium] 207. Course Schedule](%5BMedium%5D%20207.%20Course%20Schedule.md)

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
* [[Medium] 1319. Number of Operations to Make Network Connected](%5BMedium%5D%201319.%20Number%20of%20Operations%20to%20Make%20Network%20Connected.md)

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
* [[Medium] 1343. Maximum Product of Splitted Binary Tree](%5BMedium%5D%201343.%20Maximum%20Product%20of%20Splitted%20Binary%20Tree.md)

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
* [[Medium] [Solution] 756. Pyramid Transition Matrix](%5BMedium%5D%20%5BSolution%5D%20756.%20Pyramid%20Transition%20Matrix.md)

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
* [[Medium] 1202. Smallest String With Swaps](%5BMedium%5D%201202.%20Smallest%20String%20With%20Swaps.md)

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

* [[Medium] 1110. Delete Nodes And Return Forest](%5BMedium%5D%201110.%20Delete%20Nodes%20And%20Return%20Forest.md)
* [[Medium] * 450. Delete Node in a BST](%5BMedium%5D%20*%20450.%20Delete%20Node%20in%20a%20BST.md)

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

### Binary Search 2
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

### Rotated Sorted Array
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
* [[Medium] [Solution] 153. Find Minimum in Rotated Sorted Array](%5BMedium%5D%20%5BSolution%5D%20153.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array.md)

### Find local maximum
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
* [[Medium] [Solution] 162. Find Peak Element](%5BMedium%5D%20%5BSolution%5D%20162.%20Find%20Peak%20Element.md)

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
* [[Medium] 1011. Capacity To Ship Packages Within D Days](%5BMedium%5D%201011.%20Capacity%20To%20Ship%20Packages%20Within%20D%20Days.md)

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
* [[Medium] 1300. Sum of Mutated Array Closest to Target](%5BMedium%5D%201300.%20Sum%20of%20Mutated%20Array%20Closest%20to%20Target.md)

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
* [[Medium] 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold](%5BMedium%5D%201292.%20Maximum%20Side%20Length%20of%20a%20Square%20with%20Sum%20Less%20than%20or%20Equal%20to%20Threshold.md)

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
* [[Hard] [Solution] 719. Find K-th Smallest Pair Distance](%5BHard%5D%20%5BSolution%5D%20719.%20Find%20K-th%20Smallest%20Pair%20Distance.md)

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
* [[Hard] 1157. Online Majority Element In Subarray](%5BHard%5D%201330.%20Reverse%20Subarray%20To%20Maximize%20Array%20Value.md)

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

* [[Hard] 1231. Divide Chocolate](%5BHard%5D%201231.%20Divide%20Chocolate.md)
* [[Medium] 1201. Ugly Number III](%5BMedium%5D%201201.%20Ugly%20Number%20III.md)
* [[Medium] [Solution] 875. Koko Eating Bananas](%5BMedium%5D%20%5BSolution%5D%20875.%20Koko%20Eating%20Bananas.md)

## Greedy <a name="greedy"></a>
---
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
* [[Easy] [Solution] 605. Can Place Flowers](%5BEasy%5D%20%5BSolution%5D%20605.%20Can%20Place%20Flowers.md)

### 1-bit and 2-bit Characters
```python
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        parity = bits.pop()
        while bits and bits.pop(): parity ^= 1
        return parity == 0
```
* [[Easy] [Solution] 717. 1-bit and 2-bit Characters](%5BEasy%5D%20%5BSolution%5D%20717.%201-bit%20and%202-bit%20Characters.md)

### Total period
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
* [[Medium] [Solution] 495. Teemo Attacking](%5BMedium%5D%20%5BSolution%5D%20495.%20Teemo%20Attacking.md)

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
* [[Medium] [Solution] 714. Best Time to Buy and Sell Stock with Transaction Fee](%5BMedium%5D%20%5BSolution%5D%20714.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock%20with%20Transaction%20Fee.md)

### Sort
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
* [[Medium] [Solution] 870. Advantage Shuffle](%5BMedium%5D%20%5BSolution%5D%20870.%20Advantage%20Shuffle.md)

### Jump Game
```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_pos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i
        return last_pos == 0
```
* [[Medium] [Solution] 55. Jump Game](%5BMedium%5D%20%5BSolution%5D%2055.%20Jump%20Game.md)

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
* [[Medium] [Solution] 670. Maximum Swap](%5BMedium%5D%20%5BSolution%5D%20670.%20Maximum%20Swap.md)

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
* [[Medium] [Solution] 954. Array of Doubled Pairs](%5BMedium%5D%20%5BSolution%5D%20954.%20Array%20of%20Doubled%20Pairs.md)

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
* [[Medium] [Solution] 678. Valid Parenthesis String](%5BMedium%5D%20%5BSolution%5D%20678.%20Valid%20Parenthesis%20String.md)

### DFS, Tree
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
* [[Hard] [Solution] 968. Binary Tree Cameras](%5BHard%5D%20%5BSolution%5D%20968.%20Binary%20Tree%20Cameras.md)


## Prefix Sum
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
* [[Hard] 1402. Reducing Dishes](%5BHard%5D%201402.%20Reducing%20Dishes.md)

**Template 1:**
```python
ans = []
A.sort()
for i in ragen(len(A)):
    if /* max profit */:
        ans += ...
        
return ans
```

* [[Medium] [Solution] 767. Reorganize String](%5BMedium%5D%20%5BSolution%5D%20767.%20Reorganize%20String.md)
* [[Medium] [Solution] 738. Monotone Increasing Digits](%5BMedium%5D%20%5BSolution%5D%20738.%20Monotone%20Increasing%20Digits.md)
* [[Easy] [Solution] 874. Walking Robot Simulation](%5BEasy%5D%20%5BSolution%5D%20874.%20Walking%20Robot%20Simulation.md)
* [[Medium] * 1111. Maximum Nesting Depth of Two Valid Parentheses Strings](%5BMedium%5D%20*%201111.%20Maximum%20Nesting%20Depth%20of%20Two%20Valid%20Parentheses%20Strings.md)

## Breadth-first Search <a name="bfs"></a>
---
### BFS
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
* [[Medium] [Solution] 127. Word Ladder](%5BMedium%5D%20%5BSolution%5D%20127.%20Word%20Ladder.md)

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
* [[Medium] 429. N-ary Tree Level Order Traversal](%5BMedium%5D%20429.%20N-ary%20Tree%20Level%20Order%20Traversal.md)

### Bipartite
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
* [[Medium] 785. Is Graph Bipartite?](%5BMedium%5D%20785.%20Is%20Graph%20Bipartite?.md)

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
* [[Medium] 529. Minesweeper](%5BMedium%5D%20529.%20Minesweeper.md)

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
* [[Medium] * 1129. Shortest Path with Alternating Colors](%5BMedium%5D%20*%201129.%20Shortest%20Path%20with%20Alternating%20Colors.md)

### In-degree
```python
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
            course = q.popleft()
            ans.append(course)
            for pre in graph[course]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    q.append(pre)

        return ans if len(ans) == numCourses else []
```
* [[Medium] 210. Course Schedule II](%5BMedium%5D%20210.%20Course%20Schedule%20II.md)

**Template 1:**
```python
seen = [False ...]
q = collections.deque([...])
seen[(...)] = True
while q:
    el = q.popleft()
    seen[el] = True
    ...
    ans ...
    for nei in el's neighbours:
        if not seen[nei]:
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
        seen.add((r, c))
        if ...:
            return step
        for nr, nc in (r, c)'s neighbours:
            if (nr, nc) not in seen:
                q.append((nr, nc))
    step += 1
return -1
```

## Two Pointers <a name="tp"></a>
---
### Cycle
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
* [[Easy] [Solution] 141. Linked List Cycle](%5BEasy%5D%20%5BSolution%5D%20141.%20Linked%20List%20Cycle.md)

### Cycle entrance
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
* [[Medium] [Solution] 287. Find the Duplicate Number](%5BMedium%5D%20%5BSolution%5D%20287.%20Find%20the%20Duplicate%20Number.md)

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
* [[Medium] [Solution] 713. Subarray Product Less Than K](%5BMedium%5D%20%5BSolution%5D%20713.%20Subarray%20Product%20Less%20Than%20K.md)

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
* [[Medium] [Solution] 763. Partition Labels](%5BMedium%5D%20%5BSolution%5D%20763.%20Partition%20Labels.md)

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
* [[Medium] [Solution] 838. Push Dominoes](%5BMedium%5D%20%5BSolution%5D%20838.%20Push%20Dominoes.md)

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
* [[Easy] [Solution] 844. Backspace String Compare](%5BEasy%5D%20%5BSolution%5D%20844.%20Backspace%20String%20Compare.md)

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
* [[Medium] [Solution] 923. 3Sum With Multiplicity](%5BMedium%5D%20%5BSolution%5D%20923.%203Sum%20With%20Multiplicity.md)

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
* [[Easy] [Solution] 925. Long Pressed Name](%5BEasy%5D%20%5BSolution%5D%20925.%20Long%20Pressed%20Name.md)

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
* [[Medium] [Solution] 930. Binary Subarrays With Sum](%5BMedium%5D%20%5BSolution%5D%20930.%20Binary%20Subarrays%20With%20Sum.md)

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
* [[Medium] [Solution] 904. Fruit Into Baskets](%5BMedium%5D%20%5BSolution%5D%20904.%20Fruit%20Into%20Baskets.md)

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
* [[Medium] 1248. Count Number of Nice Subarrays](%5BMedium%5D%201248.%20Count%20Number%20of%20Nice%20Subarrays.md)

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
* [[Medium] 150. Evaluate Reverse Polish Notation](%5BMedium%5D%20150.%20Evaluate%20Reverse%20Polish%20Notation.md)

### Buffer
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
* [[Medium] [Solution] 456. 132 Pattern](%5BMedium%5D%20%5BSolution%5D%20456.%20132%20Pattern.md)

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
* [[Medium] [Solution] 901. Online Stock Span](%5BMedium%5D%20%5BSolution%5D%20901.%20Online%20Stock%20Span.md)

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
* [[Medium] [Solution] 907. Sum of Subarray Minimums](%5BMedium%5D%20%5BSolution%5D%20907.%20Sum%20of%20Subarray%20Minimums.md)

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
* [[Medium] [Solution] 946. Validate Stack Sequences](%5BMedium%5D%20%5BSolution%5D%20946.%20Validate%20Stack%20Sequences.md)

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
* [[Medium] 1130. Minimum Cost Tree From Leaf Values](%5BMedium%5D%201130.%20Minimum%20Cost%20Tree%20From%20Leaf%20Values.md)

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
* [[Medium] 1381. Design a Stack With Increment Operation](%5BMedium%5D%201381.%20Design%20a%20Stack%20With%20Increment%20Operation.md)

### Histogram
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
* [[Hard] 84. Largest Rectangle in Histogram](%5BHard%5D%2084.%20Largest%20Rectangle%20in%20Histogram.md)

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
* [[Hard] [Solution] 32. Longest Valid Parentheses](%5BHard%5D%20%5BSolution%5D%2032.%20Longest%20Valid%20Parentheses.md)

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

* [[Medium] [Solution] 503. Next Greater Element II](%5BMedium%5D%20%5BSolution%5D%20503.%20Next%20Greater%20Element%20II.md)
* [[Medium] [Solution] 636. Exclusive Time of Functions](%5BMedium%5D%20%5BSolution%5D%20636.%20Exclusive%20Time%20of%20Functions.md)

## Backtracking <a name="backtracking"></a>
---
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
* [[Medium] [Solution] 17. Letter Combinations of a Phone Number](%5BMedium%5D%20%5BSolution%5D%2017.%20Letter%20Combinations%20of%20a%20Phone%20Number.md)

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
* [[Medium] 46. Permutations](%5BMedium%5D%2046.%20Permutations.md)

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
```
* [[Medium] [Solution] 78. Subsets](%5BMedium%5D%20%5BSolution%5D%2078.%20Subsets.md)

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
* [[Medium] [Solution] 526. Beautiful Arrangement](%5BMedium%5D%20%5BSolution%5D%20526.%20Beautiful%20Arrangement.md)

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
* [[Medium] [Solution] 842. Split Array into Fibonacci Sequence](%5BMedium%5D%20%5BSolution%5D%20842.%20Split%20Array%20into%20Fibonacci%20Sequence.md)

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
* [[Medium] [Solution] 78. Subsets](%5BMedium%5D%20%5BSolution%5D%2078.%20Subsets.md)

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
* [[Easy] [Solution] 191. Number of 1 Bits](%5BEasy%5D%20%5BSolution%5D%20191.%20Number%20of%201%20Bits.md)

### a xor a = 0, a xor 0 = a
```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
```
* [[Easy] [Solution] 268. Missing Number](%5BEasy%5D%20%5BSolution%5D%20268.%20Missing%20Number.md)

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
* [[Medium] [Solution] 393. UTF-8 Validation](%5BMedium%5D%20%5BSolution%5D%20393.%20UTF-8%20Validation.md)

### Direct
```python
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(bin(x).count('1') in primes
                   for x in range(L, R+1))
```
* [[Easy] [Solution] 762. Prime Number of Set Bits in Binary Representation](%5BEasy%5D%20%5BSolution%5D%20762.%20Prime%20Number%20of%20Set%20Bits%20in%20Binary%20Representation.md)

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
* [[Medium] [Solution] 898. Bitwise ORs of Subarrays](%5BMedium%5D%20%5BSolution%5D%20898.%20Bitwise%20ORs%20of%20Subarrays.md)

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
* [[Medium] 1131. Maximum of Absolute Value Expression](%5BMedium%5D%201131.%20Maximum%20of%20Absolute%20Value%20Expression.md)

### g(n) = "1" + f(n)
```python
class Solution:
    def encode(self, num: int) -> str:
        return bin(num + 1)[3:]
```
* [[Medium] 1256. Encode Number](%5BMedium%5D%201256.%20Encode%20Number.md)

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
* [[Medium] 1177. Can Make Palindrome from Substring](%5BMedium%5D%201177.%20Can%20Make%20Palindrome%20from%20Substring.md)

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
* [[Easy] [Solution] 581. Shortest Unsorted Continuous Subarray](%5BEasy%5D%20%5BSolution%5D%20581.%20Shortest%20Unsorted%20Continuous%20Subarray.md)

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
* [[Medium] [Solution] 56. Merge Intervals](%5BMedium%5D%20%5BSolution%5D%2056.%20Merge%20Intervals.md)

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
* [[Medium] [Solution] 179. Largest Number](%5BMedium%5D%20%5BSolution%5D%20179.%20Largest%20Number.md)

### Heap
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
* [[Medium] [Solution] 524. Longest Word in Dictionary through Deleting](%5BMedium%5D%20%5BSolution%5D%20524.%20Longest%20Word%20in%20Dictionary%20through%20Deleting.md)

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
* [[Medium] 324. Wiggle Sort II](%5BMedium%5D%20324.%20Wiggle%20Sort%20II.md)

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
* [[Medium] 1054. Distant Barcodes](%5BMedium%5D%201054.%20Distant%20Barcodes.md)

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
* [[Medium] 1329. Sort the Matrix Diagonally](%5BMedium%5D%201329.%20Sort%20the%20Matrix%20Diagonally.md)

### DP, Binary Search
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
* [[Hard] 1235. Maximum Profit in Job Scheduling](%5BHard%5D%201235.%20Maximum%20Profit%20in%20Job%20Scheduling.md)

## Linked List <a name="ll"></a>
---
### Elementary Math
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
* [[Medium] [Solution] 2. Add Two Numbers](%5BMedium%5D%20%5BSolution%5D%202.%20Add%20Two%20Numbers.md)

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
* [[Medium] 147. Insertion Sort List](%5BMedium%5D%20147.%20Insertion%20Sort%20List.md)

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
* [[Medium] 148. Sort List](%5BMedium%5D%20148.%20Sort%20List.md)

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
* [[Medium] [Solution] 19. Remove Nth Node From End of List](%5BMedium%5D%20%5BSolution%5D%2019.%20Remove%20Nth%20Node%20From%20End%20of%20List.md)

### Merge with Divide And Conquer
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
```
* [[Hard] [Solution] 23. Merge k Sorted Lists](%5BHard%5D%20%5BSolution%5D%2023.%20Merge%20k%20Sorted%20Lists.md)

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
* [[Medium] 24. Swap Nodes in Pairs](%5BMedium%5D%2024.%20Swap%20Nodes%20in%20Pairs.md)

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
* [[Medium] [Solution] 86. Partition List](%5BMedium%5D%20%5BSolution%5D%2086.%20Partition%20List.md)

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
* [[Medium] [Solution] 109. Convert Sorted List to Binary Search Tree](%5BMedium%5D%20%5BSolution%5D%20109.%20Convert%20Sorted%20List%20to%20Binary%20Search%20Tree.md)

### Hash Table
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
* [[Medium] 138. Copy List with Random Pointer](%5BMedium%5D%20138.%20Copy%20List%20with%20Random%20Pointer.md)

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
* [[Medium] [Solution] 725. Split Linked List in Parts](%5BMedium%5D%20%5BSolution%5D%20725.%20Split%20Linked%20List%20in%20Parts.md)

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
* [[Medium] [Solution] 817. Linked List Components](%5BMedium%5D%20%5BSolution%5D%20817.%20Linked%20List%20Components.md)

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
* [[Medium] 1019. Next Greater Node In Linked List](%5BMedium%5D%201019.%20Next%20Greater%20Node%20In%20Linked%20List.md)

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
* [[Medium] 1171. Remove Zero Sum Consecutive Nodes from Linked List](%5BMedium%5D%201171.%20Remove%20Zero%20Sum%20Consecutive%20Nodes%20from%20Linked%20List.md)

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
* [[Medium] [Solution] 347. Top K Frequent Elements](%5BMedium%5D%20%5BSolution%5D%20347.%20Top%20K%20Frequent%20Elements.md)

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
* [[Medium] [Solution] 659. Split Array into Consecutive Subsequences](%5BMedium%5D%20%5BSolution%5D%20659.%20Split%20Array%20into%20Consecutive%20Subsequences.md)

### Frequency
```python
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
```
* [[Medium] [Solution] 692. Top K Frequent Words](%5BMedium%5D%20%5BSolution%5D%20692.%20Top%20K%20Frequent%20Words.md)

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
* [[Medium] [Solution] 743. Network Delay Time](%5BMedium%5D%20%5BSolution%5D%20743.%20Network%20Delay%20Time.md)

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
* [[Medium] [Solution] 767. Reorganize String](%5BMedium%5D%20%5BSolution%5D%20767.%20Reorganize%20String.md)

### nlargest
```python
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return heapq.nsmallest(K, points, key= lambda x: x[0]**2 + x[1]**2)
```
* [[Medium] [Solution] 973. K Closest Points to Origin](%5BMedium%5D%20%5BSolution%5D%20973.%20K%20Closest%20Points%20to%20Origin.md)

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
* [[Hard] [Solution] 857. Minimum Cost to Hire K Workers](%5BHard%5D%20%5BSolution%5D%20857.%20Minimum%20Cost%20to%20Hire%20K%20Workers.md)

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
* [[Medium] 1405. Longest Happy String](LeetCode/%5BMedium%5D%201405.%20Longest%20Happy%20String.md)

### Most recent min/max
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
* [[Hard] [Solution] 871. Minimum Number of Refueling Stops](%5BHard%5D%20%5BSolution%5D%20871.%20Minimum%20Number%20of%20Refueling%20Stops.md)

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
* [[Hard] [Solution] 864. Shortest Path to Get All Keys](%5BHard%5D%20%5BSolution%5D%20864.%20Shortest%20Path%20to%20Get%20All%20Keys.md)

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
* [[Hard] 218. The Skyline Problem](%5BHard%5D%20218.%20The%20Skyline%20Problem.md)

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
* [[Medium] [Solution] 684. Redundant Connection](%5BMedium%5D%20%5BSolution%5D%20684.%20Redundant%20Connection.md)

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
* [[Medium] [Solution] 959. Regions Cut By Slashes](%5BMedium%5D%20%5BSolution%5D%20959.%20Regions%20Cut%20By%20Slashes.md)

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
* [[Medium] [Solution] 990. Satisfiability of Equality Equations](%5BMedium%5D%20%5BSolution%5D%20990.%20Satisfiability%20of%20Equality%20Equations.md)

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
* [[Hard] [Solution] 803. Bricks Falling When Hit](%5BHard%5D%20%5BSolution%5D%20803.%20Bricks%20Falling%20When%20Hit.md)

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

* [[Hard] [Solution] 924. Minimize Malware Spread](%5BHard%5D%20%5BSolution%5D%20924.%20Minimize%20Malware%20Spread.md)

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
* [[Hard] [Solution] 952. Largest Component Size by Common Factor](%5BHard%5D%20%5BSolution%5D%20952.%20Largest%20Component%20Size%20by%20Common%20Factor.md)

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
### Hash Table as left index
```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        ans = 0
        d = {}
        i = 0
        for j in range(N):
            if d.get(s[j], None):
                i = max(d[s[j]], i)
            ans = max(ans, j - i + 1)
            d[s[j]] = j + 1
        return ans
```
* [[Medium] [Solution] 3. Longest Substring Without Repeating Characters](%5BMedium%5D%20%5BSolution%5D%203.%20Longest%20Substring%20Without%20Repeating%20Characters.md)

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
* [[Medium] [Solution] 978. Longest Turbulent Subarray](%5BMedium%5D%20%5BSolution%5D%20978.%20Longest%20Turbulent%20Subarray.md)

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
* [[Medium] 1004. Max Consecutive Ones III](%5BMedium%5D%201004.%20Max%20Consecutive%20Ones%20III.md)

### Hash Table to keep sliding window
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
* [[Hard] [Solution] 76. Minimum Window Substring](%5BHard%5D%20%5BSolution%5D%2076.%20Minimum%20Window%20Substring.md)

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
* [[Hard] [Solution] 992. Subarrays with K Different Integers](%5BHard%5D%20%5BSolution%5D%20992.%20Subarrays%20with%20K%20Different%20Integers.md)

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
* [[Hard] [Solution] 995. Minimum Number of K Consecutive Bit Flips](%5BHard%5D%20%5BSolution%5D%20995.%20Minimum%20Number%20of%20K%20Consecutive%20Bit%20Flips.md)

### Prefix Sum
```python
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        if not matrix:
            return 0
        
        def num_for_one_row(nums):
            prev = {}
            prev[0] = 1
            cur_sum = 0
            ans = 0
            for num in nums:
                cur_sum += num
                if cur_sum - target in prev:
                    ans += prev[cur_sum - target]
                if cur_sum not in prev:
                    prev[cur_sum] = 1
                else:
                    prev[cur_sum] += 1
            return ans 
        
        res = 0
        R = len(matrix)
        C = len(matrix[0])
        
        for i in range(R):
            col_prefix = [0]*C
            for j in range(i, R):
                for k in range(C):
                    col_prefix[k] += matrix[j][k]
                res += num_for_one_row(col_prefix)
                
        return res
```
* [[Hard] 1074. Number of Submatrices That Sum to Target](%5BHard%5D%201074.%20Number%20of%20Submatrices%20That%20Sum%20to%20Target.md)

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
* [[Medium] 1358. Number of Substrings Containing All Three Characters](%5BMedium%5D%201358.%20Number%20of%20Substrings%20Containing%20All%20Three%20Characters.md)

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
### Merge Sort
```python
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
```

### Quick Sort
```python
# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
```

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
* [[Medium] 241. Different Ways to Add Parentheses](%5BMedium%5D%20241.%20Different%20Ways%20to%20Add%20Parentheses.md)

### DP - Top-down
```python
import functools
class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        @functools.lru_cache(None)
        def dfs(seq, lower, upper):
            max_coins = 0
            for i in range(lower, upper+1):
                coins = seq[lower-1] * seq[i] * seq[upper+1]
                coins += dfs(seq, lower, i-1)
                coins += dfs(seq, i+1, upper)
                if coins > max_coins:
                    max_coins = coins
            return max_coins

        nums_ext = [1] + [num for num in nums if num != 0] + [1]
        N = len(nums_ext) - 2
        return dfs(tuple(nums_ext), 1, N)
```
* [[Hard] 312. Burst Balloons](%5BHard%5D%20312.%20Burst%20Balloons.md)

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
* [[Hard] [Solution] 282. Expression Add Operators](%5BHard%5D%20%5BSolution%5D%20282.%20Expression%20Add%20Operators.md)

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
* [[Hard] [Solution] 493. Reverse Pairs](%5BHard%5D%20%5BSolution%5D%20493.%20Reverse%20Pairs.md)

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
* [[Hard] 327. Count of Range Sum](%5BHard%5D%20327.%20Count%20of%20Range%20Sum.md)

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
* [[Easy] [Solution] 720. Longest Word in Dictionary](%5BEasy%5D%20%5BSolution%5D%20720.%20Longest%20Word%20in%20Dictionary.md)

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
* [[Medium] [Solution] 208. Implement Trie (Prefix Tree)](%5BMedium%5D%20%5BSolution%5D%20208.%20Implement%20Trie%20(Prefix%20Tree).md)

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
* [[Medium] [Solution] 677. Map Sum Pairs](%5BMedium%5D%20%5BSolution%5D%20677.%20Map%20Sum%20Pairs.md)

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
* [[Medium] [Solution] 648. Replace Words](%5BMedium%5D%20%5BSolution%5D%20648.%20Replace%20Words.md)

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
* [[Medium] 421. Maximum XOR of Two Numbers in an Array](%5BMedium%5D%20421.%20Maximum%20XOR%20of%20Two%20Numbers%20in%20an%20Array.md)

### DFS
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
* [[Hard] 212. Word Search II](%5BHard%5D%20212.%20Word%20Search%20II.md)

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
* [[Hard] [Solution] 745. Prefix and Suffix Search](%5BHard%5D%20%5BSolution%5D%20745.%20Prefix%20and%20Suffix%20Search.md)

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
* [[Easy] [Solution] 687. Longest Univalue Path](%5BEasy%5D%20%5BSolution%5D%20687.%20Longest%20Univalue%20Path.md)

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
* [[Medium] [Solution] 698. Partition to K Equal Sum Subsets](%5BMedium%5D%20%5BSolution%5D%20698.%20Partition%20to%20K%20Equal%20Sum%20Subsets.md)

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
* [[Medium] [Solution] 894. All Possible Full Binary Trees](%5BMedium%5D%20%5BSolution%5D%20894.%20All%20Possible%20Full%20Binary%20Trees.md)

## Segment Tree <a name="st"></a>
---
### Range Sum
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

    def update(self, i: int, val: int) -> None:
        pos = i + self.N
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

    def sumRange(self, i: int, j: int) -> int:
        # get leaf with value 'i'
        i += self.N;
        # get leaf with value 'j'
        j += self.N;
        rst = 0
        while i <= j:
            if (i % 2) == 1:
                rst += self.tree[i]
                i += 1
            if (j % 2) == 0:
                rst += self.tree[j]
                j -= 1
            i //= 2
            j //= 2

        return rst



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
```
* [[Medium] [Solution] 307. Range Sum Query - Mutable](%5BMedium%5D%20%5BSolution%5D%20307.%20Range%20Sum%20Query%20-%20Mutable.md)

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
* [[Hard] [Solution] 715. Range Module](%5BHard%5D%20%5BSolution%5D%20715.%20Range%20Module.md)

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
* [[Hard] [Solution] 732. My Calendar III](%5BHard%5D%20%5BSolution%5D%20732.%20My%20Calendar%20III.md)

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
* [[Hard] [Solution] 699. Falling Squares](%5BHard%5D%20%5BSolution%5D%20699.%20Falling%20Squares.md)

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
* [[Hard] [Solution] 850. Rectangle Area II](%5BHard%5D%20%5BSolution%5D%20850.%20Rectangle%20Area%20II.md)

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
* [[Hard] 315. Count of Smaller Numbers After Self](%5BHard%5D%20315.%20Count%20of%20Smaller%20Numbers%20After%20Self.md)

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
* [[Medium] [Solution] 855. Exam Room](%5BMedium%5D%20%5BSolution%5D%20855.%20Exam%20Room.md)

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
* [[Hard] 352. Data Stream as Disjoint Intervals](%5BHard%5D%20352.%20Data%20Stream%20as%20Disjoint%20Intervals.md)

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
* [[Hard] [Solution] 975. Odd Even Jump](%5BHard%5D%20%5BSolution%5D%20975.%20Odd%20Even%20Jump.md)

## Queue <a name="queue"></a>
---
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
* [[Hard] [Solution] 862. Shortest Subarray with Sum at Least K](%5BHard%5D%20%5BSolution%5D%20862.%20Shortest%20Subarray%20with%20Sum%20at%20Least%20K.md)

## Minimax <a name="minimax"></a>
---
### Math
```python
class Solution:
    def canWinNim(self, n: int) -> bool:
        return (n % 4 != 0)
```
* [[Easy] [Solution] 292. Nim Game](%5BEasy%5D%20%5BSolution%5D%20292.%20Nim%20Game.md)

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
* [[Medium] [Solution] 486. Predict the Winner](%5BMedium%5D%20%5BSolution%5D%20486.%20Predict%20the%20Winner.md)

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
* [[Medium] 375. Guess Number Higher or Lower II](%5BMedium%5D%20375.%20Guess%20Number%20Higher%20or%20Lower%20II.md)

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
* [[Hard] [Solution] 843. Guess the Word](%5BHard%5D%20%5BSolution%5D%20843.%20Guess%20the%20Word.md)

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
* [[Hard] [Solution] 913. Cat and Mouse](%5BHard%5D%20%5BSolution%5D%20913.%20Cat%20and%20Mouse.md)

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
* [[Medium] 1288. Remove Covered Intervals](%5BMedium%5D%201288.%20Remove%20Covered%20Intervals.md)

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
* [[Hard] [Solution] 850. Rectangle Area II](%5BHard%5D%20%5BSolution%5D%20850.%20Rectangle%20Area%20II.md)

## Random <a name="random"></a>
---
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
* [[Medium] [Solution] 470. Implement Rand10() Using Rand7()](%5BMedium%5D%20%5BSolution%5D%20470.%20Implement%20Rand10()%20Using%20Rand7().md)

### 2D area, Prefix Sum, Binary Search
```python
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        # number of points in each rectangle
        self.counts = [(x2 - x1 + 1) * (y2 - y1 + 1) 
                       for x1, y1, x2, y2 in rects]

        self.total = sum(self.counts)

        # accumulated (prefix) count of points
        self.accumulate_counts = []
        accumulated = 0
        for count in self.counts:
            accumulated += count
            self.accumulate_counts.append(accumulated)

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
* [[Medium] 497. Random Point in Non-overlapping Rectangles](%5BMedium%5D%20497.%20Random%20Point%20in%20Non-overlapping%20Rectangles.md)

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
* [[Medium] 398. Random Pick Index](%5BMedium%5D%20398.%20Random%20Pick%20Index.md)

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
* [[Hard] 710. Random Pick with Blacklist](%5BHard%5D%20710.%20Random%20Pick%20with%20Blacklist.md)

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
* [[Hard] 329. Longest Increasing Path in a Matrix](%5BHard%5D%20329.%20Longest%20Increasing%20Path%20in%20a%20Matrix.md?_xsrf=2%7Cb607cbb0%7C38c2ab78d0bba728bf04857e61acb0a7%7C1583367857)

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
* [[Hard] 1203. Sort Items by Groups Respecting Dependencies](%5BHard%5D%201203.%20Sort%20Items%20by%20Groups%20Respecting%20Dependencies.md)

## Brainteaser <a name="brainteaser"></a>
---
### State
```python
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n**.5)
```
* [[Medium] 319. Bulb Switcher](%5BMedium%5D%20319.%20Bulb%20Switcher.md)

### Probability
```python
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1 if n == 1 else 0.5
```
* [[Medium] 1227. Airplane Seat Assignment Probability](%5BMedium%5D%201227.%20Airplane%20Seat%20Assignment%20Probability.md)

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
* [[Easy] [Solution] 892. Surface Area of 3D Shapes](%5BEasy%5D%20%5BSolution%5D%20892.%20Surface%20Area%20of%203D%20Shapes.md)

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
* [[Medium] [Solution] 963. Minimum Area Rectangle II](%5BMedium%5D%20%5BSolution%5D%20963.%20Minimum%20Area%20Rectangle%20II.md)

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
* [[Medium] 1401. Circle and Rectangle Overlapping](%5BMedium%5D%201401.%20Circle%20and%20Rectangle%20Overlapping.md)

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
* [[Hard] [Solution] 587. Erect the Fence](%5BHard%5D%20%5BSolution%5D%20587.%20Erect%20the%20Fence.md)

## Regular Expression <a name="re"></a>
---
### Using regex for spliting
```python
class Solution:
    def solveEquation(self, equation: str) -> str:
        def coeff(x):
            if len(x) > 1 and x[len(x) - 2] >= '0' and x[len(x) - 2] <= '9':
                return x.replace('x', '')
            return x.replace('x', '1')

        lr = equation.split('=')
        lhs = 0
        rhs = 0
        for x in re.split(r"(?=\+)|(?=-)", lr[0]):
            if x.find('x') >= 0:
                lhs += int(coeff(x))
            else:
                rhs -= int(x) if x != '' else 0
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
* [[Medium] [Solution] 640. Solve the Equation](%5BMedium%5D%20%5BSolution%5D%20640.%20Solve%20the%20Equation.md)

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
* [[Medium] 468. Validate IP Address](%5BMedium%5D%20468.%20Validate%20IP%20Address.md)

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
* [[Hard] [Solution] 726. Number of Atoms](%5BHard%5D%20%5BSolution%5D%20726.%20Number%20of%20Atoms.md)
