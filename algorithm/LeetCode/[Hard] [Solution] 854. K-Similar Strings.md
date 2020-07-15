854. K-Similar Strings

Strings `A` and `B` are K-similar (for some non-negative integer `K`) if we can swap the positions of two letters in `A` exactly `K` times so that the resulting string equals `B`.

Given two anagrams `A` and `B`, return the smallest `K` for which `A` and `B` are `K`-similar.

**Example 1:**
```
Input: A = "ab", B = "ba"
Output: 1
```

**Example 2:**
```
Input: A = "abc", B = "bca"
Output: 2
```

**Example 3:**
```
Input: A = "abac", B = "baca"
Output: 2
```

**Example 4:**
```
Input: A = "aabc", B = "abca"
Output: 2
```

**Note:**

* `1 <= A.length == B.length <= 20`
* `A` and `B` contain only lowercase letters from the set `{'a', 'b', 'c', 'd', 'e', 'f'}`

# Solution
---
## Approach Framework
**Explanation**

We'll call the underlying graph of the problem, the graph with 6 nodes `'a', 'b', ..., 'f'` and the edges `A[i] -> B[i]`. Our goal is for this graph to have only self-edges (edges of the form `a -> a`.) Let's make some deductions about how swaps between `A[i]` and `A[j]` affect this graph, and the nature of optimal swap schedules.

If `A = 'ca...'` and `B = 'ab...'`, then the first two edges of the underlying graph are `c -> a` and `a -> b`; and a swap between `A[1]` and `A[0]` changes these two edges to the single edge `c -> b`. Let's call this type of operation 'cutting corners'. Intuitively, our optimal swap schedule always increases the number of matches (`A[i] == B[i]`s) for each swap, so cutting corners is the only type of operation we need to consider. (This is essentially the happy swap assumption, proved in 765 - Couples Holding Hands)

Now consider any cycle decomposition of the underlying graph. [This decomposition (or the number of cycles), is not necessarily unique.] Through operations of cutting corners, we'll delete all the (non-self) edges. Each cycle of length k requires k-1 operations to delete. Thus, the answer is just the minimum possible value of $\sum (C_k - 1)$, where $C_1, \cdots C_k$ are the lengths of the cycles in some cycle decomposition of the underlying graph. This can be re-written as $\text{(Number of non-self edges)}$ - $\text{(Number of cycles)}$. Hence, we want to maximize the number of cycles in a cycle decomposition of the underlying graph.


## Approach 1: Brute Force with Dynamic Programming
**Intuition and Algorithm**

Let $P_1, P_2, \cdots$ be possible cycles of the underlying graph $G$. Let's attempt to write $G = \sum k_i P_i$ for some constants $k_i$. Then, the number of cycles is $\sum k_i$.

We can represent $G$ and $P_i$ as the number of directed edges from node $X$ to $Y$. For example, if $P_1$ is the cycle a -> b -> d -> e -> a, then $P_1$ is a -> b plus b -> d plus d -> e plus e -> a. This can be represented as a column vector possibles[0] of 1s and 0s, with four 1s, (each possibles[0][i] == 1 represents the ith directed edge being there [and having quantity 1]). Similarly, the graph $G$ can also be represented as a column vector.

This sets the stage for dynamic programming. For each graph $G$, represented as a column vector, say we want to find numCycles(G). We can take all possible cycles $C$, and check if $G$ contains CC. If it does, then a candidate answer is 1 + numCycles(G - C).

It should also be noted that maximizing the number of cycles cannot be done in a greedy way, ie. by always removing the lowest size cycle. For example, consider the graph with edges a -> b -> c -> a, b -> d -> e -> b, and c -> e -> f -> c. Those form cycles, and there is a fourth 3-cycle b -> c -> e -> b. If we remove that cycle first, then we would have only two cycles; but if we remove the first 3 cycles, then we would have three cycles.

```python
class Solution(object):
    def kSimilarity(self, A, B):
        if A == B: return 0

        N = len(A)
        alphabet = 'abcdef'
        pairs = [(a, b) for a in alphabet for b in alphabet if a != b]
        index = {p: i for i, p in enumerate(pairs)}

        count = [0] * len(index)
        for a, b in itertools.izip(A, B):
            if a != b:
                count[index[a, b]] += 1

        seen = set()
        for size in xrange(2, len(alphabet) + 1):
            for cand in itertools.permutations(alphabet, size):
                i = cand.index(min(cand))
                seen.add(cand[i:] + cand[:i])

        possibles = []
        for cand in seen:
            row = [0] * len(alphabet) * (len(alphabet) - 1)
            for a, b in itertools.izip(cand, cand[1:] + cand[:1]):
                row[index[a, b]] += 1
            possibles.append(row)

        ZERO = tuple([0] * len(row))
        memo = {ZERO: 0}
        def solve(count):
            if count in memo: return memo[count]

            ans = float('-inf')
            for row in possibles:
                count2 = list(count)
                for i, x in enumerate(row):
                    if count2[i] >= x:
                        count2[i] -= x
                    else: break
                else:
                    ans = max(ans, 1 + solve(tuple(count2)))

            memo[count] = ans
            return ans

        return sum(count) - solve(tuple(count))
```

**Complexity Analysis**

