622. Design Circular Queue

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Your implementation should support following operations:

* `MyCircularQueue(k):` Constructor, set the size of the queue to be k.
* `Front:` Get the front item from the queue. If the queue is empty, return -1.
* `Rear:` Get the last item from the queue. If the queue is empty, return -1.
* `enQueue(value):` Insert an element into the circular queue. Return true if the operation is successful.
* `deQueue():` Delete an element from the circular queue. Return true if the operation is successful.
* `isEmpty():` Checks whether the circular queue is empty or not.
* `isFull():` Checks whether the circular queue is full or not.
 

**Example:**
```
MyCircularQueue circularQueue = new MyCircularQueue(3); // set the size to be 3
circularQueue.enQueue(1);  // return true
circularQueue.enQueue(2);  // return true
circularQueue.enQueue(3);  // return true
circularQueue.enQueue(4);  // return false, the queue is full
circularQueue.Rear();  // return 3
circularQueue.isFull();  // return true
circularQueue.deQueue();  // return true
circularQueue.enQueue(4);  // return true
circularQueue.Rear();  // return 4
```

**Note:**

* All values will be in the range of `[0, 1000]`.
* The number of operations will be in the range of `[1, 1000]`.
* Please do not use the built-in Queue library.

# Submissions
---
**Solution 1: (Array)**
```
Runtime: 72 ms
Memory Usage: 13.1 MB
```
```python
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.size = k
        self.filled = 0
        self.q = [0]*self.size
        self.head = self.tail = None

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            # no elements yet
            if self.head is None and self.tail is None:
                self.head = self.tail = 0
                
            else: # some elements
                self.tail = (self.tail+1) % self.size
            self.q[self.tail] = value    
            self.filled += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = (self.head+1)% self.size
        self.filled -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.q[self.head] if not self.isEmpty() else -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.q[self.tail] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.filled == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.filled == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
```

**Solution 2: (Queue)**
```
Runtime: 24 ms
Memory Usage: 12.5 MB
```
```c
typedef struct {
    int f, b, r, n, sz, *q;
} MyCircularQueue;

MyCircularQueue* myCircularQueueCreate(int k) {
    MyCircularQueue *q = calloc(1, sizeof *q);
    q->q = calloc(1, sizeof(int [k]));
    q->sz = k;
    return q;
}

bool myCircularQueueEnQueue(MyCircularQueue* obj, int value) {
    if (obj->n == obj->sz)
        return false;
    obj->n++;
    obj->q[obj->r = obj->b] = value;
    obj->b = (obj->b + 1) % obj->sz;
    return true;
}

bool myCircularQueueDeQueue(MyCircularQueue* obj) {
    if (!obj->n)
        return false;
    obj->n--;
    obj->f = (obj->f + 1) % obj->sz;
    return true;
}

int myCircularQueueFront(MyCircularQueue* obj) {
    return obj->n ? obj->q[obj->f] : -1;
}

int myCircularQueueRear(MyCircularQueue* obj) {
    return obj->n ? obj->q[obj->r] : -1;
}

bool myCircularQueueIsEmpty(MyCircularQueue* obj) {
    return !obj->n;
}

bool myCircularQueueIsFull(MyCircularQueue* obj) {
    return obj->n == obj->sz;
}

void myCircularQueueFree(MyCircularQueue* obj) {
    free(obj->q);
    free(obj);
}

/**
 * Your MyCircularQueue struct will be instantiated and called as such:
 * MyCircularQueue* obj = myCircularQueueCreate(k);
 * bool param_1 = myCircularQueueEnQueue(obj, value);
 
 * bool param_2 = myCircularQueueDeQueue(obj);
 
 * int param_3 = myCircularQueueFront(obj);
 
 * int param_4 = myCircularQueueRear(obj);
 
 * bool param_5 = myCircularQueueIsEmpty(obj);
 
 * bool param_6 = myCircularQueueIsFull(obj);
 
 * myCircularQueueFree(obj);
*/
```

