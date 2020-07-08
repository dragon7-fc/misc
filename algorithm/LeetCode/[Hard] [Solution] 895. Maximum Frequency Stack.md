895. Maximum Frequency Stack

Implement `FreqStack`, a class which simulates the operation of a stack-like data structure.

`FreqStack` has two functions:

* `push(int x)`, which pushes an integer `x` onto the stack.
* `pop()`, which removes and returns the most frequent element in the stack.
    * If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.
 

**Example 1:**
```
Input: 
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
Output: [null,null,null,null,null,null,null,5,7,5,4]
Explanation:
After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

pop() -> returns 5, as 5 is the most frequent.
The stack becomes [5,7,5,7,4].

pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
The stack becomes [5,7,5,4].

pop() -> returns 5.
The stack becomes [5,7,4].

pop() -> returns 4.
The stack becomes [5,7].
``` 

**Note:**

* Calls to `FreqStack.push(int x)` will be such that `0 <= x <= 10^9`.
* It is guaranteed that `FreqStack.pop()` won't be called if the stack has zero elements.
* The total number of `FreqStack.push` calls will not exceed `10000` in a single test case.
* The total number of `FreqStack.pop` calls will not exceed `10000` in a single test case.
* The total number of `FreqStack.push` and `FreqStack.pop` calls will not exceed `150000` across all test cases.

# Submissions
---
## Approach 1: Stack of Stacks
**Intuition**

Evidently, we care about the frequency of an element. Let `freq` be a Map from $x$ to the number of occurrences of $x$.

Also, we (probably) care about `maxfreq`, the current maximum frequency of any element in the stack. This is clear because we must pop the element with the maximum frequency.

The main question then becomes: among elements with the same (maximum) frequency, how do we know which element is most recent? We can use a stack to query this information: the top of the stack is the most recent.

To this end, let `group` be a map from frequency to a stack of elements with that frequency. We now have all the required components to implement `FreqStack`.

**Algorithm**

Actually, as an implementation level detail, if `x` has frequency `f`, then we'll have `x` in all `group[i] (i <= f)`, not just the top. This is because each `group[i]` will store information related to the ith copy of `x`.

Afterwards, our goal is just to maintain `freq`, `group`, and `maxfreq` as described above.

```python
class FreqStack(object):

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x):
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(x)

    def pop(self):
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x
```

**Complexity Analysis**

* Time Complexity: $O(1)$ for both push and pop operations.

* Space Complexity: $O(N)$, where `N` is the number of elements in the `FreqStack`.

# Submissions
---
**Solution: (Stack of Stacks)**
```
Runtime: 428 ms
Memory Usage: 21.5 MB
```
```python
class FreqStack:

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x: int) -> None:
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(x)

    def pop(self) -> int:
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
```

**Solution 2: (Stack)**
```
Runtime: 452 ms
Memory Usage: 87 MB
```
```c++
class FreqStack {
public:
    int maxfreq;
    unordered_map<int,int>mp;
    unordered_map<int,stack<int>>mymap;
    FreqStack() {
        maxfreq = 0;    
    }
    
    void push(int x) {
        if (mp.count(x)){
            mp[x]++;
        } else {
            mp[x] = 1;
        }
        
        mymap[mp[x]].push(x);
        maxfreq = max(maxfreq, mp[x]);
        return;
    }
    
    int pop() {
        int ans = mymap[maxfreq].top();
        mp[ans]--;
        mymap[maxfreq].pop();
        if (mymap[maxfreq].empty()) maxfreq = maxfreq-1;
        return ans;
    }
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 */
```