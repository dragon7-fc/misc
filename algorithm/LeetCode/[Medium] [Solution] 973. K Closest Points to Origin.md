973. K Closest Points to Origin

We have a list of `points` on the plane.  Find the `K` closest points to the origin `(0, 0)`.

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

**Example 1:**
```
Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
```

**Example 2:**
```
Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
```

**Note:**

* `1 <= K <= points.length <= 10000`
* `-10000 < points[i][0] < 10000`
* `-10000 < points[i][1] < 10000`

# Submissions
---
## Approach 1: Sort
**Intuition**

Sort the points by distance, then take the closest `K` points.

**Algorithm**

There are two variants.

In Java, we find the `K`-th distance by creating an array of distances and then sorting them. After, we select all the points with distance less than or equal to this `K`-th distance.

In Python, we sort by a custom key function - namely, the distance to the origin. Afterwards, we return the first `K` elements of the list.

```python
class Solution(object):
    def kClosest(self, points, K):
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]
```

**Complexity Analysis**

* Time Complexity: $O(N \log N)$, where $N$ is the length of points.

* Space Complexity: $O(N)$.

## Approach 2: Divide and Conquer
**Intuition**

We want an algorithm faster than $N \log N$. Clearly, the only way to do this is to use the fact that the `K` elements returned can be in any order -- otherwise we would be sorting which is at least $N \log N$.

Say we choose some random element `x = A[i]` and split the array into two buckets: one bucket of all the elements less than `x`, and another bucket of all the elements greater than or equal to `x`. This is known as "quickselecting by a pivot `x`".

The idea is that if we quickselect by some pivot, on average in linear time we'll reduce the problem to a problem of half the size.

**Algorithm**

Let's do the `work(i, j, K)` of partially sorting the subarray `(points[i], points[i+1], ..., points[j])` so that the smallest `K` elements of this subarray occur in the first `K` positions `(i, i+1, ..., i+K-1)`.

First, we quickselect by a random pivot element from the subarray. To do this in place, we have two pointers `i` and `j`, and move these pointers to the elements that are in the wrong bucket -- then, we swap these elements.

After, we have two buckets `[oi, i]` and `[i+1, oj]`, where `(oi, oj)` are the original `(i, j)` values when calling `work(i, j, K)`. Say the first bucket has `10` items and the second bucket has `15` items. If we were trying to partially sort say, `K = 5` items, then we only need to partially sort the first bucket: `work(oi, i, 5)`. Otherwise, if we were trying to partially sort say, `K = 17` items, then the first `10` items are already partially sorted, and we only need to partially sort the next `7` items: `work(i+1, oj, 7)`.

```python
class Solution(object):
    def kClosest(self, points, K):
        dist = lambda i: points[i][0]**2 + points[i][1]**2

        def sort(i, j, K):
            # Partially sorts A[i:j+1] so the first K elements are
            # the smallest K elements.
            if i >= j: return

            # Put random element as A[i] - this is the pivot
            k = random.randint(i, j)
            points[i], points[k] = points[k], points[i]

            mid = partition(i, j)
            if K < mid - i + 1:
                sort(i, mid - 1, K)
            elif K > mid - i + 1:
                sort(mid + 1, j, K - (mid - i + 1))

        def partition(i, j):
            # Partition by pivot A[i], returning an index mid
            # such that A[i] <= A[mid] <= A[j] for i < mid < j.
            oi = i
            pivot = dist(i)
            i += 1

            while True:
                while i < j and dist(i) < pivot:
                    i += 1
                while i <= j and dist(j) >= pivot:
                    j -= 1
                if i >= j: break
                points[i], points[j] = points[j], points[i]

            points[oi], points[j] = points[j], points[oi]
            return j

        sort(0, len(points) - 1, K)
        return points[:K]
```

**Complexity Analysis**

* Time Complexity: $O(N)$ in average case complexity, where $N$ is the length of points.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution: (Sort)**
```
Runtime: 640 ms
Memory Usage: 18.2 MB
```
```python
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]
```

