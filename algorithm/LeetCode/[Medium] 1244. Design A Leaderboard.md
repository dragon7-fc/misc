1244. Design A Leaderboard

Design a Leaderboard class, which has 3 functions:

1. `addScore(playerId, score)`: Update the leaderboard by adding score to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
1. `top(K)`: Return the score sum of the top `K` players.
1. `reset(playerId)`: Reset the score of the player with the given id to `0`. It is guaranteed that the player was added to the leaderboard before calling this function.

Initially, the leaderboard is empty.

 

**Example 1:**
```
Input: 
["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
[[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
Output: 
[null,null,null,null,null,null,73,null,null,null,141]

Explanation: 
Leaderboard leaderboard = new Leaderboard ();
leaderboard.addScore(1,73);   // leaderboard = [[1,73]];
leaderboard.addScore(2,56);   // leaderboard = [[1,73],[2,56]];
leaderboard.addScore(3,39);   // leaderboard = [[1,73],[2,56],[3,39]];
leaderboard.addScore(4,51);   // leaderboard = [[1,73],[2,56],[3,39],[4,51]];
leaderboard.addScore(5,4);    // leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
leaderboard.top(1);           // returns 73;
leaderboard.reset(1);         // leaderboard = [[2,56],[3,39],[4,51],[5,4]];
leaderboard.reset(2);         // leaderboard = [[3,39],[4,51],[5,4]];
leaderboard.addScore(2,51);   // leaderboard = [[2,51],[3,39],[4,51],[5,4]];
leaderboard.top(3);           // returns 141 = 51 + 51 + 39;
``` 

**Constraints:**

* `1 <= playerId, K <= 10000`
* It's guaranteed that `K` is less than or equal to the current number of players.
* `1 <= score <= 100`
* There will be at most `1000` function calls.

# Submissions
---
**Solution 1: (Hash Table)**
```
Runtime: 120 ms
Memory Usage: 14 MB
```
```python
class Leaderboard:

    def __init__(self):
        self.A = collections.Counter()

    def addScore(self, playerId: int, score: int) -> None:
        self.A[playerId] += score

    def top(self, K: int) -> int:
        return sum(v for i,v in self.A.most_common(K))

    def reset(self, playerId: int) -> None:
        self.A[playerId] = 0

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
```

**Solution 2: (multiset)**
```
Runtime: 7 ms, Beats 36.57%
Memory: 17.44 MB, Beats 65.74%
```
```c++
class Leaderboard {
    unordered_map<int, int> cnt;
    multiset<int> st;
public:
    Leaderboard() {
    }
    
    void addScore(int playerId, int score) {
        if (cnt.count(playerId)) {
            score += cnt[playerId];
            auto it = st.find(cnt[playerId]);
            st.erase(it);
            cnt.erase(playerId);
        }
        cnt[playerId] = score;
        st.insert(score);
    }
    
    int top(int K) {
        int rst = 0;
        auto it = st.rbegin();
        while (K) {
            rst += *it;
            it++;
            K -= 1;
        }
        return rst;
    }
    
    void reset(int playerId) {
        auto it = st.find(cnt[playerId]);
        st.erase(it);
        cnt.erase(playerId);
    }
};

/**
 * Your Leaderboard object will be instantiated and called as such:
 * Leaderboard* obj = new Leaderboard();
 * obj->addScore(playerId,score);
 * int param_2 = obj->top(K);
 * obj->reset(playerId);
 */
```

**Solution 3: (Set)**

Leaderboard leaderboard = new Leaderboard ();
leaderboard.addScore(1,73);   // leaderboard = [[1,73]];
mp    1
      |
st    v
    {73,1}
leaderboard.addScore(2,56);   // leaderboard = [[1,73],[2,56]];
mp      2      1 
        |      | 
st      v      v 
    (56,2) {73,1}
leaderboard.addScore(3,39);   // leaderboard = [[1,73],[2,56],[3,39]];
mp      3     2      1 
        |     |      | 
st      v     v      v 
    (39,3)(56,2) {73,1}
leaderboard.addScore(4,51);   // leaderboard = [[1,73],[2,56],[3,39],[4,51]];
mp      3      4      2      1 
        |      |      |      | 
st      v      v      v      v 
    (39,3) (51,4) (56,2) {73,1}
leaderboard.addScore(5,4);    // leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
mp     5      3      4      2      1 
       |      |      |      |      | 
st     v      v      v      v      v 
    (4,5) (39,3) (51,4) (56,2) {73,1}
leaderboard.top(1);           // returns 73;
mp     5      3      4      2      1 
       |      |      |      |      | 
st     v      v      v      v      v 
    (4,5) (39,3) (51,4) (56,2) {73,1}
                                ^^   
leaderboard.reset(1);         // leaderboard = [[2,56],[3,39],[4,51],[5,4]];
                                   x
mp     5      3      4      2      1 
       |      |      |      |      | 
st     v      v      v      v      v 
    (4,5) (39,3) (51,4) (56,2) {73,1}
                                  x
leaderboard.reset(2);         // leaderboard = [[3,39],[4,51],[5,4]];
                            x
mp     5      3      4      2 
       |      |      |      | 
st     v      v      v      v 
    (4,5) (39,3) (51,4) (56,2)
                           x
leaderboard.addScore(2,51);   // leaderboard = [[2,51],[3,39],[4,51],[5,4]];
mp     5      3      2      4 
       |      |      |      | 
st     v      v      v      v 
    (4,5) (39,3) (51,2) (51,4)
leaderboard.top(3);           // returns 141 = 51 + 51 + 39;
mp     5      3      2      4 
       |      |      |      | 
st     v      v      v      v 
    (4,5) (39,3) (51,2) (51,4)
           ^^     ^^     ^^

```
Runtime=: 3 ms, Beats 66.20%
Memory: 17.51 MB, Beats 51.39%
```
```c++
class Leaderboard {
    unordered_map<int, set<pair<int, int>>::iterator> mp;
    set<pair<int, int>> st;
public:
    Leaderboard() {
    }
    
    void addScore(int playerId, int score) {
        if (mp.count(playerId)) {
            score += mp[playerId]->first;
            st.erase(mp[playerId]);
            mp.erase(playerId);
        }
        auto [it, _] = st.insert({score, playerId});
        mp[playerId] = it;
    }
    
    int top(int K) {
        int rst = 0;
        auto it = st.rbegin();
        while (K) {
            rst += it->first;
            it++;
            K -= 1;
        }
        return rst;
    }
    
    void reset(int playerId) {
        st.erase(mp[playerId]);
        mp.erase(playerId);
    }
};

/**
 * Your Leaderboard object will be instantiated and called as such:
 * Leaderboard* obj = new Leaderboard();
 * obj->addScore(playerId,score);
 * int param_2 = obj->top(K);
 * obj->reset(playerId);
 */
```
