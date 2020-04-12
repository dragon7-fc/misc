943. Find the Shortest Superstring

Given an array `A` of strings, find any smallest string that contains each string in `A` as a substring.

We may assume that no string in `A` is substring of another string in `A`.

 
**Example 1:**
```
Input: ["alex","loves","leetcode"]
Output: "alexlovesleetcode"
Explanation: All permutations of "alex","loves","leetcode" would also be accepted.
```

**Example 2:**
```
Input: ["catg","ctaagt","gcta","ttca","atgcatc"]
Output: "gctaagttcatgcatc"
``` 

**Note:**

* `1 <= A.length <= 12`
* `1 <= A[i].length <= 20`

# Solution
---
## Approach 1: Dynamic Programming
**Intuition**

We have to put the words into a row, where each word may overlap the previous word. This is because no word is contained in any word.

Also, it is sufficient to try to maximize the total overlap of the words.

Say we have put some words down in our row, ending with word `A[i]`. Now say we put down word `A[j]` as the next word, where word `j` hasn't been put down yet. The overlap increases by `overlap(A[i], A[j])`.

We can use dynamic programming to leverage this recursion. Let `dp(mask, i)` be the total overlap after putting some words down (represented by a bitmask `mask`), for which `A[i]` was the last word put down. Then, the key recursion is `dp(mask ^ (1<<j), j) = max(overlap(A[i], A[j]) + dp(mask, i))`, where the `j`th bit is not set in mask, and `i` ranges over all bits set in mask.

Of course, this only tells us what the maximum overlap is for each set of words. We also need to remember each choice along the way (ie. the specific `i` that made `dp(mask ^ (1<<j), j)` achieve a minimum) so that we can reconstruct the answer.

**Algorithm**

Our algorithm has 3 main components:

* Precompute `overlap(A[i], A[j])` for all possible `i`, `j`.
* Calculate `dp[mask][i]`, keeping track of the "parent" `i` for each `j` as described above.
* Reconstruct the answer using parent information.

Please see the implementation for more details about each section.

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

**Complexity Analysis**

* Time Complexity: $O(N^2 (2^N + W))$, where $N$ is the number of words, and $W$ is the maximum length of each word.

* Space Complexity: $O(N (2^N + W))$.

# Submissions
---
**Solution 1: (Dynamic Programming)**
```
Runtime: 528 ms
Memory Usage: 14.9 MB
```
```python
class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        N = len(A)

        # Populate overlaps
        overlaps = [[0] * N for _ in range(N)]
        for i, x in enumerate(A):
            for j, y in enumerate(A):
                if i != j:
                    for ans in range(min(len(x), len(y)), -1, -1):
                        if x.endswith(y[:ans]):
                            overlaps[i][j] = ans
                            break

        # dp[mask][i] = most overlap with mask, ending with ith element
        dp = [[0] * N for _ in range(1<<N)]
        parent = [[None] * N for _ in range(1<<N)]
        for mask in range(1, 1 << N):
            for bit in range(N):
                if (mask >> bit) & 1:
                    # Let's try to find dp[mask][bit].  Previously, we had
                    # a collection of items represented by pmask.
                    pmask = mask ^ (1 << bit)
                    if pmask == 0: continue
                    for i in range(N):
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
        i = max(range(N), key = dp[-1].__getitem__)
        while i is not None:
            perm.append(i)
            mask, i = mask ^ (1<<i), parent[mask][i]

        # Reverse path to get forwards direction; add all remaining words
        perm = perm[::-1]
        seen = [False] * N
        for x in perm:
            seen[x] = True
        perm.extend([i for i in range(N) if not seen[i]])

        # Reconstruct answer given perm = word indices in left to right order
        ans = [A[perm[0]]]
        for i in range(1, len(perm)):
            overlap = overlaps[perm[i-1]][perm[i]]
            ans.append(A[perm[i]][overlap:])

        return "".join(ans)
```

**Solution 2: (DP Top-Down)**

Many thanks to @ygt2016. The original code is here. I converted the code to recursion, which might be a little easier to understand. Hope this is helpful.
The general idea is:

1. Build a (dense) graph whose node `i` is the `i`th word in `A`. The weight on the arc `i-->j` is `graph[i][j]`, representing the length of the overlapping part between `A[i]` and `A[j]`.
1. Then, our goal is to find an ordering of the words (nodes) 0,1,2,...,n-1 such that when the words are concatenated in this order, the total length is the smallest. Define the state as `(i,k)`, where `i` is a number whose binary form indicates which nodes are included in the ordering; `k` denotes the last node in the ordering. Let `memo[i,k]` be the shortest superstring when concatenating the words represented by the bits in `i` and with `k` as the last word. (You may call `memo` as dp, if you want.)
1. The recursion part is `memo[i,k]=min(i ^ (1 << k), j)`, for all the bits `j` in the ordering `i` excluding `k` itself.
1. Finally, what we are looking for is just the best result within `memo[(i << n) - 1, k]`, for all the `k` in `{0,1,2,...,n-1}`.

