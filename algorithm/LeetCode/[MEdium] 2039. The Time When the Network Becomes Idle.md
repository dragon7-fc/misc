2039. The Time When the Network Becomes Idle

There is a network of `n` servers, labeled from `0` to `n - 1`. You are given a 2D integer array `edges`, where `edges[i] = [ui, vi]` indicates there is a message channel between servers `ui` and `vi`, and they can pass any number of messages to each other directly in one second. You are also given a **0-indexed** integer array `patience` of length `n`.

All servers are **connected**, i.e., a message can be passed from one server to any other server(s) directly or indirectly through the message channels.

The server labeled `0` is the **master** server. The rest are **data** servers. Each data server needs to send its message to the master server for processing and wait for a reply. Messages move between servers **optimally**, so every message takes the **least amount of time** to arrive at the master server. The master server will process all newly arrived messages **instantly** and send a reply to the originating server via the **reversed path** the message had gone through.

At the beginning of second `0`, each data server sends its message to be processed. Starting from second 1, at the **beginning** of **every** second, each data server will check if it has received a reply to the message it sent (including any newly arrived replies) from the master server:

* If it has not, it will **resend** the message periodically. The data server i will resend the message every `patience[i]` second(s), i.e., the data server i will resend the message if `patience[i]` second(s) have **elapsed** since the last **time** the message was sent from this server.
* Otherwise, **no more resending** will occur from this server.

The network becomes **idle** when there are no messages passing between servers or arriving at servers.

Return the **earliest second** starting from which the network becomes **idle**.

 

**Example 1:**

![2039_quiet-place-example1.png](img/2039_quiet-place-example1.png)
```
Input: edges = [[0,1],[1,2]], patience = [0,2,1]
Output: 8
Explanation:
At (the beginning of) second 0,
- Data server 1 sends its message (denoted 1A) to the master server.
- Data server 2 sends its message (denoted 2A) to the master server.

At second 1,
- Message 1A arrives at the master server. Master server processes message 1A instantly and sends a reply 1A back.
- Server 1 has not received any reply. 1 second (1 < patience[1] = 2) elapsed since this server has sent the message, therefore it does not resend the message.
- Server 2 has not received any reply. 1 second (1 == patience[2] = 1) elapsed since this server has sent the message, therefore it resends the message (denoted 2B).

At second 2,
- The reply 1A arrives at server 1. No more resending will occur from server 1.
- Message 2A arrives at the master server. Master server processes message 2A instantly and sends a reply 2A back.
- Server 2 resends the message (denoted 2C).
...
At second 4,
- The reply 2A arrives at server 2. No more resending will occur from server 2.
...
At second 7, reply 2D arrives at server 2.

Starting from the beginning of the second 8, there are no messages passing between servers or arriving at servers.
This is the time when the network becomes idle.
```

**Example 2:**
![2039_network_a_quiet_place_2.png](img/2039_network_a_quiet_place_2.png)
```
Input: edges = [[0,1],[0,2],[1,2]], patience = [0,10,10]
Output: 3
Explanation: Data servers 1 and 2 receive a reply back at the beginning of second 2.
From the beginning of the second 3, the network becomes idle.
```

**Constraints:**

* `n == patience.length`
* `2 <= n <= 10^5`
* `patience[0] == 0`
* `1 <= patience[i] <= 105 for 1 <= i < n`
* `1 <= edges.length <= min(105, n * (n - 1) / 2)`
* `edges[i].length == 2`
* `0 <= ui, vi < n`
* `ui != vi`
* There are no duplicate edges.
* Each server can directly or indirectly reach another server.

# Submissions
---
**Solution 1: (BFS)**
```
Runtime: 2396 ms
Memory Usage: 68.8 MB
```
```python
class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        #Build Adjency List
        adjList = defaultdict(list)
        
        for source, target in edges:
            adjList[source].append(target)
            adjList[target].append(source)
            
        
        #BFS to get the shortest route from node to master.
        shortest = {}
        queue = deque([(0,0)])
        seen = set()
        while queue:
            currPos, currDist = queue.popleft()
            
            if currPos in seen:
                continue
            seen.add(currPos)
            shortest[currPos] = currDist
            
            for nei in adjList[currPos]:
                queue.append((nei, currDist+1))

                
        #Calculate answer using shortest paths.
        ans = 0
        for index in range(1,len(patience)):
            resendInterval = patience[index]
                
            #The server will stop sending requests after it's been sent to the master node and back.
            shutOffTime = (shortest[index] * 2)
            
            # shutOffTime-1 == Last second the server can send a re-request.
            lastSecond = shutOffTime-1
            
            #Calculate the last time a packet is actually resent.
            lastResentTime = (lastSecond//resendInterval)*resendInterval
            
            # At the last resent time, the packet still must go through 2 more cycles to the master node and back.
            lastPacketTime = lastResentTime + shutOffTime
            
            ans = max(lastPacketTime, ans)
            
        #Add +1, the current answer is the last time the packet is recieved by the target server (still active).
        #We must return the first second the network is idle, therefore + 1
        return ans + 1
```

**Solution 2: (BFS)**
```
Runtime: 616 ms
Memory Usage: 204.6 MB
```
```c++
class Solution {
public:
    int networkBecomesIdle(vector<vector<int>>& edges, vector<int>& patience) {
        int n = patience.size();
        vector <vector <int>> graph(n);
        vector <int> time(n, -1);
        
        for(auto x: edges) { // create adjacency list
            graph[x[0]].push_back(x[1]);
            graph[x[1]].push_back(x[0]);
        }
        
        queue <int> q;
        q.push(0);
        time[0] = 0;
        while(q.size()) {
            int node = q.front();
            q.pop();
            
            for(auto child: graph[node]) {
                if(time[child] == -1) { // if not visited.
                    time[child] = time[node] + 1; // calc time for child node
                    q.push(child);
                }
            }
        }
        
        int res = 0;
        for(int i = 1; i<n; i++) {
            int extraPayload = (time[i]*2 - 1)/patience[i]; // extra number of payload before the first message arrive back to data server.
			// since a data server can only send a message before first message arrives back."
			// and first message arrives at time[i]*2. so "time[i]*2-1
            int lastOut = extraPayload * patience[i]; // find the last time when a data server sends a message
            int lastIn = lastOut + time[i]*2; // this is the result for current data server
            res = max(res, lastIn);
        }
        return res+1; // since till res time all messages has beed arrived so +1
    }
};
```
