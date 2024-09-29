641. Design Circular Deque

Design your implementation of the circular double-ended queue (deque).

Your implementation should support following operations:

* `MyCircularDeque(k):` Constructor, set the size of the deque to be k.
* `insertFront():` Adds an item at the front of Deque. Return true if the operation is successful.
* `insertLast():` Adds an item at the rear of Deque. Return true if the operation is successful.
* `deleteFront():` Deletes an item from the front of Deque. Return true if the operation is successful.
* `deleteLast():` Deletes an item from the rear of Deque. Return true if the operation is successful.
* `getFront():` Gets the front item from the Deque. If the deque is empty, return -1.
* `getRear():` Gets the last item from Deque. If the deque is empty, return -1.
* `isEmpty():` Checks whether Deque is empty or not. 
* `isFull():` Checks whether Deque is full or not.
 

**Example:**
```
MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be 3
circularDeque.insertLast(1);			// return true
circularDeque.insertLast(2);			// return true
circularDeque.insertFront(3);			// return true
circularDeque.insertFront(4);			// return false, the queue is full
circularDeque.getRear();  			// return 2
circularDeque.isFull();				// return true
circularDeque.deleteLast();			// return true
circularDeque.insertFront(4);			// return true
circularDeque.getFront();			// return 4
``` 

**Note:**

* All values will be in the range of `[0, 1000]`.
* The number of operations will be in the range of `[1, 1000]`.
* Please do not use the built-in Deque library.

# Submissions
---
**Solution 1: (Arrary)**
```
Runtime: 76 ms
Memory Usage: 13 MB
```
```python
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.capacity = k
        self.size = 0
        self.circular_deque = [0] * k
        self.rear = 0
        self.front = k-1

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.size+1 <= self.capacity:
            self.circular_deque[ self.front ] = value
            self.front = (self.front-1) % self.capacity
            self.size += 1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.size+1 <= self.capacity:
            self.circular_deque[self.rear] = value
            self.rear = (self.rear+1) % self.capacity
            self.size += 1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.size != 0:    
            self.front = (self.front+1) % self.capacity
            self.size -= 1
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.size != 0:
            self.rear = (self.rear-1) % self.capacity
            self.size -= 1
            return True
        else:
            return False    

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.size != 0:
            return self.circular_deque[(self.front+1) % self.capacity]
        else:
            return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.size != 0:
            return self.circular_deque[(self.rear-1) % self.capacity]
        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
```

**Solution 2: (Linked list, pre build dummy circular list)**
```
Runtime: 84 ms
Memory Usage: 14 MB
```
```python
class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None

class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.capacity = k
        self.size = 0
        head_node = Node(0)
        
        cur = head_node
        for i in range(1,k):
            # build double linkage
            cur.next = Node(i)
            cur.next.prev = cur
            cur = cur.next
            
        # build double linkage
        cur.next = head_node
        head_node.prev = cur
        
        # initialization for front and rear
        self.front = head_node.prev
        self.rear = head_node

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.size+1 <= self.capacity:
            self.front.value = value
            self.front = self.front.prev
            self.size += 1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.size+1 <= self.capacity:
            self.rear.value = value
            self.rear = self.rear.next
            self.size += 1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.size != 0:
            self.front = self.front.next
            self.size -= 1
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.size != 0:
            self.rear = self.rear.prev
            self.size -= 1
            return True
        else:
            return False        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.size != 0:
            return self.front.next.value
        else:
            return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.size != 0:
            return self.rear.prev.value
        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
```

