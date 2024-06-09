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

**Solution 4: (Hash Table, sort)**
```
Runtime: 64 ms
Memory: 30.69 MB
```
```c++
class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        int handSize = hand.size();

        if (handSize % groupSize != 0) {
            return false;
        }

        // Map to store the count of each card value
        map<int, int> cardCount;
        for (int i = 0; i < handSize; i++) {
            cardCount[hand[i]]++;
        }

        // Process the cards until the map is empty
        while (!cardCount.empty()) {
            // Get the smallest card value
            int currentCard = cardCount.begin()->first;
            // Check each consecutive sequence of groupSize cards
            for (int i = 0; i < groupSize; i++) {
                // If a card is missing or has exhausted its occurrences
                if (cardCount[currentCard + i] == 0) {
                    return false;
                }
                cardCount[currentCard + i]--;
                if (cardCount[currentCard + i] < 1) {
                    // Remove the card value if its occurrences are exhausted
                    cardCount.erase(currentCard + i);
                }
            }
        }

        return true;
    }
};
```

**Solution 5: (Rerverse Decrement**
```
Runtime: 46 ms
Memory: 30.61 MB
```
```c++
class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        if (hand.size() % groupSize != 0) {
            return false;
        }

        // Map to store the count of each card value
        unordered_map<int, int> cardCount;
        for (int card : hand) {
            cardCount[card]++;
        }

        for (int card : hand) {
            int startCard = card;
            // Find the start of the potential straight sequence
            while (cardCount[startCard - 1]) {
                startCard--;
            }

            // Process the sequence starting from startCard
            while (startCard <= card) {
                while (cardCount[startCard]) {
                    // Check if we can form a consecutive sequence of
                    // groupSize cards
                    for (int nextCard = startCard;
                         nextCard < startCard + groupSize; nextCard++) {
                        if (!cardCount[nextCard]) {
                            return false;
                        }
                        cardCount[nextCard]--;
                    }
                }
                startCard++;
            }
        }

        return true;
    }
};
```

**Solution 6: (Counter)**
```
untime: 39 ms
Memory: 30.40 MB
```
```c++
class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        int n = hand.size(), cur, v;
        if (n%groupSize != 0) {
            return false;
        }
        unordered_map<int,int> cnt;
        for (int i = 0; i < n; i ++) {
            cnt[hand[i]] += 1;
        }
        while (cnt.size()) {
            auto [k, _] = *cnt.begin();
            cur = k;
            while (cnt.count(cur-1)) {
                cur -= 1;
            }
            v = cnt[cur];
            for (int i = 0; i < groupSize; i ++) {
                if (cnt[cur+i] < v) {
                    return false;
                }
                cnt[cur+i] -= v;
                if (cnt[cur+i] == 0) {
                    cnt.erase(cur+i);
                }
            }
        }
        return true;
    }
};
```
