2601. Prime Subtraction Operation

You are given a **0-indexed** integer array `nums` of length `n`.

You can perform the following operation as many times as you want:

* Pick an index `i` that you haven’t picked before, and pick a prime `p` **strictly less than** `nums[i]`, then subtract `p` from `nums[i]`.

Return `true` if you can make nums a strictly increasing array using the above operation and false otherwise.

A **strictly increasing array** is an array whose each element is strictly greater than its preceding element.

 

**Example 1:**
```
Input: nums = [4,9,6,10]
Output: true
Explanation: In the first operation: Pick i = 0 and p = 3, and then subtract 3 from nums[0], so that nums becomes [1,9,6,10].
In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes equal to [1,2,6,10].
After the second operation, nums is sorted in strictly increasing order, so the answer is true.
```

**Example 2:**
```
Input: nums = [6,8,11,12]
Output: true
Explanation: Initially nums is sorted in strictly increasing order, so we don't need to make any operations.
```

**Example 3:**
```
Input: nums = [5,8,3]
Output: false
Explanation: It can be proven that there is no way to perform operations to make nums sorted in strictly increasing order, so the answer is false.
```

**Constraints:**

* `1 <= nums.length <= 1000`
* `1 <= nums[i] <= 1000`
* `nums.length == n`

# Submissions
---
**Solution 1: (Greedy, Math)**
```
Runtime: 632 ms
Memory: 13.9 MB
```
```python
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        ps = [2]
        for i in range(3, 1001):
            j = 2
            while j * j <= i:
                if i % j == 0:
                    break
                j += 1
            if i % j == 0:
                continue
            ps.append(i)
        for j, n in enumerate(nums):
            ok = False
            for i in range(bisect_left(ps, n), -1, -1):
                if i >= len(ps) or ps[i] >= n:
                    continue
                if j == 0 and nums[j] > ps[i]:
                    nums[j] -= ps[i]
                    ok = True
                    break
                else:
                    if nums[j] - ps[i] > nums[j-1]:
                        nums[j] -= ps[i]
                        ok = True
                        break
            if j > 0:
                if nums[j] <= nums[j-1]:
                    return False
        return True
```

**Solution 2: (Greedy, Math, Brute Force)**
```
Runtime: 142 ms
Memory: 23.6 MB
```
```c++
class Solution {
    bool isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
public:
    bool primeSubOperation(vector<int>& nums) {
        int n = nums.size(), prev = -1; 
        for(int i = 0; i < n; i++) {
            if (nums[i] <= prev) return false;
            bool found = false;
            for (int curr = nums[i]-1; curr>1; curr--) {
                if (isPrime(curr))
                {
                    if (prev >= nums[i]-curr) {
                        continue;
                    }
                    prev = nums[i] - curr;
                    found = true;
                    break;
                }
            }
            if (!found) {
                if(nums[i] > prev) {
                    prev = nums[i];
                } else {
                    return false;
                }
            }
        }
        return true;
    }
};
```

**Solution 3: (Greedy, Brute Force)**
```
Runtime: 15 ms
Memory: 30.34 MB
```
```c++
class Solution {
public:
    bool primeSubOperation(vector<int>& nums) {
        int n = nums.size(), i, j, pre, cur;
        vector<int> dp(1001, 1);
        for (i = 2; i <= 1000; i ++) {
            j = 2;
            while (j <= sqrt(i)) {
                if (i%j == 0) {
                    dp[i] = 0;
                    break;
                }
                j += 1;
            }
        }
        pre = nums[n-1];
        for (i = n - 2; i >= 0; i --) {
            cur = nums[i];
            if (cur >= pre) {
                j = 2;
                while (j < cur) {
                    if (dp[j] && cur - j < pre) {
                        cur -= j;
                        break;
                    }
                    j += 1;
                }
            }
            if (cur >= pre) {
                return false;
            }
            pre = cur;
        }
        return true;
    }
};
```

**Solution 4: (Greedy, Storing the primes, O(n + m sqrt(m)))**
```
Runtime: 10 ms
Memory: 28.53 MB
```
```c++
class Solution {
    bool checkPrime(int x) {
        for (int i = 2; i <= sqrt(x); i++) {
            if (x % i == 0) {
                return 0;
            }
        }
        return 1;
    }
public:
    bool primeSubOperation(vector<int>& nums) {
        int maxElement = *max_element(nums.begin(), nums.end());

        // Store the previousPrime array.
        vector<int> previousPrime(maxElement + 1, 0);
        for (int i = 2; i <= maxElement; i++) {
            if (checkPrime(i)) {
                previousPrime[i] = i;
            } else {
                previousPrime[i] = previousPrime[i - 1];
            }
        }

        for (int i = 0; i < nums.size(); i++) {
            int bound;
            // In case of first index, we need to find the largest prime less
            // than nums[0].
            if (i == 0) {
                bound = nums[0];
            } else {
                // Otherwise, we need to find the largest prime, that makes the
                // current element closest to the previous element.
                bound = nums[i] - nums[i - 1];
            }

            // If the bound is less than or equal to 0, then the array cannot be
            // made strictly increasing.
            if (bound <= 0) {
                return 0;
            }

            // Find the largest prime less than bound.
            int largestPrime = previousPrime[bound - 1];

            // Subtract this value from nums[i].
            nums[i] = nums[i] - largestPrime;
        }
        return 1;
    }
};
```

**Solution 5: (Sieve of Eratosthenes + Two Pointers, O(n + m log log(m)))**
```
Runtime: 3 ms
Memory: 28.74 MB
```
```c++
class Solution {
public:
    bool primeSubOperation(vector<int>& nums) {
        int maxElement = *max_element(nums.begin(), nums.end());

        // Store the sieve array.
        vector<int> sieve(maxElement + 1, 1);
        sieve[1] = 0;
        for (int i = 2; i <= sqrt(maxElement + 1); i++) {
            if (sieve[i] == 1) {
                for (int j = i * i; j <= maxElement; j += i) {
                    sieve[j] = 0;
                }
            }
        }

        // Start by storing the currValue as 1, and the initial index as 0.
        int currValue = 1;
        int i = 0;
        while (i < nums.size()) {
            // Store the difference needed to make nums[i] equal to currValue.
            int difference = nums[i] - currValue;

            // If difference is less than 0, then nums[i] is already less than
            // currValue. Return false in this case.
            if (difference < 0) {
                return 0;
            }

            // If the difference is prime or zero, then nums[i] can be made
            // equal to currValue.
            if (sieve[difference] == 1 or difference == 0) {
                i++;
                currValue++;
            } else {
                // Otherwise, try for the next currValue.
                currValue++;
            }
        }
        return 1;
    }
};
```
