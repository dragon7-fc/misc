654. Maximum Binary Tree

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

* The root is the maximum number in the array.
* The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
* The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.

Construct the maximum tree by the given array and output the root node of this tree.

**Example 1:**
```
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
```

**Note:**

* The size of the given array will be in the range `[1,1000]`.

# Solution
---
## Approach 1: Recursive Solution
The current solution is very simple. We make use of a function `construct(nums, l, r)`, which returns the maximum binary tree consisting of numbers within the indices $l$ and $r$ in the given $nums$ array(excluding the $r^{th}$ element).

The algorithm consists of the following steps:

1. Start with the function call `construct(nums, 0, n)`. Here, $n$ refers to the number of elements in the given $nums$ array.

1. Find the index, $max_i$, of the largest element in the current range of indices $(l:r-1)$. Make this largest element, $nums[max\_i]$ as the local root node.

1. Determine the left child using `construct(nums, l, max_i)`. Doing this recursively finds the largest element in the subarray left to the current largest element.

1. Similarly, determine the right child using `construct(nums, max_i + 1, r)`.

1. Return the root node to the calling function.

```java
public class Solution {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        return construct(nums, 0, nums.length);
    }
    public TreeNode construct(int[] nums, int l, int r) {
        if (l == r)
            return null;
        int max_i = max(nums, l, r);
        TreeNode root = new TreeNode(nums[max_i]);
        root.left = construct(nums, l, max_i);
        root.right = construct(nums, max_i + 1, r);
        return root;
    }
    public int max(int[] nums, int l, int r) {
        int max_i = l;
        for (int i = l; i < r; i++) {
            if (nums[max_i] < nums[i])
                max_i = i;
        }
        return max_i;
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n^2)$. The function construct is called $n$ times. At each level of the recursive tree, we traverse over all the $n$ elements to find the maximum element. In the average case, there will be a $\log n$ levels leading to a complexity of $O\big(n\log n\big)$. In the worst case, the depth of the recursive tree can grow upto $n$, which happens in the case of a sorted $nums$ array, giving a complexity of $O(n^2)$.

* Space complexity : $O(n)$. The size of the $set$ can grow upto $n$ in the worst case. In the average case, the size will be $\log n$ for $n$ elements in $nums$, giving an average case complexity of $O(\log n)$

# Submissions
---
**Solution 1:**
```
Runtime: 188 ms
Memory Usage: 13.1 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def dfs(arr):
            if not arr:
                return None
            v = max(arr)
            node = TreeNode(v)
            index = arr.index(v)
            node.left = dfs(arr[:index])
            node.right = dfs(arr[index+1:])
            return node
        
        return dfs(nums) 
```