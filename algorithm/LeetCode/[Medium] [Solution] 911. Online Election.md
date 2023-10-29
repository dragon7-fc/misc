911. Online Election

In an election, the `i`-th vote was cast for `persons[i]` at time `times[i]`.

Now, we would like to implement the following query function:

`TopVotedCandidate.q(int t)` will return the number of the person that was leading the election at time `t`.  

Votes cast at time `t` will count towards our query.  In the case of a tie, the most recent vote (among tied candidates) wins.

 

**Example 1:**
```
Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
Output: [null,0,1,1,0,0,1]
Explanation: 
At time 3, the votes are [0], and 0 is leading.
At time 12, the votes are [0,1,1], and 1 is leading.
At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
This continues for 3 more queries at time 15, 24, and 8.
```

**Note:**

* `1 <= persons.length = times.length <= 5000`
* `0 <= persons[i] <= persons.length`
* `times` is a strictly increasing array with all elements in `[0, 10^9]`.
* `TopVotedCandidate.q` is called at most `10000` times per test case.
* `TopVotedCandidate.q(int t)` is always called with `t >= times[0]`.

# Solution
---
## Approach 1: List of Lists + Binary Search
**Intuition and Algorithm**

We can store the votes in a list `A` of lists of votes. Each vote has a person and a timestamp, and `A[count]` is a list of the `count`-th votes received for that person.

Then, `A[i][0]` and `A[i]` are monotone increasing, so we can binary search on them to find the most recent vote by time.

```python
class TopVotedCandidate(object):

    def __init__(self, persons, times):
        self.A = []
        self.count = collections.Counter()
        for p, t in zip(persons, times):
            self.count[p] = c = self.count[p] + 1
            while len(self.A) <= c: self.A.append([])
            self.A[c].append((t, p))

    def q(self, t):
        lo, hi = 1, len(self.A)
        while lo < hi:
            mi = (lo + hi) / 2
            if self.A[mi][0][0] <= t:
                lo = mi + 1
            else:
                hi = mi
        i = lo - 1
        j = bisect.bisect(self.A[i], (t, float('inf')))
        return self.A[i][j-1][1]
```

**Complexity Analysis**

* Time Complexity: $O(N + Q \log^2 N)$, where $N$ is the number of votes, and $Q$ is the number of queries.

* Space Complexity: $O(N)$.

## Approach 2: Precomputed Answer + Binary Search
**Intuition and Algorithm**

As the votes come in, we can remember every event (winner, time) when the winner changes. After, we have a sorted list of these events that we can binary search for the answer.

```python
class TopVotedCandidate(object):
    def __init__(self, persons, times):
        self.A = []
        count = collections.Counter()
        leader, m = None, 0  # leader, num votes for leader

        for p, t in itertools.izip(persons, times):
            count[p] += 1
            c = count[p]
            if c >= m:
                if p != leader:  # lead change
                    leader = p
                    self.A.append((t, leader))

                if c > m:
                    m = c

    def q(self, t):
        i = bisect.bisect(self.A, (t, float('inf')), 1)
        return self.A[i-1][1]
```

**Complexity Analysis**

* Time Complexity: $O(N + Q \log N)$, where $N$ is the number of votes, and $Q$ is the number of queries.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution: (Precomputed Answer + Binary Search)**
```
Runtime: 676 ms
Memory Usage: 17.4 MB
```
```python
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.A = []
        count = collections.Counter()
        leader, m = None, 0  # leader, num votes for leader

        for p, t in zip(persons, times):
            count[p] += 1
            c = count[p]
            if c >= m:
                if p != leader:  # lead change
                    leader = p
                    self.A.append((t, leader))

                if c > m:
                    m = c

    def q(self, t: int) -> int:
        i = bisect.bisect(self.A, (t, float('inf')), 1)
        return self.A[i-1][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
```

