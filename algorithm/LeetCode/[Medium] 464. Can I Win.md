464. Can I Win

In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer `maxChoosableInteger` and another integer `desiredTotal`, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that `maxChoosableInteger` will not be larger than 20 and `desiredTotal` will not be larger than 300.

**Example**
```
Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
```

**Solution 1:**
```
Runtime: 380 ms
Memory Usage: 33.3 MB
```
```python
import functools
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # quickly handle two special cases
        sum_of_all = (maxChoosableInteger + 1) * maxChoosableInteger // 2
        if sum_of_all < desiredTotal:
            return False
        if sum_of_all == desiredTotal:
            return maxChoosableInteger % 2 == 1
        @functools.lru_cache(None)
        def can_i_win(options, target):
            if options[-1] >= target:
                return True
            return not all(can_i_win(options[:i] + options[i + 1:],target - x) for i, x in enumerate(options))

        return can_i_win(tuple(range(1, maxChoosableInteger + 1)), desiredTotal)
```