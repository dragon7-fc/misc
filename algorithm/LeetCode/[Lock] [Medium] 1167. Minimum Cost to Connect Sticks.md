1167. Minimum Cost to Connect Sticks

You have some `sticks` with positive integer lengths.

You can connect any two sticks of lengths `X` and `Y` into one stick by paying a cost of `X + Y`.  You perform this action until there is one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.

 

**Example 1:**
```
Input: sticks = [2,4,3]
Output: 14
```

**Example 2:**
```
Input: sticks = [1,8,3,5]
Output: 30
```

**Constraints:**

* `1 <= sticks.length <= 10^4`
* `1 <= sticks[i] <= 10^4`

# Submissions
---
**Solution 1: (Heap)**
```
Runtime: 332 ms
Memory Usage: 14.7 MB
```
```python
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        ans = 0
        while len(sticks) > 1:
            val1 = heapq.heappop(sticks)
            val2 = heapq.heappop(sticks)
            ans += val1 + val2
            heapq.heappush(sticks, val1 + val2)
        return ans
```

**Solution 2: (Heap)**
```
Runtime: 328 ms
Memory Usage: 24.1 MB
```
```c++
class Solution {
public:
    int connectSticks(vector<int>& sticks) {
        if(sticks.empty())
            return 0;
        priority_queue<int,vector<int>,greater<int>>queue;
        for(auto &stick:sticks)
        {
            queue.push(stick);
        }
        int sumOfSticks{0};
        while(queue.size()!=1)
        {
            int stick1=queue.top();
            queue.pop();
            int stick2=queue.top();
            queue.pop();
            int temp=stick1+stick2;
            sumOfSticks+=temp;
            queue.push(temp);
        }
        return sumOfSticks;
    }
};
```