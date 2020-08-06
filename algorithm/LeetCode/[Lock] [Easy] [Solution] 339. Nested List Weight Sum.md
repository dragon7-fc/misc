339. Nested List Weight Sum

Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

**Example 1:**
```
Input: [[1,1],2,[1,1]]
Output: 10 
Explanation: Four 1's at depth 2, one 2 at depth 1.
Example 2:

Input: [1,[4,[6]]]
Output: 27 
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.
```

# Summary
---
This is a very simple recursion problem and is a nice introduction to Depth-first Search (DFS).

# Solution
---
## Depth-first Traversal [Accepted]
**Algorithm**

Because the input is nested, it is natural to think about the problem in a recursive way. We go through the list of nested integers one by one, keeping track of the current depth dd. If a nested integer is an integer nn, we calculate its sum as n\times dn×d. If the nested integer is a list, we calculate the sum of this list recursively using the same process but with depth $d+1$.

**Java**
```java
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer,
 *     // rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds,
 *     // if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds,
 *     // if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
public int depthSum(List<NestedInteger> nestedList) {
    return depthSum(nestedList, 1);
}

public int depthSum(List<NestedInteger> list, int depth) {
    int sum = 0;
    for (NestedInteger n : list) {
        if (n.isInteger()) {
            sum += n.getInteger() * depth;
        } else {
            sum += depthSum(n.getList(), depth + 1);
        }
    }
    return sum;
}
```

**Complexity Analysis**

* The algorithm takes $O(N)$ time, where $N$ is the total number of nested elements in the input list. For example, the list [ [[[[1]]]], 2 ] contains $4$ nested lists and 22 nested integers ($1$ and $2$), so $N=6$.

In terms of space, at most $O(D)$ recursive calls are placed on the stack, where DD is the maximum level of nesting in the input. For example, $D=2$ for the input `[[1,1],2,[1,1]]`, and $D=3$ for the input `[1,[4,[6]]]`.

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 28 ms
Memory Usage: 13.9 MB
```
```python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        if not nestedList:
            return 0
        
        def dfs(el, depth):
            total = 0
            for nel in el:
                if nel.getInteger():
                    total += depth * nel.getInteger()
                else:
                    total += dfs(nel.getList(), depth+1)
            return total
        
        return dfs(nestedList, 1)
```