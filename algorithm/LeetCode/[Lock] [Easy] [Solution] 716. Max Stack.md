716. Max Stack

Design a max stack that supports push, pop, top, peekMax and popMax.

1. push(x) -- Push element x onto stack.
1. pop() -- Remove the element on top of the stack and return it.
1. top() -- Get the element on the top.
1. peekMax() -- Retrieve the maximum element in the stack.
1. popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.

**Example 1:**
```
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
```

**Note:**

* -1e7 <= x <= 1e7
* Number of operations won't exceed 10000.
* The last four operations won't be called when stack is empty.

# Solution
---
## Approach #1: Two Stacks [Accepted]

**Intuition and Algorithm**

A regular stack already supports the first 3 operations, so we focus on the last two.

For `peekMax`, we remember the largest value we've seen on the side. For example if we add `[2, 1, 5, 3, 9]`, we'll remember `[2, 2, 5, 5, 9]`. This works seamlessly with `pop` operations, and also it's easy to compute: it's just the maximum of the element we are adding and the previous maximum.

For `popMax`, we know what the current maximum (`peekMax`) is. We can pop until we find that maximum, then push the popped elements back on the stack.

Our implementation in Python will showcase extending the `list` class.

```python
class MaxStack(list):
    def push(self, x):
        m = max(x, self[-1][1] if self else None)
        self.append((x, m))

    def pop(self):
        return list.pop(self)[0]

    def top(self):
        return self[-1][0]

    def peekMax(self):
        return self[-1][1]

    def popMax(self):
        m = self[-1][1]
        b = []
        while self[-1][0] != m:
            b.append(self.pop())

        self.pop()
        map(self.push, reversed(b))
        return m
```

**Complexity Analysis**

* Time Complexity: $O(N)$ for the popMax operation, and $O(1)$ for the other operations, where $N$ is the number of operations performed.

* Space Complexity: $O(N)$, the maximum size of the stack.

# Submissions
---
**Solution 1: (Two Stacks)**
```
Runtime: 168 ms
Memory Usage: 15.8 MB
```
```python
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)
        
        if len(self.s2) == 0 or self.s2[-1] <= x:
            self.s2.append(x)
            
    def pop(self) -> int:
        if self.s2[-1] == self.s1[-1]:
            self.s2.pop()

        return self.s1.pop()

    def top(self) -> int:
        return self.s1[-1]

    def peekMax(self) -> int:
        return self.s2[-1]


    def popMax(self) -> int:
        temp = []

        while self.s1[-1] != self.s2[-1]:
            temp.append(self.s1[-1])
            self.s1.pop()

        self.s1.pop()
        res = self.s2.pop()

        while temp:
            self.push(temp[-1])
            temp.pop()

        return res


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
```

**Solution 2: (Two Stacks)**
```
Runtime: 156 ms
Memory Usage: 36.3 MB
```
```c++
class MaxStack {

private:
    vector<int> s1;
    vector<int> s2;

public:
    /** initialize your data structure here. */
    MaxStack() {
        
    }
    
    void push(int x) {
        s1.push_back(x);

        if (s2.empty() || s2.back() <= x)
            s2.push_back(x);
    }
    
    int pop() {
        if (s2.back() == s1.back())
            s2.pop_back();

        int temp_value = s1.back();
        s1.pop_back();

        return temp_value;
    }
    
    int top() {
        return s1.back();
    }
    
    int peekMax() {
        return s2.back();
    }
    
    int popMax() {
        vector<int> temp;

        while (s1.back() != s2.back()) {
            temp.push_back(s1.back());
            s1.pop_back();
        }

        int res = s2.back();
        s1.pop_back();
        s2.pop_back();

        while (!temp.empty()) {
            push(temp.back());
            temp.pop_back();
        }

        return res;
    }
};

/**
 * Your MaxStack object will be instantiated and called as such:
 * MaxStack* obj = new MaxStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->peekMax();
 * int param_5 = obj->popMax();
 */
```