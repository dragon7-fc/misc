715. Range Module

A Range Module is a module that tracks ranges of numbers. Your task is to design and implement the following interfaces in an efficient manner.

* `addRange(int left, int right)` Adds the half-open interval `[left, right)`, tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval `[left, right)` that are not already tracked.
* `queryRange(int left, int right)` Returns `true` if and only if every real number in the interval `[left, right)` is currently being tracked.
* `removeRange(int left, int right)` Stops tracking every real number currently being tracked in the interval `[left, right)`.

**Example 1:**
```
addRange(10, 20): null
removeRange(14, 16): null
queryRange(10, 14): true (Every number in [10, 14) is being tracked)
queryRange(13, 15): false (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
queryRange(16, 17): true (The number 16 in [16, 17) is still being tracked, despite the remove operation)
```

**Note:**

* A half open interval `[left, right)` denotes all real numbers `left <= x < right`.
* `0 < left < right < 10^9` in all calls to addRange, queryRange, removeRange.
* The total number of calls to addRange in a single test case is at most `1000`.
* The total number of calls to queryRange in a single test case is at most `5000`.
* The total number of calls to removeRange in a single test case is at most `1000`.

# Solution
---
## Approach #1: Maintain Sorted Disjoint Intervals [Accepted]
**Intuition**

Because `left, right < 10^9`, we need to deal with the coordinates abstractly. Let's maintain some sorted structure of disjoint intervals. These intervals will be closed (eg. we don't store `[[1, 2], [2, 3]]`; we would store `[[1, 3]]` instead.)

In this article, we will go over Python and Java versions separately, as the data structures available to us that are relevant to the problem are substantially different.

**Algorithm (Python)**

We will maintain the structure as a list `self.ranges = []`.

Adding a Range

When we want to add a range, we first find the indices `i, j = self._bounds(left, right)` for which `self.ranges[i: j+1]` touches (in a closed sense - not halfopen) the given interval `[left, right]`. We can find this in log time by making steps of size `100`, `10`, then `1` in our linear search from both sides.

Every interval touched by `[left, right]` will be replaced by the single interval `[min(left, self.ranges[i][0]), max(right, self.ranges[j][1])]`.

Removing a Range

Again, we use `i, j = self._bounds(...)` to only work in the relevant subset of `self.ranges` that is in the neighborhood of our given range `[left, right)`. For each interval `[x, y)` from `self.ranges[i:j+1]`, we may have some subset of that interval to the left and/or right of `[left, right)`. We replace our current interval `[x, y)` with those (up to 2) new intervals.

Querying a Range

As the intervals are sorted, we use binary search to find the single interval that could intersect `[left, right)`, then verify that it does.

**Python**
```python
class RangeModule(object):
    def __init__(self):
        self.ranges = []

    def _bounds(self, left, right):
        i, j = 0, len(self.ranges) - 1
        for d in (100, 10, 1):
            while i + d - 1 < len(self.ranges) and self.ranges[i+d-1][1] < left:
                i += d
            while j >= d - 1 and self.ranges[j-d+1][0] > right:
                j -= d
        return i, j

    def addRange(self, left, right):
        i, j = self._bounds(left, right)
        if i <= j:
            left = min(left, self.ranges[i][0])
            right = max(right, self.ranges[j][1])
        self.ranges[i:j+1] = [(left, right)]

    def queryRange(self, left, right):
        i = bisect.bisect_left(self.ranges, (left, float('inf')))
        if i: i -= 1
        return (bool(self.ranges) and
                self.ranges[i][0] <= left and
                right <= self.ranges[i][1])

    def removeRange(self, left, right):
        i, j = self._bounds(left, right)
        merge = []
        for k in xrange(i, j+1):
            if self.ranges[k][0] < left:
                merge.append((self.ranges[k][0], left))
            if right < self.ranges[k][1]:
                merge.append((right, self.ranges[k][1]))
        self.ranges[i:j+1] = merge
```

**Algorithm (Java)**

We will maintain the structure as a `TreeSet ranges = new TreeSet<Interval>();`. We introduce a new Comparable class Interval to represent our half-open intervals. They compare by right-most coordinate as later we will see that it simplifies our work. Also note that this ordering is consistent with equals, which is important when dealing with Sets.

Adding and Removing a Range

