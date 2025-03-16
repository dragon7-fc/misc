2594. Minimum Time to Repair Cars

You are given an integer array `ranks` representing the ranks of some mechanics. `ranksi` is the rank of the `i`th mechanic. A mechanic with a rank `r` can repair n cars in `r * n2` minutes.

You are also given an integer `cars` representing the total number of cars waiting in the garage to be repaired.

Return the **minimum** time taken to repair all the cars.

**Note:** All the mechanics can repair the cars simultaneously.

 

**Example 1:**
```
Input: ranks = [4,2,3,1], cars = 10
Output: 16
Explanation: 
- The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
- The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
- The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
- The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​
```

**Example 2:**
```
Input: ranks = [5,1,8], cars = 6
Output: 16
Explanation: 
- The first mechanic will repair one car. The time required is 5 * 1 * 1 = 5 minutes.
- The second mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
- The third mechanic will repair one car. The time required is 8 * 1 * 1 = 8 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​
``` 

**Constraints:**

* `1 <= ranks.length <= 10^5`
* `1 <= ranks[i] <= 100`
* `1 <= cars <= 10^6`

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 319 ms
Memory: 17.7 MB
```
```python
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        count = Counter(ranks)
        left, right = 1, min(count) * cars * cars
        while left < right:
            mid = (left + right) // 2
            if sum(isqrt(mid // a) * count[a] for a in count) < cars:
                left = mid + 1
            else:
                right = mid
        return left
```

**Solution 2: (Heap0**
```
Runtime: 938 ms
Memory: 17.8 MB
```
```python
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        count = Counter(ranks)
        h = [[a, a, 1, count[a]] for a in count]
        heapify(h)
        while cars > 0:
            time, rank, k, count = heappop(h)
            cars -= count
            k += 1
            heappush(h, [rank * k * k, rank, k, count])
        return time
```
**Solution 3: (Heap0**
```
Runtime: 1294 ms, Beats 5.09%
Memory: 336.03 MB, Beats 5.08%
```
```c++
class Solution {
public:
    long long repairCars(vector<int>& ranks, int cars) {
        // Count the frequency of each rank
        unordered_map<int, int> count;
        for (int rank : ranks) {
            count[rank] += 1;
        }

        // Create a Min-heap (priority_queue in C++ std library) storing [time,
        // rank, n, count]
        // - time: time for the next repair
        // - rank: mechanic's rank
        // - n: cars repaired by this mechanic
        // - count: number of mechanics with this rank
        // Initial time = rank (as rank * 1^2 = rank)
        auto comp = [](vector<long>& a, vector<long>& b) {
            return a[0] > b[0];
        };
        priority_queue<vector<long>, vector<vector<long>>, decltype(comp)>
            minHeap(comp);

        // Add initial entries to the heap
        for (auto it : count) {
            int rank = it.first;
            // Elements: [time, rank, cars_repaired, mechanic_count]
            minHeap.push({rank, rank, 1, it.second});
        }

        long time = 0;
        // Process until all cars are repaired
        while (cars > 0) {
            // Pop the mechanic with the smallest current repair time
            vector<long> current = minHeap.top();
            minHeap.pop();
            time = current[0];
            int rank = current[1];
            long n = current[2];
            int mechCount = current[3];

            // Deduct the number of cars repaired by this mechanic group
            cars -= mechCount;

            // Increment the number of cars repaired by this mechanic
            n += 1;

            // Push the updated repair time back into the heap
            // The new repair time is rank * n^2 (time increases quadratically
            // with n)
            minHeap.push({rank * n * n, rank, n, mechCount});
        }

        return time;
    }
};
```

**Solution 4: (Binary Search)**
```
Runtime: 59 ms, Beats 38.42%
```
```c++
class Solution {
public:
    long long repairCars(vector<int>& ranks, int cars) {
        int n = ranks.size(), i;
        long long left = 1, right = 1LL * *max_element(ranks.begin(), ranks.end()) * cars * cars, mid, cur;
        while (left < right) {
            mid = left + (right - left)/2;
            cur = 0;
            for (i = 0; i < n; i ++) {
                cur += sqrt(mid/ranks[i]);
            }
            if (cur < cars) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
};
```
