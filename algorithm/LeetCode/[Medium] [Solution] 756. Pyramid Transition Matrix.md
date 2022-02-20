756. Pyramid Transition Matrix

We are stacking blocks to form a pyramid. Each block has a color which is a one letter string.

We are allowed to place any color block `C` on top of two adjacent blocks of colors `A` and `B`, if and only if `ABC` is an allowed triple.

We start with a `bottom` row of bottom, represented as a single string. We also start with a list of allowed triples `allowed`. Each allowed triple is represented as a string of length `3`.

Return `true` if we can build the pyramid all the way to the top, otherwise `false`.

**Example 1:**
```
Input: bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]
Output: true
Explanation:
We can stack the pyramid like this:
    A
   / \
  G   E
 / \ / \
B   C   D

We are allowed to place G on top of B and C because BCG is an allowed triple.  Similarly, we can place E on top of C and D, then A on top of G and E.
```

**Example 2:**
```
Input: bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
Output: false
Explanation:
We can't stack the pyramid to the top.
Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.
```

**Note:**

* `bottom` will be a string with length in range `[2, 8]`.
* `allowed` will have length in range `[0, 200]`.
* Letters in all strings will be chosen from the set `{'A', 'B', 'C', 'D', 'E', 'F', 'G'}`.

# Solution
---
## Approach #1: State to State Transition [Wrong Answer]
**Intuition and Algorithm**

We model the states that blocks can be in. Each state is a binary number where the `k`th bit is set if the `k`th type of block is a possibility. Then, we create a transition map `T[state1][state2] -> state` that takes a left state and a right state and outputs all possible parent states.

At the end, applying these transitions is straightforward. However, this approach is not correct, because the transitions are not independent. If for example we have states in a row `A, {B or C}, A`, and allowed triples `(A, B, D), (C, A, D)`, then regardless of the choice of {`B` or `C`} we cannot create the next row of the pyramid.

```python
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        T = [[0] * (1 << 7) for _ in xrange(1 << 7)]
        for triple in allowed:
            u, v, w = (1 << (ord(x) - ord('A')) for x in triple)
            for b1 in xrange(1 << 7):
                if u & b1:
                    for b2 in xrange(1 << 7):
                        if v & b2:
                            T[b1][b2] |= w

        state = [1 << (ord(x) - ord('A')) for x in bottom]
        while len(state) > 1:
            for i in xrange(len(state) - 1):
                state[i] = T[state[i]][state[i+1]]
            state.pop()
        return bool(state[0])
```

**Complexity Analysis**

* Time Complexity: $O(2^{2\mathcal{A}}A + N^2)$, where $N$ is the length of bottom, $A$ is the length of allowed, and $\mathcal{A}$ is the size of the alphabet.

* Space Complexity: $O(2^{2\mathcal{A}})$ in additional space complexity.

## Approach #2: Depth-First Search [Accepted]
**Intuition**

We exhaustively try every combination of blocks.

**Algorithm**

We can work in either strings or integers, but we need to create a transition map `T` from the list of allowed triples. This map `T[x][y] = {set of z}` will be all possible parent blocks for a left child of `x` and a right child of `y`. When we work in strings, we use `Set`, and when we work in integers, we will use the set bits of the result integer.

Afterwards, to `solve` a row, we generate every possible combination of the next row and solve them. If any of those new rows are solvable, we return `True`, otherwise `False`.

We can also cache intermediate results, saving us time. This is illustrated in the comments for Python. For Java, all caching is done with lines of code that mention the integer `R`.

```python
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
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

**Complexity Analysis**

* Time Complexity: $O(\mathcal{A}^{N})$, where $N$ is the length of bottom, and $\mathcal{A}$ is the size of the alphabet, and assuming we cache intermediate results. We might try every sequence of letters for each row. [The total complexity is because $O(\sum_{k}^n \mathcal{A}^{k})$ is a geometric series equal to $O(\frac{\mathcal{A^{n+1}}-1}{\mathcal{A}-1})$.] Without intermediate caching, this would be $O(\mathcal{A}^{N^2})$.

* Space Complexity: $O(N^2)$ additional space complexity.

# Submissions
---
**Solution:**
```
Runtime: 32 ms
Memory Usage: 12.6 MB
```
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

**Solution 1: (DFS)**
```
Runtime: 0 ms
Memory Usage: 8.1 MB
```
```c++
class Solution {
public:
    bool pyramidTransition(string bottom, vector<string>& allowed) {
        unordered_map<string, vector<char>> mapping;
        for (const string& s : allowed)
        {
            mapping[s.substr(0, 2)].push_back(s[2]);
        }

        return dfs(bottom, "", mapping);
    }
    
private:
    unordered_map<string, bool> memo;
    bool dfs(string bottom, string top, unordered_map<string, vector<char>>& mapping)
    {
        if (bottom.size() == 2 && top.size() == 1)
        {
            return true;
        }
        
        if (memo.count(bottom))
            return memo[bottom];
        
        if (bottom.size() - top.size() == 1)
        {
            bool result = dfs(top, "", mapping);
            memo[top] = result;
            return result;
        }
        
        string sub = bottom.substr(top.size(), 2);
        if (mapping.count(sub) == 0)
            return false;
        
        for (char c : mapping[sub])
        {
            bool result = dfs(bottom, top + c, mapping);
            if (result)
            {
                memo[bottom] = true;
                return true;
            }
                
        }
        
        memo[bottom] = false;
        return false;
    }
};
```
