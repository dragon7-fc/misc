2260. Minimum Consecutive Cards to Pick Up

You are given an integer array `cards` where `cards[i]` represents the **value** of the `i`th card. A pair of cards are **matching** if the cards have the **same** value.

Return the **minimum** number of **consecutive** cards you have to pick up to have a pair of **matching** cards among the picked cards. If it is impossible to have matching cards, return `-1`.

 

**Example 1:**
```
Input: cards = [3,4,2,3,4,7]
Output: 4
Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.
```

**Example 2:**
```
Input: cards = [1,0,5,3]
Output: -1
Explanation: There is no way to pick up a set of consecutive cards that contain a pair of matching cards.
```

**Constraints:**

* `1 <= cards.length <= 10^5`
* `0 <= cards[i] <= 10^6`

# Submissions
---
**Solution 1; (Hash Table)**
```
Runtime: 1226 ms
Memory Usage: 34 MB
```
```python
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        minPick = float('inf')
        seen = {}
        for i, n in enumerate(cards):
            if n in seen:
                if i - seen[n] + 1 < minPick:
                    minPick = i - seen[n] + 1
            seen[n] = i
        if minPick == float('inf'):
            return -1
        return minPick
```

**Solution 2; (Hash Table)**
```
Runtime: 200 ms
Memory Usage: 79.5 MB
```
```c++
class Solution {
public:
    int minimumCardPickup(vector<int>& cards) {
        int last[1000001] = {}, res = INT_MAX;
        for (int i = 0; i < cards.size(); ++i) {
            if (last[cards[i]])
                res = min(res, i - last[cards[i]] + 2);
            last[cards[i]] = i + 1;
        }
        return res == INT_MAX ? -1 : res;
    }
};
```
