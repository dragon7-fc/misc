1338. Reduce Array Size to The Half

Given an array `arr`.  You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that **at least** half of the integers of the array are removed.

 

**Example 1:**
```
Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has size greater than half of the size of the old array.
```

**Example 2:**
```
Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.
```

**Example 3:**
```
Input: arr = [1,9]
Output: 1
```

**Example 4:**
```
Input: arr = [1000,1000,3,7]
Output: 1
```

**Example 5:**
```
Input: arr = [1,2,3,4,5,6,7,8,9,10]
Output: 5
```

**Constraints:**

* `1 <= arr.length <= 10^5`
* `arr.length` is even.
* `1 <= arr[i] <= 10^5`

# Submissions
---
**Solution 1: (Greedy, Sort)**
```
Runtime: 580 ms
Memory Usage: 36.7 MB
```
```python
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        N = len(arr)
        cnt = collections.Counter(arr)
        ans = cur = 0
        for _, c in cnt.most_common():
            if cur < N//2:
                cur += c
                ans += 1
            else:
                break
        return ans
```

**Solution 2: (Heap)**
```
Runtime: 258 ms
Memory Usage: 78.4 MB
```
```c++
class Solution {
public:
    int minSetSize(vector<int>& arr) {
        unordered_map<int,int>h;
        for(int i = 0; i < arr.size(); i++) h[arr[i]]++;
        priority_queue<int> pq;
        for(auto it: h) pq.push(it.second);
        int ans = 0, minus = 0;
        while(!pq.empty())
        {
            ans++;
            minus += pq.top();
            pq.pop();
            if(minus >= (arr.size()/2)) break;
        }
        return ans;
    }
};
```
