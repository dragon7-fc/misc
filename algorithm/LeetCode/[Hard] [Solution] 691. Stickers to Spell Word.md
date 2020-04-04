691. Stickers to Spell Word

We are given N different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given `target` string by cutting individual letters from your collection of stickers and rearranging them.

You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

What is the minimum number of stickers that you need to spell out the `target`? If the task is impossible, return `-1`.

**Example 1:**
```
Input:

["with", "example", "science"], "thehat"
Output:

3
Explanation:

We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.
```

**Example 2:**
```
Input:

["notice", "possible"], "basicbasic"
Output:

-1
Explanation:

We can't form the target "basicbasic" from cutting letters from the given stickers.
```

**Note:**

* `stickers` has length in the range `[1, 50]`.
* `stickers` consists of lowercase English words (without apostrophes).
* `target` has length in the range `[1, 15]`, and consists of lowercase English letters.
* In all test cases, all words were chosen randomly from the 1000 most common US English words, and the target was chosen as a concatenation of two random words.
* The time limit may be more challenging than usual. It is expected that a 50 sticker test case can be solved within 35ms on average.

# Solution
---
## Approach 1: Optimized Exhaustive Search

**Intuition**

A natural answer is to exhaustively search combinations of stickers. Because the data is randomized, there are many heuristics available to us that will make this faster.

* For all `stickers`, we can ignore any letters that are not in the `target` word.

* When our candidate answer won't be smaller than an answer we have already found, we can stop searching this path.

* We should try to have our exhaustive search bound the answer as soon as possible, so the effect described in the above point happens more often.

* When a sticker dominates another, we shouldn't include the dominated sticker in our sticker collection. [Here, we say a sticker `A` dominates `B` if `A.count(letter) >= B.count(letter)` for all letters.]


**Algorithm**

Firstly, for each sticker, let's create a count of that sticker (a mapping `letter -> sticker.count(letter))` that does not consider letters not in the `target` word. Let `A` be an array of these counts. Also, let's create `t_count`, a count of our `target` word.

Secondly, let's remove dominated `stickers`. Because dominance is a transitive relation, we only need to check if a sticker is not dominated by any other sticker once - the ones that aren't dominated are included in our collection.

We are now ready to begin our exhaustive search. A call to `search(ans)` denotes that we want to decide the minimum number of stickers we can used in `A` to satisfy the target count `t_count`. `ans` will store the currently formed answer, and `best` will store the current best answer.

If our current answer can't beat our current best answer, we should stop searching. Also, if there are no stickers left and our target is satisfied, we should update our answer.

Otherwise, we want to know the maximum number of this sticker we can use. For example, if this sticker is `'abb'` and our target is `'aaabbbbccccc'`, then we could use a maximum of `3` stickers. This is the maximum of `math.ceil(target.count(letter) / sticker.count(letter))`, taken over all letters in sticker. Let's call this quantity used.

After, for the sticker we are currently considering, we try to use `used` of them, then `used - 1`, `used - 2` and so on. The reason we do it in this order is so that we can arrive at a value for best more quickly, which will stop other branches of our exhaustive search from continuing.

The Python version of this solution showcases using `collections.Counter` as a way to simplify some code sections, whereas the Java solution sticks to arrays.

```python
class Solution(object):
    def minStickers(self, stickers, target):
        t_count = collections.Counter(target)
        A = [collections.Counter(sticker) & t_count
             for sticker in stickers]

        for i in range(len(A) - 1, -1, -1):
            if any(A[i] == A[i] & A[j] for j in range(len(A)) if i != j):
                A.pop(i)

        self.best = len(target) + 1
        def search(ans = 0):
            if ans >= self.best: return
            if not A:
                if all(t_count[letter] <= 0 for letter in t_count):
                    self.best = ans
                return

            sticker = A.pop()
            used = max((t_count[letter] - 1) // sticker[letter] + 1
                        for letter in sticker)
            used = max(used, 0)

            for c in sticker:
                t_count[c] -= used * sticker[c]

            search(ans + used)
            for i in range(used - 1, -1, -1):
                for letter in sticker:
                    t_count[letter] += sticker[letter]
                search(ans + i)

            A.append(sticker)

        search()
        return self.best if self.best <= len(target) else -1
```

**Complexity Analysis**

* Time Complexity: Let $N$ be the number of stickers, and $T$ be the number of letters in the target word. A bound for time complexity is $O(N^{T+1} T^2)$: for each sticker, we'll have to try using it up to $T+1$ times, and updating our target count costs $O(T)$, which we do up to $T$ times. Alternatively, since the answer is bounded at $T$, we can prove that we can only search up to $\binom{N+T-1}{T-1}$ times. This would be $O(\binom{N+T-1}{T-1} T^2)$.

* Space Complexity: $O(N+T)$, to store `stickersCount`, `targetCount`, and handle the recursive callstack when calling search.

## Approach 2: Dynamic Programming

**Intuition**

Suppose we need `dp[state]` stickers to satisfy all `target[i]`'s for which the `i`-th bit of state is set. We would like to know `dp[(1 << len(target)) - 1]`.


