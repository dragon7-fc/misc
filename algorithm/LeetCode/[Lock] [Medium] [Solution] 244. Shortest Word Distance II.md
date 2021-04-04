244. Shortest Word Distance II

Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.

Implement the `WordDistance` class:

* `WordDistance(String[] wordsDict)` initializes the object with the strings array `wordsDict`.
* `int shortest(String word1, String word2)` returns the shortest distance between `word1` and `word2` in the array `wordsDict`.
 

**Example 1:**

```
Input
["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
Output
[null, 3, 1]

Explanation
WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
wordDistance.shortest("coding", "practice"); // return 3
wordDistance.shortest("makes", "coding");    // return 1
```

**Constraints:**

* `1 <= wordsDict.length <= 3 * 10^4`
* `1 <= wordsDict[i].length <= 10`
* wordsDict[i] consists of lowercase English letters.
* `word1` and `word2` are in `wordsDict`.
* `word1` != `word2`
* At most `5000` calls will be made to shortest.

# Submissions
---
**Solution 1: (Using Preprocessed Sorted Indices, Two Pointers)**
```
Runtime: 88 ms
Memory Usage: 21.5 MB
```
```python
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.locations = defaultdict(list)

        # Prepare a mapping from a word to all it's locations (indices).
        for i, w in enumerate(wordsDict):
            self.locations[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        loc1, loc2 = self.locations[word1], self.locations[word2]
        l1, l2 = 0, 0
        min_diff = float("inf")

        # Until the shorter of the two lists is processed
        while l1 < len(loc1) and l2 < len(loc2):
            min_diff = min(min_diff, abs(loc1[l1] - loc2[l2]))
            if loc1[l1] < loc2[l2]:
                l1 += 1
            else:
                l2 += 1
        return min_diff


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
```