```
Runtime: 1268 ms
Memory Usage: 55.4 MB
```
```python
class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        n = len(A)
        # Building the graph
        graph = [[0] * n for _ in range(n)]
        for i, word1 in enumerate(A):
            for j, word2 in enumerate(A):
                if i == j: continue
                for k in range(min(len(word1), len(word2)))[::-1]:
                    if word1[-k:] == word2[:k]:
                        graph[i][j] = k
                        break
        
        # Recursion. i is a mask to represent the ordering. k is the last node in the ordering.
        memo = {}
        def search(i, k):
            if (i, k) in memo: return memo[i, k]
            if not (i & (1 << k)): return ''
            if i == (1 << k): return A[k]
            memo[i, k] = ''
            for j in range(n):
                if j != k and i & (1 << j):
                    candidate = search(i ^ (1 << k), j) + A[k][graph[j][k]:]
                    if memo[i, k] == '' or len(candidate) < len(memo[i, k]):
                        memo[i, k] = candidate
            return memo[i, k]
        
        # Finding the best
        res = ''
        for k in range(n):
            candidate = search((1 << n) - 1, k)
            if res == '' or len(candidate) < len(res):
                res = candidate
        return res
```

**Solution 3: (Dijkstra's)**
```
Runtime: 640 ms
Memory Usage: 20.1 MB
```
```python
class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        """
        Intuitively, the shortest super string exploits the common grounds 
        shared among the given words, therefore minimizing the repetition of the 
        shared substrings. Viewing each word as a vertex in a graph, we can 
        construct a weighted directed graph in which each edge is the common 
        substring shared between a pair of words - the shared substring is the 
        suffix and prefix of the source and destination of the edge, 
        respectively, and its length is the weight. Words do not share anything 
        has an edge between each other with zero weight, so the graph is fully 
        connected. Our goal is to find the shortest hamilton path in the graph. 

        To find the shortest path, we can use Dijkstra's shortest path algorithm 
        - we start from an empty string and keep concatenating it with the given 
        words until all the words are concatenated; the concatenation merges 
        any common substring shared between two given strings in order to reduce 
        the string length; the algorithm opts for the shortest concatenation at 
        each step, and as a result, the first concatenation that includes all 
        the given words is guaranteed shortest. 

        In implementation, since the edge weights are not given directly but
        calculated by comparing the given words pairwise, which takes O(n^2) 
        time. Repeating the calculation is obviously unwise, but memoizing the 
        weights can avoid the repetitive calculations and thus save time. 
        """

        @lru_cache(None)
        def concat(i, j):
            """
            Concatenate two words at given indices and return the length of the 
            shared substring. The results are cached for reuse. 
            """
            a, b = A[i], A[j]
            for r in range(len(b) - 1, -1, -1):
                if a.endswith(b[:r]):
                    return r
            return 0
        
        n = len(A)        
        # mask the state wherein all the words are included
        end = (1<<n) - 1
        # a visit set to avoid cycles 
        visited = set()

        # add an empty string to the min heap first as the kickstart for the 
        # exhaustive search for the shortest path. The heap uses the length of 
        # the concatenated string as the key.
        heap = [(0, '', 0, -1, -1)]
        while heap:
            length, ss, state, head, tail = heappop(heap)
            # when all the words are concatenated, the current string must be 
            # the shortest one, since the heap uses the length of the 
            # concatenated string as the key and thus we always visit the 
            # shortest string first for every state. 
            if state == end:
                return ss
            
            # cycle detection and avoidance
            if state in visited:
                continue
            visited.add(state)
            
            for i, s in enumerate(A):
                # check if the word has been included
                if state&(1<<i):
                    continue
                # set the bit for current index as the next state
                next_state = state|(1<<i)
                if head == -1:
                    heappush(heap, (len(s), s, next_state, i, i))
                else:
                    # the word can be concatenated in both ends, resulting 
                    # different concatenations
                    a, b = concat(tail, i), concat(i, head)
                    # concate the strings properly
                    sa, sb = ss + (s[a:] if a else s), (s[:len(s) - b] if b else s) + ss
                    # move to next step
                    heappush(heap, (len(sa), sa, next_state, head, i))
                    heappush(heap, (len(sb), sb, next_state, i, tail))
```