916. Word Subsets

We are given two arrays `A` and `B` of words.  Each word is a string of lowercase letters.

Now, say that word `b` is a subset of word `a` if every letter in `b` occurs in `a`, including multiplicity.  For example, `"wrr"` is a subset of `"warrior"`, but is not a subset of `"world"`.

Now say a word `a` from `A` is universal if for every `b` in `B`, `b` is a subset of `a`. 

Return a list of all universal words in `A`.  You can return the words in any order.

 

**Example 1:**
```
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]
```

**Example 2:**
```
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
Output: ["apple","google","leetcode"]
```

**Example 3:**
```
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
Output: ["facebook","google"]
```

**Example 4:**
```
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
Output: ["google","leetcode"]
```

**Example 5:**
```
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]
```

**Note:**

1. `1 <= A.length, B.length <= 10000`
1. `1 <= A[i].length, B[i].length <= 10`
1. `A[i]` and `B[i]` consist only of lowercase letters.
1. All words in `A[i]` are unique: there isn't `i != j` with `A[i] == A[j]`.

# Solution
---
## Approach 1: Reduce to Single Word in B
**Intuition**

If `b` is a subset of `a`, then say `a` is a superset of `b`. Also, say $N_{\text{"a"}}(\text{word})$ (word) is the count of the number of \text{"a"}"a"'s in the word.

When we check whether a word `wordA` in `A` is a superset of `wordB`, we are individually checking the counts of letters: that for each $\text{letter}$, we have $N_{\text{letter}}(\text{wordA}) \geq N_{\text{letter}}(\text{wordB})$ (wordB).

Now, if we check whether a word `wordA` is a superset of all words $\text{wordB}_i$, we will check for each letter and each $i$, that$ N_{\text{letter}}(\text{wordA}) \geq N_{\text{letter}}(\text{wordB}_i)$. This is the same as checking $N_{\text{letter}}(\text{wordA}) \geq \max\limits_i(N_{\text{letter}}(\text{wordB}_i))$.

For example, when checking whether `"warrior"` is a superset of words `B = ["wrr", "wa", "or"]`, we can combine these words in `B` to form a `"maximum"` word `"arrow"`, that has the maximum count of every letter in each word in `B`.

**Algorithm**

Reduce `B` to a single word `bmax` as described above, then compare the counts of letters between words `a` in `A`, and `bmax`.

```python
class Solution(object):
    def wordSubsets(self, A, B):
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans

        bmax = [0] * 26
        for b in B:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)

        ans = []
        for a in A:
            if all(x >= y for x, y in zip(count(a), bmax)):
                ans.append(a)
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(\mathcal{A} + \mathcal{B})$, where $\mathcal{A}$ and $\mathcal{B}$ is the total amount of information in `A` and `B` respectively.

* Space Complexity: $O(A\text{.length} + B\text{.length})$.

# Submissions
---
**Solution 1: (Counter)**
```
Runtime: 1252 ms
Memory Usage: 16.6 MB
```
```python
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        res = []; temp = collections.Counter()
        for it in B:
            temp = (temp | collections.Counter(it))
        for i, it in enumerate(A):
            if temp == (temp & collections.Counter(it)):
                res.append(it)
        return res
```