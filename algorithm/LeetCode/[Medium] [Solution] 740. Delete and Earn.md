740. Delete and Earn

Given an array `nums` of integers, you can perform operations on the array.

In each operation, you pick any `nums[i]` and delete it to earn `nums[i]` points. After, you must delete every element equal to `nums[i] - 1` or `nums[i] + 1`.

You start with `0` points. Return the maximum number of points you can earn by applying such operations.

**Example 1:**

```
Input: nums = [3, 4, 2]
Output: 6
Explanation: 
Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points. 6 total points are earned.
```

**Example 2:**

```
Input: nums = [2, 2, 3, 3, 3, 4]
Output: 9
Explanation: 
Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.
```

**Note:**

* The length of `nums` is at most `20000`.
* Each element `nums[i]` is an integer in the range `[1, 10000]`.

# Solution
---
## Approach #1: Dynamic Programming [Accepted]
**Intuition**

Because all numbers are positive, if we "take" a number (use it to score points), we might as well take all copies of it, since we've already erased all its neighbors. We could keep a count of each number so we know how many points taking a number is worth total.

Now let's investigate what happens when we add a new number `X` (plus copies) that is larger than all previous numbers. Naively, our answer would be the previous answer, plus the value of `X` - which can be solved with dynamic programming. However, this fails if our previous answer had a number taken that was adjacent to `X`.

Luckily, we can remedy this. Let's say we knew `using`, the value of our previous answer, and `avoid`, the value of our previous answer that doesn't use the previously largest value `prev`. Then we could compute new values of `using` and `avoid` appropriately.

**Algorithm**

For each unique value `k` of `nums` in increasing order, let's maintain the correct values of `avoid` and `using`, which represent the answer if we don't take or take `k` respectively.

If the new value `k` is adjacent to the previously largest value `prev`, then the answer if we must take `k` is (the point value of `k`) + `avoid`, while the answer if we must not take `k` is `max(avoid, using)`. Similarly, if `k` is not adjacent to `prev`, the answer if we must take `k` is (the point value of `k`) + `max(avoid, using)`, and the answer if we must not take `k` is `max(avoid, using)`.

At the end, the best answer may or may not use the largest value in `nums`, so we return `max(avoid, using)`.

Our demonstrated solutions showcase two different kinds of sorts: a library one, and a radix sort. For each language, the other kind of solution can be done without much difficulty, by using an array (Python) or HashMap (Java) respectively.

```python
class Solution(object):
    def deleteAndEarn(self, nums):
        count = collections.Counter(nums)
        prev = None
        avoid = using = 0
        for k in sorted(count):
            if k - 1 != prev:
                avoid, using = max(avoid, using), k * count[k] + max(avoid, using)
            else:
                avoid, using = max(avoid, using), k * count[k] + avoid
            prev = k
        return max(avoid, using)
```

**Complexity Analysis**

* Time Complexity: $O(N \log N)$, where $N$ is the length of nums. We make a single pass through the sorted keys of $N$, and the complexity is dominated by the sorting step.

* Space Complexity: $O(N)$, the size of our count.

# Submissions
---
**Solution: (Dynamic Programming Bottom-Up)**

```
Runtime: 68 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        prev = None
        avoid = using = 0
        for k in sorted(count):
            if k - 1 != prev:
                avoid, using = max(avoid, using), k * count[k] + max(avoid, using)
            else:
                avoid, using = max(avoid, using), k * count[k] + avoid
            prev = k
        return max(avoid, using)
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 60 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        scores = {k: k * n for k, n in Counter(nums).items()}
        if len(scores) == 1: 
            return list(scores.values()).pop()
        nums = sorted(scores.keys())
        # index 0 for `i - 2`, `i - 1` left boundary validity.
        dp = [0] * (len(nums) + 1)
        prev = None
        for i, k in enumerate(sorted(nums)):
            i += 1
            currScore = scores[nums[i - 1]]
            if prev is not None and k == prev + 1:
                dp[i] = max(
                    dp[i - 2] + currScore,      # case 1. Keep the score 
                    dp[i - 1])                  # case 2. Drop the score 
            else:
                dp[i] = dp[i - 1] + currScore   # happily keep the score
            prev = k
            
        return dp[-1]
```

