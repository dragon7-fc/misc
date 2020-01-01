851. Loud and Rich

In a group of `N` people (labelled `0, 1, 2, ..., N-1`), each person has different amounts of money, and different levels of quietness.

For convenience, we'll call the person with label `x`, simply "person x".

We'll say that `richer[i] = [x, y]` if person `x` definitely has more money than person `y`.  Note that richer may only be a subset of valid observations.

Also, we'll say `quiet[x] = q` if person `x` has quietness `q`.

Now, return `answer`, where `answer[x] = y` if `y` is the least quiet person (that is, the person `y` with the smallest value of `quiet[y]`), among all people who definitely have equal to or more money than person `x`.

 

**Example 1:**
```
Input: richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
Output: [5,5,2,5,4,5,6,7]
Explanation: 
answer[0] = 5.
Person 5 has more money than 3, which has more money than 1, which has more money than 0.
The only person who is quieter (has lower quiet[x]) is person 7, but
it isn't clear if they have more money than person 0.

answer[7] = 7.
Among all people that definitely have equal to or more money than person 7
(which could be persons 3, 4, 5, 6, or 7), the person who is the quietest (has lower quiet[x])
is person 7.

The other answers can be filled out with similar reasoning.
```

**Note:**

* `1 <= quiet.length = N <= 500`
* `0 <= quiet[i] < N`, all `quiet[i]` are different.
* `0 <= richer.length <= N * (N-1) / 2`
* `0 <= richer[i][j] < N`
* `richer[i][0] != richer[i][1]`
* `richer[i]`'s are all different.
* The observations in richer are all logically consistent.

# Solution
---
## Approach #1: Cached Depth-First Search [Accepted]
**Intuition**

Consider the directed graph with edge `x -> y` if `y` is richer than `x`.

For each person `x`, we want the quietest person in the subtree at `x`.

**Algorithm**

Construct the graph described above, and say `dfs(person)` is the quietest person in the subtree at person. Notice because the statements are logically consistent, the graph must be a DAG - a directed graph with no cycles.

Now `dfs(person)` is either person, or `min(dfs(child)` for child in person). That is to say, the quietest person in the subtree is either the person itself, or the quietest person in some subtree of a child of person.

We can cache values of `dfs(person)` as `answer[person]`, when performing our post-order traversal of the graph. That way, we don't repeat work. This technique reduces a quadratic time algorithm down to linear time.

```python
class Solution(object):
    def loudAndRich(self, richer, quiet):
        N = len(quiet)
        graph = [[] for _ in xrange(N)]
        for u, v in richer:
            graph[v].append(u)

        answer = [None] * N
        def dfs(node):
            #Want least quiet person in this subtree
            if answer[node] is None:
                answer[node] = node
                for child in graph[node]:
                    cand = dfs(child)
                    if quiet[cand] < quiet[answer[node]]:
                        answer[node] = cand
            return answer[node]

        return map(dfs, range(N))
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the number of people.

* Space Complexity: $O(N)$, the space used by the answer, and the implicit call stack of `dfs`.

# Submissions
---
**Solution:**
```
Runtime: 476 ms
Memory Usage: 22.5 MB
```
```python
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        N = len(quiet)
        graph = [[] for _ in range(N)]
        for u, v in richer:
            graph[v].append(u)

        answer = [None] * N
        def dfs(node):
            #Want least quiet person in this subtree
            if answer[node] is None:
                answer[node] = node
                for child in graph[node]:
                    cand = dfs(child)
                    if quiet[cand] < quiet[answer[node]]:
                        answer[node] = cand
            return answer[node]

        return map(dfs, range(N))
```