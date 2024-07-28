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

**Solution 1: (Dijkstra, single source shortest path, O(m + n))**
```
Runtime: 156 ms
Memory: 117.47 MB
```
```c++
class Solution {
    // Find minimum conversion costs from a starting character to all other
    // characters
    vector<long long> dijkstra(
        int startChar, const vector<vector<pair<int, int>>>& adjacencyList) {
        // Priority queue to store characters with their conversion cost, sorted
        // by cost
        priority_queue<pair<long long, int>, vector<pair<long long, int>>,
                       greater<pair<long long, int>>>
            priorityQueue;

        // Initialize the starting character with cost 0
        priorityQueue.push({0, startChar});

        // Array to store the minimum conversion cost to each character
        vector<long long> minCosts(26, -1);

        while (!priorityQueue.empty()) {
            auto [currentCost, currentChar] = priorityQueue.top();
            priorityQueue.pop();

            if (minCosts[currentChar] != -1 &&
                minCosts[currentChar] < currentCost)
                continue;

            // Explore all possible conversions from the current character
            for (auto& [targetChar, conversionCost] :
                 adjacencyList[currentChar]) {
                long long newTotalCost = currentCost + conversionCost;

                // If we found a cheaper conversion, update its cost
                if (minCosts[targetChar] == -1 ||
                    newTotalCost < minCosts[targetChar]) {
                    minCosts[targetChar] = newTotalCost;
                    // Add the updated conversion to the queue for further
                    // exploration
                    priorityQueue.push({newTotalCost, targetChar});
                }
            }
        }
        // Return the array of minimum conversion costs from the starting
        // character to all others
        return minCosts;
    }
public:
    long long minimumCost(string source, string target, vector<char>& original, vector<char>& changed, vector<int>& cost) {
        // Create a graph representation of character conversions
        vector<vector<pair<int, int>>> adjacencyList(26);

        // Populate the adjacency list with character conversions
        int conversionCount = original.size();
        for (int i = 0; i < conversionCount; i++) {
            adjacencyList[original[i] - 'a'].push_back(
                {changed[i] - 'a', cost[i]});
        }

        // Calculate shortest paths for all possible character conversions
        vector<vector<long long>> minConversionCosts(26, vector<long long>(26));
        for (int i = 0; i < 26; i++) {
            minConversionCosts[i] = dijkstra(i, adjacencyList);
        }

        // Calculate the total cost of converting source to target
        long long totalCost = 0;
        int stringLength = source.length();
        for (int i = 0; i < stringLength; i++) {
            if (source[i] != target[i]) {
                long long charConversionCost =
                    minConversionCosts[source[i] - 'a'][target[i] - 'a'];
                if (charConversionCost == -1) {
                    return -1;  // Conversion not possible
                }
                totalCost += charConversionCost;
            }
        }
        return totalCost;
    }
};
```
**Solution 2: (Floyd-Warshall, all source shortest path)**
```
Runtime: 190 ms
Memory: 99.17 MB
```
```c++
class Solution {
public:
    long long minimumCost(string source, string target, vector<char>& original, vector<char>& changed, vector<int>& cost) {
        vector<vector<long long>> dp(26, vector<long long>(26, INT_MAX));
        for (int i = 0; i < original.size(); i ++) {
            dp[original[i]-'a'][changed[i]-'a'] = min(dp[original[i]-'a'][changed[i]-'a'], (long long)cost[i]);
        }
        for (int i = 0; i < 26; i ++) {
            dp[i][i] = 0;
        }
        for (int k = 0; k < 26; k ++) {
            for (int i = 0; i < 26; i ++) {
                for (int j = 0; j < 26; j ++) {
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]);
                }
            }
        }
        long long ans = 0;
        for (int i = 0; i < source.size(); i ++) {
            if (dp[source[i]-'a'][target[i]-'a'] == INT_MAX) {
                return -1;
            }
            ans += dp[source[i]-'a'][target[i]-'a'];
        }
        return ans;
    }
};
```

**Solution 3: (Floyd-Warshall, all source shortest path, O(m + n))**
```
Runtime: 174 ms
Memory: 99.09 MB
```
```c++
class Solution {
public:
    long long minimumCost(string source, string target, vector<char>& original, vector<char>& changed, vector<int>& cost) {
        // Initialize result to store the total minimum cost
        long long totalCost = 0;

        // Initialize a 2D vector to store the minimum transformation cost
        // between any two characters
        vector<vector<long long>> minCost(26, vector<long long>(26, INT_MAX));

        // Fill the initial transformation costs from the given original,
        // changed, and cost arrays
        for (int i = 0; i < original.size(); ++i) {
            int startChar = original[i] - 'a';
            int endChar = changed[i] - 'a';
            minCost[startChar][endChar] =
                min(minCost[startChar][endChar], (long long)cost[i]);
        }

        // Use Floyd-Warshall algorithm to find the shortest path between any
        // two characters
        for (int k = 0; k < 26; ++k) {
            for (int i = 0; i < 26; ++i) {
                for (int j = 0; j < 26; ++j) {
                    minCost[i][j] =
                        min(minCost[i][j], minCost[i][k] + minCost[k][j]);
                }
            }
        }

        // Calculate the total minimum cost to transform the source string to
        // the target string
        for (int i = 0; i < source.size(); ++i) {
            if (source[i] == target[i]) {
                continue;
            }
            int sourceChar = source[i] - 'a';
            int targetChar = target[i] - 'a';

            // If the transformation is not possible, return -1
            if (minCost[sourceChar][targetChar] >= INT_MAX) {
                return -1;
            }
            totalCost += minCost[sourceChar][targetChar];
        }

        return totalCost;
    }
};
```
