147. Insertion Sort List

![Example](img/147_Insertion-sort-example-300px.gif)

A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

1. Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
1. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
1. It repeats until no input elements remain.

Example 1:
```
Input: 4->2->1->3
Output: 1->2->3->4
```

Example 2:
```
Input: -1->5->3->4->0
Output: -1->0->3->4->5
```

Solution: 208 ms, 15.6 MB
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy=ListNode(-1)
        dummy.next=head
        prev=dummy
        while(prev.next and prev.next.next):
            # incremental number
            if prev.next.val<=prev.next.next.val:
                prev=prev.next
            else:
                cur=prev.next.next
                prev.next.next=cur.next
                tmp=dummy
                
                # insert node
                while tmp.next.val<=cur.val:
                    tmp=tmp.next
                cur.next=tmp.next
                tmp.next=cur
        return dummy.next
```
