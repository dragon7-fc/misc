2107. Number of Unique Flavors After Sharing K Candies

You are given a **0-indexed** integer array `candies`, where `candies[i]` represents the flavor of the `i`th candy. Your mom wants you to share these candies with your little sister by giving her `k` **consecutive** candies, but you want to keep as many flavors of candies as possible.

Return the **maximum** number of **unique** flavors of candy you can keep after sharing with your sister.

 

**Example 1:**
```
Input: candies = [1,2,2,3,4,3], k = 3
Output: 3
Explanation: 
Give the candies in the range [1, 3] (inclusive) with flavors [2,2,3].
You can eat candies with flavors [1,4,3].
There are 3 unique flavors, so return 3.
```

**Example 2:**
```
Input: candies = [2,2,2,2,3,3], k = 2
Output: 2
Explanation: 
Give the candies in the range [3, 4] (inclusive) with flavors [2,3].
You can eat candies with flavors [2,2,2,3].
There are 2 unique flavors, so return 2.
Note that you can also share the candies with flavors [2,2] and eat the candies with flavors [2,2,3,3].
```

**Example 3:**
```
Input: candies = [2,4,5], k = 0
Output: 3
Explanation: 
You do not have to give any candies.
You can eat the candies with flavors [2,4,5].
There are 3 unique flavors, so return 3.
```

**Constraints:**

* `1 <= candies.length <= 10^5`
* `1 <= candies[i] <= 10^5`
* `0 <= k <= candies.length`

# Submissions
---
**Solution 1: (Sliding Window)**
```
Runtime: 817 ms
Memory Usage: 38.8 MB
```
```python
class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        dct=collections.Counter(candies[k:])
        res=len(dct)
        for i in range(k,len(candies)):
            dct[candies[i]]-=1
            if dct[candies[i]]==0: del dct[candies[i]]
            dct[candies[i-k]]+=1
            res=max(res,len(dct))   
        return res
```

**Solution 2: (Sliding Window)**
```
Runtime: 252 ms
Memory Usage: 69.2 MB
```
```c++
class Solution {
public:
    int shareCandies(vector<int>& candies, int k) {
        unordered_map<int, int> cnt;
        int ans = 0;
        for (int n : candies) cnt[n]++;
        for (int i = 0, N = candies.size(); i < N; ++i) { // Give out candies in window `[i-k+1, i]`
            cnt[candies[i]]--; // Give out `A[i]`
            if (i - k >= 0) cnt[candies[i - k]]++; // Reclaim `A[i-k]`
            if (cnt[candies[i]] == 0) cnt.erase(candies[i]);
            if (i >= k - 1) ans = max(ans, (int)cnt.size()); // Take the maximum possible unique flavors left after giving out.
        }
        return ans;
    }
};
```
