3629. Minimum Jumps to Reach End via Prime Teleportation

You are given an integer array `nums` of length `n`.

You start at index 0, and your goal is to reach index `n - 1`.

From any index `i`, you may perform one of the following operations:

* **Adjacent Step**: Jump to index `i + 1` or `i - 1`, if the index is within bounds.
* **Prime Teleportation**: If `nums[i]` is a prime number p, you may instantly jump to any index `j != i` such that `nums[j] % p == 0`.

Return the **minimum** number of jumps required to reach index `n - 1`.

 

**Example 1:**
```
Input: nums = [1,2,4,6]

Output: 2

Explanation:

One optimal sequence of jumps is:

Start at index i = 0. Take an adjacent step to index 1.
At index i = 1, nums[1] = 2 is a prime number. Therefore, we teleport to index i = 3 as nums[3] = 6 is divisible by 2.
Thus, the answer is 2.
```

**Example 2:**
```
Input: nums = [2,3,4,7,9]

Output: 2

Explanation:

One optimal sequence of jumps is:

Start at index i = 0. Take an adjacent step to index i = 1.
At index i = 1, nums[1] = 3 is a prime number. Therefore, we teleport to index i = 4 since nums[4] = 9 is divisible by 3.
Thus, the answer is 2.
```

**Example 3:**
```
Input: nums = [4,6,5,8]

Output: 3

Explanation:

Since no teleportation is possible, we move through 0 → 1 → 2 → 3. Thus, the answer is 3.
```

**Constraints:**

* `1 <= n == nums.length <= 10^5`
* `1 <= nums[i] <= 10^6`

# Submissions
---
**Solution 1: (Math, BFS)**
```
Runtime: 1155 ms, Beats 30.64%
Memory: 371.54 MB, Beats 24.13%
```
```c++
class Solution {
    vector<int>factor(int x){
        vector<int>res;
        for(int d=2;d*d<=x;d++){
            if(x%d==0){
                res.push_back(d);
                while(x%d==0)x/=d;
            }
        }
        if(x>1)res.push_back(x);
        return res;
    }
public:
    int minJumps(vector<int>& nums) {
        unordered_map<int,vector<int>>adj;
        int n=nums.size(), ans = INT_MAX;
        for(int i=0;i<n;i++){
            vector<int>temp=factor(nums[i]);
            for(int it:temp)adj[it].push_back(i);
        }
        // vector<int>vis(n,0);
        queue<pair<int,int>>q;
        vector<int> visited(n);
        q.push({0,0});
        visited[0] = 1;
        while(!q.empty()){
            auto [dis,node]=q.front();
            q.pop();
            if (node == n-1) {
                ans = min(ans, dis);
                continue;
            }

            if(node+1<n && !visited[node+1]){
                visited[node+1] = 1;
                q.push({dis + 1, node+1});
            }
            if(node-1>=0 && !visited[node-1]){
                visited[node-1]=1;
                q.push({dis + 1, node-1});
            }
            for(auto it:adj[nums[node]]){
                if (!visited[it]){
                    visited[it] = 1;
                    q.push({dis + 1, it});
                }
            }
            adj[nums[node]].clear(); 
        }
        return ans;
    }
};
```
