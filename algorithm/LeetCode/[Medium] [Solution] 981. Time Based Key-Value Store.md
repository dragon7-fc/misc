981. Time Based Key-Value Store

Create a timebased key-value store class `TimeMap`, that supports two operations.

1. `set(string key, string value, int timestamp)``

    * Stores the `key` and `value`, along with the given `timestamp`.
1. `get(string key, int timestamp)``

    * Returns a `value` such that `set(key, value, timestamp_prev)` was called previously, with `timestamp_prev <= timestamp`.
    * If there are multiple such values, it returns the one with the largest `timestamp_prev`.
    * If there are no values, it returns the empty string (`""`).
 

**Example 1:**
```
Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
Explanation:   
TimeMap kv;   
kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1   
kv.get("foo", 1);  // output "bar"   
kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"   
kv.set("foo", "bar2", 4);   
kv.get("foo", 4); // output "bar2"   
kv.get("foo", 5); //output "bar2"   
```

**Example 2:**
```
Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
Output: [null,null,null,"","high","high","low","low"]
```

**Note:**

* All key/value strings are lowercase.
* All key/value strings have length in the range `[1, 100]`
* The timestamps for all `TimeMap.set` operations are strictly increasing.
* `1 <= timestamp <= 10^7`
* `TimeMap.set` and `TimeMap.get` functions will be called a total of `120000` times (combined) per test case.

## Approach 1: HashMap + Binary Search
**Intuition and Algorithm**

For each `key` we get or set, we only care about the timestamps and values for that key. We can store this information in a `HashMap`.

Now, for each `key`, we can binary search the sorted list of timestamps to find the relevant `value` for that `key`.

```python
class TimeMap(object):
    def __init__(self):
        self.M = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        self.M[key].append((timestamp, value))

    def get(self, key, timestamp):
        A = self.M.get(key, None)
        if A is None: return ""
        i = bisect.bisect(A, (timestamp, chr(127)))
        return A[i-1][1] if i else ""
```

**Complexity Analysis**

* Time Complexity: $O(1)$ for each set operation, and $O(\log N)$ for each get operation, where $N$ is the number of entries in the `TimeMap`.

* Space Complexity: $O(N)$.

## Approach 2: TreeMap
**Intuition and Algorithm**

In Java, we can use `TreeMap.floorKey(timestamp)` to find the largest timestamp smaller than the given timestamp.

We build our solution in the same way as Approach 1, swapping in this functionality.

```java
class TimeMap {
    Map<String, TreeMap<Integer, String>> M;

    public TimeMap() {
        M = new HashMap();
    }

    public void set(String key, String value, int timestamp) {
        if (!M.containsKey(key))
            M.put(key, new TreeMap());

        M.get(key).put(timestamp, value);
    }

    public String get(String key, int timestamp) {
        if (!M.containsKey(key)) return "";

        TreeMap<Integer, String> tree = M.get(key);
        Integer t = tree.floorKey(timestamp);
        return t != null ? tree.get(t) : "";
    }
}
```

**Complexity Analysis**

* Time Complexity: $O(1)$ for each set operation, and $O(\log N)$ for each get operation, where $N$ is the number of entries in the `TimeMap`.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution:**
```
Runtime: 744 ms
Memory Usage: 68.5 MB
```
```python
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.M = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.M[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        A = self.M.get(key, None)
        if A is None: return ""
        i = bisect.bisect(A, (timestamp, chr(127)))
        return A[i-1][1] if i else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```