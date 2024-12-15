1792. Maximum Average Pass Ratio

There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where `classes[i] = [passi, totali]`. You know beforehand that in the ith class, there are `totali` total students, but only `passi` number of students will pass the exam.

You are also given an integer `extraStudents`. There are another extraStudents brilliant students that are **guaranteed** to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that **maximizes** the **average** pass ratio across **all** the classes.

The **pass ratio** of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The **average pass ratio** is the sum of pass ratios of all the classes divided by the number of the classes.

Return the **maximum** possible average pass ratio after assigning the extraStudents students. Answers within `10^-5` of the actual answer will be accepted.

 

**Example 1:**
```
Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
Output: 0.78333
Explanation: You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.
```

**Example 2:**
```
Input: classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
Output: 0.53485
```

**Constraints:**

* `1 <= classes.length <= 10^5`
* `classes[i].length == 2`
* `1 <= passi <= totali <= 10^5`
* `1 <= extraStudents <= 10^5`

# Submissions
---
**Solution 1: (Heap)**

* (b+1)/(a+1) - b/a = (a-b)/(a*(a+1))
* for every class, we can calculate the increment if we add one student
* for every extraStudents, find the largest increment and add one

```
Runtime: 2752 ms
Memory Usage: 64.2 MB
```
```python
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        d = [(-(y-x)/(y*(y+1)),x,y) for x,y in classes]
        heapq.heapify(d)
        ans = 0
        while d:
            increase, pass_n, total_n = heapq.heappop(d)
            extraStudents,total_n,pass_n = extraStudents-1,total_n+1,pass_n+1
            increase = -(total_n-pass_n)/(total_n*(total_n+1))
            heapq.heappush(d, (increase, pass_n, total_n))
            if extraStudents<=0:
                break

        return sum([x[1]/(x[2]*len(classes)) for x in d])
```

**Solution 2: (Heap, math)**

    [[2,4],               [3,9],               [4,5],                [2,10]]
pq: [3/5-2/4,             4/10-3/9,            5/6-4/5,              3/11-2/10]
    [0.09999999999999998, 0.06666666666666671, 0.033333333333333326, 0.0727272727272727]
        ^
    [4/6-3/5,             4/10-3/9,            5/6-4/5,              3/11-2/10]
    [0.06666666666666665, 0.06666666666666671, 0.033333333333333326, 0.0727272727272727]
                                                                         ^
    [4/6-3/5,             4/10-3/9,            5/6-4/5,              4/12-3/11]
    [0.06666666666666665, 0.06666666666666671, 0.033333333333333326, 0.06060606060606061]
                              ^
    [4/6-3/5,             5/11-4/10,           5/6-4/5,              4/12-3/11]
    [0.06666666666666665, 0.05454545454545451, 0.033333333333333326, 0.06060606060606061]
        ^
```
Runtime: 322 ms
Memory: 98.90 MB
```
```c++
class Solution {
public:
    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        int n = classes.size(), i, k = extraStudents;
        priority_queue<tuple<double,int,int>> pq;
        double ans = 0;
        for (i = 0; i < n; i ++) {
            ans += (double)classes[i][0]/classes[i][1];
            pq.push({((double)classes[i][0]+1)/(classes[i][1]+1) - (double)classes[i][0]/classes[i][1], classes[i][0]+1, classes[i][1]+1});
        }
        while (k) {
            auto [r, c, p] = pq.top();
            pq.pop();
            ans += r;
            pq.push({((double)c+1)/(p+1)-(double)c/p, c+1, p+1});
            k -= 1;
        }
        return ans/n;
    }
};
```
