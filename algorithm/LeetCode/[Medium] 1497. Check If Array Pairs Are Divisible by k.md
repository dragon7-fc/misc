1497. Check If Array Pairs Are Divisible by k

Given an array of integers `arr` of even length `n` and an integer `k`.

We want to divide the array into exactly `n / 2` pairs such that the sum of each pair is divisible by `k`.

Return `True` If you can find a way to do that or `False` otherwise.

 

**Example 1:**
```
Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
```

**Example 2:**
```
Input: arr = [1,2,3,4,5,6], k = 7
Output: true
Explanation: Pairs are (1,6),(2,5) and(3,4).
```

**Example 3:**
```
Input: arr = [1,2,3,4,5,6], k = 10
Output: false
Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.
```

**Example 4:**
```
Input: arr = [-10,10], k = 2
Output: true
```

**Example 5:**
```
Input: arr = [-1,1,-2,2,-3,3,-4,4], k = 3
Output: true
```

**Constraints:**

* `arr.length == n`
* `1 <= n <= 10^5`
* `n is even`.
* `-10^9 <= arr[i] <= 10^9`
* `1 <= k <= 10^5`

# Submissions
---
**Solution 1: (Hash Table)**
```
Runtime: 1032 ms
Memory Usage: 27.9 MB
```
```python
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt = [0] * k
        for a in arr:
            a = (a % k + k) % k
            theOther = (k - a) % k
            if cnt[theOther] > 0:
                cnt[theOther] -=  1
            else:
                cnt[a] += 1
        return all(c == 0 for c in cnt)
```

**Soluton 2: (Hash Table, counter)**
```
Runtime: 78 ms
Memory: 64.33 MB
```
```c++
class Solution {
public:
    bool canArrange(vector<int>& arr, int k) {
        vector<int> cnt(k);
        for (auto a: arr) {
            cnt[((a%k)+k)%k] += 1;
        }
        if (cnt[0]%2) {
            return false;
        }
        for (int i = 1; i < k-i; i ++) {
            if (cnt[i] != cnt[k-i]) {
                return false;
            }
        }
        return true;
    }
};
```
