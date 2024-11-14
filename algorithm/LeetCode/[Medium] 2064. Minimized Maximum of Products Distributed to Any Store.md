2064. Minimized Maximum of Products Distributed to Any Store

You are given an integer `n` indicating there are n specialty retail stores. There are `m` product types of varying amounts, which are given as a **0-indexed** integer array `quantities`, where `quantities[i]` represents the number of products of the i^th product type.

You need to distribute **all products** to the retail stores following these rules:

* A store can only be given **at most one product type** but can be given **any** amount of it.
* After distribution, each store will be given some number of products (possibly `0`). Let x represent the maximum number of products given to any store. You want x to be as small as possible, i.e., you want to **minimize** the **maximum** number of products that are given to any store.

Return the minimum possible `x`.

 

**Example 1:**
```
Input: n = 6, quantities = [11,6]
Output: 3
Explanation: One optimal way is:
- The 11 products of type 0 are distributed to the first four stores in these amounts: 2, 3, 3, 3
- The 6 products of type 1 are distributed to the other two stores in these amounts: 3, 3
The maximum number of products given to any store is max(2, 3, 3, 3, 3, 3) = 3.
```

**Example 2:**
```
Input: n = 7, quantities = [15,10,10]
Output: 5
Explanation: One optimal way is:
- The 15 products of type 0 are distributed to the first three stores in these amounts: 5, 5, 5
- The 10 products of type 1 are distributed to the next two stores in these amounts: 5, 5
- The 10 products of type 2 are distributed to the last two stores in these amounts: 5, 5
The maximum number of products given to any store is max(5, 5, 5, 5, 5, 5, 5) = 5.
```

**Example 3:**
```
Input: n = 1, quantities = [100000]
Output: 100000
Explanation: The only optimal way is:
- The 100000 products of type 0 are distributed to the only store.
The maximum number of products given to any store is max(100000) = 100000.
```

**Constraints:**

* `m == quantities.length`
* `1 <= m <= n <= 10^5`
* `1 <= quantities[i] <= 10^5`

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 1908 ms
Memory Usage: 28.6 MB
```
```python
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left, right = 1, max(quantities)
        while left < right:
            x = (left + right) // 2
            if sum((a + x - 1) // x for a in quantities) > n:
                left = x + 1
            else:
                right = x
        return left
```

**Solution 2: (Binary Search)**
```
Runtime: 176 ms
Memory Usage: 84.4 MB
```
```c++
class Solution {
public:
    int minimizedMaximum(int n, vector<int>& quantities) {
        int left = 1, right = 100000;
        while (left < right) {
            int mid = (left + right) / 2, sum = 0;
            for (int a : quantities)
                sum += (a + mid - 1) / mid;
            if (sum > n)
                left = mid + 1;
            else
                right = mid;
        }
        return left;
    }
};
```

**Solution 3: (Greedy Approach Using a Heap)**
```
Runtime: 1748 ms
Memory: 113.71 MB
```
```c++
class Solution {
public:
    int minimizedMaximum(int n, vector<int>& quantities) {
        int m = quantities.size();

        // Define a custom comparator for the priority queue
        // It sorts the pairs based on the ratio of their first to their second
        // element
        auto compareTypeStorePairs = [](pair<int, int>& a, pair<int, int>& b) {
            return (long long)a.first * b.second <
                   (long long)a.second * b.first;
        };

        // Helper array - useful for the efficient initialization of the
        // priority queue
        vector<pair<int, int>> typeStorePairsArray;

        // Push all product types to the array, after assigning one store to
        // each of them
        for (int i = 0; i < m; i++) {
            typeStorePairsArray.push_back({quantities[i], 1});
        }

        // Initialize the priority queue
        priority_queue<pair<int, int>, vector<pair<int, int>>,
                       decltype(compareTypeStorePairs)>
            typeStorePairs(typeStorePairsArray.begin(),
                           typeStorePairsArray.begin() + m);

        // Iterate over the remaining n - m stores.
        for (int i = 0; i < n - m; i++) {
            // Pop first element
            pair<int, int> pairWithMaxRatio = typeStorePairs.top();
            int totalQuantityOfType = pairWithMaxRatio.first;
            int storesAssignedToType = pairWithMaxRatio.second;
            typeStorePairs.pop();

            // Push same element after assigning one more store to its product
            // type
            typeStorePairs.push(
                {totalQuantityOfType, storesAssignedToType + 1});
        }

        // Pop first element
        pair<int, int> pairWithMaxRatio = typeStorePairs.top();
        int totalQuantityOfType = pairWithMaxRatio.first;
        int storesAssignedToType = pairWithMaxRatio.second;

        // Return the maximum minimum ratio
        return ceil((double)totalQuantityOfType / storesAssignedToType);
    }
};
```

**Solution 4: (Binary Search, lower bound, O(n log(k)))**
```
Runtime: 19 ms
Memory: 87.35 MB
```
```c++
class Solution {
    bool check(int mid, vector<int>& quantities, int n) {
        int k = 0;
        for (auto q: quantities) {
            k += q/mid + ((q%mid) > 0);
        }
        return k <= n;
    }
public:
    int minimizedMaximum(int n, vector<int>& quantities) {
        int left = 1, right = *max_element(quantities.begin(), quantities.end()), mid, ans;
        while (left <= right) {
            mid = left + (right-left)/2;
            if (!check(mid, quantities, n)) {
                left = mid+1;
            } else {
                ans = mid;
                right = mid-1;
            }
        }
        return ans;
    }
};
```
