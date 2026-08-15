2029. Stone Game IX

Alice and Bob continue their games with stones. There is a row of n stones, and each stone has an associated value. You are given an integer array `stones`, where `stones[i]` is the **value** of the `i`th stone.

Alice and Bob take turns, with **Alice** starting first. On each turn, the player may remove any stone from `stones`. The player who removes a stone loses if the **sum** of the values of **all removed stones** is divisible by `3`. Bob will win automatically if there are no remaining stones (even if it is Alice's turn).

Assuming both players play **optimally**, return `true` if Alice wins and `false` if Bob wins.

 

**Example 1:**
```
Input: stones = [2,1]
Output: true
Explanation: The game will be played as follows:
- Turn 1: Alice can remove either stone.
- Turn 2: Bob removes the remaining stone. 
The sum of the removed stones is 1 + 2 = 3 and is divisible by 3. Therefore, Bob loses and Alice wins the game.
```

**Example 2:**
```
Input: stones = [2]
Output: false
Explanation: Alice will remove the only stone, and the sum of the values on the removed stones is 2. 
Since all the stones are removed and the sum of values is not divisible by 3, Bob wins the game.
```

**Example 3:**
```
Input: stones = [5,1,2,4,3]
Output: false
Explanation: Bob will always win. One possible way for Bob to win is shown below:
- Turn 1: Alice can remove the second stone with value 1. Sum of removed stones = 1.
- Turn 2: Bob removes the fifth stone with value 3. Sum of removed stones = 1 + 3 = 4.
- Turn 3: Alices removes the fourth stone with value 4. Sum of removed stones = 1 + 3 + 4 = 8.
- Turn 4: Bob removes the third stone with value 2. Sum of removed stones = 1 + 3 + 4 + 2 = 10.
- Turn 5: Alice removes the first stone with value 5. Sum of removed stones = 1 + 3 + 4 + 2 + 5 = 15.
Alice loses the game because the sum of the removed stones (15) is divisible by 3. Bob wins the game.
```

**Constraints:**

* `1 <= stones.length <= 10^5`
* `1 <= stones[i] <= 10^4`

# Sumbissions
---
**Solution 1: (Math)**

**Observation**

Count the frequency of mod3 = 0,1,2.

Firstly, don't consider the multiples of 3.
Alice starts with mod3 = 1, Alice and Bob have to pick 1,1,2,1,2... in order.
Alice starts with mod3 = 2, Alice and Bob have to pick 2,2,1,2,1... in order.
So if cnt[0] == 0, the result can be decided by Alice.

Then, consider the number of multiples of 3.
If cnt[0] is even,
Bob picks a 3, Alice can always picks one another.
the result won't be affected.

If cnt[0] is odd,
the finall result will be reversed,
(unless the case Bob win for all numbers consumed)


**Missing Case**

[1,1,1,3],
gave by @mittal582 and @qingqi_lei,
this can hack most solution.
I was right in the contest :)


**Explanation**

If cnt[1] == 0, Alice needs to start with mod3 = 2,
If cnt[2] == 0, Alice needs to start with mod3 = 1.
Alice can win if max(cnt[1], cnt[2]) > 2 && cnt[0] % 2 > 0,
for example [1,1,1,3].

If cnt[0] % 2 == 0, easy case for Alice.
Alice can win in at leasy one of the two options, picking the less one.

Otherwise cnt[0] % 2 == 1, this will reverse the result.
If abs(cnt[1] - cnt[2]) > 2,
Alice will pick mod3=2 if mod3=2 is more
Alice will pick mod3=1 if mod3=1 is more
If abs(cnt[1] - cnt[2]) <= 2,
Alice will lose for no number remaining.


**Complexity**

* Time O(n)
* Space O(1)

```
Runtime: 1296 ms
Memory Usage: 28 MB
```
```python
class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = collections.Counter(a % 3 for a in stones)
        if min(cnt[1], cnt[2]) == 0:
            return max(cnt[1], cnt[2]) > 2 and cnt[0] % 2 > 0
        return abs(cnt[1] - cnt[2]) > 2 or cnt[0] % 2 == 0
```

**Solution 2: (Math)**
```
Runtime: 180 ms
Memory Usage: 127 MB
```
```c++
class Solution {
public:
    bool stoneGameIX(vector<int>& stones) {
        int cnt[3] = {};
        for (int a: stones)
            cnt[a % 3]++;
        if (min(cnt[1], cnt[2]) == 0)
            return max(cnt[1], cnt[2]) > 2 && cnt[0] % 2 > 0;
        return abs(cnt[1] - cnt[2]) > 2 || cnt[0] % 2 == 0;
    }
};
```

**Solution 3: (Case Study)**

cnt0 % 2 == 1:
= reverse condition

cnt0 % 2 == 0
-> alice win
cnt0 % 2 == 1
-> bob win


                      | A  B  A  B  A  B  A   | bob win                 | alice win
                      | 1, 1, 2, 1, 2, 1, 2   |                         |
----------------------|-----------------------|-------------------------|----------------
all stone removed     |                       |                         |
                      | ------A               | cnt1 = cnt2 + 1         | 
                      | ------------A         |                         |
                      |                       |                         |
                      | ---------B            | cnt1 = cnt2 + 2         |
                      | ---------------B      |                         |
----------------------|-----------------------|-------------------------| cnt1 >= 1 && cnt1 <= cnt2
not all stone removed |                       |                         |
                      |                       | cnt1 = cnt2 + ? (? > 3) |

                      | A  B  A  B  A  B  A   | bob win                 | alice win  
                      | 2, 2, 1, 2, 1, 2, 1   |                         |
----------------------|-----------------------|-------------------------|----------------
                      |                       |                         | cnt2 >= 1 && cnt2 <= cnt1        

```
Runtime: 8 ms, Beats 30.20%
Memory: 131.16 MB, Beats 92.89%
```
```c++
class Solution {
public:
    bool stoneGameIX(vector<int>& stones) {
        int cnt0 = 0, cnt1 = 0, cnt2 = 0;
        for (int val : stones) {
            if (int type = val % 3; type == 0) {
                ++cnt0;
            } else if (type == 1) {
                ++cnt1;
            } else {
                ++cnt2;
            }
        }

        // Case 1: Even number of 0-stones (0-stones don't change parity)
        // alice win
        if (cnt0 % 2 == 0) {
            // cnt1 >= 1 && cnt1 <= cnt2
            // cnt2 >= 1 && cnt2 <= cnt1
            return cnt1 >= 1 && cnt2 >= 1;
        }

        // Case 2: Odd number of 0-stones (0-stones flip parity)
        // bob win, not all stone removed (transfer status to another owner)
        return cnt1 - cnt2 > 2 || cnt2 - cnt1 > 2;
    }
};
```
