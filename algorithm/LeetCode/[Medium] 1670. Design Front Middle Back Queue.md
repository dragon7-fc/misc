1670. Design Front Middle Back Queue

Design a queue that supports `push` and `pop` operations in the front, middle, and back.

Implement the `FrontMiddleBack` class:

* FrontMiddleBack() Initializes the queue.
* `void pushFront(int val)` Adds val to the front of the queue.
* `void pushMiddle(int val)` Adds val to the middle of the queue.
* `void pushBack(int val)` Adds val to the back of the queue.
* `int popFront()` Removes the front element of the queue and returns it. If the queue is empty, return -1.
* `int popMiddle()` Removes the middle element of the queue and returns it. If the queue is empty, return -1.
* `int popBack()` Removes the back element of the queue and returns it. If the queue is empty, return -1.

Notice that when there are two middle position choices, the operation is performed on the frontmost middle position choice. For example:

Pushing `6` into the middle of `[1, 2, 3, 4, 5]` results in `[1, 2, 6, 3, 4, 5]`.
Popping the middle from `[1, 2, 3, 4, 5, 6]` returns `3` and results in `[1, 2, 4, 5, 6]`.
 

**Example 1:**
```
Input:
["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
[[], [1], [2], [3], [4], [], [], [], [], []]
Output:
[null, null, null, null, null, 1, 3, 4, 2, -1]

Explanation:
FrontMiddleBackQueue q = new FrontMiddleBackQueue();
q.pushFront(1);   // [1]
q.pushBack(2);    // [1, 2]
q.pushMiddle(3);  // [1, 3, 2]
q.pushMiddle(4);  // [1, 4, 3, 2]
q.popFront();     // return 1 -> [4, 3, 2]
q.popMiddle();    // return 3 -> [4, 2]
q.popMiddle();    // return 4 -> [2]
q.popBack();      // return 2 -> []
q.popFront();     // return -1 -> [] (The queue is empty)
```

**Constraints:**

* `1 <= val <= 109`
* At most `1000` calls will be made to `pushFront`, `pushMiddle`, `pushBack`, `popFront`, `popMiddle`, and `popBack`.

# Submissions
---
**Solution 1: (Queue)**
```
Runtime: 64 ms
Memory Usage: 15.1 MB
```
```python
class FrontMiddleBackQueue:

    def __init__(self):
        self.A = []

    def pushFront(self, val: int) -> None:
        self.A.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        self.A.insert(len(self.A) // 2, val)

    def pushBack(self, val: int) -> None:
        self.A.append(val)

    def popFront(self) -> int:
        return (self.A or [-1]).pop(0)

    def popMiddle(self) -> int:
        return (self.A or [-1]).pop((len(self.A) - 1) // 2)

    def popBack(self) -> int:
        return (self.A or [-1]).pop()

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
```

