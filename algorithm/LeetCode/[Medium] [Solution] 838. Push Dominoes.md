838. Push Dominoes

There are `N` dominoes in a line, and we place each domino vertically upright.

In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

![838_domino](img/838_domino.png)

After each second, each domino that is falling to the left pushes the adjacent domino on the left.

Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.

Return a string representing the final state. 

**Example 1:**

```
Input: ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
```

**Example 2:**

```
Input: "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
```

**Note:**

1. `0 <= N <= 10^5`
1. String dominoes contains only 'L', 'R' and '.'

# Solution
---
## Approach #1: Adjacent Symbols [Accepted]
**Intuition**

Between every group of vertical dominoes `('.')`, we have up to two non-vertical dominoes bordering this group. Since additional dominoes outside this group do not affect the outcome, we can analyze these situations individually: there are 9 of them (as the border could be empty). Actually, if we border the dominoes by `'L'` and `'R'`, there are only 4 cases. We'll write new letters between these symbols depending on each case.

**Algorithm**

1. Continuing our explanation, we analyze cases:

* If we have say `"A....B"`, where `A = B`, then we should write `"AAAAAA"`.

* If we have `"R....L"`, then we will write `"RRRLLL"`, or `"RRR.LLL"` if we have an odd number of dots. If the initial symbols are at positions `i` and `j`, we can check our distance `k-i` and `j-k` to decide at position `k` whether to write `'L'`, `'R'`, or `'.'`.

(If we have `"L....R"` we don't do anything. We can skip this case.)

```python
class Solution(object):
    def pushDominoes(self, dominoes):
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]

        ans = list(dominoes)
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            if x == y:
                for k in xrange(i+1, j):
                    ans[k] = x
            elif x > y: #RL
                for k in xrange(i+1, j):
                    ans[k] = '.LR'[cmp(k-i, j-k)]

        return "".join(ans)
```

**Complexity Analysis**

* Time and Space Complexity: $O(N)$, where $N$ is the length of dominoes.

## Approach #2: Calculate Force [Accepted]
**Intuition**

We can calculate the net force applied on every domino. The forces we care about are how close a domino is to a leftward `'R'`, and to a rightward `'L'`: the closer we are, the stronger the force.

**Algorithm**

Scanning from left to right, our force decays by 1 every iteration, and resets to `N` if we meet an `'R'`, so that `force[i]` is higher (than `force[j]`) if and only if `dominoes[i]` is closer (looking leftward) to `'R'` (than `dominoes[j]`).

Similarly, scanning from right to left, we can find the force going rightward (closeness to `'L'`).

For some domino `answer[i]`, if the forces are equal, then the answer is `'.'`. Otherwise, the answer is implied by whichever force is stronger.

**Example**

Here is a worked example on the string `S = 'R.R...L'`: We find the force going from left to right is `[7, 6, 7, 6, 5, 4, 0]`. The force going from right to left is `[0, 0, 0, -4, -5, -6, -7]`. Combining them (taking their vector addition), the combined force is `[7, 6, 7, 2, 0, -2, -7]`, for a final answer of `RRRR.LL`.

```python
class Solution(object):
    def pushDominoes(self, dominoes):
        N = len(dominoes)
        force = [0] * N

        # Populate forces going from left to right
        f = 0
        for i in xrange(N):
            if dominoes[i] == 'R': f = N
            elif dominoes[i] == 'L': f = 0
            else: f = max(f-1, 0)
            force[i] += f

        # Populate forces going from right to left
        f = 0
        for i in xrange(N-1, -1, -1):
            if dominoes[i] == 'L': f = N
            elif dominoes[i] == 'R': f = 0
            else: f = max(f-1, 0)
            force[i] -= f

        return "".join('.' if f==0 else 'R' if f > 0 else 'L'
                       for f in force)
```

**Complexity Analysis**

* Time and Space Complexity: $O(N)$.

# Submissions
---
**Solution: (Adjacent Symbols, Two Pointers)**
```
Runtime: 132 ms
Memory Usage: 20 MB
```
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

**Solution: (Calculate Force, DP Bottom-Up)**
```
Runtime: 252 ms
Memory Usage: 18 MB
```
```python
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
        force = [0] * N

        # Populate forces going from left to right
        f = 0
        for i in range(N):
            if dominoes[i] == 'R': f = N
            elif dominoes[i] == 'L': f = 0
            else: f = max(f-1, 0)
            force[i] += f

        # Populate forces going from right to left
        f = 0
        for i in range(N-1, -1, -1):
            if dominoes[i] == 'L': f = N
            elif dominoes[i] == 'R': f = 0
            else: f = max(f-1, 0)
            force[i] -= f

        return "".join('.' if f==0 else 'R' if f > 0 else 'L'
                       for f in force)
```

**Solution 1: (Two Pointers)**
```
Runtime: 49 ms
Memory Usage: 12.5 MB
```
```c++
class Solution {
    void modifyState(string& dominoes, int i, int j, char state) {
        while (i < j) {
            dominoes[i++] = state;
        }
    }
public:
    string pushDominoes(string dominoes) {
        int n = dominoes.size(), i, j;
        for (i = 0, j = 0; j < n; j++) {
            if (dominoes[j] != '.') {
                if ((dominoes[i] == '.' and dominoes[j] == 'L') or dominoes[i] == dominoes[j]) {
                    modifyState(dominoes, i, j, dominoes[j]);
                }
                else if (dominoes[i] == 'R' and dominoes[j] == 'L') {
                    int mid = (i+j+1) / 2;
                    int skipMid = (j - i)%2 == 0;
                    modifyState(dominoes, i, mid, dominoes[i]);
                    modifyState(dominoes, mid+skipMid, j, dominoes[j]);
                }
                i = j;
            }
        }
        if (dominoes[j-1] == '.' and dominoes[i] == 'R') {
            modifyState(dominoes, i, j, dominoes[i]);
        }
        return dominoes;
    }
};
```

**Solution 2: (Calculate Force, DP Bottom-Up)**
```
Runtime: 108 ms
Memory Usage: 17.6 MB
```
```c++
class Solution {
public:
    string pushDominoes(string dominoes) {
        int N = dominoes.size();
        vector<int> forces(N);

        // Populate forces going from left to right
        int force = 0;
        for (int i = 0; i < N; ++i) {
            if (dominoes[i] == 'R') force = N;
            else if (dominoes[i] == 'L') force = 0;
            else force = max(force - 1, 0);
            forces[i] += force;
        }

        // Populate forces going from right to left
        force = 0;
        for (int i = N-1; i >= 0; --i) {
            if (dominoes[i] == 'L') force = N;
            else if (dominoes[i] == 'R') force = 0;
            else force = max(force - 1, 0);
            forces[i] -= force;
        }

        string ans(N, ' ');
        for (int i = 0; i < N; i ++)
            ans[i] = forces[i] > 0 ? 'R' : forces[i] < 0 ? 'L' : '.';
        return ans;
    }
};
```
