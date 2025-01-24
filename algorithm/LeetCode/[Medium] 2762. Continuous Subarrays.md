2762. Continuous Subarrays

You are given a **0-indexed** integer array `nums`. A subarray of nums is called **continuous** if:

* Let `i`, `i + 1`, ..., `j` be the indices in the subarray. Then, for each pair of indices `i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2`.

Return the total number of **continuous** subarrays.

A subarray is a contiguous **non-empty** sequence of elements within an array.

 

**Example 1:**
```
Input: nums = [5,4,2,4]
Output: 8
Explanation: 
Continuous subarray of size 1: [5], [4], [2], [4].
Continuous subarray of size 2: [5,4], [4,2], [2,4].
Continuous subarray of size 3: [4,2,4].
Thereare no subarrys of size 4.
Total continuous subarrays = 4 + 3 + 1 = 8.
It can be shown that there are no more continuous subarrays.
```

**Example 2:**
```
Input: nums = [1,2,3]
Output: 6
Explanation: 
Continuous subarray of size 1: [1], [2], [3].
Continuous subarray of size 2: [1,2], [2,3].
Continuous subarray of size 3: [1,2,3].
Total continuous subarrays = 3 + 2 + 1 = 6.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (multiset)**
```
Runtime: 410 ms
Memory: 149.8 MB
```
```c++
class Solution {
public:
    long long continuousSubarrays(vector<int>& nums) {
        long long ans = 0;
        int l = 0,r = 0;
        int n = nums.size();
        
        multiset<int> st;
        while(l<n){
            
            while(r<n){
                if(st.size()==0){
                    st.insert(nums[r]);
                    r++;
                }
                else{
                    int mn = *st.begin();    
                    int mx = *st.rbegin();
                
                    mn = min(mn,nums[r]);
                    mx = max(mx,nums[r]);
                    if(mx-mn>2)break;
                    st.insert(nums[r]);
                    r++;
                }
            }
          
            long long len = r-l;
            ans+=len;
            st.erase(st.find(nums[l]));
            l++;
        }
        return ans;
    }
};
```

**Solution 2: (min heap and max heap)**
```
Runtime: 399 ms
Memory: 122.6 MB
```
```c++
class Solution {
public:
    long long continuousSubarrays(vector<int>& nums) {
        int n = nums.size();
        priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>>s;
        priority_queue<pair<int,int>>b;
        long long ans = n;
        int i = 0, j = 0;
        while (j < n) {
            int i1 = i;
            if(i == j)
            {
                s.push({nums[i],i});
                b.push({nums[i],i});
                j++;
                continue;
            }
            if (abs(nums[j]-s.top().first) <= 2 && abs(nums[j]-b.top().first) <= 2)
            {   
                ans = ans+j-i;
                s.push({nums[j],j});
                b.push({nums[j],j});
                j++;
            }
            else
            {
                while (!s.empty() &&  (abs(s.top().first-nums[j])>2 || s.top().second<=i)) {
                    i1=max(i1,s.top().second+1);
                    s.pop();
                }
                while(!b.empty() &&  (abs(b.top().first-nums[j])>2 || b.top().second<=i))
                {   
                    i1=max(i1,b.top().second+1);
                    b.pop();
                }
                i=i1;
            }
        }
        return ans;
    }
};
```

**Solution 3: (Hasp Table, Sliding Window, counter, sorted map)**
```
Runtime: 92 ms
Memory: 112.99 MB
```
```c++
class Solution {
public:
    long long continuousSubarrays(vector<int>& nums) {
        int n = nums.size(), i = 0, j;
        long long ans = 0;
        map<int,int> cnt;
        for (int j = 0; j < n; j ++) {
            cnt[nums[j]] += 1;
            while (nums[j] - cnt.begin()->first > 2) {
                cnt[nums[i]] -= 1;
                if (cnt[nums[i]] == 0) {
                    cnt.erase(nums[i]);
                }
                i += 1;
            }
            while (cnt.rbegin()->first - nums[j] > 2) {
                cnt[nums[i]] -= 1;
                if (cnt[nums[i]] == 0) {
                    cnt.erase(nums[i]);
                }
                i += 1;
            }
            ans += j - i + 1;
        }
        return ans;
    }
};
```

**Solution 4: (Monotonic Deque)**
```
Runtime: 102 ms
Memory: 121.40 MB
```
```c++
class Solution {
public:
    long long continuousSubarrays(vector<int>& nums) {
        // Monotonic deque to track maximum and minimum elements
        deque<int> maxQ, minQ;
        int left = 0;
        long long count = 0;

        for (int right = 0; right < nums.size(); right++) {
            // Maintain decreasing monotonic deque for maximum values
            while (!maxQ.empty() && nums[maxQ.back()] < nums[right]) {
                maxQ.pop_back();
            }
            maxQ.push_back(right);

            // Maintain increasing monotonic deque for minimum values
            while (!minQ.empty() && nums[minQ.back()] > nums[right]) {
                minQ.pop_back();
            }
            minQ.push_back(right);

            // Shrink window if max-min difference exceeds 2
            while (!maxQ.empty() && !minQ.empty() &&
                   nums[maxQ.front()] - nums[minQ.front()] > 2) {
                // Move left pointer past the element that breaks the condition
                if (maxQ.front() < minQ.front()) {
                    left = maxQ.front() + 1;
                    maxQ.pop_front();
                } else {
                    left = minQ.front() + 1;
                    minQ.pop_front();
                }
            }

            // Add count of all valid subarrays ending at current right pointer
            count += right - left + 1;
        }
        return count;
    }
};
```

**Solution 5: (Optimized Two Pointer)**
```
Runtime: 78 ms
Memory: 111.80 MB
```
```c++
class Solution {
public:
    long long continuousSubarrays(vector<int>& nums) {
        int right = 0, left = 0;
        int curMin, curMax;
        long long windowLen = 0, total = 0;

        // Initialize window with the first element
        curMin = curMax = nums[right];

        for (right = 0; right < nums.size(); right++) {
            // Update min and max for the current window
            curMin = min(curMin, nums[right]);
            curMax = max(curMax, nums[right]);

            // If window condition breaks (diff > 2)
            if (curMax - curMin > 2) {
                // Add subarrays from the previous valid window
                windowLen = right - left;
                total += (windowLen * (windowLen + 1) / 2);

                // Start a new window at the current position
                left = right;
                curMin = curMax = nums[right];

                // Expand left boundary while maintaining the condition
                while (left > 0 && abs(nums[right] - nums[left - 1]) <= 2) {
                    left--;
                    curMin = min(curMin, nums[left]);
                    curMax = max(curMax, nums[left]);
                }

                // Remove overcounted subarrays if left boundary expanded
                if (left < right) {
                    windowLen = right - left;
                    total -= (windowLen * (windowLen + 1) / 2);
                }
            }
        }

        // Add subarrays from the final window
        windowLen = right - left;
        total += (windowLen * (windowLen + 1) / 2);

        return total;
    }
};
```
