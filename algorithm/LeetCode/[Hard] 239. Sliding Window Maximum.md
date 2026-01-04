239. Sliding Window Maximum

Given an array `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

**Example:**
```
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

**Note:**

* You may assume `k` is always valid, `1 ≤ k ≤ input array's size` for non-empty array.

**Follow up:**

* Could you solve it in linear time?

# Submissions
---
**Solution 1: (Sliding Window)**
```
Runtime: 9784 ms
Memory Usage: 30.7 MB
```
```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        num_cur = nums[:k]
        ans = [max(num_cur)]
        for i, v in enumerate(nums[k:]):
            num_cur += [v]
            if ans[-1] != num_cur.pop(0) and k > 1:
                ans += max(ans[-1], v),                
            else:                
                ans += [max(num_cur)]
        return ans
```

**Solution 2: (Decreasing deque index)**
```
Runtime: 1552 ms
Memory Usage: 30.5 MB
```
```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq, n, ans = deque([0]), len(nums), []

        for i in range (n):
            while deq and deq[0] <= i - k:
                deq.popleft()
            while deq and nums[i] >= nums[deq[-1]] :
                deq.pop()
            deq.append(i)
            
            ans.append(nums[deq[0]])
            
        return ans[k-1:]
```

**Solution 3: (Heap)**
```
Runtime: 253 ms
Memory: 144.1 MB
```
```c++
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n=nums.size();
        priority_queue<pair<int, int>> pq;

        vector<int> ans(n-k+1);
        for (int i=0; i<k; i++)
            pq.push({nums[i], i});
        
        ans[0]=pq.top().first;
        for(int i=k; i<n; i++){
            while(!pq.empty() && pq.top().second<=(i-k))
                pq.pop(); //Pop up element not in the window
            pq.push({nums[i], i});
            ans[i-k+1]=pq.top().first;//Max element for this window
        }
        return ans;
    }
};
```

**Solution 4: (Hash Table, Sort, Counter)**
```
Runtime: 331 ms, Beats 9.30%
Memory: 175.11 MB, Beats 9.53%
```
```c++
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size(), i, j = 0;
        vector<int> ans(n-k+1);
        map<int,int> cnt;
        for (i = 0; i < n; i ++) {
            cnt[nums[i]] += 1;
            if (i >= k-1) {
                ans[j] = cnt.rbegin()->first;
                j += 1;
                cnt[nums[i-k+1]] -= 1;
                if (cnt[nums[i-k+1]] == 0) {
                    cnt.erase(nums[i-k+1]);
                }
            }
        }
        return ans;
    }
};
```

**Solution 5: (Deque)**

    nums = [  1,  3, -1, -3,  5,  3,  6,  7], k = 3
dq            1
                  3
                      3,-1
                           3,-1,-3
                              5
                                  5,3
                                      6
                                          7
ans                   3   3   5   5   6   7

```
Runtime: 33 ms, Beats 30.91%
Memory: 139.13 MB, Beats 60.18%
```
```c++
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size(), i;
        deque<int> dq;
        vector<int> ans;
        for (i = 0; i < n; i ++) {
            while (dq.size() && nums[i] >= nums[dq.back()]) {
                dq.pop_back();
            }
            dq.push_back(i);
            if (i >= k-1) {
                while (i - dq.front() >= k) {
                    dq.pop_front();
                }
                ans.push_back(nums[dq.front()]);
            }
        }
        return ans;
    }
};
````
