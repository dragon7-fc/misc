155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

* `push(x)` -- Push element x onto stack.
* `pop()` -- Removes the element on top of the stack.
* `top()` -- Get the top element.
* `getMin()` -- Retrieve the minimum element in the stack.
 

**Example:**
```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
```

# Submissions
---
**Solution 1: (Stack)**
```
Runtime: 40 ms
Memory Usage: 15.7 MB
```
```python
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        else:
            if x < self.min_stack[-1]:
                self.min_stack.append(x)
            else:
                self.min_stack.append(self.min_stack[-1])

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```