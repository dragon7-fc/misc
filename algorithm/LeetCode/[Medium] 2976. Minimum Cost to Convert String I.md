2976. Minimum Cost to Convert String I

You are given two **0-indexed** strings `source` and `target`, both of length `n` and consisting of lowercase English letters. You are also given two **0-indexed** character arrays `original` and `changed`, and an integer array `cost`, where `cost[i]` represents the cost of changing the character original[i] to the character changed[i].

You start with the string `source`. In one operation, you can pick a character `x` from the string and change it to the character `y` at a cost of `z` if there exists any index `j` such that `cost[j] == z`, `original[j] == x`, and `changed[j] == y`.

Return the **minimum** cost to convert the string `source` to the string `target` using any number of operations. If it is impossible to convert `source` to `target`, return `-1`.

**Note** that there may exist indices `i`, `j` such that `original[j] == original[i]` and `changed[j] == changed[i]`.

 

**Example 1:**
```
Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
Output: 28
Explanation: To convert the string "abcd" to string "acbe":
- Change value at index 1 from 'b' to 'c' at a cost of 5.
- Change value at index 2 from 'c' to 'e' at a cost of 1.
- Change value at index 2 from 'e' to 'b' at a cost of 2.
- Change value at index 3 from 'd' to 'e' at a cost of 20.
The total cost incurred is 5 + 1 + 2 + 20 = 28.
It can be shown that this is the minimum possible cost.
```

**Example 2:**
```
Input: source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2]
Output: 12
Explanation: To change the character 'a' to 'b' change the character 'a' to 'c' at a cost of 1, followed by changing the character 'c' to 'b' at a cost of 2, for a total cost of 1 + 2 = 3. To change all occurrences of 'a' to 'b', a total cost of 3 * 4 = 12 is incurred.
```

**Example 3:**
```
Input: source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000]
Output: -1
Explanation: It is impossible to convert source to target because the value at index 3 cannot be changed from 'd' to 'e'.
```

**Constraints:**

* `1 <= source.length == target.length <= 10^5`
* `source`, `target` consist of lowercase English letters.
* `1 <= cost.length == original.length == changed.length <= 2000`
* `original[i]`, `changed[i]` are lowercase English letters.
* `1 <= cost[i] <= 10^6`
* `original[i] != changed[i]`

# Submissions
---
**Solution 1: (Floyd-Warshall, all source shortest path)**
```
Runtime: 337 ms
Memory: 94 MB
```
```c++
class Solution {
public:
    long long minimumCost(string source, string target, vector<char>& original, vector<char>& changed, vector<int>& cost) {
        long long res = 0;
        vector<vector<long long>> d(26, vector<long long>(26, INT_MAX));
        for (int i = 0; i < original.size(); ++i) {
            int s = original[i] - 'a', t = changed[i] - 'a';
            d[s][t] = d[s][t] == 0 ? cost[i] : min(d[s][t], (long long)cost[i]);
        }
        for (int k = 0; k < 26; ++k) {
            for (int i = 0; i < 26; ++i) {
                for (int j = 0; j < 26; ++j) {
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j]); 
                }
            }
        }
        for (int i = 0; i < source.size(); ++i) {
            if (source[i] == target[i])
                continue;
            int s = source[i] - 'a', t = target[i] - 'a';
            if (d[s][t] >= INT_MAX)
                return -1;
            res += d[s][t];
        }
        return res;
    }
};
```

**Solution 2: (Dijkstra, single source shortest path)**
```
Runtime: 540 ms
Memory: 166.6 MB
```
```c++
typedef pair<int,int> pii;

class Solution {
public:
    long long minimumCost(string source, string target, vector<char>& original, vector<char>& changed, vector<int>& cost) {
        vector<vector<pii>> adj(26);
        for (int i = 0; i < original.size(); i++) {
            adj[original[i]-'a'].push_back({changed[i]-'a', cost[i]});
        }
        
        vector<vector<int>> memo(26, vector<int>(26, -1));
        
        function<int(int,int)> dijkstra = [&](int s, int e) {
            if (memo[s][e] != -1) return memo[s][e];
            
            int n = adj.size();
            vector<int> dist(n, INT_MAX);
            dist[s] = 0;

            priority_queue<pii, vector<pii>, greater<pii>> minq;
            minq.push({0, s});

            int u, v, w;
            while (!minq.empty()) {
                auto p = minq.top(); minq.pop();
                u = p.second;

                if (dist[u] < p.first)
                    continue;

                if (u == e)
                    return memo[s][e] = p.first;

                for (auto& node: adj[u]) {
                    v = node.first, w = node.second;
                    if (dist[v] > dist[u] + w) {
                        dist[v] = dist[u] + w;
                        minq.push({dist[v], v});
                    }
                }
            }
            return memo[s][e] = (dist[e] == INT_MAX ? -2 : dist[e]);
        };
        
        long long res = 0;
        for (int i = 0; i < source.size(); i++) {
            if (source[i] != target[i]) {
                int c = dijkstra(source[i]-'a', target[i]-'a');
                if (c < 0) return -1;
                res += c;
            }
        }
        return res;
    }
};
```
