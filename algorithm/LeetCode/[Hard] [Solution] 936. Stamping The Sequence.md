936. Stamping The Sequence

You want to form a `target` string of **lowercase letters**.

At the beginning, your sequence is `target.length` `'?'` marks.  You also have a `stamp` of lowercase letters.

On each turn, you may place the stamp over the sequence, and replace every letter in the sequence with the corresponding letter from the stamp.  You can make up to `10 * target.length` turns.

For example, if the initial sequence is `"?????"`, and your stamp is "abc",  then you may make "abc??", "?abc?", "??abc" in the first turn.  (Note that the stamp must be fully contained in the boundaries of the sequence in order to stamp.)

If the sequence is possible to stamp, then return an array of the index of the left-most letter being stamped at each turn.  If the sequence is not possible to stamp, return an empty array.

For example, if the sequence is "ababc", and the stamp is "abc", then we could return the answer [0, 2], corresponding to the moves "?????" -> "abc??" -> "ababc".

Also, if the sequence is possible to stamp, it is guaranteed it is possible to stamp within `10 * target.length` moves.  Any answers specifying more than this number of moves will not be accepted.

 

**Example 1:**
```
Input: stamp = "abc", target = "ababc"
Output: [0,2]
([1,0,2] would also be accepted as an answer, as well as some other answers.)
```

**Example 2:**
```
Input: stamp = "abca", target = "aabcaca"
Output: [3,0,1]
```

**Note:**

* `1 <= stamp.length <= target.length <= 1000`
* `stamp` and `target` only contain lowercase letters`.

# Solution
---
## Approach 1: Work Backwards
**Intuition**

Imagine we stamped the sequence with moves $m_1, m_2, \cdots$. Now, from the final position `target`, we will make those moves in reverse order.

Let's call the `i`th window, a subarray of target of length `stamp.length` that starts at `i`. Each move at position `i` is possible if the `i`th window matches the stamp. After, every character in the window becomes a wildcard that can match any character in the stamp.

For example, say we have `stamp = "abca"` and `target = "aabcaca"`. Working backwards, we will reverse `stamp` at window `1` to get `"a????ca"`, then reverse `stamp` at window `3` to get `"a??????"`, and finally reverse stamp at position `0` to get `"???????"`.

**Algorithm**

Let's keep track of every window. We want to know how many cells initially match the stamp (our `"made"` list), and which ones don't (our "todo" list). Any windows that are ready (ie. have no todo list), get enqueued.

Specifically, we enqueue the positions of each character. (To save time, we enqueue by character, not by window.) This represents that the character is ready to turn into a `"?"` in our working `target` string.

Now, how to process characters in our queue? For each character, let's look at all the windows that intersect it, and update their todo lists. If any todo lists become empty in this manner (window.todo is empty), then we enqueue the characters in window.made that we haven't processed yet.

```python
class Solution(object):
    def movesToStamp(self, stamp, target):
        M, N = len(stamp), len(target)

        queue = collections.deque()
        done = [False] * N
        ans = []
        A = []
        for i in xrange(N - M + 1):
            # For each window [i, i+M),
            # A[i] will contain info on what needs to change
            # before we can reverse stamp at i.

            made, todo = set(), set()
            for j, c in enumerate(stamp):
                a = target[i+j]
                if a == c:
                    made.add(i+j)
                else:
                    todo.add(i+j)
            A.append((made, todo))

            # If we can reverse stamp at i immediately,
            # enqueue letters from this window.
            if not todo:
                ans.append(i)
                for j in xrange(i, i + len(stamp)):
                    if not done[j]:
                        queue.append(j)
                        done[j] = True

        # For each enqueued letter,
        while queue:
            i = queue.popleft()

            # For each window that is potentially affected,
            # j: start of window
            for j in xrange(max(0, i-M+1), min(N-M, i)+1):
                if i in A[j][1]:  # This window is affected
                    A[j][1].discard(i) # Remove it from todo list of this window
                    if not A[j][1]:  # Todo list of this window is empty
                        ans.append(j)
                        for m in A[j][0]: # For each letter to potentially enqueue,
                            if not done[m]:
                                queue.append(m)
                                done[m] = True

        return ans[::-1] if all(done) else []