The basic structure of adding and removing a range is the same. First, we must iterate over the relevant subset of ranges. This is done using iterators so that we can itr.remove on the fly, and breaking when the intervals go too far to the right.

The critical logic of addRange is simply to make left, right the smallest and largest seen coordinates. After, we add one giant interval representing the union of all intervals seen that touched `[left, right]`.

The logic of removeRange is to remember in todo the intervals we wanted to replace the removed interval with. After, we can add them all back in.

Querying a Range

As the intervals are sorted, we search to find the single interval that could intersect `[left, right)`, then verify that it does. As the TreeSet uses a balanced (red-black) tree, this has logarithmic complexity.

**Java**
```java
class RangeModule {
    TreeSet<Interval> ranges;
    public RangeModule() {
        ranges = new TreeSet();
    }

    public void addRange(int left, int right) {
        Iterator<Interval> itr = ranges.tailSet(new Interval(0, left - 1)).iterator();
        while (itr.hasNext()) {
            Interval iv = itr.next();
            if (right < iv.left) break;
            left = Math.min(left, iv.left);
            right = Math.max(right, iv.right);
            itr.remove();
        }
        ranges.add(new Interval(left, right));
    }

    public boolean queryRange(int left, int right) {
        Interval iv = ranges.higher(new Interval(0, left));
        return (iv != null && iv.left <= left && right <= iv.right);
    }

    public void removeRange(int left, int right) {
        Iterator<Interval> itr = ranges.tailSet(new Interval(0, left)).iterator();
        ArrayList<Interval> todo = new ArrayList();
        while (itr.hasNext()) {
            Interval iv = itr.next();
            if (right < iv.left) break;
            if (iv.left < left) todo.add(new Interval(iv.left, left));
            if (right < iv.right) todo.add(new Interval(right, iv.right));
            itr.remove();
        }
        for (Interval iv: todo) ranges.add(iv);
    }
}

class Interval implements Comparable<Interval>{
    int left;
    int right;

    public Interval(int left, int right){
        this.left = left;
        this.right = right;
    }

    public int compareTo(Interval that){
        if (this.right == that.right) return this.left - that.left;
        return this.right - that.right;
    }
}
```

**Complexity Analysis**

* Time Complexity: Let $K$ be the number of elements in ranges. `addRange` and `removeRange` operations have $O(K)$ complexity. `queryRange` has $O(\log K)$ complexity. Because `addRange`, `removeRange` adds at most 1 interval at a time, you can bound these further. For example, if there are $A$ `addRange`, $R$ `removeRange`, and $Q$ `queryRange` number of operations respectively, we can express our complexity as $O((A+R)^2 Q \log(A+R))$.

* Space Complexity: $O(A+R)$, the space used by ranges.

# Submissions
---
**Solution 1: (Maintain Sorted Disjoint Intervals)**
```
Runtime: 516 ms
Memory Usage: 16.5 MB
```
```python
class RangeModule:

    def __init__(self):
        self.ranges = []
    
    def _bounds(self, left, right):
        i, j = 0, len(self.ranges) - 1
        for d in (100, 10, 1):  # The total number of calls to addRange in a single test case is at most 1000
            while i + d - 1 < len(self.ranges) and self.ranges[i+d-1][1] < left:
                i += d
            while j >= d - 1 and self.ranges[j-d+1][0] > right:
                j -= d
        return i, j

    def addRange(self, left: int, right: int) -> None:
        i, j = self._bounds(left, right)
        if i <= j:
            left = min(left, self.ranges[i][0])
            right = max(right, self.ranges[j][1])
        self.ranges[i:j+1] = [(left, right)]

    def queryRange(self, left: int, right: int) -> bool:
        i = bisect.bisect_left(self.ranges, (left, float('inf')))
        if i: i -= 1
        return (bool(self.ranges) and
                self.ranges[i][0] <= left and
                right <= self.ranges[i][1])

    def removeRange(self, left: int, right: int) -> None:
        i, j = self._bounds(left, right)
        merge = []
        for k in range(i, j+1):
            if self.ranges[k][0] < left:
                merge.append((self.ranges[k][0], left))
            if right < self.ranges[k][1]:
                merge.append((right, self.ranges[k][1]))
        self.ranges[i:j+1] = merge


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
```