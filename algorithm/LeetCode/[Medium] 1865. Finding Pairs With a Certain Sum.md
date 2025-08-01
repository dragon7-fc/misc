1865. Finding Pairs With a Certain Sum

You are given two integer arrays `nums1` and `nums2`. You are tasked to implement a data structure that supports queries of two types:

1. **Add** a positive integer to an element of a given `index` in the array `nums2`.
1. **Count** the number of pairs `(i, j)` such that `nums1[i] + nums2[j]` equals a given value (`0 <= i < nums1.length` and `0 <= j < nums2.length`).

Implement the `FindSumPairs` class:

* `FindSumPairs(int[] nums1, int[] nums2)` Initializes the `FindSumPairs` object with two integer arrays `nums1` and `nums2`.
* `void add(int index, int val)` Adds `val` to `nums2[index]`, i.e., apply `nums2[index] += val`.
* `int count(int tot)` Returns the number of pairs `(i, j)` such that `nums1[i] + nums2[j] == tot`.
 

**Example 1:**
```
Input
["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
[[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]
Output
[null, 8, null, 2, 1, null, null, 11]

Explanation
FindSumPairs findSumPairs = new FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]);
findSumPairs.count(7);  // return 8; pairs (2,2), (3,2), (4,2), (2,4), (3,4), (4,4) make 2 + 5 and pairs (5,1), (5,5) make 3 + 4
findSumPairs.add(3, 2); // now nums2 = [1,4,5,4,5,4]
findSumPairs.count(8);  // return 2; pairs (5,2), (5,4) make 3 + 5
findSumPairs.count(4);  // return 1; pair (5,0) makes 3 + 1
findSumPairs.add(0, 1); // now nums2 = [2,4,5,4,5,4]
findSumPairs.add(1, 1); // now nums2 = [2,5,5,4,5,4]
findSumPairs.count(7);  // return 11; pairs (2,1), (2,2), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,4) make 2 + 5 and pairs (5,3), (5,5) make 3 + 4
```

**Constraints:**

* `1 <= nums1.length <= 1000`
* `1 <= nums2.length <= 10^5`
* `1 <= nums1[i] <= 10^9`
* `1 <= nums2[i] <= 10^5`
* `0 <= index < nums2.length`
* `1 <= val <= 10^5`
* `1 <= tot <= 10^9`
* At most `1000` calls are made to `add` and `count` each.

# Submissions
---
**Solution 1: (Hash Table)**
```
Runtime: 1232 ms
Memory Usage: 44.5 MB
```
```python
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.freq[self.nums2[index]] -= 1  # Remove old one
        self.nums2[index] += val
        self.freq[self.nums2[index]] += 1  # Count new one

    def count(self, tot: int) -> int:
        ans = 0
        for a in self.nums1:  
            ans += self.freq[tot - a]  # a + b = tot -> b = tot - a
        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
```

**Solution 2: (Hash Table)**
```
Runtime: 291 ms, Beats 34.03%
Memory: 189.75 MB, Beats 19.00%
```
```c++
class FindSumPairs {
    vector<int> dp, dp2;
    unordered_map<int,int> cnt;
public:
    FindSumPairs(vector<int>& nums1, vector<int>& nums2) {
        dp = nums1;
        dp2 = nums2;
        for (auto &num: nums2) {
            cnt[num] += 1;
        }
    }
    
    void add(int index, int val) {
        cnt[dp2[index]] -= 1;
        cnt[dp2[index] + val] += 1;
        dp2[index] += val;
    }
    
    int count(int tot) {
        int ans = 0;
        for (auto &num: dp) {
            ans += cnt[tot - num];
        }
        return ans;
    }
};
```
