2013. Detect Squares

You are given a stream of points on the X-Y plane. Design an algorithm that:

* **Adds** new points from the stream into a data structure. **Duplicate** points are allowed and should be treated as different points.
* Given a query point, **counts** the number of ways to choose three points from the data structure such that the three points and the query point form an **axis-aligned square** with **positive area**.

An **axis-aligned square** is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

Implement the `DetectSquares` class:

* `DetectSquares()` Initializes the object with an empty data structure.
* `void add(int[] point)` Adds a new point `point = [x, y]` to the data structure.
* `int count(int[] point)` Counts the number of ways to form **axis-aligned squares** with point `point = [x, y]` as described above.
 

**Example 1:**

![img/2013_imag](eimg/2013_image.png)
```
Input
["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
Output
[null, null, null, null, 1, 0, null, 2]

Explanation
DetectSquares detectSquares = new DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
detectSquares.count([11, 10]); // return 1. You can choose:
                               //   - The first, second, and third points
detectSquares.count([14, 8]);  // return 0. The query point cannot form a square with any points in the data structure.
detectSquares.add([11, 2]);    // Adding duplicate points is allowed.
detectSquares.count([11, 10]); // return 2. You can choose:
                               //   - The first, second, and third points
                               //   - The first, third, and fourth points
``` 

**Constraints:**

* `point.length == 2`
* `0 <= x, y <= 1000`
* At most `5000` calls in total will be made to `add` and `count`.

# Submissions
---
**Solution 1: (Hash Table)**
```
Runtime: 2396 ms
Memory Usage: 16.5 MB
```
```python
class DetectSquares:

    def __init__(self):
        self.d = Counter()
        self.x_coord = defaultdict(Counter)   # x -> all y coordinates with freqs

    def add(self, point: List[int]) -> None:
        x, y = point
        self.d[x, y] += 1
        self.x_coord[x][y] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        ans = 0
        for y2 in self.x_coord[x]:
            if y == y2: continue
            ans += self.d[x, y2] * self.d[x + y2 - y, y] * self.d[x + y2 - y, y2]
            ans += self.d[x, y2] * self.d[x + y - y2, y] * self.d[x + y - y2, y2]
        return ans

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
```

**Solution 2: (Hash Table)**
```
Runtime: 216 ms
Memory Usage: 145 MB
```
```c++
class DetectSquares {
public:
    map<int,vector<pair<int,int>>>sum,diff;
    int arr[1002][1002];
    DetectSquares() {
        sum.clear();
        diff.clear();
        memset(arr, 0, sizeof(arr[0][0]) * 1002 * 1002);
    }
    
    void add(vector<int> point) {
        sum[point[0]+point[1]].push_back({point[0],point[1]});
        diff[point[0]-point[1]].push_back({point[0],point[1]});
        arr[point[0]][point[1]]++;
    }
    
    int count(vector<int> point) {
        int x=point[0];
        int y=point[1];
        int ans=0;
        for(auto temp:sum[x+y]){
            if(temp.first==x&&temp.second==y)
                continue;
           if(abs(temp.first-x)==abs(temp.second-y))
                ans+= (arr[temp.first][y]*arr[x][temp.second]);
        }
        for(auto temp:diff[x-y]){
            if(temp.first==x&&temp.second==y)
                continue;
            if(abs(temp.first-x)==abs(temp.second-y))
                ans+= (arr[temp.first][y]*arr[x][temp.second]);
        }
        return ans;
    }
};

/**
 * Your DetectSquares object will be instantiated and called as such:
 * DetectSquares* obj = new DetectSquares();
 * obj->add(point);
 * int param_2 = obj->count(point);
 */
```
