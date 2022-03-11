846. Hand of Straights

Alice has a `hand` of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size `W`, and consists of `W` consecutive cards.

Return `true` if and only if she can.

 

**Example 1:**
```
Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
```

**Example 2:**
```
Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.
```

**Note:**

* `1 <= hand.length <= 10000`
* `0 <= hand[i] <= 10^9`
* `1 <= W <= hand.length`

# Solution
---
## Approach #1: Brute Force [Accepted]
**Intuition**

We will repeatedly try to form a group (of size `W`) starting with the lowest card. This works because the lowest card still in our hand must be the bottom end of a size `W` straight.

**Algorithm**

Let's keep a `count` {card: number of copies of card} as a `TreeMap` (or `dict`).

Then, repeatedly we will do the following steps: find the lowest value card that has `1` or more copies (say with value `x`), and try to remove `x, x+1, x+2, ..., x+W-1` from our `count`. If we can't, then the task is impossible.

```python
class Solution(object):
    def isNStraightHand(self, hand, W):
        count = collections.Counter(hand)
        while count:
            m = min(count)
            for k in xrange(m, m+W):
                v = count[k]
                if not v: return False
                if v == 1:
                    del count[k]
                else:
                    count[k] = v - 1

        return True
```

**Complexity Analysis**

* Time Complexity: $O(N * (N/W))$, where $N$ is the length of `hand`. The $(N / W)$ factor comes from `min(count)`. In Java, the $(N / W)$ factor becomes $\log N$ due to the complexity of TreeMap.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 816 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        count = collections.Counter(hand)
        while count:
            m = min(count)
            for k in range(m, m+W):
                v = count[k]
                if not v: return False
                if v == 1:
                    del count[k]
                else:
                    count[k] = v - 1

        return True
```

**Solution 2: (Greedy, Sort)**
```
Runtime: 192 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        count = collections.Counter(hand)
        for card in sorted(hand):
            if count[card] > 0:
                for i in range(W):
                    if count[card+i] == 0:
                        return False
                    count[card+i] -= 1
        
        return True
```

**Solution 3: (Hash Table)**
```
Runtime: 114 ms
Memory Usage: 28.2 MB
```
```c++
class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        if(hand.size() % groupSize != 0) return false;
    
        map<int,int>table;
        for(auto x: hand) table[x]++;

        for(auto [x, n] : table)
          while(n--)
            for(int i = 1; i != groupSize; i++)
              if(!table.count(x+i) || table[x+i]-- == 0) return false;

        return true;
    }
};
```
