810. Chalkboard XOR Game

We are given non-negative integers nums[i] which are written on a chalkboard.  Alice and Bob take turns erasing exactly one number from the chalkboard, with Alice starting first.  If erasing a number causes the bitwise XOR of all the elements of the chalkboard to become 0, then that player loses.  (Also, we'll say the bitwise XOR of one element is that element itself, and the bitwise XOR of no elements is 0.)

Also, if any player starts their turn with the bitwise XOR of all the elements of the chalkboard equal to 0, then that player wins.

Return True if and only if Alice wins the game, assuming both players play optimally.

**Example:**
```
Input: nums = [1, 1, 2]
Output: false
Explanation: 
Alice has two choices: erase 1 or erase 2. 
If she erases 1, the nums array becomes [1, 2]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 2 = 3. Now Bob can remove any element he wants, because Alice will be the one to erase the last element and she will lose. 
If Alice erases 2 first, now nums becomes [1, 1]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 1 = 0. Alice will lose.
```

**Notes:**

* `1 <= N <= 1000`.
* `0 <= nums[i] <= 2^16`.

# Solution
---
## Approach #1: Mathematical [Accepted]
**Intuition and Algorithm**

As in the problem statement, if the XOR of the entire array is `0`, then Alice wins.

If the XOR condition is never triggered, then clearly Alice wins if and only if there are an even number of elements, as every player always has a move.

Now for the big leap in intuition. Actually, Alice always has a move when there are an even number of elements. If $S = x_1 \oplus x_2 \oplus \cdots x_n \neq 0$, but there are no possible moves ($S \oplus x_i = 0$), then $(S \oplus x_1) \oplus (S \oplus x_2) \oplus \cdots \oplus (S \oplus x_n) = (S \oplus \cdots \oplus S) \oplus (x_1 \oplus x_2 \oplus \cdots \oplus x_n) = 0 \oplus S \neq 0$, a contradiction.

Similarly, if there are an odd number of elements, then Bob always faces an even number of elements, and has a move. So the answer is just the parity of the number of elements in the array.

Those that are familiar with the Sprague-Grundy theorem may know that this game is a misère-form game, meaning the theorem does not apply, and giving a big hint that there may exist a simpler solution.

```python
class Solution(object):
    def xorGame(self, nums):
        return reduce(operator.xor, nums) == 0 or len(nums) % 2 == 0
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of `nums`.

* Space Complexity: $O(1)$.

# Submissions
---
**Solution: (Mathematical)**
```
Runtime: 144 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        return reduce(operator.xor, nums) == 0 or len(nums) % 2 == 0
```