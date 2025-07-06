295. Find Median from Data Stream

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,

`[2,3,4]`, the median is `3`

`[2,3]`, the median is `(2 + 3) / 2 = 2.5`

Design a data structure that supports the following two operations:

* `void addNum(int num)` - Add a integer number from the data stream to the data structure.
* `double findMedian()` - Return the median of all elements so far.
 

**Example:**
```
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
```

**Follow up:**

* If all integer numbers from the stream are between `0` and `100`, how would you optimize it?
* If 99% of all integer numbers from the stream are between `0` and `100`, how would you optimize it?

# Solution
---
## Approach 1: Simple Sorting
**Intuition**

Do what the question says.

**Algorithm**

Store the numbers in a resize-able container. Every time you need to output the median, sort the container and output the median.

```c++
class MedianFinder {
    vector<double> store;

public:
    // Adds a number into the data structure.
    void addNum(int num)
    {
        store.push_back(num);
    }

    // Returns the median of current data stream
    double findMedian()
    {
        sort(store.begin(), store.end());

        int n = store.size();
        return (n & 1 ? store[n / 2] : (store[n / 2 - 1] + store[n / 2]) * 0.5);
    }
};
```

**Complexity Analysis**

* Time complexity: $O(n\log n) + O(1) \simeq O(n\log n)$.

Adding a number takes amortized $O(1)$ time for a container with an efficient resizing scheme.
Finding the median is primarily dependent on the sorting that takes place. This takes $O(n\log n)$ time for a standard comparative sort.

* Space complexity: $O(n)$ linear space to hold input in a container. No extra space other than that needed (since sorting can usually be done in-place).

## Approach 2: Insertion Sort
**Intuition**

Keeping our input container always sorted (i.e. maintaining the sorted nature of the container as an invariant).

**Algorithm**

Which algorithm allows a number to be added to a sorted list of numbers and yet keeps the entire list sorted? Well, for one, insertion sort!

We assume that the current list is already sorted. When a new number comes, we have to add it to the list while maintaining the sorted nature of the list. This is achieved easily by finding the correct place to insert the incoming number, using a binary search (remember, the list is always sorted). Once the position is found, we need to shift all higher elements by one space to make room for the incoming number.

This method would work well when the amount of insertion queries is lesser or about the same as the amount of median finding queries.

```c++
class MedianFinder {
    vector<int> store; // resize-able container

public:
    // Adds a number into the data structure.
    void addNum(int num)
    {
        if (store.empty())
            store.push_back(num);
        else
            store.insert(lower_bound(store.begin(), store.end(), num), num);     // binary search and insertion combined
    }

    // Returns the median of current data stream
    double findMedian()
    {
        int n = store.size();
        return n & 1 ? store[n / 2] : (store[n / 2 - 1] + store[n / 2]) * 0.5;
    }
};
```

**Complexity Analysis**

* Time complexity: $O(n) + O(\log n) \approx O(n)$.

    * Binary Search takes $O(\log n)$ time to find correct insertion position.
    * Insertion can take up to $O(n)$ time since elements have to be shifted inside the container to make room for the new element.

>Pop quiz: Can we use a linear search instead of a binary search to find insertion position, without incurring any significant runtime penalty?

* Space complexity: $O(n)$ linear space to hold input in a container.

## Approach 3: Two Heaps
**Intuition**

The above two approaches gave us some valuable insights on how to tackle this problem. Concretely, one can infer two things:

1. If we could maintain direct access to median elements at all times, then finding the median would take a constant amount of time.
1. If we could find a reasonably fast way of adding numbers to our containers, additional penalties incurred could be lessened.

But perhaps the most important insight, which is not readily observable, is the fact that we only need a consistent way to access the median elements. Keeping the entire input sorted is **not a requirement**.

>Well, if only there were a data structure which could handle our needs.

As it turns out there are two data structures for the job:

