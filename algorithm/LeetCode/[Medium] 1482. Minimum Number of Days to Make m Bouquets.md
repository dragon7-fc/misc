1482. Minimum Number of Days to Make m Bouquets

Given an integer array `bloomDay`, an integer `m` and an integer `k`.

We need to make `m` bouquets. To make a bouquet, you need to use `k` **adjacent flowers** from the garden.

The garden consists of `n` flowers, the `i`th flower will bloom in the `bloomDay[i]` and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make `m` bouquets from the garden. If it is impossible to make m bouquets return `-1`.

 

**Example 1:**
```
Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let's see what happened in the first three days. x means flower bloomed and _ means flower didn't bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
```

**Example 2:**
```
Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.
```

**Example 3:**
```
Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
Explanation: We need 2 bouquets each should have 3 flowers.
Here's the garden after the 7 and 12 days:
After day 7: [x, x, x, x, _, x, x]
We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
After day 12: [x, x, x, x, x, x, x]
It is obvious that we can make two bouquets in different ways.
```

**Example 4:**
```
Input: bloomDay = [1000000000,1000000000], m = 1, k = 1
Output: 1000000000
Explanation: You need to wait 1000000000 days to have a flower ready for a bouquet.
```

**Example 5:**
```
Input: bloomDay = [1,10,2,9,3,8,4,7,5,6], m = 4, k = 2
Output: 9
```

**Constraints:**

* `bloomDay.length == n`
* `1 <= n <= 10^5`
* `1 <= bloomDay[i] <= 10^9`
* `1 <= m <= 10^6`
* `1 <= k <= n`

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 1468 ms
Memory Usage: 26.8 MB
```
```python
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay): return -1
        left, right = 1, max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            flow = bouq = 0
            for a in bloomDay:
                flow = 0 if a > mid else flow + 1
                if flow >= k:
                    flow = 0
                    bouq += 1
                    if bouq == m: break
            if bouq == m:
                right = mid
            else:
                left = mid + 1
        return left
```

**Solution 2: (Binary Search, sliding window)**
```
Runtime: 107 ms
Memory: 68.92 MB
```
```c++
class Solution {
    bool check(int mid, vector<int> &bloomDay, int m, int k) {
        int b = 0, i = 0, j = 0, n = bloomDay.size(), cnt = 0;
        while (j < n) {
            if (bloomDay[j] <= mid) {
                i = j;
                while (j+1 < n && bloomDay[j+1] <= mid && (j-i+1) < k) {
                    j += 1;
                }
                if (j-i+1 == k) {
                    cnt += 1;
                }
            }
            j += 1;
        }
        return cnt >= m;
    }
public:
    int minDays(vector<int>& bloomDay, int m, int k) {
        if (bloomDay.size() < (long long)m*k) {
            return -1;
        }
        int lo = *min_element(bloomDay.begin(), bloomDay.end()), hi = *max_element(bloomDay.begin(), bloomDay.end()), mid;
        while (lo < hi) {
            mid = lo + (hi-lo)/2;
            if (!check(mid, bloomDay, m, k)) {
                lo = mid+1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
};
```
**Solution 3: (Binary Search, greedy)**
```
Runtime: 118 ms
Memory: 68.97 MB
```
```c++
class Solution {
    // Return the number of maximum bouquets that can be made on day mid.
    int getNumOfBouquets(vector<int>& bloomDay, int mid, int k) {
        int numOfBouquets = 0;

        int count = 0;
        for (int i = 0; i < bloomDay.size(); i++) {
            // If the flower is bloomed, add to the set. Else reset the count.
            if (bloomDay[i] <= mid) {
                count++;
            } else {
                count = 0;
            }

            if (count == k) {
                numOfBouquets++;
                count = 0;
            }
        }

        return numOfBouquets;
    }
public:
    int minDays(vector<int>& bloomDay, int m, int k) {
        int start = 0;
        int end = 0;
        for (int day : bloomDay) {
            end = max(end, day);
        }

        int minDays = -1;
        while (start <= end) {
            int mid = (start + end) / 2;

            if (getNumOfBouquets(bloomDay, mid, k) >= m) {
                minDays = mid;
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }

        return minDays;
    }
};
```