**Solution 3: (DP Top-Down)**
```
Runtime: 52 ms
Memory Usage: 15.1 MB
```
```python
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        scores = {k: k * n for k, n in Counter(nums).items()}
        if len(scores) == 1: 
            return list(scores.values()).pop()
        nums = sorted(scores.keys())
        
        @functools.lru_cache(None)
        def dfs(j):
            if j < 0:
                return 0
            currScore = scores[nums[j]]
            if j == 0:
                return currScore
            elif nums[j] == nums[j - 1] + 1:
                return max(dfs(j - 2) + currScore, dfs(j - 1))
            else:
                return dfs(j - 1) + currScore

        return dfs(len(nums) - 1)
```

**Solution 4: (DP Bottom-Up)**
```
Runtime: 12 ms
Memory Usage: 13.9 MB
```
```c++
class Solution {
    unordered_map<int,int> cnt;
public:
    int deleteAndEarn(vector<int>& nums) {
        vector<int> freq(10001, 0);
		vector<int> dp(10001, 0);

		for (auto num : nums) freq[num]++;
		dp[1] = freq[1];

		for (int i=2; i<10001; i++)
            dp[i] = max(dp[i-2]+i*freq[i], dp[i-1]);

		return dp[10000];
    }
};
```

**Solution 5: (DP Bottom-Up)**

for numbers from [1 - 10000], each has a total sum sums[i]; if you earn sums[i], you cannot earn sums[i-1] and sums[i+1]
kind of like house robbing. you cannot rob 2 connected houses.

```
Runtime: 7 ms
Memory Usage: 11.5 MB
```
```c++
class Solution {
    unordered_map<int,int> cnt;
public:
    int deleteAndEarn(vector<int>& nums) {
        int n = 10001;
        vector<int> values(n, 0);
        for (int num : nums)
            values[num] += num;

        int pick = 0, leave = 0;
        for (int i = 0; i < n; i++) {
            int pickit = leave + values[i];
            int leaveit = max(pick, leave);
            pick = pickit;
            leave = leaveit;
        }
        return max(pick, leave);
    }
};
```

**Solution 6: (DP Bottom-Up)**
```
Runtime: 40 ms
Memory Usage: 11 MB
```
```c++
class Solution {
    unordered_map<int,int> cnt;
public:
    int deleteAndEarn(vector<int>& nums) {
        // a map to hold the frequency of a number (how often that frequency occurs)
        // the key being the number and the value being the frequency of that number
		map<int, int> freq; 
        
        // used to know when to end our loop, we don't need to check numbers past our max value                           
		// since they won't exist. A lot of solutions use arrays/vectors of size 10001, which                             
		// could potentially be unoptimal. If our max number is only 5, then we won't need to                            
		// calculate values for 6, 7... or 10000 for that matter. Although, if we did always loop 10001 times, it would still be 
		// considered O(1) loop time since it is constant and never changing.
		int maxNum = 0;
        
        // Populate our frequency map and find the largest number in the vector (array)
        for (int& num : nums)
        {
            freq[num]++;
            maxNum = max(maxNum, num);
        }
        
        // initialize a vector of our maximum number + 1, since we want to index up to the maximum number. If the max number is 10
		// we will want to have a vector of size 11 so we will have index 10. If we were to just use maxNum (10) as the size
		// then our array will go from 0 to 9, and in our loop we will miss a step. 
		vector<int> dp(maxNum + 1, 0); 
        
        // index 0 will always be 0 since our numbers only go from 1 to 10000
		dp[0] = 0; 
        
        // index 1 simply represents the frequency of 1, since 1 (the index) * (frequency of one) will always just 
		// be that frequency amount
		dp[1] = freq[1]; 
        
        // loop starting from 2 to the maximum number we found. 
        // for example: if the nums array is [3, 4, 2], with i = 2 (our first loop), we will look for whichever
        // is higher, freq[2] * 2 + dp[i-2] (basically 2 * how many times 2 occurs + the last value we took which         
		// is dp[i-2]) OR just the the previous value of dp[i-1] (which means we didn't take the index we're currently on). 
		// This problem is very similar to House Robber on leetcode, which is probably simpler to understand than this one.
        for (int i = 2; i <= maxNum; i++)
        {            
            dp[i] = max(freq[i] * i + dp[i-2], dp[i-1]);
        }
        
		// return the index of maxNum which will now contain the max points we could receive
        return dp[maxNum]; 
    }
};
```
