382. Linked List Random Node

Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

**Example:**
```
// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();
```

# Sobmissions
---
**Solution 1: (Fixed-Range Sampling)**
```
Runtime: 64 ms
Memory Usage: 17.1 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.range = []
        while head:
            self.range.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        pick = int(random.random() * len(self.range))
        return self.range[pick]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
```

**Solution 2: (Reservoir Sampling)**
```
Runtime: 88 ms
Memory Usage: 17.2 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        scope = 1
        chosen_value = 0
        curr = self.head

        while curr:
            # decide whether to include the element in reservoir
            if random.random() < 1 / scope:
                chosen_value = curr.val
            # move on to the next node
            curr = curr.next
            scope += 1
        return chosen_value


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
```

**Solution 3: (Linked List, Random)**
```
Runtime: 92 ms
Memory Usage: 17.1 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.length = 0
        self.head = head
        while head:
            self.length += 1
            head = head.next
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        r = random.randrange(self.length)
        cur = self.head
        while r:
            cur = cur.next
            r -= 1
        return cur.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
```

**Solution 4: (Linked List, Random)**
```
Runtime: 24 ms
Memory Usage: 12.6 MB
```
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */



typedef struct {
    int count;
    struct ListNode* head;
} Solution;


Solution* solutionCreate(struct ListNode* head) {
    Solution* obj=(Solution*)malloc(sizeof(Solution));
    obj->head=head;
    obj->count=0;
    while(head!=NULL){
        obj->count++;
        head=head->next;
    }
    return obj;
}

int solutionGetRandom(Solution* obj) {
    int temp=rand()%(obj->count)+1;
    struct ListNode* head=obj->head;
    for(int i=1;i<temp;i++){
        head=head->next;
    }
    return head->val;
}

void solutionFree(Solution* obj) {
    free(obj->head);
    free(obj);
}

/**
 * Your Solution struct will be instantiated and called as such:
 * Solution* obj = solutionCreate(head);
 * int param_1 = solutionGetRandom(obj);
 
 * solutionFree(obj);
*/
```
**Solution 5: (Reservoir Sampling)**
```
Runtime: 28 ms
Memory: 16.6 MB
```
```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
    ListNode *head = NULL;
public:
    Solution(ListNode* head) {
        this->head = head;
    }
    
    int getRandom() {
        int ans = 0, cnt = 1;
        ListNode *p = this->head;
        while (p) {
            if (rand() % cnt == 0) ans = p->val; // replace ans with i-th node.val with probability 1/i
            cnt ++;
            p = p->next;
        }
        return ans;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head);
 * int param_1 = obj->getRandom();
 */
```
