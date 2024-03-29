649. Dota2 Senate

In the world of Dota2, there are two parties: the `Radiant` and the `Dire`.

The Dota2 senate consists of senators coming from two parties. Now the senate wants to make a decision about a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise `one` of the two rights:

1. `Ban one senator's right`:

    A senator can make another senator lose **all his rights** in this and all the following rounds.
1. `Announce the victory`:

    If this senator found the senators who still have rights to vote are all from **the same party**, he can announce the victory and make the decision about the change in the game.
 

Given a string representing each senator's party belonging. The character `'R'` and `'D'` represent the `Radiant` party and the `Dire` party respectively. Then if there are `n` senators, the size of the given string will be `n`.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party, you need to predict which party will finally announce the victory and make the change in the Dota2 game. The output should be `Radiant` or `Dire`.

**Example 1:**
```
Input: "RD"
Output: "Radiant"
Explanation: The first senator comes from Radiant and he can just ban the next senator's right in the round 1. 
And the second senator can't exercise any rights any more since his right has been banned. 
And in the round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
```

**Example 2:**
```
Input: "RDD"
Output: "Dire"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in the round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And the third senator comes from Dire and he can ban the first senator's right in the round 1. 
And in the round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
```

**Note:**

* The length of the given string will in the range `[1, 10,000]`.

# Solution
---
## Approach #1: Simulation [Accepted]
**Intuition**

A senator performing a ban doesn't need to use it on another senator immediately. We can wait to see when another team's senator will vote, then use that ban retroactively.

**Algorithm**

Put the senators in an integer `queue`: `1` for `'Radiant'` and `0` for `'Dire'`.

Now process the `queue`: if there is a floating `ban` for that senator, exercise it and continue. Otherwise, add a floating `ban` against the other team, and enqueue this senator again.

```python
def predictPartyVictory(self, senate):
    queue = collections.deque()
    people, bans = [0, 0], [0, 0]

    for person in senate:
        x = person == 'R'
        people[x] += 1
        queue.append(x)

    while all(people):
        x = queue.popleft()
        if bans[x]:
            bans[x] -= 1
            people[x] -= 1
        else:
            bans[x^1] += 1
            queue.append(x)

    return "Radiant" if people[1] else "Dire"
```

**Complexity Analysis**

* Time Complexity: $O(N)$ where $N$ is the size of the senate. Every vote removes one senator from the other team.

* Space Complexity: $O(N)$, the space used by our queue.

# Submissions
---
**Solution: (Simulation)**
```
Runtime: 72 ms
Memory Usage: 13 MB
```
```python
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = collections.deque()
        people, bans = [0, 0], [0, 0]

        for person in senate:
            x = person == 'R'
            people[x] += 1
            queue.append(x)

        while all(people):
            x = queue.popleft()
            if bans[x]:
                bans[x] -= 1
                people[x] -= 1
            else:
                bans[x^1] += 1
                queue.append(x)

        return "Radiant" if people[1] else "Dire"
```

**Solution 1; (Queue)**
```
Runtime: 8 ms
Memory: 8 MB
```
```c++
class Solution {
public:
    string predictPartyVictory(string senate) {
        queue<int> rad, dir;
        int n = senate.length();
        // Add all senators to respect queue with index
        for (int i = 0; i < n; i++){
            if (senate[i] == 'R'){
                rad.push(i);
            }
            else {
                dir.push(i);
            }
        }
        // Use increasing n to keep track of position
        while (!rad.empty() && !dir.empty()){
            // Only "winner" stays in their queue
            if (rad.front() < dir.front()){
                rad.push(n++);
            }
            else {
                dir.push(n++);
            }
            rad.pop(), dir.pop();
        }
        return (rad.empty()) ? ("Dire") : ("Radiant");
    }
};
```
