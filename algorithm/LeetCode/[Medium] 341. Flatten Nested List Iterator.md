341. Flatten Nested List Iterator

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

**Example 1:**
```
Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,1,2,1,1].
```

**Example 2:**
```
Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,4,6].
```

# Sobmissions
---
**Solution 1: (DFS, Backtracking)**
```
Runtime: 64 ms
Memory Usage: 17.7 MB
```
```python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.s = []
        
        def dfs(lst):
            for node in lst:
                if node.isInteger():
                    self.s += [node.getInteger()]
                else:
                    dfs(node.getList())
                
        dfs(nestedList)
    
    def next(self) -> int:
        return self.s.pop(0)
    
    def hasNext(self) -> bool:
         return self.s

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
```

**Solution 2: (DFS, Queue)**
```
Runtime: 11 ms
Memory Usage: 12.9 MB
```
```c++
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */

class NestedIterator {
    queue<int> Q;
    void solve(vector<NestedInteger> &nl){
        for(auto &v:nl){
            if(v.isInteger()) Q.push(v.getInteger());
            else solve(v.getList());
        }
        return;
    }
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        solve(nestedList);
    }
    
    int next() {
        int val=Q.front();
        Q.pop();
        return val;
    }
    
    bool hasNext() {
        return !Q.empty();
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */
```
