1488. Avoid Flood in The City

Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the nth lake, the nth lake becomes full of water. If it rains over a lake which is **full of water**, there will be a **flood**. Your goal is to avoid the flood in any lake.

Given an integer array rains where:

* `rains[i] > 0` means there will be rains over the `rains[i]` lake.
* `rains[i] == 0` means there are no rains this day and you can choose **one lake** this day and **dry** it.

Return an array `ans` where:

* `ans.length == rains.length`
* `ans[i] == -1 if rains[i] > 0.`
* `ans[i]` is the lake you choose to dry in the `i`th day if `rains[i] == 0`.

If there are multiple valid answers return **any** of them. If it is impossible to avoid flood return an **empty array**.

Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes. (see example 4)

**Example 1:**
```
Input: rains = [1,2,3,4]
Output: [-1,-1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day full lakes are [1,2,3]
After the fourth day full lakes are [1,2,3,4]
There's no day to dry any lake and there is no flood in any lake.
```

**Example 2:**
```
Input: rains = [1,2,0,0,2,1]
Output: [-1,-1,2,1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day, we dry lake 2. Full lakes are [1]
After the fourth day, we dry lake 1. There is no full lakes.
After the fifth day, full lakes are [2].
After the sixth day, full lakes are [1,2].
It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another acceptable scenario.
```

**Example 3:**
```
Input: rains = [1,2,0,1,2]
Output: []
Explanation: After the second day, full lakes are  [1,2]. We have to dry one lake in the third day.
After that, it will rain over lakes [1,2]. It's easy to prove that no matter which lake you choose to dry in the 3rd day, the other one will flood.
```

**Example 4:**
```
Input: rains = [69,0,0,0,69]
Output: [-1,69,1,1,-1]
Explanation: Any solution on one of the forms [-1,69,x,y,-1], [-1,x,69,y,-1] or [-1,x,y,69,-1] is acceptable where 1 <= x,y <= 10^9
```

**Example 5:**
```
Input: rains = [10,20,20]
Output: []
Explanation: It will rain over lake 20 two consecutive days. There is no chance to dry any lake.
```

**Constraints:**

* `1 <= rains.length <= 10^5`
* `0 <= rains[i] <= 10^9`

# Submissions
---
**Solution 1: (Greedy, Heap, Set)**
```
Runtime: 1256 ms
Memory Usage: 78.5 MB
```
```python
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        seen = set()
        closest = []
        locs = collections.defaultdict(collections.deque)
        for i, lake in enumerate(rains):
            locs[lake].append(i)
        ret = []
        for lake in rains:
            if lake in seen:
                return []
            if not lake:
                # get closest that's already seen
                if not closest:
                    # there's nothing filled that will be filled again later
                    ret.append(1) 
                    continue
                nxt = heapq.heappop(closest)
                ret.append(rains[nxt])
                seen.remove(rains[nxt])
            else:
                seen.add(lake)
                l = locs[lake]
                l.popleft()
                if l:
                    nxt = l[0]
                    heapq.heappush(closest, nxt)
                ret.append(-1)
        return ret
```

**Solution 2: (Greedy, Heap, Set)**
```
Runtime: 992 ms
Memory Usage: 378.4 MB
```
```c++
class Solution {
public:
    vector<int> avoidFlood(vector<int>& rains) {
        using myPair = pair<int, int>;

        unordered_map<int, deque<int>> m;
        unordered_set<int> s;
        priority_queue<myPair, vector<myPair>, greater<myPair>> q;

        for (int i = 0; i < rains.size(); ++i) {
            if (rains[i] > 0) m[rains[i]].push_back(i);
        }

        for (int i = 0; i < rains.size(); ++i) {

            if (rains[i] > 0) {
                if (s.count(rains[i])) return vector<int>();
                s.insert(rains[i]);
                m[rains[i]].pop_front();
                if (!m[rains[i]].empty()) q.push({m[rains[i]].front(), rains[i]});
                rains[i] = -1;
            } else {
                if (!q.empty()) {
                    myPair tmp = q.top();
                    q.pop();
                    rains[i] = tmp.second;
                    s.erase(tmp.second);
                } else {
                    rains[i] = 1;
                }
            }

        }

        return rains;
    }
};
```