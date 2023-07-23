673. Number of Longest Increasing Subsequence

Given an unsorted array of integers, find the number of longest increasing subsequence.

**Example 1:**

```
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
```

**Example 2:**

```
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
```

**Note:** Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.

# Solution
---
## Approach 1: Dynamic Programming
**Intuition and Algorithm**

Suppose for sequences ending at `nums[i]`, we knew the length `length[i]` of the longest sequence, and the number `count[i]` of such sequences with that length.

For every `i < j` with `A[i] < A[j]`, we might append `A[j]` to a longest subsequence ending at `A[i]`. It means that we have demonstrated `count[i]` subsequences of length `length[i] + 1`.

Now, if those sequences are longer than `length[j]`, then we know we have `count[i]` sequences of this length. If these sequences are equal in length to `length[j]`, then we know that there are now `count[i]` additional sequences to be counted of that length (ie. `count[j] += count[i]`).

```python
class Solution(object):
    def findNumberOfLIS(self, nums):
        N = len(nums)
        if N <= 1: return N
        lengths = [0] * N #lengths[i] = longest ending in nums[i]
        counts = [1] * N #count[i] = number of longest ending in nums[i]

        for j, num in enumerate(nums):
            for i in xrange(j):
                if nums[i] < nums[j]:
                    if lengths[i] >= lengths[j]:
                        lengths[j] = 1 + lengths[i]
                        counts[j] = counts[i]
                    elif lengths[i] + 1 == lengths[j]:
                        counts[j] += counts[i]

        longest = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$ where $N$ is the length of nums. There are two for-loops and the work inside is $O(1)$.

* Space Complexity: $O(N)$, the space used by lengths and counts.

## Approach 2: Segment Tree
**Intuition**

Suppose we knew for each length `L`, the number of sequences with length `L` ending in `x`. Then when considering the next element of `nums`, updating our knowledge hinges on knowing the number of sequences with length `L-1` ending in `y < x`. This type of query over an interval is a natural fit for using some sort of tree.

We could try using Fenwick trees, but we would have to store $N$ of them, which naively might be $O(N^2)$ space. Here, we focus on an implementation of a Segment Tree.

**Algorithm**

Implementing Segment Trees is discussed in more detail here. In this approach, we will attempt a variant of segment tree that doesn't use lazy propagation.

First, let us call the "value" of an interval, the longest length of an increasing subsequence, and the number of such subsequences in that interval.

Each node knows about the interval of nums values it is considering `[node.range_left, node.range_right]`, and it knows about `node.val`, which contains information on the value of interval. Nodes also have `node.left` and `node.right` children that represents the left and right half of the interval node considers. These child nodes are created on demand as appropriate.

Now, `query(node, key)` will tell us the value of the interval specified by `node`, except we'll exclude anything above `key`. When `key` is outside the interval specified by `node`, we return the answer. Otherwise, we'll divide the interval into two and query both intervals, then `merge` the result.

What does `merge(v1, v2)` do? Suppose two nodes specify adjacent intervals, and have corresponding values `v1 = node1.val`, `v2 = node2.val`. What should the aggregate value, `v = merge(v1, v2)` be? If there are longer subsequences in one node, then `v` will just be that. If both nodes have longest subsequences of equal length, then we should count subsequences in both nodes. Note that we did not have to consider cases where larger subsequences were made, since these were handled by insert.

What does `insert(node, key, val)` do? We repeatedly insert the key into the correct half of the interval that node specifies (possibly a point), and after such insertion this node's value could change, so we merge the values together again.

Finally, in our main algorithm, for each num in `nums` we query for the value length, `count` of the interval below num, and we know it will lead to `count` additional sequences of length `length + 1`. We then update our tree with that knowledge.

```python
class Node(object):
    def __init__(self, start, end):
        self.range_left, self.range_right = start, end
        self._left = self._right = None
        self.val = 0, 1 #length, count
    @property
    def range_mid(self):
        return (self.range_left + self.range_right) / 2
    @property
    def left(self):
        self._left = self._left or Node(self.range_left, self.range_mid)
        return self._left
    @property
    def right(self):
        self._right = self._right or Node(self.range_mid + 1, self.range_right)
        return self._right

def merge(v1, v2):
    if v1[0] == v2[0]:
        if v1[0] == 0: return (0, 1)
        return v1[0], v1[1] + v2[1]
    return max(v1, v2)

def insert(node, key, val):
    if node.range_left == node.range_right:
        node.val = merge(val, node.val)
        return
    if key <= node.range_mid:
        insert(node.left, key, val)
    else:
        insert(node.right, key, val)
    node.val = merge(node.left.val, node.right.val)

def query(node, key):
    if node.range_right <= key:
        return node.val
    elif node.range_left > key:
        return 0, 1
    else:
        return merge(query(node.left, key), query(node.right, key))

class Solution(object):
    def findNumberOfLIS(self, nums):
        if not nums: return 0
        root = Node(min(nums), max(nums))
        for num in nums:
            length, count = query(root, num-1)
            insert(root, num, (length+1, count))
        return root.val[1]
```

**Complexity Analysis**

* Time Complexity: $O(N\log {N})$ where $N$ is the length of nums. In our main for loop, we do $O(\log{N})$ work to query and insert.

* Space Complexity: $O(N)$, the space used by the segment tree.

# Submissions
---
**Solution 1: (Dynamic Programming Bottom-Up)**
```
Runtime: 768 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1: return N
        lengths = [0] * N #lengths[i] = longest ending in nums[i]
        counts = [1] * N #count[i] = number of longest ending in nums[i]

        for j, num in enumerate(nums):
            for i in range(j):
                if nums[i] < nums[j]:
                    if lengths[i] >= lengths[j]:
                        lengths[j] = 1 + lengths[i]
                        counts[j] = counts[i]
                    elif lengths[i] + 1 == lengths[j]:
                        counts[j] += counts[i]

        longest = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 197 ms
Memory: 13.1 MB
```
```c++
class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n, 1);
        vector<int> cnt(n, 1);
        int mx = INT_MIN;
        for (int j = 0; j < nums.size(); j ++) {
            for (int i = 0; i < j; i ++) {
                if (nums[i] < nums[j]) {
                    if (dp[i] >= dp[j]) {
                        dp[j] = dp[i] + 1;
                        cnt[j] = cnt[i];
                    } else if (dp[j] == dp[i]+1) {
                        cnt[j] += cnt[i];
                    }
                }
            }
            mx = max(mx, dp[j]);
        }
        int ans = 0;
        for (int i = 0; i < n; i ++) {
            if (dp[i] == mx) {
                ans += cnt[i];
            }
        }
        return ans;
    }
};
```
