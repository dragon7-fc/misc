1104. Path In Zigzag Labelled Binary Tree

In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.



Given the `label` of a node in this tree, return the labels in the path from the root of the tree to the node with that `label`.

 ![1104_tree.png](img/1104_tree.png)

**Example 1:**
```
Input: label = 14
Output: [1,3,4,14]
```

**Example 2:**
```
Input: label = 26
Output: [1,2,6,10,26]
``` 

**Constraints:**

* `1 <= label <= 10^6`

# Submissions
---
**Solution 1:**

for every node , try to restore the zigzag bin-tree to a normal bin-tree and find it's parent
let's start from a normal bin-tree, the parent node will be floor(label/2),
however, in zigzag tree .

1. if current layer is even it's parent will be the mirror pos of label so the mirror pos is `2^(k-1) + 2^k - 1 - label`, where `k` is layer num, can be calculated by `floor(log2(label))`, so it's parent node is `floor((2 ^ (k - 1) + 2 ^ k - 1 - label) / 2)`,which equals `floor((3 * 2 ^ (k - 1) - 1 - label) / 2)`
2. if current layer is odd, the order of this layer is right, but the order of it's parent layer is still reverse, so the formuler is the same as above

```
Runtime: 24 ms
Memory Usage: 12.6 MB
```
```python
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        p = label
        res = []
        while p >= 1:
            res.append(p)
            k = math.floor(math.log(p,2)) + 1
            p = int((3*math.pow(2,k-1) - 1 - p) / 2)
        res.reverse()
        return res
```