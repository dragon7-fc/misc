841. Keys and Rooms

There are `N` rooms and you start in room `0`.  Each room has a distinct number in `0, 1, 2, ..., N-1`, and each room may have some keys to access the next room. 

Formally, each room `i` has a list of keys `rooms[i]`, and each key `rooms[i][j]` is an integer in `[0, 1, ..., N-1]` where `N = rooms.length`.  A key `rooms[i][j] = v` opens the room with number `v`.

Initially, all the rooms start locked (except for room `0`). 

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

**Example 1:**
```
Input: [[1],[2],[3],[]]
Output: true
Explanation:  
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.
```

**Example 2:**
```
Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.
```

**Note:**

* `1 <= rooms.length <= 1000`
* `0 <= rooms[i].length <= 1000`
* The number of keys in all rooms combined is at most `3000`.

# Solution
---
## Approach #1: Depth-First Search [Accepted]
**Intuition and Algorithm**

When visiting a room for the first time, look at all the keys in that room. For any key that hasn't been used yet, add it to the todo list (`stack`) for it to be used.

See the comments of the code for more details.

```python
class Solution(object):
    def canVisitAllRooms(self, rooms):
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]
        #At the beginning, we have a todo list "stack" of keys to use.
        #'seen' represents at some point we have entered this room.
        while stack:  #While we have keys...
            node = stack.pop() # get the next key 'node'
            for nei in rooms[node]: # For every key in room # 'node'...
                if not seen[nei]: # ... that hasn't been used yet
                    seen[nei] = True # mark that we've entered the room
                    stack.append(nei) # add the key to the todo list
        return all(seen) # Return true iff we've visited every room
```

# Submissions
---
**Solution: (DFS, Stack, Graph)**
```
Runtime: 68 ms
Memory Usage: 13.2 MB
```
```python
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]
        #At the beginning, we have a todo list "stack" of keys to use.
        #'seen' represents at some point we have entered this room.
        while stack:  #While we have keys...
            node = stack.pop() # get the next key 'node'
            for nei in rooms[node]: # For every key in room # 'node'...
                if not seen[nei]: # ... that hasn't been used yet
                    seen[nei] = True # mark that we've entered the room
                    stack.append(nei) # add the key to the todo list
        return all(seen) # Return true iff we've visited every room
```

**Solution 1: (DFS, Graph)**
```
Runtime: 64 ms
Memory Usage: 13.5 MB
```
```python
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set()
        
        def dfs(room):
            if room in seen:
                return
            seen.add(room)
            
            for nei in rooms[room]:
                if nei not in seen:
                    dfs(nei)
        
        dfs(0)
        
        return len(seen)== len(rooms)
```

**Solution 2: (DFS)**
```
Runtime: 8 ms
Memory Usage: 6.5 MB
```
```c
void dfs(int i, bool* seen, int **rooms, int *roomsColSize) {
    seen[i] = true;
    for (int j = 0; j < roomsColSize[i]; j ++) {
        if (!seen[rooms[i][j]])
            dfs(rooms[i][j], seen, rooms, roomsColSize); 
    }
}

bool canVisitAllRooms(int** rooms, int roomsSize, int* roomsColSize){
    bool *seen = calloc(1, roomsSize*sizeof(bool));
    dfs(0, seen, rooms, roomsColSize);
    for (int i = 0; i < roomsSize; i ++) {
        if (!seen[i])
            return false;
    }
    return true;
}
```

**Solution 3: (DFS)**
```
Runtime: 12 ms
Memory Usage: 10.3 MB
```
```c++
class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        vector<bool> seen (rooms.size(), false);
        seen[0] = true;
        stack<int> stk;
        stk.push(0);
        while (!stk.empty()) {
            int node = stk.top();
            stk.pop();
            for (auto nei: rooms[node]) {
                if (!seen[nei]) {
                    seen[nei] = true;
                    stk.push(nei);
                }
            }
        }
        return all_of(seen.begin(), seen.end(), [](bool x) {return x == true;});
    }
};
```

**Solution4 : (DFS)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 14.76 MB, Beats 34.84%
```
```c++
class Solution {
    void dfs(int u, vector<vector<int>> &g, vector<int> &visited) {
        visited[u] = 1;
        for (auto v: g[u]) {
            if (!visited[v]) {
                dfs(v, g, visited);
            }
        }
    }
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        vector<int> visited(n);
        dfs(0, rooms, visited);
        return count(visited.begin(), visited.end(), 1) == n;
    }
};

```
