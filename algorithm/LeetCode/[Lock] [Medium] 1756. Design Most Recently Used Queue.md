1756. Design Most Recently Used Queue

Design a queue-like data structure that moves the most recently used element to the end of the queue.

Implement the MRUQueue class:

* `MRUQueue(int n)` constructs the `MRUQueue` with `n` elements: `[1,2,3,...,n]`.
* `int fetch(int k)` moves the `k`th element (**1-indexed**) to the end of the queue and returns it.
 

**Example 1:**
```
Input:
["MRUQueue", "fetch", "fetch", "fetch", "fetch"]
[[8], [3], [5], [2], [8]]
Output:
[null, 3, 6, 2, 2]

Explanation:
MRUQueue mRUQueue = new MRUQueue(8); // Initializes the queue to [1,2,3,4,5,6,7,8].
mRUQueue.fetch(3); // Moves the 3rd element (3) to the end of the queue to become [1,2,4,5,6,7,8,3] and returns it.
mRUQueue.fetch(5); // Moves the 5th element (6) to the end of the queue to become [1,2,4,5,7,8,3,6] and returns it.
mRUQueue.fetch(2); // Moves the 2nd element (2) to the end of the queue to become [1,4,5,7,8,3,6,2] and returns it.
mRUQueue.fetch(8); // The 8th element (2) is already at the end of the queue so just return it.
```

**Constraints:**

* `1 <= n <= 2000`
* `1 <= k <= n`
* At most `2000` calls will be made to `fetch`.
 

**Follow up:** Finding an `O(n)` algorithm per fetch is a bit easy. Can you find an algorithm with a better complexity for each fetch call?

**Solution 1: (Array)**
```
Runtime: 152 ms
Memory Usage: 15.2 MB
```
```python
class MRUQueue:

    def __init__(self, n: int):
        self.nums = [x for x in range(1,n+1)]

    def fetch(self, k: int) -> int:
        self.nums.append(self.nums.pop(k-1))
        return self.nums[-1]


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
```

**Solution 2: (Array)**
```
Runtime: 159 ms
Memory Usage: 34.1 MB
```
```c++
class MRUQueue {
public:
    vector<int> v;
    MRUQueue(int n) {
        for(int i=1; i<=n; i++)
            v.push_back(i);
    }
    
    int fetch(int k) {
        int res = v[k-1];
        v.erase(v.begin()+k-1);
        v.push_back(res);
        return res;
    }
};

/**
 * Your MRUQueue object will be instantiated and called as such:
 * MRUQueue* obj = new MRUQueue(n);
 * int param_1 = obj->fetch(k);
 */
```

**Solution 3: (BIT, Fenwick Tree)**
‵``
Runtime: 12 ms, Beats 86.88%
Memory: 42.47 MB, Beats 43.92%
```
```c++
class FenwickTree {
private:
    vector<int> tree;

public:
    FenwickTree(int size) : tree(size + 1, 0) {}

    // Calculates the sum up to the given index
    int sum(int index) {
        int result = 0;
        while (index > 0) {
            result += tree[index];
            index &= index - 1;
        }
        return result;
    }

    // Updates the tree by adding value at the given index
    void insert(int index, int value) {
        // Adjust for 1-based indexing
        index += 1;
        while (index < tree.size()) {
            tree[index] += value;
            index += index & -index;
        }
    }
};

class MRUQueue {
private:
    int size;
    FenwickTree tree;
    vector<int> values;
public:
    MRUQueue(int n): size(n), tree(n + 2000), values(n + 2000, 0) {
        for (int i = 0; i < n; ++i) {
            // Mark positions in the Fenwick Tree
            tree.insert(i, 1);
            // Set the initial values
            values[i] = i + 1;
        }
    }
    
    int fetch(int k) {
        int low = 0, high = size;

        // Binary search to find the kth value
        while (low < high) {
            int mid = (low + high) >> 1;
            if (tree.sum(mid) < k) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }

        // Move the found value to the end
        tree.insert(low - 1, -1);
        tree.insert(size, 1);
        values[size] = values[low - 1];
        size += 1;

        // Return the fetched value
        return values[low - 1];
    }
};

/**
 * Your MRUQueue object will be instantiated and called as such:
 * MRUQueue* obj = new MRUQueue(n);
 * int param_1 = obj->fetch(k);
 */
```
