225. Implement Stack using Queues

Implement the following operations of a stack using queues.

* push(x) -- Push element x onto stack.
* pop() -- Removes the element on top of the stack.
* top() -- Get the top element.
* empty() -- Return whether the stack is empty.

**Example:**
```
MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
```

**Notes:**

* You must use only standard operations of a queue -- which means only `push to back`, `peek/pop from front`, `size`, and `is empty` operations are valid.
* Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
* You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

# Submissions
---
**Solution 1: (Stack)**
```
Runtime: 28 ms
Memory Usage: 12.8 MB
```
```python
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```

**Solution 2: (Queue)**
```
Runtime: 0 ms
Memory Usage: 6.2 MB
```
```c
typedef struct {
    int t1;
    int t2;
    int *Q1;
    int *Q2;
    int front;
    int rear1;
    int rear2;
} MyStack;


MyStack* myStackCreate() {
    MyStack* S = (MyStack  *)malloc(sizeof(MyStack));
    S->t1 = -1;
    S->t2 = -1;
    S->Q1 = (int *)malloc(sizeof(int)*100);
    S->Q2 = (int *)malloc(sizeof(int)*100);
    S->rear1=-1;
    S->rear2=-1;
    //S->front =0;
    return S;
}

void myStackPush(MyStack* obj, int x) {
    obj->front = x;
    printf("t1=%d\n", obj->t1);
    
    obj->Q1[++(obj->t1)] = x;
}

int myStackPop(MyStack* obj) {
    int x;
    
    //printf("Pop1 t1=%d, t2=%d\n", obj->t1, obj->t2);
    
    if(obj->t2==-1){
         
       obj->rear2 = obj->t1;
       printf("Pop2 rear1=%d, rear2=%d t1=%d, t2=%d\n", obj->rear1, obj->rear2, obj->t1, obj->t2);
        while(obj->rear1<obj->t1){
           printf("Pop3 rear1=%d, rear2=%d t1=%d, t2=%d\n", obj->rear1, obj->rear2, obj->t1, obj->t2);
            obj->Q2[++(obj->t2)] = obj->Q1[++(obj->rear1)];
            printf("Pop3a rear1=%d, rear2=%d t1=%d, t2=%d\n", obj->rear1, obj->rear2, obj->t1, obj->t2);
        }
        obj->t1=-1;
        obj->rear1=-1;
    }
    if(obj->rear2<=obj->t2){
        
        printf("Pop4 rear1=%d, rear2=%d t1=%d, t2=%d\n", obj->rear1, obj->rear2, obj->t1, obj->t2);
        x  = obj->Q2[(obj->rear2)--];
        
    }
    if(obj->rear2<0){
        obj->rear2=-1; 
        obj->t2=-1;
        }
        
    printf("Pop5 rear1=%d, rear2=%d t1=%d, t2=%d\n", obj->rear1, obj->rear2, obj->t1, obj->t2);
        
    return x;
}

int myStackTop(MyStack* obj) {
    printf("Top t1=%d, t2=%d\n", obj->t1, obj->t2);
    if(obj->t2==-1){
        return obj->front;   
    }
    
    return obj->Q2[obj->rear2];
}

bool myStackEmpty(MyStack* obj) {
    if(obj->t1==-1 && obj->t2==-1)
        return 1;
    
    return 0;
}

void myStackFree(MyStack* obj) {
    free(obj->Q1);
    free(obj->Q2);
    free(obj);
}

/**
 * Your MyStack struct will be instantiated and called as such:
 * MyStack* obj = myStackCreate();
 * myStackPush(obj, x);
 
 * int param_2 = myStackPop(obj);
 
 * int param_3 = myStackTop(obj);
 
 * bool param_4 = myStackEmpty(obj);
 
 * myStackFree(obj);
*/
```
