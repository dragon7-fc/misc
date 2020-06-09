925. Long Pressed Name

Your friend is typing his `name` into a keyboard.  Sometimes, when typing a character `c`, the key might get long pressed, and the character will be typed 1 or more times.

You examine the `typed` characters of the keyboard.  Return `True` if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

**Example 1:**
```
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
```

**Example 2:**
```
Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
```

**Example 3:**
```
Input: name = "leelee", typed = "lleeelee"
Output: true
```

**Example 4:**
```
Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.
```

**Note:**

1. `name.length <= 1000`
1. `typed.length <= 1000`
1. The characters of name and typed are lowercase letters.

# Submissions
---
## Approach 1: Group into Blocks
**Intuition and Algorithm**

For a string like `S = 'aabbbbccc'`, we can group it into blocks `groupify(S) = [('a', 2), ('b', 4), ('c', 3)]`, that consist of a key `'abc'` and a count `[2, 4, 3]`.

Then, the necessary and sufficient condition for typed to be a long-pressed version of name is that the keys are the same, and each entry of the count of typed is at least the entry for the count of name.

For example, `'aaleex'` is a long-pressed version of `'alex'`: because when considering the groups `[('a', 2), ('l', 1), ('e', 2), ('x', 1)]` and `[('a', 1), ('l', 1), ('e', 1), ('x', 1)]`, they both have the key `'alex'`, and the count `[2,1,2,1]` is at least `[1,1,1,1]` when making an element-by-element comparison `(2 >= 1, 1 >= 1, 2 >= 1, 1 >= 1)`.

```python
class Solution(object):
    def isLongPressedName(self, name, typed):
        g1 = [(k, len(list(grp))) for k, grp in itertools.groupby(name)]
        g2 = [(k, len(list(grp))) for k, grp in itertools.groupby(typed)]
        if len(g1) != len(g2):
            return False

        return all(k1 == k2 and v1 <= v2
                   for (k1,v1), (k2,v2) in zip(g1, g2))
```

**Complexity Analysis**

* Time Complexity: $O(N+T)$, where $N, T$ are the lengths of `name` and `typed`.

* Space Complexity: $O(N+T)$.

## Approach 2: Two Pointer
**Intuition**

As in Approach 1, we want to check the key and the count. We can do this on the fly.

Suppose we read through the characters `name`, and eventually it doesn't match `typed`.

There are some cases for when we are allowed to skip characters of `typed`. Let's use a tuple to denote the case `(name, typed)`:

* In a case like `('aab', 'aaaaab')`, we can skip the 3rd, 4th, and 5th `'a'` in typed because we have already processed an `'a'` in this block.

* In a case like `('a', 'b')`, we can't skip the 1st `'b'` in typed because we haven't processed anything in the current block yet.

**Algorithm**

This leads to the following algorithm:

* For each character in `name`, if there's a mismatch with the next character in `typed`:
    * If it's the first character of the block in `typed`, the answer is `False`.
    * Else, discard all similar characers of `typed` coming up. The next (different) character coming must match.

Also, we'll keep track on the side of whether we are at the first character of the block.

```python
class Solution(object):
    def isLongPressedName(self, name, typed):
        j = 0
        for c in name:
            if j == len(typed):
                return False

            # If mismatch...
            if typed[j] != c:
                # If it's the first char of the block, ans is False.
                if (j == 0) or (typed[j-1] != typed[j]):
                    return False

                # Discard all similar chars.
                cur = typed[j]
                while j < len(typed) and typed[j] == cur:
                    j += 1

                # If next isn't a match, ans is False.
                if j == len(typed) or typed[j] != c:
                    return False

            j += 1

        return True
```

**Complexity Analysis**

* Time Complexity: $O(N+T)$, where $N, T$ are the lengths of `name` and `typed`.

* Space Complexity: $O(1)$ in additional space complexity. (In Java, .`toCharArray` makes this $O(N)$, but this can be easily remedied.)

# Submissions
---
**Solution: (Group into Blocks)**
```
Runtime: 28 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        g1 = [(k, len(list(grp))) for k, grp in itertools.groupby(name)]
        g2 = [(k, len(list(grp))) for k, grp in itertools.groupby(typed)]
        if len(g1) != len(g2):
            return False

        return all(k1 == k2 and v1 <= v2
                   for (k1,v1), (k2,v2) in zip(g1, g2))
```

**Solution: (Two Pointers)**
```
Runtime: 32 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        j = 0
        for c in name:
            if j == len(typed):
                return False

            # If mismatch...
            if typed[j] != c:
                # If it's the first char of the block, ans is False.
                if (j == 0) or (typed[j-1] != typed[j]):
                    return False

                # Discard all similar chars.
                cur = typed[j]
                while j < len(typed) and typed[j] == cur:
                    j += 1

                # If next isn't a match, ans is False.
                if j == len(typed) or typed[j] != c:
                    return False

            j += 1

        return True
```