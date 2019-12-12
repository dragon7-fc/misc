937. Reorder Data in Log Files

You have an array of `logs`.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

* Each word after the identifier will consist only of lowercase letters, or;
* Each word after the identifier will consist only of digits.

We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

 

**Example 1:**
```
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
```

**Constraints:**

1. `0 <= logs.length <= 100`
1. `3 <= logs[i].length <= 100`
1. `logs[i]`` is guaranteed to have an identifier, and a word after the identifier.

# Solution
---
## Approach 1: Custom Sort
**Intuition and Algorithm**

Instead of sorting in the default order, we'll sort in a custom order we specify.

The rules are:

* Letter-logs come before digit-logs;
* Letter-logs are sorted alphanumerically, by content then identifier;
* Digit-logs remain in the same order.

It is straightforward to translate these ideas into code.

```python
class Solution(object):
    def reorderLogFiles(self, logs):
        def f(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key = f)
```

**Complexity Analysis**

* Time Complexity: $O(\mathcal{A}\log \mathcal{A})$, where $\mathcal{A}$ is the total content of `logs`.

* Space Complexity: $O(\mathcal{A})$.

# Submissions
---
**Solution**
```
Runtime: 36 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def f(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key = f)
```