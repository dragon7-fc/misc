2070. Most Beautiful Item for Each Query

You are given a 2D integer array items where `items[i] = [pricei, beautyi]` denotes the **price** and **beauty** of an item respectively.

You are also given a **0-indexed** integer array `queries`. For each `queries[j]`, you want to determine the **maximum beauty** of an item whose **price** is **less than or equal** to `queries[j]`. If no such item exists, then the answer to this query is `0`.

Return an array `answer` of the same length as `queries` where `answer[j]` is the answer to the `j`th query.

 

**Example 1:**
```
Input: items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]
Output: [2,4,5,5,6,6]
Explanation:
- For queries[0]=1, [1,2] is the only item which has price <= 1. Hence, the answer for this query is 2.
- For queries[1]=2, the items which can be considered are [1,2] and [2,4]. 
  The maximum beauty among them is 4.
- For queries[2]=3 and queries[3]=4, the items which can be considered are [1,2], [3,2], [2,4], and [3,5].
  The maximum beauty among them is 5.
- For queries[4]=5 and queries[5]=6, all items can be considered.
  Hence, the answer for them is the maximum beauty of all items, i.e., 6.
```

**Example 2:**
```
Input: items = [[1,2],[1,2],[1,3],[1,4]], queries = [1]
Output: [4]
Explanation: 
The price of every item is equal to 1, so we choose the item with the maximum beauty 4. 
Note that multiple items can have the same price and/or beauty.  
```

**Example 3:**
```
Input: items = [[10,1000]], queries = [5]
Output: [0]
Explanation:
No item has a price less than or equal to 5, so no item can be chosen.
Hence, the answer to the query is 0.
```

Constraints:

* `1 <= items.length, queries.length <= 10^5`
* `items[i].length == 2`
* `1 <= pricei, beautyi, queries[j] <= 10^9`

# Submissions
---
**Solution 1: (Sort, Binary Search)**
```
Runtime: 1267 ms
Memory Usage: 74.2 MB
```
```python
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        maxArr = [items[0][1]] * len(items)
		# for each cell calculate maximum beautifulnes
        for i in range(1, len(items)):
            maxArr[i] = max(maxArr[i-1], items[i][1])
        
        onlyKeys = list(map(lambda x:x[0], items)) # since 3.9 python doesn't have `key` in bisect
        
        res = []
        for q in queries:
            # if minimum price is greated than query, no items can be found for query
            notPossible = items[0][0] > q
            if notPossible:
                res.append(0)
            else:
                # otherwise find last cell with value less or equals to query
                i = bisect.bisect_right(onlyKeys, q)
                # lookup result in our maximum array by index
                res.append(maxArr[i-1])
        
        return res
```

**Solution 1: (Sort, Binary Search)**
```
Runtime: 322 ms
Memory: 88.9 MB
```
```c++
class Solution {
public:
    vector<int> maximumBeauty(vector<vector<int>>& items, vector<int>& queries) {
        sort(items.begin(),items.end());
        int maxi = items[0][1];
        for (auto &xt : items)
        {
            maxi = max(maxi , xt[1]);
            xt[1] = maxi;
        }
        vector<int>ans;
        int n = items.size();
        for (int key : queries){
            int left = 0;
            int right = n - 1;
            while (left < right) {
                int mid = right - (right - left) / 2;
                if (items[mid][0] <= key) {
                    left = mid;
                }
                else
                    right = mid - 1;
            }
            if (items[left][0] > key) {
                ans.push_back(0);
            } else {
                ans.push_back(items[left][1]);
            }
        }
        return ans;
    }
};
```


**Solution 3: (Sorting Items + Sorting Queries)**
```
Runtime: 59 ms
Memory: 99.09 MB
```
```c++
class Solution {
public:
    vector<int> maximumBeauty(vector<vector<int>>& items, vector<int>& queries) {
        vector<int> ans(queries.size());
        // sort both items and queries in ascending order
        sort(items.begin(), items.end(),
             [](vector<int>& a, vector<int>& b) { return a[0] < b[0]; });

        vector<vector<int>> queriesWithIndices(queries.size(), vector<int>(2));

        for (int i = 0; i < queries.size(); i++) {
            queriesWithIndices[i][0] = queries[i];
            queriesWithIndices[i][1] = i;
        }

        sort(queriesWithIndices.begin(), queriesWithIndices.end(),
             [](vector<int>& a, vector<int>& b) { return a[0] < b[0]; });

        int itemIndex = 0;
        int maxBeauty = 0;

        for (int i = 0; i < queries.size(); i++) {
            int query = queriesWithIndices[i][0];
            int originalIndex = queriesWithIndices[i][1];

            while (itemIndex < items.size() && items[itemIndex][0] <= query) {
                maxBeauty = max(maxBeauty, items[itemIndex][1]);
                itemIndex++;
            }

            ans[originalIndex] = maxBeauty;
        }
        return ans;
    }
};
```

**Solution 4: (Sort, Binary Search, lower bound)**
```
Runtime: 48 ms
Memory: 94.78 MB
```
```c++
class Solution {
public:
    vector<int> maximumBeauty(vector<vector<int>>& items, vector<int>& queries) {
        sort(items.begin(), items.end());
        vector<pair<int,int>> dp;
        int i;
        for (i = 0; i < items.size(); i ++) {
            if (dp.size() && dp.back().first == items[i][0]) {
                dp.back().second = max(dp.back().second, items[i][1]);
            } else {
                if (!dp.size()) {
                    dp.push_back({items[i][0], items[i][1]});
                } else {
                    dp.push_back({items[i][0], max(dp.back().second, items[i][1])});
                }
            }
        }
        cout << endl;
        vector<int> ans;
        for (auto q: queries) {
            i = lower_bound(dp.begin(), dp.end(), make_pair(q, 0)) - dp.begin();
            if (i < dp.size() && dp[i].first <= q) {
                ans.push_back(dp[i].second);
            } else if (i && dp[i-1].first <= q) {
                ans.push_back(dp[i-1].second);
            } else {
                ans.push_back(0);
            }
        }
        return ans;
    }
};
```

**Solution 5: (Sort, Binary Search, upper bound)**
```
Runtime: 48 ms
Memory: 94.54 MB
```
```c++
class Solution {
public:
    vector<int> maximumBeauty(vector<vector<int>>& items, vector<int>& queries) {
        sort(items.begin(), items.end());
        vector<pair<int,int>> dp;
        int i;
        for (i = 0; i < items.size(); i ++) {
            if (dp.size() && dp.back().first == items[i][0]) {
                dp.back().second = max(dp.back().second, items[i][1]);
            } else {
                if (!dp.size()) {
                    dp.push_back({items[i][0], items[i][1]});
                } else {
                    dp.push_back({items[i][0], max(dp.back().second, items[i][1])});
                }
            }
        }
        cout << endl;
        vector<int> ans;
        for (auto q: queries) {
            i = upper_bound(dp.begin(), dp.end(), make_pair(q, INT_MAX)) - dp.begin();
            if (dp.size() && i && dp[i-1].first <= q) {
                ans.push_back(dp[i-1].second);
            } else {
                ans.push_back(0);
            }
        }
        return ans;
    }
};
```
