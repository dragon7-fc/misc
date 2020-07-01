108. Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

**Example:**
```
Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
```

# Submissions
---
**Solution 1:**
```
Runtime: 64 ms
Memory Usage: 14.9 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        node = TreeNode(nums[len(nums)//2])
        node.left = self.sortedArrayToBST(nums[:len(nums)//2])
        node.right = self.sortedArrayToBST(nums[len(nums)//2 + 1:])
        return node
```

**Solution 2: (DFS)**
```
Runtime: 84 ms
Memory Usage: 360.1 MB
```
```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode *construct(vector<int> nums,int start,int stop)
    {
        if(start > stop)
        {
            return NULL;
        }
        if(start == stop)
        {
            return new TreeNode(nums[start]);
        }
        int mid = start+(stop-start)/2;
        TreeNode *root = new TreeNode(nums[mid], construct(nums, start, mid-1), construct(nums, mid+1, stop));
        return root;
        
    }
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return construct(nums, 0, nums.size()-1);
    }
};
```