* Heaps (or Priority Queues [1])
* Self-balancing Binary Search Trees (we'll talk more about them in Approach 4)

Heaps are a natural ingredient for this dish! Adding elements to them take logarithmic order of time. They also give direct access to the maximal/minimal elements in a group.

If we could maintain two heaps in the following way:

* A max-heap to store the smaller half of the input numbers
* A min-heap to store the larger half of the input numbers

This gives access to median values in the input: they comprise the top of the heaps!

**Wait, what? How?**

If the following conditions are met:

1. Both the heaps are balanced (or nearly balanced)
1. The max-heap contains all the smaller numbers while the min-heap contains all the larger numbers

then we can say that:

* All the numbers in the max-heap are smaller or equal to the top element of the max-heap (let's call it $x$)
* All the numbers in the min-heap are larger or equal to the top element of the min-heap (let's call it $y$)
Then $x$ and/or $y$ are smaller than (or equal to) almost half of the elements and larger than (or equal to) the other half. That is the definition of median elements.

This leads us to a huge point of pain in this approach: **balancing the two heaps!**

**Algorithm**

* Two priority queues:

    * A max-heap lo to store the smaller half of the numbers
    * A min-heap hi to store the larger half of the numbers

* The max-heap lo is allowed to store, at worst, one more element more than the min-heap hi. Hence if we have processed kk elements:

    * If $k = 2*n + 1 \quad (\forall \, n \in \mathbb{Z})$, then lo is allowed to hold $n+1$ elements, while `hi` can hold $n$ elements.
    * If $k = 2*n \quad (\forall \, n \in \mathbb{Z})$, then both heaps are balanced and hold nn elements each.

    This gives us the nice property that when the heaps are perfectly balanced, the median can be derived from the tops of both heaps. Otherwise, the top of the max-heap `lo` holds the legitimate median.

* Adding a number num:

    * Add `num` to max-heap `lo`. Since lo received a new element, we must do a balancing step for `hi`. So remove the largest element from `lo` and offer it to `hi`.
    * The min-heap `hi` might end holding more elements than the max-heap `lo`, after the previous operation. We fix that by removing the smallest element from `hi` and offering it to `lo`.
    
The above step ensures that we do not disturb the nice little size property we just mentioned.

A little example will clear this up! Say we take input from the stream `[41, 35, 62, 5, 97, 108]`. The run-though of the algorithm looks like this:
```
Adding number 41
MaxHeap lo: [41]           // MaxHeap stores the largest value at the top (index 0)
MinHeap hi: []             // MinHeap stores the smallest value at the top (index 0)
Median is 41
=======================
Adding number 35
MaxHeap lo: [35]
MinHeap hi: [41]
Median is 38
=======================
Adding number 62
MaxHeap lo: [41, 35]
MinHeap hi: [62]
Median is 41
=======================
Adding number 4
MaxHeap lo: [35, 4]
MinHeap hi: [41, 62]
Median is 38
=======================
Adding number 97
MaxHeap lo: [41, 35, 4]
MinHeap hi: [62, 97]
Median is 41
=======================
Adding number 108
MaxHeap lo: [41, 35, 4]
MinHeap hi: [62, 97, 108]
Median is 51.5
```

```c++
class MedianFinder {
    priority_queue<int> lo;                              // max heap
    priority_queue<int, vector<int>, greater<int>> hi;   // min heap

public:
    // Adds a number into the data structure.
    void addNum(int num)
    {
        lo.push(num);                                    // Add to max heap

        hi.push(lo.top());                               // balancing step
        lo.pop();

        if (lo.size() < hi.size()) {                     // maintain size property
            lo.push(hi.top());
            hi.pop();
        }
    }

    // Returns the median of current data stream
    double findMedian()
    {
        return lo.size() > hi.size() ? (double) lo.top() : (lo.top() + hi.top()) * 0.5;
    }
};
```

**Complexity Analysis**

* Time complexity: $O(5 \cdot \log n) + O(1) \approx O(\log n)$.

At worst, there are three heap insertions and two heap deletions from the top. Each of these takes about $O(\log n)$ time.
Finding the mean takes constant $O(1)$ time since the tops of heaps are directly accessible.

* Space complexity: $O(n)$ linear space to hold input in containers.

## Approach 4: Multiset and Two Pointers
**Intuition**

Self-balancing Binary Search Trees (like an AVL Tree) have some very interesting properties. They maintain the tree's height to a logarithmic bound. Thus inserting a new element has reasonably good time performance. The median always winds up in the root of the tree and/or one of its children. Solving this problem using the same approach as Approach 3 but using a Self-balancing BST seems like a good choice. Except the fact that implementing such a tree is not trivial and prone to errors.

Why reinvent the wheel? Most languages implement a `multiset` class which emulates such behavior. The only problem remains keeping track of the median elements. That is easily solved with pointers! [2]

We maintain two pointers: one for the lower median element and the other for the higher median element. When the total number of elements is odd, both the pointers point to the same median element (since there is only one median in this case). When the number of elements is even, the pointers point to two consecutive elements, whose mean is the representative median of the input.

**Algorithm**

* Two iterators/pointers lo_median and hi_median, which iterate over the data multiset.

* While adding a number num, three cases arise:

    1. The container is currently empty. Hence we simply insert num and set both pointers to point to this element.

    1. The container currently holds an odd number of elements. This means that both the pointers currently point to the same element.

        * If `num` is not equal to the current median element, then num goes on either side of it. Whichever side it goes, the size of that part increases and hence the corresponding pointer is updated. For example, if num is less than the median element, the size of the lesser half of input increases by 11 on inserting num. Thus it makes sense to decrement lo_median.
        * If `num` is equal to the current median element, then the action taken is dependent on how num is inserted into data. NOTE: In our given C++ code example, `std::multiset::insert` inserts an element after all elements of equal value. Hence we increment hi_median.

    1. The container currently holds an even number of elements. This means that the pointers currently point to consecutive elements.

        * If `num` is a number between both median elements, then num becomes the new median. Both pointers must point to it.
Otherwise, num increases the size of either the lesser or higher half of the input. We update the pointers accordingly. It is important to remember that both the pointers must point to the same element now.
        * Finding the median is easy! It is simply the mean of the elements pointed to by the two pointers `lo_median` and `hi_median`.
        
```c++
class MedianFinder {
    multiset<int> data;
    multiset<int>::iterator lo_median, hi_median;

public:
    MedianFinder()
        : lo_median(data.end())
        , hi_median(data.end())
    {
    }

    void addNum(int num)
    {
        const size_t n = data.size();   // store previous size

        data.insert(num);               // insert into multiset

        if (!n) {
            // no elements before, one element now
            lo_median = hi_median = data.begin();
        }
        else if (n & 1) {
            // odd size before (i.e. lo == hi), even size now (i.e. hi = lo + 1)

            if (num < *lo_median)       // num < lo
                lo_median--;
            else                        // num >= hi
                hi_median++;            // insertion at end of equal range
        }
        else {
            // even size before (i.e. hi = lo + 1), odd size now (i.e. lo == hi)

            if (num > *lo_median && num < *hi_median) {
                lo_median++;                    // num in between lo and hi
                hi_median--;
            }
            else if (num >= *hi_median)         // num inserted after hi
                lo_median++;
            else                                // num <= lo < hi
                lo_median = --hi_median;        // insertion at end of equal range spoils lo
        }
    }

    double findMedian()
    {
        return (*lo_median + *hi_median) * 0.5;
    }
};
```

A much shorter (but harder to understand), one pointer version [3] of this solution is given below:

```c++
class MedianFinder {
    multiset<int> data;
    multiset<int>::iterator mid;

public:
    MedianFinder()
        : mid(data.end())
    {
    }

    void addNum(int num)
    {
        const int n = data.size();
        data.insert(num);

        if (!n)                                 // first element inserted
            mid = data.begin();
        else if (num < *mid)                    // median is decreased
            mid = (n & 1 ? mid : prev(mid));
        else                                    // median is increased
            mid = (n & 1 ? next(mid) : mid);
    }

    double findMedian()
    {
        const int n = data.size();
        return (*mid + *next(mid, n % 2 - 1)) * 0.5;
    }
};
```

**Complexity Analysis**

* Time complexity: $O(\log n) + O(1) \approx O(\log n)$.

Inserting a number takes $O(\log n)$ time for a standard multiset scheme. [4]
Finding the mean takes constant $O(1)$ time since the median elements are directly accessible from the two pointers.

* Space complexity: $O(n)$ linear space to hold input in container.

# Submissions
---
```
Runtime: 1236 ms
Memory Usage: 24 MB
```
**Solution 1: (Simple Sorting)**

```python
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.store = []

    def addNum(self, num: int) -> None:
        self.store.append(num)

    def findMedian(self) -> float:
        self.store.sort()
        N = len(self.store)
        return self.store[N//2] if N % 2 else (self.store[N//2 -1] + self.store[N//2]) * .5


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```

**Solution 2: (Insertion Sort)**
```
Runtime: 220 ms
Memory Usage: 23.9 MB
```
```python
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.store = []

    def addNum(self, num: int) -> None:
        if not self.store:
            self.store.append(num)
        else:
            bisect.insort(self.store, num)

    def findMedian(self) -> float:
        N = len(self.store)
        
        return self.store[N//2] if N % 2 else (self.store[N//2 - 1] + self.store[N//2]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```

**Solution 3: (Two Heaps, Min and Max Heap)**
```
Runtime: 212 ms
Memory Usage: 23.6 MB
```
```python
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lo = []  // max heap
        self.hi = []  // min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -self.lo[0])
        heapq.heappop(self.lo)
        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -self.hi[0])
            heapq.heappop(self.hi)

    def findMedian(self) -> float:
        return -self.lo[0] if len(self.lo) > len(self.hi) else (-self.lo[0] + self.hi[0]) * .5


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```

**Solution 4: (SortedList)**
```
Runtime: 308 ms
Memory Usage: 24.2 MB
```
```python
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        from sortedcontainers import SortedList
        self.sl = SortedList([])

    def addNum(self, num: int) -> None:
        self.sl.add(num)

    def findMedian(self) -> float:
        n = len(self.sl)
        if n % 2:
            return self.sl[n//2]
        else:
            return (self.sl[n//2] + self.sl[n//2 - 1])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```

**Solution 5: (Two Heaps)**
```
Runtime: 87 ms, Beats 15.11%
Memory: 125.08 MB, Beats 43.41%
```
```c++
class MedianFinder {
    priority_queue<int> lo;
    priority_queue<int,vector<int>,greater<>> hi;
public:
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        lo.push(num);
        hi.push(lo.top());
        lo.pop();
        if (hi.size() - lo.size() > 1) {
            lo.push(hi.top());
            hi.pop();
        }
    }
    
    double findMedian() {
        if (lo.size() == hi.size()) {
            return (lo.top() + hi.top())/2.0;
        } else {
            return hi.top();
        }
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
```
