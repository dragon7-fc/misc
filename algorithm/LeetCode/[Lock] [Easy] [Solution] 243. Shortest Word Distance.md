243. Shortest Word Distance

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

**Example:**
```
Assume that `words = ["practice", "makes", "perfect", "coding", "makes"]`.

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
```

**Note:**

* You may assume that word1 **does not equal to** word2, and word1 and word2 are both in the list.

# Solution
---
This is a straight-forward coding problem. The distance between any two positions $i_1$ and $i_2$ in an array is $|i_1 - i_2|$. To find the shortest distance between `word1` and `word2`, we need to traverse the input array and find all occurrences $i_1$ and $i_2$ of the two words, and check if $|i_1 - i_2|$ is less than the minimum distance computed so far.

## Approach #1 (Brute Force) [Accepted]
**Algorithm**

A naive solution to this problem is to go through the entire array looking for the first word. Every time we find an occurrence of the first word, we search the entire array for the closest occurrence of the second word.

**Java**
```java
public int shortestDistance(String[] words, String word1, String word2) {
    int minDistance = words.length;
    for (int i = 0; i < words.length; i++) {
        if (words[i].equals(word1)) {
            for (int j = 0; j < words.length; j++) {
                if (words[j].equals(word2)) {
                    minDistance = Math.min(minDistance, Math.abs(i - j));
                }
            }
        }
    }
    return minDistance;
}
```

**Complexity Analysis**

* The time complexity is $O(n^2)$, since for every occurrence of `word1`, we traverse the entire array in search for the closest occurrence of `word2`.

* Space complexity is $O(1)$, since no additional space is used.

## Approach #2 (One-pass) [Accepted]
**Algorithm**

We can greatly improve on the brute-force approach by keeping two indices i1 and i2 where we store the most recent locations of `word1` and `word2`. Each time we find a new occurrence of one of the words, we do not need to search the entire array for the other word, since we already have the index of its most recent occurrence.

**Java**
```java
public int shortestDistance(String[] words, String word1, String word2) {
    int i1 = -1, i2 = -1;
    int minDistance = words.length;
    int currentDistance;
    for (int i = 0; i < words.length; i++) {
        if (words[i].equals(word1)) {
            i1 = i;
        } else if (words[i].equals(word2)) {
            i2 = i;
        }

        if (i1 != -1 && i2 != -1) {
            minDistance = Math.min(minDistance, Math.abs(i1 - i2));
        }
    }
    return minDistance;
}
```

**Complexity Analysis**

* The time complexity is $O(n)$. This problem is inherently linear; we cannot do better than $O(n)$ because at the very least, we have to read the entire input.

* Space complexity is $O(1)$, since no additional space is allocated.

# Submissions
---
**Sotution 1: (Array, Greedy)**
```
Runtime: 68 ms
Memory Usage: 17.5 MB
```
```python
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        word1_idx = -1
        word2_idx = -1
        res = float('inf')
        
        for idx, word in enumerate(words):
            if word == word1:
                word1_idx = idx
                if word2_idx!=-1:
                    res = min(res, word1_idx-word2_idx)
            if word == word2:
                word2_idx = idx
                if word1_idx!=-1:
                    res = min(res, word2_idx-word1_idx)
            if res == 1: # can't do better
                break
        return res
```

**Solution 2: (Array, Greedy)**
```
Runtime: 20 ms
Memory Usage: 11.8 MB
```
```c++
class Solution {
public:
    int shortestDistance(vector<string>& words, string word1, string word2) {
        int w1 = -1, w2 = -1, dist = INT_MAX;
        for (int i=0; i<words.size(); i++) {
            if (words[i] == word1) w1 = i;
            else if (words[i] == word2) w2 = i;
            if (w1 != -1 and w2 != -1) 
                dist = min(dist, abs(w2 - w1));
        }
        return dist;
    }
};
```