**Solution 1: (Two Pointers)**
```
Runtime: 0 ms
Memory: 6.7 MB
```
```c++
class Solution {
public:
    int shortestWay(string source, string target) {
        // Boolean array to mark all characters of source
        bool sourceChars[26] = {false};
        for (char c : source) {
            sourceChars[c - 'a'] = true;
        }

        // Check if all characters of target are present in source
        // If any character is not present, return -1
        for (char c : target) {
            if (!sourceChars[c - 'a']) {
                return -1;
            }
        }

        // Length of source to loop back to start of source using mod
        int m = source.length();

        // Pointer for source
        int sourceIterator = 0;

        // Number of times source is traversed. It will be incremented when
        // while finding occurrence of a character in target, sourceIterator
        // reaches the start of source again.
        int count = 0;

        // Find all characters of target in source
        for (char c : target) {

            // If while finding, iterator reaches start of source again,
            // increment count
            if (sourceIterator == 0) {
                count++;
            }

            // Find the first occurrence of c in source
            while (source[sourceIterator] != c) {

                // Formula for incrementing while looping back to start.
                sourceIterator = (sourceIterator + 1) % m;

                // If while finding, iterator reaches start of source again,
                // increment count
                if (sourceIterator == 0) {
                    count++;
                }
            }

            // Loop will break when c is found in source. Thus, increment.
            // Don't increment count until it is not clear that target has
            // remaining characters.
            sourceIterator = (sourceIterator + 1) % m;
        }

        // Return count
        return count;
    }
};
```

**Solution 2: (Inverted Index and Binary Search)**
```
Runtime: 8 ms
Memory: 9.1 MB
```
```c++
class Solution {
public:
    int shortestWay(string source, string target) {
        // Array to store the vector of charToIndices of each character in source
        vector < int > charToIndices[26];
        for (int i = 0; i < source.size(); i++) {
            charToIndices[source[i] - 'a'].push_back(i);
        }

        // The current index in source
        int sourceIterator = 0;

        // Number of times we have to iterate through source to get target
        int count = 1;

        // Find all characters of target in source
        for (int i = 0; i < target.size(); i++) {

            // If the character is not present in source, return -1
            if (charToIndices[target[i] - 'a'].size() == 0) {
                return -1;
            }

            // Binary search to find the index of the character in source next to the source iterator
            vector < int > indices = charToIndices[target[i] - 'a'];
            int index = lower_bound(indices.begin(), indices.end(), sourceIterator) - indices.begin();

            // If we have reached the end of the list, we need to iterate
            // through source again, hence first index of character in source.
            if (index == indices.size()) {
                count++;
                sourceIterator = indices[0] + 1;
            } else {
                sourceIterator = indices[index] + 1;
            }
        }

        return count;
    }
};
```

**Solution 2: (2D Array)**
```
Runtime: 0 ms
Memory: 6.9 MB
```
```c++
class Solution {
public:
    int shortestWay(string source, string target) {
        // Next Occurrence of Character after Index
        int nextOccurrence[source.length()][26];

        // Base Case
        for (int c = 0; c < 26; c++) {
            nextOccurrence[source.length() - 1][c] = -1;
        }
        nextOccurrence[source.length() - 1][source[source.length() - 1] - 'a'] = source.length() - 1;

        // Fill using recurrence relation
        for (int idx = source.length() - 2; idx >= 0; idx--) {
            for (int c = 0; c < 26; c++) {
                nextOccurrence[idx][c] = nextOccurrence[idx + 1][c];
            }
            nextOccurrence[idx][source[idx] - 'a'] = idx;
        }

        // Pointer to the current index in source
        int sourceIterator = 0;

        // Number of times we need to iterate through source
        int count = 1;

        // Find all characters of target in source
        for (char c : target) {

            // If the character is not present in source
            if (nextOccurrence[0][c - 'a'] == -1) {
                return -1;
            }

            // If we have reached the end of source, or character is not in
            // source after source_iterator, loop back to beginning
            if (sourceIterator == source.length() || nextOccurrence[sourceIterator][c - 'a'] == -1) {
                count++;
                sourceIterator = 0;
            }

            // Next occurrence of character in source after source_iterator
            sourceIterator = nextOccurrence[sourceIterator][c - 'a'] + 1;
        }

        // Return the number of times we need to iterate through source
        return count;
    }
};
```