**Solution 3: (Linked List)**
```
Runtime: 50 ms
Memory Usage: 12.6 MB
```
```c

struct CircularListNode {
    int val;
    struct CircularListNode *next;
    struct CircularListNode *prev;
};

typedef struct {
    int cap;
    int n;
    struct CircularListNode *front;
    struct CircularListNode *last;
} MyCircularDeque;

MyCircularDeque* myCircularDequeCreate(int k) {
    MyCircularDeque *rst = calloc(1, sizeof(MyCircularDeque));
    rst->cap = k;
    return rst;
}

bool myCircularDequeInsertFront(MyCircularDeque* obj, int value) {
    if (obj->n == obj->cap)
        return false;
    struct CircularListNode *node;
    node = malloc(sizeof(struct CircularListNode));
    node->val = value;
    if (obj->n == 0) {
        node->next = node;
        node->prev = node;
        obj->front = node;
        obj->last = node;
        obj->n = 1;
        return true;
    }
    obj->front->next->prev = node;
    node->next = obj->front->next;
    node->prev = obj->front;
    obj->front->next = node;
    obj->front = node;
    obj->n += 1;
    return true;
}

bool myCircularDequeInsertLast(MyCircularDeque* obj, int value) {
    if (obj->n == obj->cap)
        return false;
    struct CircularListNode *node;
    node = malloc(sizeof(struct CircularListNode));
    node->val = value;
    if (obj->n == 0) {
        node->next = node;
        node->prev = node;
        obj->front = node;
        obj->last = node;
        obj->n = 1;
        return true;
    }
    obj->last->prev->next = node;
    node->prev = obj->last->prev;
    node->next = obj->last;
    obj->last->prev = node;
    obj->last = node;
    obj->n += 1;
    return true;
}

bool myCircularDequeDeleteFront(MyCircularDeque* obj) {
    if (obj->n == 0)
        return false;
    obj->front->prev->next = obj->front->next;
    obj->front->next->prev = obj->front->prev;
    struct CircularListNode *tmp = obj->front;
    obj->front = obj->front->prev;
    free(tmp);
    obj->n -= 1;
    return true;
}

bool myCircularDequeDeleteLast(MyCircularDeque* obj) {
    if (obj->n == 0)
        return false;
    if (obj->n == 1) {
        free(obj->front);
        obj->front = NULL;
        obj->last = NULL;
        obj->n = 0;
        return true;
    }
    obj->last->prev->next = obj->last->next;
    obj->last->next->prev = obj->last->prev;
    struct CircularListNode *tmp = obj->last;
    obj->last = obj->last->next;
    free(tmp);
    obj->n -= 1;
    return true;
}

int myCircularDequeGetFront(MyCircularDeque* obj) {
    if (obj->n == 0)
        return -1;
    return obj->front->val;
}

int myCircularDequeGetRear(MyCircularDeque* obj) {
    if (obj->n == 0)
        return -1;
    return obj->last->val;
}

bool myCircularDequeIsEmpty(MyCircularDeque* obj) {
    return obj->n == 0;
}

bool myCircularDequeIsFull(MyCircularDeque* obj) {
    return obj->n == obj->cap;
}

void myCircularDequeFree(MyCircularDeque* obj) {
    while (obj->front != obj->last) {
        struct ListNode *tmp = obj->front;
        obj->front = obj->front->prev;
        free(tmp);
    }
    free(obj->front);
    free(obj);
}

/**
 * Your MyCircularDeque struct will be instantiated and called as such:
 * MyCircularDeque* obj = myCircularDequeCreate(k);
 * bool param_1 = myCircularDequeInsertFront(obj, value);
 
 * bool param_2 = myCircularDequeInsertLast(obj, value);
 
 * bool param_3 = myCircularDequeDeleteFront(obj);
 
 * bool param_4 = myCircularDequeDeleteLast(obj);
 
 * int param_5 = myCircularDequeGetFront(obj);
 
 * int param_6 = myCircularDequeGetRear(obj);
 
 * bool param_7 = myCircularDequeIsEmpty(obj);
 
 * bool param_8 = myCircularDequeIsFull(obj);
 
 * myCircularDequeFree(obj);
*/
```

**Solution 4: (Vector)**
```
Runtime: 24 ms
Memory: 22.50 MB
```
```c++
class MyCircularDeque {
    vector<int> dp;
    int sz;
public:
    MyCircularDeque(int k) {
        sz = k;
    }
    
    bool insertFront(int value) {
        if (dp.size() < sz) {
            dp.insert(dp.begin(), value);
            return true;
        }
        return false;
    }
    
    bool insertLast(int value) {
        if (dp.size() < sz) {
            dp.push_back(value);
            return true;
        }
        return false;
    }
    
    bool deleteFront() {
        if (dp.size()) {
            dp.erase(dp.begin());
            return true;
        }
        return false;
    }
    
    bool deleteLast() {
        if (dp.size()) {
            dp.pop_back();
            return true;
        }
        return false;
    }
    
    int getFront() {
        if (dp.size()) {
            return dp[0];
        }
        return -1;
    }
    
    int getRear() {
        if (dp.size()) {
            return dp.back();
        }
        return -1;
    }
    
    bool isEmpty() {
        return dp.empty();
    }
    
    bool isFull() {
        return dp.size() == sz;
    }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */
```

**Solution 5: (Array)**
```
Runtime: 20 ms
Memory: 23.02 MB
```
```c++
class MyCircularDeque {
    int dp[2001];
    int sz, left = 1000, right = left + 1;
public:
    MyCircularDeque(int k) {
        sz = k;
    }
    
    bool insertFront(int value) {
        if (!isFull()) {
            dp[left] = value;
            left -= 1;
            return true;
        }
        return false;
    }
    
    bool insertLast(int value) {
        if (!isFull()) {
            dp[right] = value;
            right += 1;
            return true;
        }
        return false;
    }
    
    bool deleteFront() {
        if (!isEmpty()) {
            left += 1;
            return true;
        }
        return false;
    }
    
    bool deleteLast() {
        if (!isEmpty()) {
            right -= 1;
            return true;
        }
        return false;
    }
    
    int getFront() {
        if (!isEmpty()) {
            return dp[left+1];
        }
        return -1;
    }
    
    int getRear() {
        if (!isEmpty()) {
            return dp[right-1];
        }
        return -1;
    }
    
    bool isEmpty() {
        return right == left + 1;
    }
    
    bool isFull() {
        return (right - left) == sz + 1;
    }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */
```
