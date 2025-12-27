2080. Range Frequency Queries

Design a data structure to find the **frequency** of a given value in a given subarray.

The **frequency** of a value in a subarray is the number of occurrences of that value in the subarray.

Implement the `RangeFreqQuery` class:

* `RangeFreqQuery(int[] arr)` Constructs an instance of the class with the given **0-indexed** integer array `arr`.
* `int query(int left, int right, int value)` Returns the frequency of `value` in the subarray `arr[left...right]`.

A **subarray** is a contiguous sequence of elements within an array. `arr[left...right]` denotes the subarray that contains the elements of nums between indices `left` and `right` (inclusive).

 

**Example 1:**
```
Input
["RangeFreqQuery", "query", "query"]
[[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]
Output
[null, 1, 2]

Explanation
RangeFreqQuery rangeFreqQuery = new RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]);
rangeFreqQuery.query(1, 2, 4); // return 1. The value 4 occurs 1 time in the subarray [33, 4]
rangeFreqQuery.query(0, 11, 33); // return 2. The value 33 occurs 2 times in the whole array.
```

**Constraints:**

* `1 <= arr.length <= 10^5`
* `1 <= arr[i], value <= 10^4`
* `0 <= left <= right < arr.length`
* At most 10^5 calls will be made to `query`

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 1888 ms
Memory Usage: 53.2 MB
```
```python
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        N = len(arr)
        self.pre = collections.defaultdict(list)
        for i, a in enumerate(arr):
            self.pre[a] += [i]

    def query(self, left: int, right: int, value: int) -> int:
        return bisect.bisect_right(self.pre[value], right) - bisect.bisect_left(self.pre[value], left)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
```

**Solution 2: (Binary Search)**
```
Runtime: 73 ms, Beats 37.99%
Memory: 242.48 MB, Beats 49.82%
```
```c++
class RangeFreqQuery {
    unordered_map<int, vector<int>> mp;
public:
    RangeFreqQuery(vector<int>& arr) {
        for (int i = 0; i < size(arr); i++) {
            mp[arr[i]].push_back(i);
        }
    }
    
    int query(int left, int right, int value) {
        return upper_bound(begin(mp[value]), end(mp[value]), right) - lower_bound(begin(mp[value]), end(mp[value]), left);
    }
};

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * RangeFreqQuery* obj = new RangeFreqQuery(arr);
 * int param_1 = obj->query(left,right,value);
 */
```
