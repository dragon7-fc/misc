2059. Minimum Operations to Convert Number

You are given a **0-indexed** integer array `nums` containing **distinct** numbers, an integer `start`, and an integer `goal`. There is an integer `x` that is initially set to `start`, and you want to perform operations on `x` such that it is converted to `goal`. You can perform the following operation repeatedly on the number `x`:

If `0 <= x <= 1000`, then for any index `i` in the array (`0 <= i < nums.length`), you can set `x` to any of the following:

* x + nums[i]
* x - nums[i]
* x ^ nums[i] (bitwise-XOR)

Note that you can use each `nums[i]` any number of times in any order. Operations that set `x` to be out of the range `0 <= x <= 1000` are valid, but no more operations can be done afterward.

Return the **minimum** number of operations needed to convert `x = start` into `goal`, and `-1` if it is not possible.

 

**Example 1:**
```
Input: nums = [1,3], start = 6, goal = 4
Output: 2
Explanation:
We can go from 6 → 7 → 4 with the following 2 operations.
- 6 ^ 1 = 7
- 7 ^ 3 = 4
```

**Example 2:**
```
Input: nums = [2,4,12], start = 2, goal = 12
Output: 2
Explanation:
We can go from 2 → 14 → 12 with the following 2 operations.
- 2 + 12 = 14
- 14 - 2 = 12
```

**Example 3:**
```
Input: nums = [3,5,7], start = 0, goal = -4
Output: 2
Explanation:
We can go from 0 → 3 → -4 with the following 2 operations. 
- 0 + 3 = 3
- 3 - 7 = -4
Note that the last operation sets x out of the range 0 <= x <= 1000, which is valid.
```

**Example 4:**
```
Input: nums = [2,8,16], start = 0, goal = 1
Output: -1
Explanation:
There is no way to convert 0 into 1.
```

**Example 5:**
```
Input: nums = [1], start = 0, goal = 3
Output: 3
Explanation: 
We can go from 0 → 1 → 2 → 3 with the following 3 operations. 
- 0 + 1 = 1 
- 1 + 1 = 2
- 2 + 1 = 3
```

**Constraints:**

* `1 <= nums.length <= 1000`
* `-10^9 <= nums[i], goal <= 10^9`
* `0 <= start <= 1000`
* `start != goal`
* All the integers in `nums` are **distinct**.

# Submissions
---
**Solution 1: (BFS)**
```
Runtime: 4552 ms
Memory Usage: 97.2 MB
```
```python
class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        seen = set()
        q = collections.deque([start])
        ans = 0
        while q:
            for _ in range(len(q)):
                x = q.popleft()
                if x == goal:
                    return ans
                if x in seen or x < 0 or x > 1000:
                    continue
                seen.add(x)
                for num in nums:
                    q += [x+num]
                    q += [x-num]
                    q += [x^num]
            ans += 1
            
        return -1
```

**Solution 2: (BFS)**
```
Runtime: 456 ms
Memory Usage: 133.8 MB
```
```c++
class Solution {
public:
    int minimumOperations(vector<int>& nums, int start, int goal) {
        vector<bool>visited(1001,false);
        int ans=0;
        queue<int>q;
        q.push(start);
        while(!q.empty()){
            int size=q.size();
            while(size--){
                int node=q.front();q.pop();
                if(node==goal)
                    return ans;
                if(node>1000 || node<0 || visited[node])
                    continue;
                visited[node]=true;
                for(int i=0;i<nums.size();i++){
                    int a=node+nums[i],b=node-nums[i],c=node^nums[i];
                    for(auto j :{a,b,c})
                            q.push(j);
                }
            }
            ans++;
        }
        return -1;
    }
};
```
