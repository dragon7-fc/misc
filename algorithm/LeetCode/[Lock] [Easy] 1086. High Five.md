1086. High Five

Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's **id**.

Each entry `items[i]` has `items[i][0]` the student's id, and `items[i][1]` the student's score.  The average score is calculated using integer division.

 

**Example 1:**
```
Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.
```

**Note:**

* `1 <= items.length <= 1000`
* `items[i].length == 2`
* The IDs of the students is between `1` to `1000`
* The score of the students is between `1` to `100`
* For each student, there are at least `5` scores

# Submissions
---
**Solution 1: (Heap)**
```
Runtime: 76 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        h = defaultdict(list)
        for idx, score in items:
            heapq.heappush(h[idx], score)
        return [[i, sum(heapq.nlargest(5, h[i])) // 5] for i in range(1, 1001) if i in h]
```

**Solution 2: (Hash Table)**
```
Runtime: 64 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores_dict={}
        for i in items:
            if i[0] not in scores_dict:
                scores_dict[i[0]] = [i[1]]
            else:
                scores_dict[i[0]].append(i[1])

        return [[i,sum(sorted(scores_dict[i])[::-1][:5])//5] for i in scores_dict.keys()]
```

**Solution 3: (Sort)**
```
Runtime: 74 ms
Memory: 14.1 MB
```
```python
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        cnt = collections.defaultdict(list)
        for i, s in items:
            cnt[i] += [s]
        return sorted([[k, sum(sorted(vs)[-5:])//5] for k, vs in cnt.items()])
```