* Time Complexity: $O(2^{N+W})$, where $N$ is the length of the string, and $W$ is the length of the alphabet.

* Space Complexity: $O(2^{N+W})$.

## Approach 2: Pruned Breadth First Search
**Intuition**

Based on the underlying graph interpretation of the problem, we can prove that an optimal solution swaps the left-most unmatched character A[i] with an appropriate match A[j] == B[i] (j > i).

This reduces the number of "neighbors" of a node (string state) from $O(N^2)$ to $O(N)$, but it also focuses our search greatly. Each node searched with k matches, will have at most $2^k$ swaps on the unmatched characters. This leads to $\sum_k \binom{N}{k} 2^k = 3^N$ checked states. Furthermore, some characters are the same, so we must divide the number of states by approximate factors of $\prod (N_i)!$ [where $N_i$ is the number of occurrences of the iith character in A.] With $N \leq 20$, this means the number of states will be small.

**Algorithm**

We'll perform a regular breadth-first search. The neighbors to each node string S are all the strings reachable with 1 swap, that match the first unmatched character in `S`.

```python
class Solution(object):
    def kSimilarity(self, A, B):
        def neighbors(S):
            for i, c in enumerate(S):
                if c != B[i]:
                    break

            T = list(S)
            for j in xrange(i+1, len(S)):
                if S[j] == B[i]:
                    T[i], T[j] = T[j], T[i]
                    yield "".join(T)
                    T[j], T[i] = T[i], T[j]

        queue = collections.deque([A])
        seen = {A: 0}
        while queue:
            S = queue.popleft()
            if S == B: return seen[S]
            for T in neighbors(S):
                if T not in seen:
                    seen[T] = seen[S] + 1
                    queue.append(T)
```

**Complexity Analysis**

* Time Complexity: $O(\sum_{k=0}^n \binom{N}{k} \frac{\min(2^k, (N-k)!)}{W * (\frac{N-k}{W})!})$, where $N$ is the length of the string, and $W$ is the length of the alphabet.

* Space Complexity: $O(N * t)$, where $t$ is the time complexity given above.

# Submissions
---
**Solution 1: (Brute Force with Dynamic Programming)**
```
Runtime: 3572 ms
Memory Usage: 16.6 MB
```
```python
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        if A == B: return 0

        N = len(A)
        alphabet = 'abcdef'
        pairs = [(a, b) for a in alphabet for b in alphabet if a != b]
        index = {p: i for i, p in enumerate(pairs)}

        count = [0] * len(index)
        for a, b in zip(A, B):
            if a != b:
                count[index[a, b]] += 1

        seen = set()
        for size in range(2, len(alphabet) + 1):
            for cand in itertools.permutations(alphabet, size):
                i = cand.index(min(cand))
                seen.add(cand[i:] + cand[:i])

        possibles = []
        for cand in seen:
            row = [0] * len(alphabet) * (len(alphabet) - 1)
            for a, b in zip(cand, cand[1:] + cand[:1]):
                row[index[a, b]] += 1
            possibles.append(row)

        ZERO = tuple([0] * len(row))
        memo = {ZERO: 0}
        def solve(count):
            if count in memo: return memo[count]

            ans = float('-inf')
            for row in possibles:
                count2 = list(count)
                for i, x in enumerate(row):
                    if count2[i] >= x:
                        count2[i] -= x
                    else: break
                else:
                    ans = max(ans, 1 + solve(tuple(count2)))

            memo[count] = ans
            return ans

        return sum(count) - solve(tuple(count))
```

**Solution 2: (Pruned Breadth First Search)**
```
Runtime: 736 ms
Memory Usage: 21.1 MB
```
```python
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        def neighbors(S):
            for i, c in enumerate(S):
                if c != B[i]:
                    break

            T = list(S)
            for j in range(i+1, len(S)):
                if S[j] == B[i]:
                    T[i], T[j] = T[j], T[i]
                    yield "".join(T)
                    T[j], T[i] = T[i], T[j]

        queue = collections.deque([A])
        seen = {A: 0}
        while queue:
            S = queue.popleft()
            if S == B: return seen[S]
            for T in neighbors(S):
                if T not in seen:
                    seen[T] = seen[S] + 1
                    queue.append(T)

```

**Solution 3: (BFS)**
```
Runtime: 652 ms
Memory Usage: 143 MB
```
```c++
class Solution {
public:
    int kSimilarity(string A, string B) {
        if(A == B){return 0;}
        queue<string> myq;
        myq.push(A);
        unordered_map<string,int> dist;
        dist[A] = 0;
        while(!myq.empty()){
            string cur = myq.front();
            myq.pop();
            if(cur == B){
                return dist[cur];
            }
            vector<string> nexts = neighbers(cur, B);
            for(auto it : nexts){
                if(dist.count(it) == 0){
                    dist[it] = dist[cur]+1;
                    myq.push(it);
                }
            }
        }
        return -1;
    }
    vector<string> neighbers(string s, string t){
        vector<string> res;
        int i = 0;
        while(s[i]==t[i]){i++;}
        for(int j = i+1; j < s.length(); j++){
            if(s[j] == t[i]){
                swap(s[j],s[i]);
                res.push_back(s);
                swap(s[j],s[i]);
            }
        }
        return res;
    }
};
```