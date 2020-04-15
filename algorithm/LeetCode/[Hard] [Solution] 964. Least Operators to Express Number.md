964. Least Operators to Express Number

Given a single positive integer `x`, we will write an expression of the form `x (op1) x (op2) x (op3) x ...` where each operator `op1`, `op2`, etc. is either addition, subtraction, multiplication, or division (`+`, `-`, `*`, or `/`).  For example, with `x = 3`, we might write `3 * 3 / 3 + 3 - 3` which is a value of `3`.

When writing such an expression, we adhere to the following conventions:

* The division operator (`/`) returns rational numbers.
* There are no parentheses placed anywhere.
* We use the usual order of operations: multiplication and division happens before addition and subtraction.
* It's not allowed to use the unary negation operator (`-`).  For example, `"x - x"` is a valid expression as it only uses subtraction, but `"-x + x"` is not because it uses negation.

We would like to write an expression with the least number of operators such that the expression equals the given target.  Return the least number of operators used.

 

**Example 1:**
```
Input: x = 3, target = 19
Output: 5
Explanation: 3 * 3 + 3 * 3 + 3 / 3.  The expression contains 5 operations.
```

**Example 2:**
```
Input: x = 5, target = 501
Output: 8
Explanation: 5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5.  The expression contains 8 operations.
```

**Example 3:**
```
Input: x = 100, target = 100000000
Output: 3
Explanation: 100 * 100 * 100 * 100.  The expression contains 3 operations.
``` 

**Note:**

* `2 <= x <= 100`
* `1 <= target <= 2 * 10^8`

# Solution
---
## Approach 1: Dynamic Programming
**Intuition**

First, we notice that we can consider blocks of multiplication and division separately. Each block is a power of `x`: either `x / x`, `x`, `x * x`, `x * x * x`, `x * x * x * x` and so on. (There is no point to write expressions like `x * x / x` because it uses strictly more operators.)

Let's think of the cost of a block as all the operators needed to express it, including the addition or subtraction operator in front of it. For example, we can think of `x * x + x + x / x` as `(+ x * x) (+ x) (+ x / x)` for a cost of `2 + 1 + 2`, minus `1` for the leading `+` (so the total cost is `4`).

We can write the cost of writing a block that has value $x^e$: it is $e$, except when $e = 0$ it is 2. We want the sum of the costs of all blocks minus 1.

Now, we have the reduced problem: we have the costs of writing all $x^e$ or $-x^e$, and we want to find the least cost to express the target.

Notice that modulo $x$, the only blocks that change the expression are $x^0$. Let $r_1 = \text{target} \pmod x$. So we must either subtract $r_1$ $x^0$'s, or add $x-r_1$ $x^0$'s. This will form a new "remaining" target, $\text{target}_2$, that is divisible by $x$.

Then, modulo $x^2$, the only blocks that change the expression are $x^1$ and $x^0$. However, since the new target is divisible by $x$, there is no point to use $x^0$, as we would have to use at least $x$ of them to do the same work as one use of $x^1$, which is a strictly higher cost.

Again, in a similar way, we have $r_2 = \text{target}_2 \pmod {x^2}$, and we must either subtract $r_2 / x$ $x^1$'s, or add $x - r_2 / x$ $x^1$'s. This will form a new remaining target $\text{target}_3$, and so on.

As a concrete example, say `x = 5`, `target = 123`. We either add `2` or subtract `3`. This leaves us with a target of `120` or `125`. If the target is `120`, we can either add `5` or subtract `20`, leaving us with a target of `100` or `125`. If the target is 100, we can either add `25` or subtract `100`, leaving us with a target of `125` or `0`. If the target is `125`, we subtract `125`.

**Algorithm**

Let's calculate `dp(i, target)` using a top down `dp`. Here, `i` will be the exponent of the block $x^i$ being considered, and target will be the remaining target, already divided by $x^i$.

From here, the recursion is straightforward: $r = \text{target} \pmod x$, and we either subtract $r$ blocks or add $(x-r)$ of them. The base cases are easily deduced - see the code for more details.

```python
from functools import lru_cache

class Solution(object):
    def leastOpsExpressTarget(self, x, target):
        cost = list(range(40))
        cost[0] = 2

        @lru_cache(None)
        def dp(i, targ):
            if targ == 0: return 0
            if targ == 1: return cost[i]
            if i >= 39: return float('inf')

            t, r = divmod(targ, x)
            return min(r * cost[i] + dp(i+1, t),
                       (x-r) * cost[i] + dp(i+1, t+1))

        return dp(0, target) - 1
```

**Complexity Analysis**

* Time Complexity: $O(\log_{x} \text{target})$. We can prove that we only visit up to two states for each base-x digit of $\text{target}$.

* Space Complexity: $O(\log \text{target}$.

# Submissions
---
**Solution: (Dynamic Programming Top-Down)**
```
Runtime: 32 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        cost = list(range(40))
        cost[0] = 2

        @lru_cache(None)
        def dp(i, targ):
            if targ == 0: return 0
            if targ == 1: return cost[i]
            if i >= 39: return float('inf')

            t, r = divmod(targ, x)
            return min(r * cost[i] + dp(i+1, t),
                       (x-r) * cost[i] + dp(i+1, t+1))

        return dp(0, target) - 1
```