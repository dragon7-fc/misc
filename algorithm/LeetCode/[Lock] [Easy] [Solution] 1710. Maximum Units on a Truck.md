1710. Maximum Units on a Truck

You are assigned to put some amount of boxes onto **one truck**. You are given a 2D array `boxTypes`, where `boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]`:

* `numberOfBoxesi` is the number of boxes of type `i`.
* `numberOfUnitsPerBoxi` is the number of units in each box of the type `i`.

You are also given an integer `truckSize`, which is the **maximum** number of **boxes** that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed `truckSize`.

Return the **maximum** total number of **units** that can be put on the truck.

 

**Example 1:**
```
Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
```

**Example 2:**
```
Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91
```

**Constraints:**

* `1 <= boxTypes.length <= 1000`
* `1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000`
* `1 <= truckSize <= 10^6`

# Submissions
---
**Solution 1: (Sort)**
```
Runtime: 144 ms
Memory Usage: 15 MB
```
```python
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        A = sorted(boxTypes, key = lambda x:x[1] , reverse = True)
        res = 0
        for i in range(len(A)):
            if truckSize - A[i][0] >= 0:
                res += A[i][0] * A[i][1]
                truckSize = truckSize - A[i][0]
            else:
                res += truckSize * A[i][1]
                break
        return res
```

**Solution 2: (Heap)**
```
Runtime: 76 ms
Memory Usage: 21.6 MB
```
```c++
class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        priority_queue<vector<int>, vector<vector<int>>, Comparator> queue;
        for (auto boxType : boxTypes) {
            queue.push(boxType);
        }
        int unitCount = 0;
        while (!queue.empty()) {
            vector<int> top = queue.top();
            queue.pop();
            int boxCount = min(truckSize, top[0]);
            unitCount += boxCount * top[1];
            truckSize -= boxCount;
            if(truckSize == 0)
                break;
        }
        return unitCount;
    }
    
    struct Comparator {
        bool operator()(vector<int> const& p1, vector<int> const& p2) {
            return p1[1] < p2[1];
        }
    };
};
```

**Solution 3: (Sort)**
```
Runtime: 40 ms
Memory Usage: 15.9 MB
```
```c++
class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        // Sort boxes so that boxes with the most units appear first
        sort(boxTypes.begin(), boxTypes.end(), [](auto& box1, auto& box2) {
            return box1[1] > box2[1];
        });
        
        int totalUnits = 0;
        for (auto& box : boxTypes) {
            // Take as many boxes until we're out of space on the truck
            // or we're out of boxes of this type
            int numBoxes = min(truckSize, box[0]);
            totalUnits += numBoxes * box[1];
            truckSize -= numBoxes;
        }
        return totalUnits;
    }
};
```
