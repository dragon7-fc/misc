141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer `pos` which represents the position (`0`-indexed) in the linked list where tail connects to. If `pos` is `-1`, then there is no cycle in the linked list.

 

**Example 1:**
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```
![141_circularlinkedlist.png](img/141_circularlinkedlist.png)

**Example 2:**
```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```
![141_circularlinkedlist_test2.png](img/141_circularlinkedlist_test2.png)

**Example 3:**
```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```
![141_circularlinkedlist_test3.png](img/141_circularlinkedlist_test3.png)
 

**Follow up:**

* Can you solve it using `O(1)` (i.e. constant) memory?

# Solution
---
## Approach 1: Hash Table
**Intuition**

To detect if a list is cyclic, we can check whether a node had been visited before. A natural way is to use a hash table.

**Algorithm**

We go through each node one by one and record each node's reference (or memory address) in a hash table. If the current node is null, we have reached the end of the list and it must not be cyclic. If current node’s reference is in the hash table, then return `true`.

```java
public boolean hasCycle(ListNode head) {
    Set<ListNode> nodesSeen = new HashSet<>();
    while (head != null) {
        if (nodesSeen.contains(head)) {
            return true;
        } else {
            nodesSeen.add(head);
        }
        head = head.next;
    }
    return false;
}
```

**Complexity analysis**

* Time complexity : $O(n)$. We visit each of the $n$ elements in the list at most once. Adding a node to the hash table costs only $O(1)$ time.

* Space complexity: $O(n)$. The space depends $n$ the number of elements added to the hash table, which contains at most $n$ elements.

## Approach 2: Two Pointers
**Intuition**

Imagine two runners running on a track at different speed. What happens when the track is actually a circle?

**Algorithm**

The space complexity can be reduced to $O(1)$ by considering two pointers at different speed - a `slow` pointer and a `fast` pointer. The `slow` pointer moves one step at a time while the `fast` pointer moves two steps at a time.

If there is no cycle in the list, the `fast` pointer will eventually reach the end and we can return `false` in this case.

Now consider a cyclic list and imagine the `slow` and `fast` pointers are two runners racing around a circle track. The `fast` runner will eventually meet the `slow` runner. Why? Consider this case (we name it case A) - The `fast` runner is just one step behind the `slow` runner. In the next iteration, they both increment one and two steps respectively and meet each other.

How about other cases? For example, we have not considered cases where the `fast` runner is two or three steps behind the `slow` runner yet. This is simple, because in the next or next's next iteration, this case will be reduced to case A mentioned above.

```java
public boolean hasCycle(ListNode head) {
    if (head == null || head.next == null) {
        return false;
    }
    ListNode slow = head;
    ListNode fast = head.next;
    while (slow != fast) {
        if (fast == null || fast.next == null) {
            return false;
        }
        slow = slow.next;
        fast = fast.next.next;
    }
    return true;
}
```

**Complexity analysis**

* Time complexity : $O(n)$. Let us denote nn as the total number of nodes in the linked list. To analyze its time complexity, we consider the following two cases separately.

    * List has no cycle:
    
    The `fast` pointer reaches the end first and the run time depends on the list's length, which is $O(n)$.
    * List has a cycle:
    
    We break down the movement of the `slow` pointer into two steps, the non-cyclic part and the cyclic part:

        * The `slow` pointer takes "non-cyclic length" steps to enter the cycle. At this point, the fast pointer has already reached the cycle. $\text{Number of iterations} = \text{non-cyclic length} = N$

        * Both pointers are now in the cycle. Consider two runners running in a cycle - the `fast` runner moves 2 steps while the `slow` runner moves 1 steps at a time. Since the speed difference is 1, it takes $\dfrac{\text{distance between the 2 runners}}{\text{difference of speed}}$ loops for the `fast` runner to catch up with the `slow` runner. As the distance is at most "$\text{cyclic length K}$" and the speed difference is 1, we conclude that
$\text{Number of iterations} = \text{almost}$ "$\text{cyclic length K}$".

Therefore, the worst case time complexity is $O(N+K)$, which is $O(n)$.

* Space complexity : $O(1)$. We only use two nodes (`slow` and `fast`) so the space complexity is $O(1)$.

# Submissions
---
**Solution 1: (Two Pointers)**
```
Runtime: 76 ms
Memory Usage: 15.9 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False
```

**Solution 1: (Two Pointers)**
```
Runtime: 8 ms
Memory Usage: 8.1 MB
```
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    struct ListNode *slow, *fast;
    fast = slow = head;
    while (fast && fast->next) {
        fast = fast->next->next;
        slow = slow->next;
        if (fast == slow)
            return true;
    }
    return false;
}
```