**Algorithm**

For each state, let's work with it as `now` and look at what happens to it after applying a sticker. For each letter in the sticker that can satisfy an unset bit of `state`, we set the bit (`now |= 1 << i`). At the end, we know `now` is the result of applying that sticker to `state`, and we update our `dp` appropriately.

When using Python, we will need some extra techniques from Approach #1 to pass in time.

```python
class Solution(object):
    def minStickers(self, stickers, target):
        t_count = collections.Counter(target)
        A = [collections.Counter(sticker) & t_count
             for sticker in stickers]

        for i in range(len(A) - 1, -1, -1):
            if any(A[i] == A[i] & A[j] for j in range(len(A)) if i != j):
                A.pop(i)

        stickers = ["".join(s_count.elements()) for s_count in A]
        dp = [-1] * (1 << len(target))
        dp[0] = 0
        for state in xrange(1 << len(target)):
            if dp[state] == -1: continue
            for sticker in stickers:
                now = state
                for letter in sticker:
                    for i, c in enumerate(target):
                        if (now >> i) & 1: continue
                        if c == letter:
                            now |= 1 << i
                            break
                if dp[now] == -1 or dp[now] > dp[state] + 1:
                    dp[now] = dp[state] + 1

        return dp[-1]
```

**Complexity Analysis**

* Time Complexity: $O(2^T * S * T)$ where $S$ be the total number of letters in all `stickers`, and $T$ be the number of letters in the `target` word. We can examine each loop carefully to arrive at this conclusion.

* Space Complexity: $O(2^T)$, the space used by `dp`.

# Submissions
---
**Solution: (Optimized Exhaustive Search)**
```
Runtime: 388 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        t_count = collections.Counter(target)
        A = [collections.Counter(sticker) & t_count
             for sticker in stickers]

        for i in range(len(A) - 1, -1, -1):
            if any(A[i] == A[i] & A[j] for j in range(len(A)) if i != j):
                A.pop(i)

        self.best = len(target) + 1
        def search(ans = 0):
            if ans >= self.best: return
            if not A:
                if all(t_count[letter] <= 0 for letter in t_count):
                    self.best = ans
                return

            sticker = A.pop()
            used = max((t_count[letter] - 1) // sticker[letter] + 1
                        for letter in sticker)
            used = max(used, 0)

            for c in sticker:
                t_count[c] -= used * sticker[c]

            search(ans + used)
            for i in range(used - 1, -1, -1):
                for letter in sticker:
                    t_count[letter] += sticker[letter]
                search(ans + i)

            A.append(sticker)

        search()
        return self.best if self.best <= len(target) else -1
```

**Solution: (Dynamic Programming Bottom-Up)**
```
Runtime: 668 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        t_count = collections.Counter(target)
        A = [collections.Counter(sticker) & t_count
             for sticker in stickers]

        for i in range(len(A) - 1, -1, -1):
            if any(A[i] == A[i] & A[j] for j in range(len(A)) if i != j):
                A.pop(i)

        stickers = ["".join(s_count.elements()) for s_count in A]
        dp = [-1] * (1 << len(target))
        dp[0] = 0
        for state in range(1 << len(target)):
            if dp[state] == -1: continue
            for sticker in stickers:
                now = state
                for letter in sticker:
                    for i, c in enumerate(target):
                        if (now >> i) & 1: continue
                        if c == letter:
                            now |= 1 << i
                            break
                if dp[now] == -1 or dp[now] > dp[state] + 1:
                    dp[now] = dp[state] + 1

        return dp[-1]
```

**Solution 3: (Backtracking)**
```
Runtime: 2740 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        def backtrack(index, used):
            if index == N:
                self.ans = min(self.ans, used)
                return
            if self.ans == used:
                return
            if cnt[target[index]] <= 0:
                backtrack(index + 1, used)
            else:
                for stick in stickers:
                    if target[index] in stick:
                        for s in stick:
                            cnt[s] -= 1
                        backtrack(index + 1, used + 1)
                        for s in stick:
                            cnt[s] += 1

        N = len(target)
        cnt = collections.Counter(target)
        self.ans = float('inf')
        backtrack(0, 0)
        return self.ans if self.ans < float('inf') else -1
```

**Solution 3: (BFS)**
```
Runtime: 1224 ms
Memory Usage: 20.8 MB
```
```python
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        IndexDict = collections.defaultdict(list)
        for i in range(len(target)):
            IndexDict[target[i]].append(i)
        def applySticker(s, state):
            for c in s:
                if c not in IndexDict:
                    continue
                for index in IndexDict[c]:
                    if not state & (1 << index):
                        state = state | (1 << index)
                        break
            return state
                    
        queue = collections.deque([(0, 0)])
        visited = set()
        while queue: # O(2^T)
            state, level = queue.popleft()
            # print ("{0:b}".format(state), level)
            if state == 2**len(target)-1:
                return level
            if state in visited:
                continue
            visited.add(state)
            for s in stickers: # O(S)
                newState = applySticker(s, state) # O(C*T)
                queue.append((newState, level+1))
        return -1
```