913. Cat and Mouse

A game on an **undirected** graph is played by two players, Mouse and Cat, who alternate turns.

The graph is given as follows: `graph[a]` is a list of all nodes `b` such that `ab` is an edge of the graph.

Mouse starts at node `1` and goes first, Cat starts at node `2` and goes second, and there is a Hole at node `0`.

During each player's turn, they **must** travel along one edge of the graph that meets where they are.  For example, if the Mouse is at node `1`, it **must** travel to any node in `graph[1]`.

Additionally, it is not allowed for the Cat to travel to the Hole (node `0`.)

Then, the game can end in 3 ways:

* If ever the Cat occupies the same node as the Mouse, the Cat wins.
* If ever the Mouse reaches the Hole, the Mouse wins.
* If ever a position is repeated (ie. the players are in the same position as a previous turn, and it is the same player's turn to move), the game is a draw.

Given a graph, and assuming both players play optimally, return `1` if the game is won by Mouse, `2` if the game is won by Cat, and `0` if the game is a draw.

 

**Example 1:**
```
Input: [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
Output: 0
Explanation:
4---3---1
|   |
2---5
 \ /
  0
```

**Note:**

* `3 <= graph.length <= 50`
* It is guaranteed that `graph[1]` is non-empty.
* It is guaranteed that `graph[2]` contains a non-zero element.

# Solution
---
## Approach 1: Minimax / Percolate from Resolved States
**Intuition**

The state of the game can be represented as `(m, c, t)` where `m` is the location of the mouse, `c` is the location of the cat, and `t` is `1` if it is the mouse's move, else `2`. Let's call these states nodes. These states form a directed graph: the player whose turn it is has various moves which can be considered as outgoing edges from this node to other nodes.

Some of these nodes are already resolved: if the mouse is at the hole (`m = 0`), then the mouse wins; if the cat is where the mouse is (`c = m`), then the cat wins. Let's say that nodes will either be colored $\small\text{MOUSE}$, $\small\text{CAT}$, or $\small\text{DRAW}$ depending on which player is assured victory.

As in a standard minimax algorithm, the Mouse player will prefer $\small\text{MOUSE}$ nodes first, $\small\text{DRAW}$ nodes second, and $\small\text{CAT}$ nodes last, and the Cat player prefers these nodes in the opposite order.

**Algorithm**

We will color each node marked $\small\text{DRAW}$ according to the following rule. (We'll suppose the node has node.turn = Mouse: the other case is similar.)

("Immediate coloring"): If there is a child that is colored $\small\text{MOUSE}$, then this node will also be colored $\small\text{MOUSE}$.

("Eventual coloring"): If all children are colored $\small\text{CAT}$, then this node will also be colored $\small\text{CAT}$.

We will repeatedly do this kind of coloring until no node satisfies the above conditions. To perform this coloring efficiently, we will use a queue and perform a bottom-up percolation:

* Enqueue any node initially colored (because the Mouse is at the Hole, or the Cat is at the Mouse.)

* For every node in the queue, for each parent of that node:

    * Do an immediate coloring of parent if you can.

    * If you can't, then decrement the side-count of the number of children marked $\small\text{DRAW}$. If it becomes zero, then do an "eventual coloring" of this parent.

    * All parents that were colored in this manner get enqueued to the queue.

**Proof of Correctness**

Our proof is similar to a proof that minimax works.

Say we cannot color any nodes any more, and say from any node colored $\small\text{CAT}$ or $\small\text{MOUSE}$ we need at most $K$ moves to win. If say, some node marked $\small\text{DRAW}$ is actually a win for Mouse, it must have been with $> K$ moves. Then, a path along optimal play (that tries to prolong the loss as long as possible) must arrive at a node colored $\small\text{MOUSE}$ (as eventually the Mouse reaches the Hole.) Thus, there must have been some transition $\small\text{DRAW} \rightarrow \small\text{MOUSE}$ along this path.

If this transition occurred at a node with node.turn = Mouse, then it breaks our immediate coloring rule. If it occured with node.turn = Cat, and all children of node have color $\small\text{MOUSE}$, then it breaks our eventual coloring rule. If some child has color $\small\text{CAT}$, then it breaks our immediate coloring rule. Thus, in this case node will have some child with $\small\text{DRAW}$, which breaks our optimal play assumption, as moving to this child ends the game in $> K$ moves, whereas moving to the colored neighbor ends the game in $\leq K$ moves.

```python
class Solution(object):
    def catMouseGame(self, graph):
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
        for m in xrange(N):
            for c in xrange(N):
                degree[m,c,1] = len(graph[m])
                degree[m,c,2] = len(graph[c]) - (0 in graph[c])

        # enqueued : all nodes that are colored
        queue = collections.deque([])
        for i in xrange(N):
            for t in xrange(1, 3):
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

**Complexity Analysis**

* Time Complexity: $O(N^3)$, where $N$ is the number of nodes in the graph. There are $O(N^2)$ states, and each state has an outdegree of $N$, as there are at most $N$ different moves.

* Space Complexity: $O(N^2)$.

# Submissions
---
**Solution 1: (Minimax / Percolate from Resolved States)**
```
Runtime: 464 ms
Memory Usage: 13.9 MB
```
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