364. Nested List Weight Sum II

Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

**Example 1:**
```
Input: [[1,1],2,[1,1]]
Output: 8 
Explanation: Four 1's at depth 1, one 2 at depth 2.
```

**Example 2:**
```
Input: [1,[4,[6]]]
Output: 17 
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17.
```

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 20 ms
Memory Usage: 14 MB
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
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        max_depth = 0
        def dfs(nestedList, cur_depth):
            nonlocal max_depth
            for ni in nestedList:
                if ni.isInteger(): 
                    max_depth = max(max_depth, cur_depth)
                else:
                    dfs(ni.getList(), cur_depth+1)
        dfs(nestedList, 1)            
        
        ans = 0
        def dfs_calc(nestedList, cur_depth):
            nonlocal max_depth, ans
            for ni in nestedList:
                if ni.isInteger(): 
                    ans += (max_depth-cur_depth) * ni.getInteger()
                else:
                    dfs_calc(ni.getList(), cur_depth+1)
        dfs_calc(nestedList, 0)
        return ans
```

**Solution 2: (BFS)**
```
Runtime: 4 ms
Memory Usage: 9.3 MB
```
```c++
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Constructor initializes an empty nested list.
 *     NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     NestedInteger(int value);
 *
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Set this NestedInteger to hold a single integer.
 *     void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     void add(const NestedInteger &ni);
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class Solution {
public:
    int depthSumInverse(vector<NestedInteger>& nestedList) {
        queue<NestedInteger> q;
        int res = 0;
        int update = 0;
        for(auto& n : nestedList){
            if(n.isInteger()) {
                res += n.getInteger();
                update += n.getInteger();
            }
            else q.push(n);
        }
        while(!q.empty()){
            res += update;
            int l = q.size();
            for(int k = 0; k < l; k++){
                NestedInteger cur = q.front();
                q.pop();
                vector<NestedInteger> nlist = cur.getList();
                for(auto n: nlist){
                    if(n.isInteger()) {
                        res += n.getInteger();
                        update += n.getInteger();
                    }
                    else q.push(n);
                }
            }
        }
        return res;
    }
};
```