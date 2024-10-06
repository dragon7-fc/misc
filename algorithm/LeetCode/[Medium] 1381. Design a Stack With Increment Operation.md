1381. Design a Stack With Increment Operation

Design a stack which supports the following operations.

Implement the `CustomStack` class:

* `CustomStack(int maxSize)` Initializes the object with `maxSize` which is the maximum number of elements in the stack or do nothing if the stack reached the `maxSize`.
* `void push(int x)` Adds `x` to the top of the stack if the stack hasn't reached the maxSize.
* `int pop()` Pops and returns the top of stack or `-1` if the stack is empty.
* void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, just increment all the elements in the stack.
 

**Example 1:**
```
Input
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
Output
[null,null,null,2,null,null,null,null,null,103,202,201,-1]
Explanation
CustomStack customStack = new CustomStack(3); // Stack is Empty []
customStack.push(1);                          // stack becomes [1]
customStack.push(2);                          // stack becomes [1, 2]
customStack.pop();                            // return 2 --> Return top of the stack 2, stack becomes [1]
customStack.push(2);                          // stack becomes [1, 2]
customStack.push(3);                          // stack becomes [1, 2, 3]
customStack.push(4);                          // stack still [1, 2, 3], Don't add another elements as size is 4
customStack.increment(5, 100);                // stack becomes [101, 102, 103]
customStack.increment(2, 100);                // stack becomes [201, 202, 103]
customStack.pop();                            // return 103 --> Return top of the stack 103, stack becomes [201, 202]
customStack.pop();                            // return 202 --> Return top of the stack 102, stack becomes [201]
customStack.pop();                            // return 201 --> Return top of the stack 101, stack becomes []
customStack.pop();                            // return -1 --> Stack is empty return -1.
``` 

**Constraints:**

* `1 <= maxSize <= 1000`
* `1 <= x <= 1000`
* `1 <= k <= 1000`
* `0 <= val <= 100`
* At most `1000` calls will be made to each method of increment, push and pop each separately.

# Submissions
---
**Solution 1: (Stack)**

**Explanation**

Use an additional array to record the increment value.  
`inc[i]` means for all elements `stack[0] ~ stack[i]`,  
we should plus `inc[i]` when popped from the stack.  
Then `inc[i-1]+=inc[i]`, so that we will keep it from next pop.


**Complexity**

Initailze, `O(N)` time & space.
It can be strick `O(1)` here, like we use stack for inc too.
But shrug, I just keep it simple here.

push, pop, increment, all `O(1)` time and space.


```
Runtime: 88 ms
Memory Usage: 13.4 MB
```
```python
class CustomStack:

    def __init__(self, maxSize: int):
        self.n = maxSize
        self.stack = []
        self.inc = [0] * maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.n:
            self.stack.append(x)

    def pop(self) -> int:
        i = len(self.stack) - 1
        if i < 0:
            return -1
        inc = self.inc[i]
        self.inc[i] = 0
        if i: self.inc[i - 1] += inc
        return self.stack.pop() + inc
        

    def increment(self, k: int, val: int) -> None:
        i = min(k, len(self.stack)) - 1
        if i >= 0:
            self.inc[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
```

**Solution 2: (Array, aux array)**
```
Runtime: 30 ms
Memory: 25.86 MB
```
```c++
class CustomStack {
    vector<int> stk, dp;
    int i = -1;
public:
    CustomStack(int maxSize) {
        stk.resize(maxSize);
        dp.resize(maxSize);
    }
    
    void push(int x) {
        if (i+1 < stk.size()) {
            i += 1;
            stk[i] = x;
            dp[i] = 0;
        }
    }
    
    int pop() {
        if (i >= 0) {
            int rst = stk[i] + dp[i];
            stk[i] = 0;
            if (i) {
                dp[i-1] += dp[i];
            }
            dp[i] = 0;
            i -= 1;
            return rst;
        }
        return -1;
    }
    
    void increment(int k, int val) {
        int ck = min(k, i+1);
        if (ck) {
            dp[ck-1] += val;
        }
    }
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */
```
