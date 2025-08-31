3664. Two-Letter Card Game

You are given a deck of cards represented by a string array `cards`, and each card displays two lowercase letters.

You are also given a letter `x`. You play a game with the following rules:

* Start with 0 points.
* On each turn, you must find two **compatible** cards from the deck that both contain the letter `x` in any position.
* Remove the pair of cards and earn 1 point.
* The game ends when you can no longer find a pair of compatible cards.

Return the **maximum** number of points you can gain with optimal play.

Two cards are **compatible** if the strings differ in **exactly** 1 position.

 

**Example 1:**
```
Input: cards = ["aa","ab","ba","ac"], x = "a"

Output: 2

Explanation:

On the first turn, select and remove cards "ab" and "ac", which are compatible because they differ at only index 1.
On the second turn, select and remove cards "aa" and "ba", which are compatible because they differ at only index 0.
Because there are no more compatible pairs, the total score is 2.
```

**Example 2:**
```
Input: cards = ["aa","ab","ba"], x = "a"

Output: 1

Explanation:

On the first turn, select and remove cards "aa" and "ba".
Because there are no more compatible pairs, the total score is 1.
```

**Example 3:**
```
Input: cards = ["aa","ab","ba","ac"], x = "b"

Output: 0

Explanation:

The only cards that contain the character 'b' are "ab" and "ba". However, they differ in both indices, so they are not compatible. Thus, the output is 0.
```

**Constraints:**

* `2 <= cards.length <= 10^5`
* `cards[i].length == 2`
* Each `cards[i]` is composed of only lowercase English letters between `'a'` and `'j'`.
* `x` is a lowercase English letter between `'a'` and `'j'`.

# Submissions
---
**Solution 1: (Counter)**
```
Runtime: 24 ms, Beats 51.11%
Runtime: 24 ms, Beats 51.11%
```
```c++
class Solution {
public:
    int score(vector<string>& cards, char x) {
        // Groups:
        // leftgroup : cards where s[0] == x
        // rightgroup: cards where s[1] == x
        // XXCHAR    : cards where both characters are x
        map<int, int> leftgroup;
        map<int, int> rightgroup;
        int XXCHAR = 0;

        for (auto &a : cards) {
            if (a[0] == x && a[1] == x) {
                XXCHAR++;
            } else if (a[0] == x) {
                leftgroup[a[1] - 'a']++;
            } else if (a[1] == x) {
                rightgroup[a[0] - 'a']++;
            }
        }

        // Max-heaps for pairing within left/right groups
        priority_queue<int> lpq;
        priority_queue<int> rpq;

        for (auto &a : leftgroup) lpq.push(a.second);
        for (auto &a : rightgroup) rpq.push(a.second);

        int ans = 0;

        // Pair cards inside left group
        while (lpq.size() > 1) {
            int a = lpq.top(); lpq.pop();
            int b = lpq.top(); lpq.pop();
            a--; b--;                // form 1 pair
            if (a > 0) lpq.push(a);
            if (b > 0) lpq.push(b);
            ans++;
        }

        // Pair cards inside right group
        while (rpq.size() > 1) {
            int a = rpq.top(); rpq.pop();
            int b = rpq.top(); rpq.pop();
            a--; b--;                // form 1 pair
            if (a > 0) rpq.push(a);
            if (b > 0) rpq.push(b);
            ans++;
        }

        // Collect leftovers from PQ
        int totalLeftFreq = 0;
        while (!lpq.empty()) {
            totalLeftFreq += lpq.top();
            lpq.pop();
        }
        int totalRightFreq = 0;
        while (!rpq.empty()) {
            totalRightFreq += rpq.top();
            rpq.pop();
        }

        int ansTillNow = ans;

        // First, pair leftover LEFT chars with XX
        int c = min(totalLeftFreq, XXCHAR);
        ans += c;
        XXCHAR -= c;

        // Then, pair leftover RIGHT chars with XX
        if (XXCHAR > 0) {
            int c = min(totalRightFreq, XXCHAR);
            ans += c;
            XXCHAR -= c;
        }

        // Special case:
        // If XX still remains, we can "improve" some already-formed pairs
        // Example: 1 ac + 1 ab paired, 2 aa remain.
        // Better: (aa + ac) + (aa + ab) → so ans += min(ansTillNow, XXCHAR/2)
        if (XXCHAR > 0) {
            ans += min(ansTillNow, XXCHAR / 2);
        }

        return ans;
    }
};
```
