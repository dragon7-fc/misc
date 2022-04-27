284. Peeking Iterator

Given an Iterator class interface with methods: `next()` and `hasNext()`, design and implement a PeekingIterator that support the `peek()` operation -- it essentially `peek()` at the element that will be returned by the next call to `next()`.

**Example:**
```
Assume that the iterator is initialized to the beginning of the list: [1,2,3].

Call next() gets you 1, the first element in the list.
Now you call peek() and it returns 2, the next element. Calling next() after that still return 2. 
You call next() the final time and it returns 3, the last element. 
Calling hasNext() after that should return false.
```

**Follow up:** How would you extend your design to be generic and work with all types, not just integer?

# Submissions
---
**Solution 1: (Linked List)**
```
Runtime: 28 ms
Memory Usage: 12.7 MB
```
```python
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self.val = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.val is None: self.val = self.it.next()
        return self.val

    def next(self):
        """
        :rtype: int
        """
        if self.val: 
            tmp, self.val = self.val, None
            return tmp
        return self.it.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.val is not None or self.it.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
```

**Solution 2: (Linked List)**
```
Runtime: 0 ms
Memory Usage: 6.4 MB
```
```c
/*
 *	struct Iterator {
 *		// Returns true if the iteration has more elements.
 *		bool (*hasNext)();
 *
 * 		// Returns the next element in the iteration.
 *		int (*next)();
 *	};
 */

typedef struct PeekingIterator {
    struct Iterator *it;
    int c, hp;
} piter;

struct PeekingIterator* Constructor(struct Iterator* iter) {
    piter *pi = calloc(1, sizeof *pi);
    pi->it = iter;
    return pi;
}

int peek(struct PeekingIterator* obj) {
    return obj->hp ? obj->c : (obj->hp = 1, obj->c = obj->it->next());
}

int next(struct PeekingIterator* obj) {
    return obj->hp ? obj->hp = 0, obj->c : (obj->c = obj->it->next());
}

bool hasNext(struct PeekingIterator* obj) {
    return obj->hp || obj->it->hasNext();
}

/**
 * Your PeekingIterator struct will be instantiated and called as such:
 * PeekingIterator* obj = peekingIteratorCreate(arr, arrSize);
 * int param_1 = peek(obj);
 * int param_2 = next(obj);
 * bool param_3 = hasNext(obj);
 * peekingIteratorFree(obj);
*/
```

**Solution 3: ()**
```
Runtime: 4 ms
Memory Usage: 7.4 MB
```
```c++
/*
 * Below is the interface for Iterator, which is already defined for you.
 * **DO NOT** modify the interface for Iterator.
 *
 *  class Iterator {
 *		struct Data;
 * 		Data* data;
 *  public:
 *		Iterator(const vector<int>& nums);
 * 		Iterator(const Iterator& iter);
 *
 * 		// Returns the next element in the iteration.
 *		int next();
 *
 *		// Returns true if the iteration has more elements.
 *		bool hasNext() const;
 *	};
 */

class PeekingIterator : public Iterator {
    int nextVal;
public:
	PeekingIterator(const vector<int>& nums) : Iterator(nums) {
	    // Initialize any member here.
	    // **DO NOT** save a copy of nums and manipulate it directly.
	    // You should only use the Iterator interface methods.
	    nextVal = Iterator::next();
	}
	
    // Returns the next element in the iteration without advancing the iterator.
	int peek() {
        return nextVal;
	}
	
	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	int next() {
	    int temp = nextVal;
        if (Iterator::hasNext())
            nextVal = Iterator::next();
        else
            nextVal = NULL;
	    return temp;
	}
	
	bool hasNext() const {
	    return (nextVal != NULL);
	}
};
```
