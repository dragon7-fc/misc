744. Find Smallest Letter Greater Than Target

Given a list of sorted characters `letters` containing only lowercase letters, and given a target letter `target`, find the smallest element in the list that is larger than the given `target`.

Letters also wrap around. For example, if the `target` is `target = 'z'` and `letters = ['a', 'b']`, the answer is `'a'`.

**Examples:**
```
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
```

**Note:**

* letters has a length in range `[2, 10000]`.
* letters consists of lowercase letters, and contains at least `2` unique letters.
* `target` is a lowercase letter.

# Solution
---
## Approach #1: Record Letters Seen [Accepted]
**Intuition and Algorithm**

Let's scan through `letters` and record if we see a letter or not. We could do this with an array of size 26, or with a Set structure.

Then, for every next letter (starting with the letter that is one greater than the `target`), let's check if we've seen it. If we have, it must be the answer.

```
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        seen = set(letters)
        for i in xrange(1, 26):
            cand = chr((ord(target) - ord('a') + i) % 26 + ord('a'))
            if cand in seen:
                return cand
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of letters. We scan every element of the array.

* Space Complexity: $O(1)$, the maximum size of `seen`.

## Approach #2: Linear Scan [Accepted]
**Intuition and Algorithm**

Since `letters` are sorted, if we see something larger when scanning form left to right, it must be the answer. Otherwise, (since `letters` is non-empty), the answer is `letters[0]`.

```python
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        for c in letters:
            if c > target:
                return c
        return letters[0]
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of letters. We scan every element of the array.

* Space Complexity: $O(1)$, as we maintain only pointers.

## Approach #3: Binary Search [Accepted]
**Intuition and Algorithm**

Like in Approach #2, we want to find something larger than target in a sorted array. This is ideal for a binary search: Let's find the rightmost position to insert target into letters so that it remains sorted.

Our binary search (a typical one) proceeds in a number of rounds. At each round, let's maintain the loop invariant that the answer must be in the interval `[lo, hi]`. Let `mi = (lo + hi) / 2`. If `letters[mi] <= target`, then we must insert it in the interval `[mi + 1, hi]`. Otherwise, we must insert it in the interval `[lo, mi]`.

At the end, if our insertion position says to insert target into the last position `letters.length`, we return `letters[0]` instead. This is what the modulo operation does.

```python
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]
```

**Complexity Analysis**

* Time Complexity: $O(\log N)$, where $N$ is the length of letters. We peek only at $\log N$ elements in the array.

* Space Complexity: $O(1)$, as we maintain only pointers.

# Submissions
---

**Solution 1: (Binary Search)**
```
Runtime: 112 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]
```

**Solution 2: (Binary Search)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 19.80 MB, Beats 62.61%
```
```c++
class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        int left = 0, right = letters.size() - 1, mid;
        char ans = letters[0];
        while (left <= right) {
            mid = left + (right - left) / 2;
            if (letters[mid] <= target) {
                left = mid + 1;
            } else {
                ans = letters[mid];
                right = mid - 1;
            }
        }
        return ans;
    }
};
```

**Solution 3: (Binary Search)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 19.67 MB, Beats 88.80%
```
```c++
class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        auto it = upper_bound(begin(letters), end(letters), target);
        if (it == end(letters)) {
            return letters[0];
        }
        return *it;
    }
};
```
