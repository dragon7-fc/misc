752. Open the Lock

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: `'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'`. The wheels can rotate freely and wrap around: for example we can turn `'9'` to be `'0'`, or `'0'` to be `'9'`. Each move consists of turning one wheel one slot.

The lock initially starts at `'0000'`, a string representing the state of the `4` wheels.

You are given a list of `deadends` dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or `-1` if it is impossible.

**Example 1:**
```
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
```

**Example 2:**
```
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".
```

**Example 3:**
```
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.
```

**Example 4:**
```
Input: deadends = ["0000"], target = "8888"
Output: -1
```

**Note:**

* The length of deadends will be in the range `[1, 500]`.
* `target` will not be in the list deadends.
* Every string in deadends and the string target will be a string of 4 digits from the `10,000` possibilities `'0000'` to `'9999'`.

# Submissions
---
**Solution 1: (BFS)**
```
Runtime: 1048 ms
Memory Usage: 15.4 MB
```
```python
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def neighbors(code):
            for i in range(4):
                x = int(code[i])
                for diff in (-1, 1):
                    y = (x + diff + 10) % 10
                    yield code[:i] + str(y) + code[i + 1:]

        deadSet = set(deadends)
        if "0000" in deadSet: return -1
        q = deque(["0000"])
        steps = 0
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == target:
                    return steps
                for nei in neighbors(curr):
                    if nei in deadSet: continue
                    deadSet.add(nei)  # Marked as visited
                    q.append(nei)
            steps += 1

        return -1
```

**Solution 2: (BFS)**
```
Runtime: 344 ms
Memory Usage: 34.6 MB
```
```c++
class Solution {
public:
    unordered_set<string> hash;
    int openLock(vector<string>& deadends, string target) {
        for(int i=0;i<deadends.size();i++){
            if(deadends[i]=="0000") return -1;
            hash.insert(deadends[i]);
        }
        queue<string> q; q.push("0000"); hash.insert("0000");
        int moves=0;
        vector<int> x = {-1,1};
        while(!q.empty()){
            int size=q.size();
            while(size--){
                string front = q.front(); q.pop();
                if(front==target) return moves;
                for(int i=0;i<4;i++){
                    string temp = front;
                    for(int j=0;j<2;j++){
                        front[i]=(((front[i]-'0')+10+x[j])%10 + '0');
                        if(!hash.count(front)){
                            hash.insert(front);
                            q.push(front);
                        }
                        front=temp;
                    }
                }
            }
            moves++;
        }
        return -1;
    }
};
```
