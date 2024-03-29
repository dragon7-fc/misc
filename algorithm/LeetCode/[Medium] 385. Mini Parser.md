385. Mini Parser

Given a nested list of integers represented as a string, implement a parser to deserialize it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Note: You may assume that the string is well-formed:

* String is non-empty.
* String does not contain white spaces.
* String contains only digits `0-9`, `[`, `-`, `,`, `]`.

**Example 1:**
```
Given s = "324",

You should return a NestedInteger object which contains a single integer 324.
```

**Example 2:**
```
Given s = "[123,[456,[789]]]",

Return a NestedInteger object containing a nested list with 2 elements:

1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789.
```

# Submissions
---
**Solution 1: (Stack)**
```
Runtime: 68 ms
Memory Usage: 16 MB
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
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))
        stack = []
        num = None
        sign = 1
        res = None
        for c in s:
            if c == '[':
                curr = NestedInteger()
                if stack:
                    stack[-1].add(curr)
                else:
                    res = curr
                stack.append(curr)
            elif c == ']':
                if num is not None:
                    stack[-1].add(NestedInteger(num * sign))
                    num = None
                    sign = 1
                stack.pop()
            elif c == ',':
                if num is not None:
                    stack[-1].add(NestedInteger(num * sign))
                    num = None
                    sign = 1
            elif c == '-':
                sign = -1
            else:
                if num is not None:
                    num = num * 10 + ord(c) - ord('0')
                else:
                    num = ord(c) - ord('0')  
        return res
```

**Solution 2: (Stack)**
```
Runtime: 10 ms
Memory Usage: 8.9 MB
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
    NestedInteger deserialize(string s) {
        if(s[0]!='[') return stoi(s);

        NestedInteger out;
        stack<NestedInteger*> st({&out});
        for(auto i{1}, x{0}, sign{1}; i+1<size(s); ++i)
            switch(s[i])
            {
                case ',' : break; 
                case '-' : sign=-1;
                           break;                   
                case '[' : st.top()->add({});
                           st.push(&st.top()->getList().back());
                           break;
                case ']' : st.pop();
                           break;  
                default  : x = 10*x+s[i]-'0';  
                           if(!isdigit(s[i+1]))
                           {
                               st.top()->add(sign*x);
                               sign=1, x=0;
                           }
                           break;
            }
        return out;
    }
};
```
