437. Path Sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

**Example:**
```
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
```

**Solution 1:**

So the idea is similar as Two sum, using HashMap to store ( key : the prefix sum, value : how many ways get to this prefix sum) , and whenever reach a node, we check if prefix sum - target exists in hashmap or not, if it does, we added up the ways of prefix sum - target into res.

```
ex.
add 10:
  cnt = 0, prev_sum = {0: 1, 2: 0, 10: 1}
add 5:
  cnt = 0, prev_sum = {0: 1, 2: 0, 10: 1, 7: 0, 15: 1}
add 3:
  cnt = 1, prev_sum = {0: 1, 2: 0, 10: 1, 7: 0, 15: 1, 18: 1}
add 3:
  cnt = 1, prev_sum = {0: 1, 2: 0, 10: 1, 7: 0, 15: 1, 18: 1, 13: 0, 21: 1}
remove 3:
  cnt = 1, prev_sum = {0: 1, 2: 0, 10: 1, 7: 0, 15: 1, 18: 1, 13: 0, 21: 0}
add =2:
  cnt = 1 prev_sum = {0: 1, 2: 0, 10: 1, 7: 0, 15: 1, 18: 1, 13: 0, 21: 0, 8: 0, 16: 1}
remove -2:
  cnt = 1, prev_sum = {0: 1, 2: 0, 10: 1, 7: 0, 15: 1, 18: 1, 13: 0, 21: 0, 8: 0, 16: 0}
add 5:
  cnt = 1, prev_sum = {0: 1, 2: 0, 10: 1, 7: 0, 15: 1, 18: 0, 13: 0, 21: 0, 8: 0, 16: 0}
add 2:
  cnt = 1, prev_sum = {0: 1, 2: 0, 10: 1, 7: 0, 15: 1, 18: 0, 13: 0, 21: 0, 8: 0, 16: 0, 9: 0, 17: 1}
add 1:
  cnt = 2, rev_sum = {0: 1, 2: 0, 10: 1, 7: 0, 15: 1, 18: 1, 13: 0, 21: 0, 8: 0, 16: 0, 9: 0, 17: 1}
remove 1:
  cnt = 2, prev_sum = {0: 1, 2: 0, 10: 1, 7: 0, 15: 1, 18: 0, 13: 0, 21: 0, 8: 0, 16: 0, 9: 0, 17: 1}
remove 2:
  cnt = 2, prev_sum = {0: 1, 2: 0, 10: 1, 7: 0, 15: 1, 18: 0, 13: 0, 21: 0, 8: 0, 16: 0, 9: 0, 17: 0}
remove 5:
  cnt = 2, prev_sum = {0: 1, 2: 0, 10: 1, 7: 0, 15: 0, 18: 0, 13: 0, 21: 0, 8: 0, 16: 0, 9: 0, 17: 0}
add -3:
  cnt = 2, prev_sum = {0: 1, 2: 0, 10: 1, 7: 1, 15: 0, 18: 0, 13: 0, 21: 0, 8: 0, 16: 0, 9: 0, 17: 0, -1: 0}
add 11:
  cnt = 3, prev_sum = {0: 1, 2: 0, 10: 1, 7: 1, 15: 0, 18: 1, 13: 0, 21: 0, 8: 0, 16: 0, 9: 0, 17: 0, -1: 0}
remove 11:
  cnt = 3, prev_sum = {0: 1, 2: 0, 10: 1, 7: 1, 15: 0, 18: 0, 13: 0, 21: 0, 8: 0, 16: 0, 9: 0, 17: 0, -1: 0}
remove -3:
  cnt = 3, prev_sum = {0: 1, 2: 0, 10: 1, 7: 0, 15: 0, 18: 0, 13: 0, 21: 0, 8: 0, 16: 0, 9: 0, 17: 0, -1: 0}
remove 10:
  cnt = 3, prev_sum = {0: 1, 2: 0, 10: 0, 7: 0, 15: 0, 18: 0, 13: 0, 21: 0, 8: 0, 16: 0, 9: 0, 17: 0, -1: 0}
```

```
Runtime: 48 ms
Memory Usage: 13.8 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def pathSum(self, root: TreeNode, sum: int) -> int:
        target = sum
        prev_sum = collections.defaultdict(int)
        prev_sum[0] = 1
        cnt = 0
        
        def dfs(node, curr_sum):
            nonlocal cnt, prev_sum
            if node is not None:
                curr_sum += node.val
                cnt += prev_sum[curr_sum - target]
                prev_sum[curr_sum] += 1

                dfs(node.left, curr_sum)
                dfs(node.right, curr_sum)
                prev_sum[curr_sum] -= 1

        dfs(root, 0)
        return cnt

    
```