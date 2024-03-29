1423. Maximum Points You Can Obtain from Cards

here are several cards **arranged in a row**, and each card has an associated number of points The points are given in the integer array `cardPoints`.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly `k` cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array `cardPoints` and the integer `k`, return the maximum score you can obtain.

 

**Example 1:**
```
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
```

**Example 2:**
```
Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
```

**Example 3:**
```
Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
```

**Example 4:**
```
Input: cardPoints = [1,1000,1], k = 1
Output: 1
Explanation: You cannot take the card in the middle. Your best score is 1. 
```

**Example 5:**
```
Input: cardPoints = [1,79,80,1,1,1,200,1], k = 3
Output: 202
```

**Constraints:**

* `1 <= cardPoints.length <= 10^5`
* `1 <= cardPoints[i] <= 10^4`
* `1 <= k <= cardPoints.length`

# Submissions
---
**Solution 1: (DP Top-Down, Time Limit Exceeded)**
```python
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints)
        
        @functools.lru_cache(None)
        def dp(i, j):
            s = N-1-j + i-0
            if s == k:
                return 0
            return max(cardPoints[i] + dp(i+1, j), cardPoints[j] + dp(i, j-1))
        
        return dp(0, N-1)
```


**Solution 2: (Sliding Window)**

Problem Translation: Find the smallest subarray sum of length `len(cardPoints) - k`

```
Runtime: 864 ms
Memory Usage: 27 MB
```
```python
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints) - k
        minSubArraySum = float('inf')
        i = curr = 0
        
        for j, v in enumerate(cardPoints):
            curr += v
            if j - i + 1 > size:
                curr -= cardPoints[i]
                i += 1
            if j - i + 1 == size:    
                minSubArraySum = min(minSubArraySum, curr)

        return sum(cardPoints) - minSubArraySum
```

**Solution 3: (Sliding Window)**
```
Runtime: 740 ms
Memory Usage: 27 MB
```
```python
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans = win = 0
        for i in range(-k, k):
            win += cardPoints[i]
            if i >= 0:
                win -= cardPoints[i - k]
            ans = max(win, ans)    
        return ans
```

**Solution 4: (DP Bottom-Up, Sliding Window)**
```
Runtime: 592 ms
Memory Usage: 26.6 MB
```
```python
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        dp = [0 for _ in range(k+1)]
        dp[0] = sum(cardPoints[-k:])
        for i in range(1, k+1):
            dp[i] = dp[i-1] + cardPoints[i-1] - cardPoints[-k+i-1]
        return max(dp)
```

**Solution 5: (Sliding Window)**
```
Runtime: 400 ms
Memory Usage: 27.6 MB
```
```python
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints)
        s = sum(cardPoints)
        min_ = cur = sum(cardPoints[:N-k])
        i = 0
        for j in range(N-k, N):
            cur += cardPoints[j]
            cur -= cardPoints[i]
            min_ = min(min_, cur)
            i += 1
        return s - min_
```

**Solution 6: (Sliding Window)**
```
Runtime: 76 ms
Memory Usage: 42.3 MB
```
```c++
class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int sum = accumulate(cardPoints.begin(), cardPoints.end(), 0);
        
        int ans = 0;
        int n = cardPoints.size();
        int windowSize = n - k;
        int L = 0;
        int R = 0;
        int windowSum = 0;
        
        while(R < n) {
            int right = cardPoints[R++];
            windowSum += right;
            while(R - L > windowSize) {
                int left = cardPoints[L++];
                windowSum -= left;
            }
            if(R-L == windowSize) {
                ans = max(ans, (int)(sum - windowSum));
            }
        }
        return ans;
    }
};
```