**Solution 2: (Linked List)**
```
Runtime: 48 ms
Memory Usage: 14.3 MB
```
```c
typedef struct node
{
    int val;
    struct node * next;
}Node;

typedef struct {
    Node * front;
    Node * rear;
    int count;
} FrontMiddleBackQueue;


FrontMiddleBackQueue* frontMiddleBackQueueCreate() {
    FrontMiddleBackQueue * queue = (FrontMiddleBackQueue *)malloc(sizeof(FrontMiddleBackQueue));
    queue->front = NULL;
    queue->rear = NULL;
    queue->count = 0;
    return queue;
}

void frontMiddleBackQueuePushFront(FrontMiddleBackQueue* obj, int val) {
    Node * new_node = (Node *)malloc(sizeof(Node));
    new_node->val = val;
    
    new_node->next = obj->front;
    obj->front = new_node;
    
    //Only if the insertion at front is first insertion
    if(obj->rear == NULL)
    {
        obj->rear = obj->front;
    }
    
    obj->count++;
}

void frontMiddleBackQueuePushMiddle(FrontMiddleBackQueue* obj, int val) {
    Node * slow_ptr = obj->front;
    
    if(slow_ptr == NULL)    //First element
    {
       Node * new_node = (Node *)malloc(sizeof(Node));
       new_node->val = val; 
       new_node->next = NULL;
        
       obj->front = new_node;
       obj->rear = new_node;
       obj->count++;
       return;
    }
    
    else if(slow_ptr->next == NULL) //Only one element in queue
    {
        Node * new_node = (Node *)malloc(sizeof(Node));
        new_node->val = val;
        
        obj->front = new_node;
        new_node->next = slow_ptr;
        obj->count++;
        return;
    }
    
    Node * prev_slow_ptr = NULL;
    Node * fast_ptr = obj->front->next;
    
    while(fast_ptr != NULL)
    {
        prev_slow_ptr = slow_ptr;
        slow_ptr = slow_ptr->next;
        fast_ptr = fast_ptr->next;
        
        if(fast_ptr != NULL)
            fast_ptr = fast_ptr->next;
    }
    
    Node * new_node = (Node *)malloc(sizeof(Node));
    new_node->val = val;
    
    prev_slow_ptr->next = new_node;
    new_node->next = slow_ptr;   
    
    obj->count++;
}

void frontMiddleBackQueuePushBack(FrontMiddleBackQueue* obj, int val) {
    Node * new_node = (Node *)malloc(sizeof(Node));
    new_node->val = val;  
    
    if(obj->rear != NULL)
    {
        obj->rear->next = new_node; 
    }
    else    //First Node
    {
        obj->front = new_node;
    }
    obj->rear = new_node;    
    new_node->next = NULL;
    
    obj->count++;
}

int frontMiddleBackQueuePopFront(FrontMiddleBackQueue* obj) {
    if(obj->front == NULL)
        return -1;
    
    int ret_val = obj->front->val;    
    Node * del_node = obj->front;    
    obj->front = obj->front->next;
    free(del_node);
    
    if(obj->front == NULL)  //Queue is empty
    {
        obj->rear = NULL;
    } 
    
    obj->count--;
    return ret_val;
}

int frontMiddleBackQueuePopMiddle(FrontMiddleBackQueue* obj) {
    Node * slow_ptr = obj->front;
    int ret_val;
    
    if(slow_ptr == NULL)
        return -1;
    
    if(slow_ptr->next == NULL)  //Only 1 element
    {
        printf("Here");
        ret_val = slow_ptr->val;
        obj->front = NULL;
        obj->rear = NULL;
        obj->count--;
        free(slow_ptr);
        return ret_val;
    }
    
    Node * prev_slow_ptr = NULL;
    Node * prev_prev_slow_ptr = NULL;
    Node * fast_ptr = obj->front->next;
    
    while(fast_ptr != NULL)
    {
        prev_prev_slow_ptr = prev_slow_ptr;
        prev_slow_ptr = slow_ptr;
        slow_ptr = slow_ptr->next;
        fast_ptr = fast_ptr->next;
        
        if(fast_ptr!=NULL)
            fast_ptr = fast_ptr->next;
    }
    
    if((obj->count)%2 == 0) //Even number of nodes
    {
        ret_val = prev_slow_ptr->val;
        if(obj->count == 2)
        {
            free(prev_slow_ptr);
            obj->front = slow_ptr;        
        }
        else
        {
            prev_prev_slow_ptr->next = slow_ptr;
            free(prev_slow_ptr);
        }       
    }
    else    //Odd number of nodes
    {
        ret_val = slow_ptr->val;
        prev_slow_ptr->next = slow_ptr->next;
        free(slow_ptr);
    }
    
    obj->count--;
    return ret_val;
}

int frontMiddleBackQueuePopBack(FrontMiddleBackQueue* obj) {
    if(obj->rear == NULL)
        return -1;
    
    int ret_val = obj->rear->val;
    Node * trav_ptr = obj->front;    
    if(trav_ptr == obj->rear)   //Only one element
    {
        obj->front = NULL;
        obj->rear = NULL;
        free(trav_ptr);
    }
    else
    {
        while(trav_ptr->next != obj->rear)
        {
            trav_ptr = trav_ptr->next;
        }
        trav_ptr->next = NULL;
        free(obj->rear);
        obj->rear = trav_ptr;
    }
    obj->count--;
    return ret_val;
}

void frontMiddleBackQueueFree(FrontMiddleBackQueue* obj) {
    Node * trav_ptr = obj->front;
    Node * del_ptr = NULL;
    
    while(trav_ptr != NULL)
    {
        del_ptr = trav_ptr;
        trav_ptr = trav_ptr->next;
        free(del_ptr);
    }
    
    obj->front = NULL;
    obj->rear = NULL;
    obj->count = 0;
}

/**
 * Your FrontMiddleBackQueue struct will be instantiated and called as such:
 * FrontMiddleBackQueue* obj = frontMiddleBackQueueCreate();
 * frontMiddleBackQueuePushFront(obj, val);
 
 * frontMiddleBackQueuePushMiddle(obj, val);
 
 * frontMiddleBackQueuePushBack(obj, val);
 
 * int param_4 = frontMiddleBackQueuePopFront(obj);
 
 * int param_5 = frontMiddleBackQueuePopMiddle(obj);
 
 * int param_6 = frontMiddleBackQueuePopBack(obj);
 
 * frontMiddleBackQueueFree(obj);
*/
```

