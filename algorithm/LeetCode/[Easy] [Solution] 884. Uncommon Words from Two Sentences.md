884. Uncommon Words from Two Sentences

We are given two sentences `A` and `B`.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

 

**Example 1:**
```
Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
```

**Example 2:**
```
Input: A = "apple apple", B = "banana"
Output: ["banana"]
```

**Note:**

* `0 <= A.length <= 200`
* `0 <= B.length <= 200`
* `A` and `B` both contain only spaces and lowercase letters.

# Submissions
---
## Approach 1: Counting
Intuition and Algorithm

Every uncommon word occurs exactly once in total. We can count the number of occurrences of every word, then return ones that occur exactly once.

```python
class Solution(object):
    def uncommonFromSentences(self, A, B):
        count = {}
        for word in A.split():
            count[word] = count.get(word, 0) + 1
        for word in B.split():
            count[word] = count.get(word, 0) + 1

        #Alternatively:
        #count = collections.Counter(A.split())
        #count += collections.Counter(B.split())

        return [word for word in count if count[word] == 1]
```

**Complexity Analysis**

* Time Complexity: $O(M + N)$, where $M, N$ are the lengths of `A` and `B` respectively.

* Space Complexity: $O(M + N)$, the space used by count.

# Submissions
---
**Solution:**
```
Runtime: 28 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        count = {}
        for word in A.split():
            count[word] = count.get(word, 0) + 1
        for word in B.split():
            count[word] = count.get(word, 0) + 1

        #Alternatively:
        #count = collections.Counter(A.split())
        #count += collections.Counter(B.split())

        return [word for word in count if count[word] == 1]
```

**Solution 2: (String, Counter)**
```
Runtime: 4 ms
Memory: 8.97 MB
```
```c++
class Solution {
public:
    vector<string> uncommonFromSentences(string s1, string s2) {
        unordered_map<string, int> cnt;
        stringstream ss(s1);
        string w;
        while (getline(ss, w, ' ')) {
            cnt[w] += 1;
        }
        ss = stringstream(s2);
        while (getline(ss, w, ' ')) {
            cnt[w] += 1;
        }
        vector<string> ans;
        for (auto [w, c]: cnt) {
            if (c == 1) {
                ans.push_back(w);
            }
        }
        return ans;
    }
};
```
