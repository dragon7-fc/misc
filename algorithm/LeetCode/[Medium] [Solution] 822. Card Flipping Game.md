822. Card Flipping Game

On a table are `N` cards, with a positive integer printed on the front and back of each card (possibly different).

We flip any number of cards, and after we choose one card. 

If the number `X` on the back of the chosen card is not on the front of any card, then this number `X` is good.

What is the smallest number that is good?  If no number is good, output `0`.

Here, `fronts[i]` and `backs[i]` represent the number on the front and back of card `i`. 

A flip swaps the front and back numbers, so the value on the front is now on the back and vice versa.

**Example:**
```
Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
Output: 2
Explanation: If we flip the second card, the fronts are [1,3,4,4,7] and the backs are [1,2,4,1,3].
We choose the second card, which has number 2 on the back, and it isn't on the front of any card, so 2 is good.
```

**Note:**

* `1 <= fronts.length == backs.length <= 1000.`
* `1 <= fronts[i] <= 2000.`
* `1 <= backs[i] <= 2000.`

# Solution
---
## Approach #1: Hash Set [Accepted]
**Intuition**

If a card has the same value `x` on the front and back, it is impossible to win with `x`. Otherwise, it has two different values, and if we win with `x`, we can put `x` face down on the rest of the cards.

Algorithm

Remember all values `same` that occur twice on a single card. Then for every value `x` on any card that isn't in same, `x` is a candidate answer. If we have no candidate answers, the final answer is zero.

```python
class Solution(object):
    def flipgame(self, fronts, backs):
        same = {x for i, x in enumerate(fronts) if x == backs[i]}
        ans = 9999
        for x in itertools.chain(fronts, backs):
            if x not in same:
                ans = min(ans, x)

        return ans % 9999
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of fronts (and backs). We scan through the arrays.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution 1: (Hash Set)**
```
Runtime: 176 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same = {x for i, x in enumerate(fronts) if x == backs[i]}
        ans = 9999
        for x in itertools.chain(fronts, backs):
            if x not in same:
                ans = min(ans, x)

        return ans % 9999
```

**Solution 2: (Array)**
```
Runtime: 32 ms
Memory Usage: 18.5 MB
```
```c++
class Solution {
public:
    int flipgame(vector<int>& fronts, vector<int>& backs) {
        int ans = 1000000000;
        bool bad[2000] = {false};
        for(int i = 0; i < fronts.size(); i ++)
            if(fronts[i] == backs[i])
                bad[fronts[i]] = true;
        for(int i = 0; i < fronts.size(); i ++)
        {
            if(!bad[fronts[i]])
                ans = min(ans, fronts[i]);
            if(!bad[backs[i]])
                ans = min(ans, backs[i]);
        }
        if(ans == 1000000000) return 0;
        return ans;
    }
};
```