```

**Complexity Analysis**

* Time Complexity: $O(N(N-M))$, where $M, N$ are the lengths of stamp, target.

* Space Complexity: $O(N(N-M))$.

# Submissions
---
**Solution 1: (Work Backwards)**
```
Runtime: 320 ms
Memory Usage: 17.8 MB
```
```python
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        M, N = len(stamp), len(target)

        queue = collections.deque()
        done = [False] * N
        ans = []
        A = []
        for i in range(N - M + 1):
            # For each window [i, i+M),
            # A[i] will contain info on what needs to change
            # before we can reverse stamp at i.

            made, todo = set(), set()
            for j, c in enumerate(stamp):
                a = target[i+j]
                if a == c:
                    made.add(i+j)
                else:
                    todo.add(i+j)
            A.append((made, todo))

            # If we can reverse stamp at i immediately,
            # enqueue letters from this window.
            if not todo:
                ans.append(i)
                for j in range(i, i + len(stamp)):
                    if not done[j]:
                        queue.append(j)
                        done[j] = True

        # For each enqueued letter,
        while queue:
            i = queue.popleft()

            # For each window that is potentially affected,
            # j: start of window
            for j in range(max(0, i-M+1), min(N-M, i)+1):
                if i in A[j][1]:  # This window is affected
                    A[j][1].discard(i) # Remove it from todo list of this window
                    if not A[j][1]:  # Todo list of this window is empty
                        ans.append(j)
                        for m in A[j][0]: # For each letter to potentially enqueue,
                            if not done[m]:
                                queue.append(m)
                                done[m] = True

        return ans[::-1] if all(done) else []
```

**Solution 2: (Greedy)**

This problem has two steps:

1. Collection all possible patterns from given stamp.
1. Greedy replace all matched substring until converged to "\*\*\*\*\*\*"

```
Runtime: 512 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        ns = len(stamp)        
        stamp_patterns = []
        # Step - 1:
        # we need to collect all possible stamp patters, like
        # 'abcde'
        # 'abcd*'
        # '*bcde'
        # 'abc**'
        # '**cde'
        # 'ab***'
        # '*bc**'
        # '**cd*'
        # '***de'
        # ‘****e’ and etc
        for window_size in range(1, ns + 1):
            for i in range(ns - window_size + 1):
                curr = '*' * i + stamp[i:i + window_size] + '*' * (ns - window_size - i)
                stamp_patterns.append(curr)
        stamp_patterns.append('*' * ns)

        res = []
        nt = len(target)
		# Step - 2
        # '*****' is our final target
        while target != '*' * nt:
            old_target = target
            # greedy, keep replace current target string with possible patter
            for pattern in stamp_patterns:
                inx = target.find(pattern)
                if inx != -1:
                    target = target[:inx] + '*' * ns + target[inx + ns:]
                    res.append(inx)
            if old_target == target:
                return []
        
        return res[::-1]
```

**Solution 3: (Greedy)**
```
Runtime: 11 ms
Memory Usage: 7.5 MB
```
```c++
class Solution {
public:
    vector<int> movesToStamp(string stamp, string target) {
        vector<int> res;
        bool matched = true;
        while (matched) {  
            matched = false;
            for (int i = 0; i <= target.size() - stamp.size(); ++i) { 
                int j = 0, stars_cnt = 0;
				//find a match with stamp.
                for (; j < stamp.size(); ++j) {
                    
                    if (target[i + j] == '*') {
                        ++stars_cnt;
                    } else if (target[i + j] != stamp[j]) {
                        break;
                    }
                }
			//let if we find a match with stamp, do a reverse operation on target.
                if (j == stamp.size() && stars_cnt < stamp.size()) {
                    res.push_back(i);
                    
                    for (int k = 0; k < stamp.size(); ++k) {
                        target[i + k] = '*';
                    }
                    matched = true;
                }
            }
        }
        for (auto c : target) {
            if (c != '*') {
                return vector<int>();
            }
        }
        reverse(res.begin(), res.end());
        return res;  
    }
};
```
