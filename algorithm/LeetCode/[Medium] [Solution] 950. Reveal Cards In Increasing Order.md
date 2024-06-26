950. Reveal Cards In Increasing Order

In a deck of cards, every card has a unique integer.  You can order the deck in any order you want.

Initially, all the cards start face down (unrevealed) in one deck.

Now, you do the following steps repeatedly, until all cards are revealed:

1. Take the top card of the deck, reveal it, and take it out of the deck.
1. If there are still cards in the deck, put the next top card of the deck at the bottom of the deck.
1. If there are still unrevealed cards, go back to step 1.  Otherwise, stop.

Return an ordering of the deck that would reveal the cards in **increasing order**.

The first entry in the answer is considered to be the top of the deck.

**Example 1:**
```
Input: [17,13,11,2,3,5,7]
Output: [2,13,3,11,5,17,7]
Explanation: 
We get the deck in the order [17,13,11,2,3,5,7] (this order doesn't matter), and reorder it.
After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
We reveal 13, and move 17 to the bottom.  The deck is now [17].
We reveal 17.
Since all the cards revealed are in increasing order, the answer is correct.
```

**Note:**

1. `1 <= A.length <= 1000`
1. `1 <= A[i] <= 10^6`
1. `A[i] != A[j]` for all `i` != `j`

## Solution
---
## Approach 1: Simulation
**Intuition and Algorithm**

Simulate the revealing process with a deck set to `[0, 1, 2, ...]`. If for example this deck is revealed in the order `[0, 2, 4, ...]` then we know we need to put the smallest card in index `0`, the second smallest card in index `2`, the third smallest card in index `4`, etc.

```python
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        N = len(deck)
        index = collections.deque(range(N))
        ans = [None] * N

        for card in sorted(deck):
            ans[index.popleft()] = card
            if index:
                index.append(index.popleft())

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N \log N)$, where $N$ is the length of deck.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution: (Simulation)**
```
Runtime: 48 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        index = collections.deque(range(N))
        ans = [None] * N

        for card in sorted(deck):
            ans[index.popleft()] = card
            if index:
                index.append(index.popleft())

        return ans
```

**Solution 2: (Simulation, deque, sort and greedy over index)**
```
Runtime: 3 ms
Memory: 10.90 MB
```
```c++
class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        int n = deck.size();
        deque<int> q(n);
        vector<int> ans(n);
        for (int i = 0; i < n; i ++) {
            q[i] = i;
        }
        sort(deck.begin(), deck.end());
        for (auto d: deck) {
            ans[q.front()] = d;
            q.pop_front();
            q.push_back(q.front());
            q.pop_front();
        }
        return ans;
    }
};
```

**Solution 3: (Simulation, deque, sort, walk backward)**
```
Runtime: 3 ms
Memory: 11.04MB
```
```c++
class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        int n = deck.size();
        sort(deck.begin(), deck.end());
        deque<int> q;
        q.push_front(deck[n - 1]);
        for (int i = n - 2; i >= 0; i--) {
            q.push_front(q.back());
            q.pop_back();
            q.push_front(deck[i]);
        }
        return vector<int>(q.begin(), q.end());
    }
};
```
