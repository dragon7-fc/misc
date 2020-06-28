332. Reconstruct Itinerary

Given a list of airline tickets represented by pairs of departure and arrival airports `[from, to]`, reconstruct the itinerary in order. All of the tickets belong to a man who departs from `JFK`. Thus, the itinerary must begin with `JFK`.

**Note:**

* If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary `["JFK", "LGA"]` has a smaller lexical order than `["JFK", "LGB"]`.
* All airports are represented by three capital letters (IATA code).
* You may assume all tickets form at least one valid itinerary.

**Example 1:**
```
Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
```

**Example 2:**
```
Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
```

# Submissions
---
**Solution 1: (DFS, Graph)**
```
Runtime: 88 ms
Memory Usage: 13.2 MB
```
```python
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        
        for departure, arrival in tickets:
             graph[departure].append(arrival)
                
        for airport in graph:
            graph[airport].sort()
                
        total = len(tickets) + 1
        
        def dfs(ticket, way):
            if len(way) == total:
                return way
            
            for i in range(len(graph[ticket])):
                if graph[ticket][i] == None:
                    continue
                    
                arrival = graph[ticket][i]
                graph[ticket][i] = None
                
                reconstruction = dfs(arrival, way + [arrival])
                if reconstruction:
                    return reconstruction
                
                graph[ticket][i] = arrival
                
        return dfs('JFK', ['JFK'])
```

**Solution 2: (DFS)**
```
Runtime: 48 ms
Memory Usage: 15.4 MB
```
```c++
class Solution {
public:
    void dfs(string src,unordered_map<string,vector<string>>& m,vector<string>& ans){
        while(!m[src].empty()){
            string s=m[src].back();
            m[src].pop_back();
            dfs(s,m,ans);
        }
        ans.push_back(src);
    }
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        unordered_map<string,vector<string>> m;
        // Create Graph
        for(auto i:tickets)
            m[i[0]].push_back(i[1]);
        // Sorting in descending order since we will be popping elements from the end
        for(auto &i:m)
            sort(i.second.begin(),i.second.end(),greater<string>());  

        vector<string> ans;
        dfs("JFK",m,ans);
        reverse(ans.begin(),ans.end());
        return ans;
    }
};
```