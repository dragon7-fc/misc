666. Path Sum IV

If the depth of a tree is smaller than `5`, then this tree can be represented by an array of three-digit integers. For each integer in this array:

* The hundreds digit represents the depth `d` of this node where `1 <= d <= 4`.
* The tens digit represents the position `p` of this node in the level it belongs to where `1 <= p <= 8`. The position is the same as that in a full binary tree.
* The units digit represents the value `v` of this node where `0 <= v <= 9`.

Given an array of **ascending** three-digit integers `nums` representing a binary tree with a depth smaller than `5`, return the sum of all paths from the root towards the leaves.

It is **guaranteed** that the given array represents a valid connected binary tree.

 

**Example 1:**

![666_pathsum4-1-tree.jpg](img/666_pathsum4-1-tree.jpg)
```
Input: nums = [113,215,221]
Output: 12
Explanation: The tree that the list represents is shown.
The path sum is (3 + 5) + (3 + 1) = 12.
```

**Example 2:**

![666_pathsum4-2-tree.jpg](img/666_pathsum4-2-tree.jpg)
```
Input: nums = [113,221]
Output: 4
Explanation: The tree that the list represents is shown. 
The path sum is (3 + 1) = 4.
```

**Constraints:**

* `1 <= nums.length <= 15`
* `110 <= nums[i] <= 489`
* `nums` represents a valid binary tree with depth less than `5`.

# Submissions
**Solution 1: (Convert to Tree)**
```
Runtime: 24 ms
Memory Usage: 14.3 MB
```
```python
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        self.ans = 0
        root = Node(nums[0] % 10)

        for x in nums[1:]:
            depth, pos, val = x//100, x//10 % 10, x % 10
            pos -= 1
            cur = root
            for d in range(depth - 2, -1, -1):
                if pos < 2**d:
                    cur.left = cur = cur.left or Node(val)
                else:
                    cur.right = cur = cur.right or Node(val)

                pos %= 2**d

        def dfs(node, running_sum = 0):
            if not node: return
            running_sum += node.val
            if not node.left and not node.right:
                self.ans += running_sum
            else:
                dfs(node.left, running_sum)
                dfs(node.right, running_sum)

        dfs(root)
        return self.ans
```

**Solution 2: (Direct Traversal)**
```
Runtime: 28 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        self.ans = 0
        values = {x // 10: x % 10 for x in nums}
        def dfs(node, running_sum = 0):
            if node not in values: return
            running_sum += values[node]
            depth, pos = divmod(node, 10)
            left = (depth + 1) * 10 + 2 * pos - 1
            right = left + 1

            if left not in values and right not in values:
                self.ans += running_sum
            else:
                dfs(left, running_sum)
                dfs(right, running_sum)

        dfs(nums[0] // 10)
        return self.ans
```
