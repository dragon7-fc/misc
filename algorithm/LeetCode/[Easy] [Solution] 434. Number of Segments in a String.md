434. Number of Segments in a String

Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any **non-printable** characters.

**Example:**
```
Input: "Hello, my name is John"
Output: 5
```

# Solution
---
## Approach #1 Using Language Builtins [Accepted]
**Intuition**

In a situation where raw efficiency is less important than code legibility, it is likely better to use language-idiomatic builtin functions to solve this problem.

**Algorithm**

There are a few corner cases that you can get snagged on in this problem, at least in Java. First, one or more leading spaces will cause split to deduce an erroneous "" token at the beginning of the string, so we use the builtin `trim` method to remove leading and trailing spaces. Then, if the resulting string is the empty string, then we can simply output `0`. This is necessary due to the following behavior of the split method:
```
String[] tokens = "".split("\s++");
tokens.length; // 1
tokens[0]; // ""
```
If we reach the final return statement, we `split` the trimmed string on sequences of one or more whitespace characters (`split` can take a regular expression) and return the length of the resulting array.

The Python solution is trivially short because Python's `split` has a lot of default behavior that makes it perfect for this sort of problem. Notably, it returns an empty list when splitting an empty string, it `split`s on whitespace by default, and it implicitly `trim`s (strips, in Python lingo) the string beforehand.

```python
class Solution:
    def countSegments(self, s):
        return len(s.split())
```

**Complexity Analysis**

* Time complexity : $O(n)$

All builtin language functionality used here (in both the Java and Python examples) runs in either $O(n)$ or $O(1)$ time, so the entire algorithm runs in linear time.

* Space complexity : $O(n)$

split (in both languages) returns an array/list of $O(n)$ length, so the algorithm uses linear additional space.

## Approach #2 In-place [Accepted]
**Intuition**

If we cannot afford to allocate linear additional space, a fairly simple algorithm can deduce the number of segments in linear time and constant space.

**Algorithm**

To count the number of segments, it is equivalent to count the number of string indices at which a segment begins. Therefore, by formally defining the characteristics of such an index, we can simply iterate over the string and test each index in turn. Such a definition is as follows: a string index begins a segment if it is preceded by whitespace (or is the first index) and is not whitespace itself, which can be checked in constant time. Finally, we simply return the number of indices for which the condition is satisfied.

```python
class Solution:
    def countSegments(self, s):
        segment_count = 0

        for i in range(len(s)):
            if (i == 0 or s[i-1] == ' ') and s[i] != ' ':
                segment_count += 1

        return segment_count
```

**Complexity Analysis**

* Time complexity : $O(n)$

We do a constant time check for each of the string's $n$ indices, so the runtime is overall linear.

* Space complexity : $O(1)$

There are only a few integers allocated, so the memory footprint is constant.

# Submissions
---
**Solution 1: (Using Language Builtins)**
```
Runtime: 28 ms
Memory Usage: 12.6 MB
```
```python
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
```