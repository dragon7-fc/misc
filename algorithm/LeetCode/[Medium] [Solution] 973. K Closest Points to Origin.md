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

**Solution 3: (Heap)**
```
Runtime: 716 ms
Memory Usage: 18.2 MB
```
```python
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return heapq.nsmallest(K, points, key= lambda x: x[0]**2 + x[1]**2)
```

**Solutiopn 4: (qsort)**
```
Runtime: 448 ms
Memory Usage: 34 MB
```
```c
int cmpFunc(const int** a, const int** b)
{
    return ((a[0][0]-b[0][0])*(a[0][0]+b[0][0]))+((a[0][1]-b[0][1])*(a[0][1]+b[0][1]));
}

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