**Solution: (Divide and Conquer)**
```
Runtime: 896 ms
Memory Usage: 18.3 MB
```
```python
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = lambda i: points[i][0]**2 + points[i][1]**2

        def sort(i, j, K):
            # Partially sorts A[i:j+1] so the first K elements are
            # the smallest K elements.
            if i >= j: return

            # Put random element as A[i] - this is the pivot
            k = random.randint(i, j)
            points[i], points[k] = points[k], points[i]

            mid = partition(i, j)
            if K < mid - i + 1:
                sort(i, mid - 1, K)
            elif K > mid - i + 1:
                sort(mid + 1, j, K - (mid - i + 1))

        def partition(i, j):
            # Partition by pivot A[i], returning an index mid
            # such that A[i] <= A[mid] <= A[j] for i < mid < j.
            oi = i
            pivot = dist(i)
            i += 1

            while True:
                while i < j and dist(i) < pivot:
                    i += 1
                while i <= j and dist(j) >= pivot:
                    j -= 1
                if i >= j: break
                points[i], points[j] = points[j], points[i]

            points[oi], points[j] = points[j], points[oi]
            return j

        sort(0, len(points) - 1, K)
        return points[:K]
```

**Solution: (Sort with Custom Comparator)**
```
Memory Usage: 57144000
```
```c++
class Solution {
    int squaredDistance(vector<int>& point) {
        // Calculate and return the squared Euclidean distance
        return point[0] * point[0] + point[1] * point[1];
    }
    
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        // Sort the vector with a custom lambda comparator function
        sort(points.begin(), points.end(), [&](vector<int>& a, vector<int>& b) {
            return squaredDistance(a) < squaredDistance(b);
        });
        
        // Return the first k elements of the sorted vector
        return vector<vector<int>>(points.begin(), points.begin() + k);
    }
};
```

**Solution: (Max Heap or Max Priority Queue)**
```
Memory Usage: 62412000
```
```c++
class Solution {
    int squaredDistance(vector<int>& point) {
        // Calculate and return the squared Euclidean distance
        return point[0] * point[0] + point[1] * point[1];
    }
    
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<pair<int, int>> maxPQ;
        for (int i = 0 ; i < points.size(); i++) {
            pair<int, int> entry = {squaredDistance(points[i]), i};
            if (maxPQ.size() < k) {
                // Fill the max PQ up to k points
                maxPQ.push(entry);
            } else if (entry.first < maxPQ.top().first) {
                // If the max PQ is full and a closer point is found,
                // discard the farthest point and add this one
                maxPQ.pop();
                maxPQ.push(entry);
            }
        }
        
        // Return all points stored in the max PQ
        vector<vector<int>> answer;
        while (!maxPQ.empty()) {
            int entryIndex = maxPQ.top().second;
            maxPQ.pop();
            answer.push_back(points[entryIndex]);
        }
        return answer;
    }
};
```

**Solution: (Binary Search)**
```
Memory Usage: 78504000
```
```c++
class Solution {
    vector<vector<int>> splitDistances(vector<int>& remaining, vector<double>& distances,
                                       double mid) {
        // Split the distances around the midpoint
        // and return them in separate vectors
        vector<vector<int>> result(2);
        vector<int> &closer = result[0], &farther = result[1];
        for (int index : remaining) {
            if (distances[index] <= mid) {
                closer.push_back(index);
            } else {
                farther.push_back(index);
            }
        }
        return result;
    } 
    
    double euclideanDistance(vector<int>& point) {
        // Calculate and return the squared Euclidean distance
        return point[0] * point[0] + point[1] * point[1];
    }
    
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        // Precompute the Euclidean distance for each point,
        // define the initial binary search range,
        // and create a reference list of point indices
        vector<double> distances;
        vector<int> remaining;
        double low = 0, high = 0;
        for (int i = 0; i < points.size(); i++) {
            distances.push_back(euclideanDistance(points[i]));
            high = max(high, distances[i]);
            remaining.push_back(i);
        }
                
        // Perform a binary search of the distances
        // to find the k closest points
        vector<int> closest;
        while (k) {
            double mid = low + (high - low) / 2;
            vector<vector<int>> result = splitDistances(remaining, distances, mid);
            vector<int>& closer = result[0];
            vector<int>& farther = result[1];
            if (closer.size() > k) {
                // If more than k points are in the closer distances
                // then discard the farther points and continue
                remaining.swap(closer);
                high = mid;
            } else {
                // Add the closer points to the answer array and keep
                // searching the farther distances for the remaining points
                k -= closer.size();
                closest.insert(closest.end(), closer.begin(), closer.end());
                remaining.swap(farther);
                low = mid;
            }
        }
        
        // Return the k closest points using the reference indices
        vector<vector<int>> answer;
        for (int index : closest) {
            answer.push_back(points[index]);
        }
        return answer;
    }
};
```