**Solution 3: (Array)**
```
Runtime: 40 ms
Memory Usage: 15 MB
```
```c

typedef struct {
    int *array; int a,b,c,d;
} FrontMiddleBackQueue;

#define leftsize (obj->b - obj->a)
#define rightsize (obj->d - obj->c)
#define empty (leftsize + rightsize == 0)
#define pusha(x) obj->array[--obj->a] = x
#define pushb(x) obj->array[obj->b++] = x
#define pushc(x) obj->array[--obj->c] = x
#define pushd(x) obj->array[obj->d++] = x
#define popa obj->array[obj->a++]
#define popb obj->array[--obj->b]
#define popc obj->array[obj->c++]
#define popd obj->array[--obj->d]
#define shiftleft pushb(popc)
#define shiftright pushc(popb)

FrontMiddleBackQueue* frontMiddleBackQueueCreate() {
FrontMiddleBackQueue *obj = malloc(sizeof *obj);
    obj->array = malloc(3000*sizeof(int));
    obj->a = 1000; obj->b = 1000; obj->c = 2000; obj->d = 2000;
    return obj;
}

void frontMiddleBackQueuePushFront(FrontMiddleBackQueue* obj, int val) {
    if (leftsize > rightsize) shiftright;
    pusha(val);
}

void frontMiddleBackQueuePushMiddle(FrontMiddleBackQueue* obj, int val) {
    if (leftsize > rightsize) shiftright;
    pushb(val);
}

void frontMiddleBackQueuePushBack(FrontMiddleBackQueue* obj, int val) {
    if (rightsize > leftsize) shiftleft;
    pushd(val);
}

int frontMiddleBackQueuePopFront(FrontMiddleBackQueue* obj) {
    if empty return -1;
    if (rightsize > leftsize) shiftleft;
    return popa;
}

int frontMiddleBackQueuePopMiddle(FrontMiddleBackQueue* obj) {
    if empty return -1;
    if (leftsize>=rightsize) return popb;
    return popc;
}

int frontMiddleBackQueuePopBack(FrontMiddleBackQueue* obj) {
    if empty return -1;
    if (leftsize > rightsize) shiftright;
    return popd;
}

void frontMiddleBackQueueFree(FrontMiddleBackQueue* obj) {
    free(obj->array); free(obj);
}

/**
 * Your FrontMiddleBackQueue struct will be instantiated and called as such:
 * FrontMiddleBackQueue* obj = frontMiddleBackQueueCreate();
 * frontMiddleBackQueuePushFront(obj, val);
 
 * frontMiddleBackQueuePushMiddle(obj, val);
 
 * frontMiddleBackQueuePushBack(obj, val);
 
 * int param_4 = frontMiddleBackQueuePopFront(obj);
 
 * int param_5 = frontMiddleBackQueuePopMiddle(obj);
 
 * int param_6 = frontMiddleBackQueuePopBack(obj);
 
 * frontMiddleBackQueueFree(obj);
*/
```
