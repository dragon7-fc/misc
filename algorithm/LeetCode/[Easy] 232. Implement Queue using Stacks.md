232. Implement Queue using Stacks

Implement the following operations of a queue using stacks.

* push(x) -- Push element x to the back of queue.
* pop() -- Removes the element from in front of queue.
* peek() -- Get the front element.
* empty() -- Return whether the queue is empty.

**Example:**
```
MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
```

**Notes:**

* You must use only standard operations of a stack -- which means only `push to top`, `peek/pop from top`, `size`, and `is empty` operations are valid.
* Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
* You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

# Submissions
---
**Solution 1: (Stack)**
```
Runtime: 24 ms
Memory Usage: 12.7 MB
```
```python
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.q.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        val = self.q[0]
        del self.q[0]
        return val

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.q) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```

**Solution 2: (Stack, Queue)**
```
Runtime: 0 ms
Memory Usage: 6.1 MB
```
```c



typedef struct {
    int stk1[100];
    int top1;
    int stk2[100];
    int top2;
} MyQueue;


MyQueue* myQueueCreate() {
    MyQueue *obj = malloc(sizeof(MyQueue));
    obj->top1 = -1;
    obj->top2 = -1;
    return obj;
}

void myQueuePush(MyQueue* obj, int x) {
    obj->stk1[++obj->top1] = x;
}

int myQueuePop(MyQueue* obj) {
    if (obj->top2 == -1)
        while (obj->top1 >= 0)
            obj->stk2[++obj->top2] = obj->stk1[obj->top1--];
    return obj->stk2[obj->top2--];
}

int myQueuePeek(MyQueue* obj) {
    if (obj->top2 == -1)
        while (obj->top1 >= 0)
            obj->stk2[++obj->top2] = obj->stk1[obj->top1--];
    return obj->stk2[obj->top2];
}

bool myQueueEmpty(MyQueue* obj) {
    return obj->top1 == -1 && obj->top2 == -1;
}

void myQueueFree(MyQueue* obj) {
    free(obj);
}

/**
 * Your MyQueue struct will be instantiated and called as such:
 * MyQueue* obj = myQueueCreate();
 * myQueuePush(obj, x);
 
 * int param_2 = myQueuePop(obj);
 
 * int param_3 = myQueuePeek(obj);
 
 * bool param_4 = myQueueEmpty(obj);
 
 * myQueueFree(obj);
*/
```

**Solution 3: (Two Stacks) Push - O(1) per operation, Pop - Amortized O(1) per operation)**
```
Runtime: 33 ms
Memory: 13.9 MB
```
```python
class MyQueue:

    def __init__(self):
        self.stk = []
        self.tmp = []
        

    def push(self, x: int) -> None:
        self.tmp += [x]

    def pop(self) -> int:
        if self.stk:
            return self.stk.pop()
        else:
            while self.tmp:
                self.stk += [self.tmp.pop()]
            return self.stk.pop()

    def peek(self) -> int:
        if self.stk:
            return self.stk[-1]
        else:
            return self.tmp[0]

    def empty(self) -> bool:
        return not self.stk and not self.tmp


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```

**Solution 4: (Two Stacks)**

           vpush
stk    1 2 3
stk2   3 2 1
           ^pop
```
Runtime: 0 ms, Beats 100.00%
Memory: 9.78 MB, Beats 26.42%
```
```c++
class MyQueue {
    stack<int> stk, stk2;
public:
    MyQueue() {
        
    }
    
    void push(int x) {
        stk.push(x);
    }
    
    int pop() {
        int rst = peek();
        stk2.pop();
        return rst;
    }
    
    int peek() {
        if (stk2.empty()) {
            while (stk.size()) {
                stk2.push(stk.top());
                stk.pop();
            }
        }
        return stk2.top();
    }
    
    bool empty() {
        return stk.size() == 0 && stk2.size() == 0;
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
```