**Solution: (QuickSelect)**
```
Memory Usage: 57100000
```
```c++
class Solution {
    vector<vector<int>> quickSelect(vector<vector<int>>& points, int k) {
        int left = 0, right = points.size() - 1;
        int pivotIndex = points.size();
        while (pivotIndex != k) {
            // Repeatedly partition the vector
            // while narrowing in on the kth element
            pivotIndex = partition(points, left, right);
            if (pivotIndex < k) {
                left = pivotIndex;
            } else {
                right = pivotIndex - 1;
            }
        }
        
        // Return the first k elements of the partially sorted vector
        return vector<vector<int>>(points.begin(), points.begin() + k);
    };

    int partition(vector<vector<int>>& points, int left, int right) {
        vector<int>& pivot = choosePivot(points, left, right);
        int pivotDist = squaredDistance(pivot);
        while (left < right) {
            // Iterate through the range and swap elements to make sure
            // that all points closer than the pivot are to the left
            if (squaredDistance(points[left]) >= pivotDist) {
                points[left].swap(points[right]);
                right--;
            } else {
                left++;
            }
        }
        
        // Ensure the left pointer is just past the end of
        // the left range then return it as the new pivotIndex
        if (squaredDistance(points[left]) < pivotDist)
            left++;
        return left;
    };

    vector<int>& choosePivot(vector<vector<int>>& points, int left, int right) {
        // Choose a pivot element of the vector
        return points[left + (right - left) / 2];
    }
    
    int squaredDistance(vector<int>& point) {
        // Calculate and return the squared Euclidean distance
        return point[0] * point[0] + point[1] * point[1];
    }
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        return quickSelect(points, k);
    }
};
```

**Solution 1: (Heap)**
```
Runtime: 716 ms
Memory Usage: 18.2 MB
```
```python
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return heapq.nsmallest(K, points, key= lambda x: x[0]**2 + x[1]**2)
```

**Solutiopn 2: (qsort)**
```
Runtime: 448 ms
Memory Usage: 34 MB
```
```c
int cmpFunc(void *a, void *b)
{
    return ((*(int **)a)[0]-(*(int **)b)[0])*((*(int **)a)[0]+(*(int **)b)[0]) + ((*(int **)a)[1]-(*(int **)b)[1])*((*(int **)a)[1]+(*(int **)b)[1]);
}

// int cmpFunc(const int** a, const int** b)
// {
//     return ((a[0][0]-b[0][0])*(a[0][0]+b[0][0]))+((a[0][1]-b[0][1])*(a[0][1]+b[0][1]));
// }

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** kClosest(int** points, int pointsSize, int* pointsColSize, int k, int* returnSize, int** returnColumnSizes){
    int** ans = malloc(sizeof(int*)*k);
    *returnColumnSizes = malloc(sizeof(int)*k);
    *returnSize = k;
    for (int i = 0; i < k; i++)
    {
        returnColumnSizes[0][i] = 2;
    }
    
    qsort(points, pointsSize, sizeof(int*), cmpFunc);
    return points;
}
```
