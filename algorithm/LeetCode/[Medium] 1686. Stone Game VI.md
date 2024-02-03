1686. Stone Game VI

Alice and Bob take turns playing a game, with Alice starting first.

There are `n` stones in a pile. On each player's turn, they can **remove** a stone from the pile and receive points based on the stone's value. Alice and Bob may **value the stones differently**.

You are given two integer arrays of length `n`, `aliceValues` and `bobValues`. Each `aliceValues[i]` and `bobValues[i]` represents how Alice and Bob, respectively, value the `i`th stone.

The winner is the person with the most points after all the stones are chosen. If both players have the same amount of points, the game results in a draw. Both players will play **optimally**.

Determine the result of the game, and:

* If Alice wins, return `1`.
* If Bob wins, return `-1`.
* If the game results in a draw, return `0`.
 

**Example 1:**
```
Input: aliceValues = [1,3], bobValues = [2,1]
Output: 1
Explanation:
If Alice takes stone 1 (0-indexed) first, Alice will receive 3 points.
Bob can only choose stone 0, and will only receive 2 points.
Alice wins.
```

**Example 2:**
```
Input: aliceValues = [1,2], bobValues = [3,1]
Output: 0
Explanation:
If Alice takes stone 0, and Bob takes stone 1, they will both have 1 point.
Draw.
```

**Example 3:**
```
Input: aliceValues = [2,4,3], bobValues = [1,6,7]
Output: -1
Explanation:
Regardless of how Alice plays, Bob will be able to have more points than Alice.
For example, if Alice takes stone 1, Bob can take stone 2, and Alice takes stone 0, Alice will have 6 points to Bob's 7.
Bob wins.
```

**Constraints:**

* `n == aliceValues.length == bobValues.length`
* `1 <= n <= 105`
* `1 <= aliceValues[i], bobValues[i] <= 100`

# Submissions
---
**Solution 1: (Heap, Greedy)**
```
Runtime: 1616 ms
Memory Usage: 29.7 MB
```
```python
class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        heap = [(-i-j, i, j) for i,j in zip(aliceValues,bobValues)] #max heap
        AScore = 0
        BScore = 0
        heapq.heapify(heap)
        turn = "A"
        while heap:
            _, ascore, bscore = heapq.heappop(heap)
            if turn == "A":
                AScore += ascore
                turn = "B"
            else:
                BScore += bscore
                turn = "A"
        if AScore == BScore : return 0
        return 1 if AScore > BScore else  -1
```

**Solution 2: (Sort)**

__Intuition__

Sort stones by their sum value for Alice and Bob.
If a stone is super valued for Alice, Alice wants to take it.
If a stone is super valued for Bob, Alice also wants to take it.
Because she doesn't want Bob to take it.


__Explanation__

Here is more convinced explanation.
Assume a stone valued [a,b] for Alice and Bod.
Alice takes it, worth a for Alice,
Bob takes it, worth b for Bob,
we can also consider that it worth -b for Alice.
The difference will be a+b.
That's the reason why we need to sort based on a+b.
And Alice and Bob will take one most valued stone each turn.


__Complexity__

* Time O(nlogn)
* Space O(n)

```
Runtime: 285 ms
Memory: 159.75 MB
```
```c++
class Solution {
public:
    int stoneGameVI(vector<int>& aliceValues, vector<int>& bobValues) {
        vector<vector<int>> C;
        int res[2] = {0, 0}, n = aliceValues.size();
        for (int i = 0; i < n; ++i)
            C.push_back({ -aliceValues[i] - bobValues[i], aliceValues[i], bobValues[i]});
        sort(begin(C), end(C));
        for (int i = 0; i < n; ++i)
            res[i % 2] += C[i][1 + i % 2];
        return res[0] == res[1] ? 0 : res[0] > res[1] ? 1 : -1;
    }
};
```
