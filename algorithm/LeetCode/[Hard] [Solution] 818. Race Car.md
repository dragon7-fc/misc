818. Race Car

Your car starts at position `0` and speed `+1` on an infinite number line.  (Your car can go into negative positions.)

Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).

When you get an instruction "A", your car does the following: `position += speed, speed *= 2`.

When you get an instruction "R", your car does the following: if your speed is positive then `speed = -1` , otherwise `speed = 1`.  (Your position stays the same.)

For example, after commands "AAR", your car goes to positions `0->1->3->3`, and your speed goes to `1->2->4->-1`.

Now for some target position, say the **length** of the shortest sequence of instructions to get there.

**Example 1:**
```
Input: 
target = 3
Output: 2
Explanation: 
The shortest instruction sequence is "AA".
Your position goes from 0->1->3.
```

**Example 2:**
```
Input: 
target = 6
Output: 5
Explanation: 
The shortest instruction sequence is "AAARA".
Your position goes from 0->1->3->7->7->6.
```

**Note:**

* `1 <= target <= 10000`.

# Solution
---
## Approach Framework
**Explanation**

Let $A^k$ denote the command $A A A \cdots A$ (k times).

Starting with an "R" command doesn't help, and as the final sequence does not end on an "R", so we have some sequence like $R A^{k_1} R A^{k_2} \cdots R A^{k_n}$ which could be instead $A^{k_2} R A^{k_3} R \cdots A^{k_n} R R A^{k_1}$ for the same final position of the car. (Here, $k_i \geq 0$, where $A^0$  means no command.)

So let's suppose our command is always of the form $A^{k_1} R A^{k_2} R \cdots A^{k_n}$. Note that under such a command, the car will move to final position $(2^{k_1} - 1) - (2^{k_2} - 1) + (2^{k_3} - 1) - \cdots$.

Without loss of generality, we can say that $(k_i$, $i$ odd) is monotone decreasing, and ($k_i$, $i$ even) is also monotone decreasing.

Also because terms will cancel out, we can also ignore the possibility that $k_i = k_j$ (for $i, j$ with different parity).

A key claim is that $k_i$ is bounded by $a+1$, where $a$ is the smallest integer such that $2^a \geq \text{target}$ - basically, if you drive past the target, you don't need to keep driving. This is because it adds another power of two (as $2^{k_i} - 1 = \sum_{j < k_i} 2^j$ to the position that must get erased by one or more negative terms later (in whole or in part), as it is not part of the target.

## Approach #1: Dijkstra's [Accepted]
**Intuition**

With some target, we have different moves we can perform (such as $k_1 = 0, 1, 2, \cdots$, using the notation from our Approach Framework), with different costs.

This is an ideal setup for Dijkstra's algorithm, which can help us find the shortest cost path in a weighted graph.

**Algorithm**

Dijkstra's algorithm uses a priority queue to continually searches the path with the lowest cost to destination, so that when we reach the target, we know it must have been through the lowest cost path. Refer to this link for more detail.

Back to the problem, as described above, we have some barrier where we are guaranteed to never cross. We will also handle negative targets; in total we will have `2 * barrier + 1` nodes.

After, we could move `walk = 2**k - 1` steps for a cost of `k + 1` (the 1 is to reverse). If we reach our destination exactly, we don't need the R, so it is just k steps.

```python
class Solution(object):
    def racecar(self, target):
        K = target.bit_length() + 1
        barrier = 1 << K
        pq = [(0, target)]
        dist = [float('inf')] * (2 * barrier + 1)
        dist[target] = 0

        while pq:
            steps, targ = heapq.heappop(pq)
            if dist[targ] > steps: continue

            for k in xrange(K+1):
                walk = (1 << k) - 1
                steps2, targ2 = steps + k + 1, walk - targ
                if walk == targ: steps2 -= 1 #No "R" command if already exact

                if abs(targ2) <= barrier and steps2 < dist[targ2]:
                    heapq.heappush(pq, (steps2, targ2))
                    dist[targ2] = steps2

        return dist[0]
```

**Complexity Analysis**

* Time Complexity: $O(T \log T)$. There are $O(T)$ nodes, we process each one using $O(\log T)$ work (both popping from the heap and adding the edges).

* Space Complexity: $O(T)$.


## Approach #2: Dynamic Programming [Accepted]
**Intuition and Algorithm**

As in our Approach Framework, we've framed the problem as a series of moves $k_i$.

Now say we have some target `2**(k-1) <= t < 2**k` and we want to know the cost to go there, if we know all the other costs dp[u] (for `u < t`).

If `t == 2**k - 1`, the cost is just `k`: we use the command $A^k$, and clearly we can't do better.

Otherwise, we might drive without crossing the target for a position change of $2^{k-1} - 2**j$, by the command $A^{k-1} R A^{j} R$, for a total cost of $k - 1 + j + 2$.

Finally, we might drive $2^k - 1$ which crosses the target, by the command $A^k R$, for a total cost of $k + 1$.

We can use dynamic programming together with the above recurrence to implement the code below.

```python
class Solution(object):
    def racecar(self, target):
        dp = [0, 1, 4] + [float('inf')] * target
        for t in xrange(3, target + 1):
            k = t.bit_length()
            if t == 2**k - 1:
                dp[t] = k
                continue
            for j in xrange(k - 1):
                dp[t] = min(dp[t], dp[t - 2**(k - 1) + 2**j] + k - 1 + j + 2)
            if 2**k - 1 - t < t:
                dp[t] = min(dp[t], dp[2**k - 1 - t] + k + 1)
        return dp[target]
```

**Complexity Analysis**

* Time Complexity: $O(T \log T)$. Each node `i` does $\log i$ work.

* Space Complexity: $O(T)$.

# Submissions
---
**Solution 1:**