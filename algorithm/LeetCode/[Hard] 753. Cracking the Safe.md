753. Cracking the Safe

There is a box protected by a password. The password is a sequence of `n` digits where each digit can be one of the first `k` digits `0, 1, ..., k-1`.

While entering a password, the last `n` digits entered will automatically be matched against the correct password.

For example, assuming the correct password is `"345"`, if you type `"012345"`, the box will open because the correct password matches the suffix of the entered password.

Return any password of minimum length that is guaranteed to open the box at some point of entering it.

 

**Example 1:**
```
Input: n = 1, k = 2
Output: "01"
Note: "10" will be accepted too.
```

**Example 2:**
```
Input: n = 2, k = 2
Output: "00110"
Note: "01100", "10011", "11001" will be accepted too.
```

**Note:**

* `n` will be in the range `[1, 4]`.
* `k` will be in the range `[1, 10]`.
* `k^n` will be at most `4096`.

# Solution
---
## Approach #1: Hierholzer's Algorithm [Accepted]
**Intuition**

We can think of this problem as the problem of finding an Euler path (a path visiting every edge exactly once) on the following graph: there are $k^{n-1}$ nodes with each node having $k$ edges.

For example, when `k = 4, n = 3`, the nodes are `'00', '01', '02', ..., '32', '33'` and each node has `4` edges `'0', '1', '2', '3'`. A node plus edge represents a complete edge and viewing that substring in our answer.

Any connected directed graph where all nodes have equal in-degree and out-degree has an Euler circuit (an Euler path ending where it started.) Because our graph is highly connected and symmetric, we should expect intuitively that taking any path greedily in some order will probably result in an Euler path.

This intuition is called Hierholzer's algorithm: whenever there is an Euler cycle, we can construct it greedily. The algorithm goes as follows:

* Starting from a vertex `u`, we walk through (unwalked) edges until we get stuck. Because the in-degrees and out-degrees of each node are equal, we can only get stuck at `u`, which forms a cycle.

* Now, for any node `v` we had visited that has unwalked edges, we start a new cycle from `v` with the same procedure as above, and then merge the cycles together to form a new cycle $u \rightarrow \dots \rightarrow v \rightarrow \dots \rightarrow v \rightarrow \dots \rightarrow u$.

**Algorithm**

We will modify our standard depth-first search: instead of keeping track of nodes, we keep track of (complete) edges: seen records if an edge has been visited.

Also, we'll need to visit in a sort of "post-order", recording the answer after visiting the edge. This is to prevent getting stuck. For example, with `k = 2, n = 2`, we have the nodes `'0', '1'`. If we greedily visit complete edges `'00', '01', '10'`, we will be stuck at the node `'0'` prematurely. However, if we visit in post-order, we'll end up visiting `'00', '01', '11', '10'` correctly.

In general, during our Hierholzer walk, we will record the results of other subcycles first, before recording the main cycle we started from, just as in our first description of the algorithm. Technically, we are recording backwards, as we exit the nodes.

For example, we will walk (in the "original cycle") until we get stuck, then record the node as we exit. (Every edge walked is always marked immediately so that it can no longer be used.) Then in the penultimate node of our original cycle, we will do a Hierholzer walk and then record this node; then in the third-last node of our original cycle we will do a Hierholzer walk and then record this node, and so on.

```python
class Solution(object):
    def crackSafe(self, n, k):
        seen = set()
        ans = []
        def dfs(node):
            for x in map(str, range(k)):
                nei = node + x
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei[1:])
                    ans.append(x)

        dfs("0" * (n-1))
        return "".join(ans) + "0" * (n-1)
```

**Complexity Analysis**

* Time Complexity: $O(n * k^n)$. We visit every edge once in our depth-first search, and nodes take $O(n)$ space.

* Space Complexity: $O(n * k^n)$, the size of `seen`.

## Approach #2: Inverse Burrows-Wheeler Transform [Accepted]
**Explanation**

If we are familiar with the theory of combinatorics on words, recall that a Lyndon Word `L` is a word that is the unique minimum of it's rotations.

One important mathematical result (due to Fredericksen and Maiorana), is that the concatenation in lexicographic order of Lyndon words with length dividing `n`, forms a de Bruijin sequence: a sequence where every word (from the $k^n$ available) appears as a substring of length `n` (where we are allowed to wrap around.)

For example, when `n = 6, k = 2`, all the Lyndon words with length dividing `n` in lexicographic order are (spaces for convenience): `0 000001 000011 000101 000111 001 001011 001101 001111 01 010111 011 011111 1`. It turns out this is the smallest de Bruijin sequence.

We can use the Inverse Burrows-Wheeler Transform (IBWT) to generate these Lyndon words. Consider two sequences: `S` is the alphabet repeated $k^{n-1}$ times: `S = 0123...0123...0123....`, and `S'` is the alphabet repeated $k^{n-1}$ times for each letter: `S' = 00...0011...1122....` We can think of `S'` and `S` as defining a permutation, where the `j`-th occurrence of each letter of the alphabet in `S'` maps to the corresponding `j`-th occurrence in `S`. The cycles of this permutation turn out to be the corresponding smallest de Bruijin sequence (link).

Under this view, the permutation $S' \rightarrow S$ [mapping permutation indices $(i * k^{n-1} + q) \rightarrow (q * k + i)$ form the desired Lyndon words.

```python
class Solution(object):
    def crackSafe(self, n, k):
        M = k**(n-1)
        P = [q*k+i for i in xrange(k) for q in xrange(M)]
        ans = []

        for i in xrange(k**n):
            j = i
            while P[j] >= 0:
                ans.append(str(j / M))
                P[j], j = -1, P[j]

        return "".join(ans) + "0" * (n-1)
```

**Complexity Analysis**

* Time Complexity: $O(k^n)$. We loop through every possible substring.

* Space Complexity: $O(k^n)$, the size of `P` and `ans`.

# Submissions
---
**Solution 1: (Hierholzer's Algorithm)**
```
Runtime: 48 ms
Memory Usage: 19.9 MB
```
```python
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        seen = set()
        ans = []
        def dfs(node):
            for x in map(str, range(k)):
                nei = node + x
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei[1:])
                    ans.append(x)

        dfs("0" * (n-1))
        return "".join(ans) + "0" * (n-1)
```

**Solution 2: (Inverse Burrows-Wheeler Transform)**
```
Runtime: 28 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        M = k**(n-1)
        P = [q*k+i for i in range(k) for q in range(M)]
        ans = []

        for i in range(k**n):
            j = i
            while P[j] >= 0:
                ans.append(str(j // M))
                P[j], j = -1, P[j]

        return "".join(ans) + "0" * (n-1)
```

**Solution 3: (Backtracking, try Euler Path)**
```
Runtime: 10 ms, Beats 63.92%
Memory: 12.73 MB, Beats 52.58%
```
```c++
\class Solution {
    bool bt(int n, int k, int r, unordered_set<string> &visited, string &ans) {
        if (r == 0) {
            return true;
        }
        string pre;
        for (char a = '0'; a < '0' + k; a ++) {
            pre = ans.substr(ans.length()-n+1) + a;
            if (!visited.count(pre)) {
                visited.insert(pre);
                ans += a;
                if (bt(n, k, r-1, visited, ans)) {
                    return true;
                }
                ans.pop_back();
                visited.erase(pre);
            }
            pre.pop_back();
        }
        return false;
    }
public:
    string crackSafe(int n, int k) {
        unordered_set<string> visited;
        string ans(n-1, '0');
        bt(n, k, pow(k,n), visited, ans);
        return ans;
    }
};
```
