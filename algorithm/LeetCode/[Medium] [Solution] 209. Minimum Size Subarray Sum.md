209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer `s`, find the minimal length of a **contiguous subarray** of which the sum ≥ `s`. If there isn't one, return `0` instead.

**Example:**
```
input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
```

**Follow up:**

If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

# Solution
---
## Approach #1 Brute force [Time Limit Exceeded]
**Intuition**

Do as directed in question. Find the sum for all the possible subarrays and update the $\text{ans}$ as and when we get a better subarray that fulfill the requirements ($\text{sum} \geq \text{s}$).

**Algorithm**

* Initialize $\text{ans}=\text{INT_MAX}$
* Iterate the array from left to right using $i$
    * Iterate from the current element to the end of vector using $j$:
        * Find the $\text{sum}$ of elements from index $i$ to $j$
        * If sum is greater then $s$:
            * Update $\text{ans} = \min(\text{ans}, (j - i + 1))$
            * Start the next $i^{th}$ iteration, since, we got the smallest subarray with $\text{sum} \geq s$ starting from the current index.

```cpp
int minSubArrayLen(int s, vector<int>& nums)
{
    int n = nums.size();
    int ans = INT_MAX;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int sum = 0;
            for (int k = i; k <= j; k++) {
                sum += nums[k];
            }
            if (sum >= s) {
                ans = min(ans, (j - i + 1));
                break; //Found the smallest subarray with sum>=s starting with index i, hence move to next index
            }
        }
    }
    return (ans != INT_MAX) ? ans : 0;
}
```

**Complexity Analysis**

* Time complexity: $O(n^3)$.

For each element of array, we find all the subarrays starting from that index which is $O(n^2)$.
Time complexity to find the sum of each subarray is $O(n)$.
Thus, the total time complexity : $O(n^2 * n) = O(n^3)$

* Space complexity: $O(1)$ extra space.

## Approach #2 A better brute force [Accepted]
**Intuition**

In Approach #1, you may notice that the sum is calculated for every surarray in $O(n)$ time. But, we could easily find the sum in O(1) time by storing the cumulative sum from the beginning(Memoization). After we have stored the cumulative sum in $\text{sums}$, we could easily find the sum of any subarray from $i$ to $j$.

**Algorithm**
* The algorithm is similar to Approach #1.
* The only difference is in the way of finding the sum of subarrays:
    * Create a vector $\text{sums}$ of size of $\text{nums}$
    * Initialize $\text{sums}[0]=\text{nums}$
    * Iterate over the $\text{sums}$ vector:
        * Update $\text{sums}[i] = \text{sums}[i-1] + \text{nums}[i]$
    * Sum of subarray from $i$ to $j$ is calculated as: $\text{sum}=\text{sums}[j] - \text{sums}[i] +\text{nums}[i]$, wherein $\text{sums}[j] - \text{sums}[i]$ is the sum from $(i+1)^{th}$ element to the $j^{th}$ element.

```cpp
int minSubArrayLen(int s, vector<int>& nums)
{
    int n = nums.size();
    if (n == 0)
        return 0;
    int ans = INT_MAX;
    vector<int> sums(n);
    sums[0] = nums[0];
    for (int i = 1; i < n; i++)
        sums[i] = sums[i - 1] + nums[i];
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int sum = sums[j] - sums[i] + nums[i];
            if (sum >= s) {
                ans = min(ans, (j - i + 1));
                break; //Found the smallest subarray with sum>=s starting with index i, hence move to next index
            }
        }
    }
    return (ans != INT_MAX) ? ans : 0;
}
```

**Complexity analysis**

* Time complexity: $O(n^2)$.

Time complexity to find all the subarrays is $O(n^2)$.
Sum of the subarrays is calculated in $O(1)$ time.
Thus, the total time complexity: $O(n^2 * 1) = O(n^2)$

* Space complexity: $O(n)$ extra space.

Additional $O(n)$ space for $\text{sums}$ vector than in Approach #1.

## Approach #3 Using Binary search [Accepted]
**Intuition**

We could further improve the Approach #2 using the binary search. Notice that we find the subarray with $\text{sum} >=\text{s}$ starting with an index $i$ in $O(n)$ time. But, we could reduce the time to $O(\log(n))$ using binary search. Note that in Approach #2, we search for subarray starting with index $i$, until we find $\text{sum}=\text{sums}[j] - \text{sums}[i] +\text{nums}[i]$ that is greater than $\text{s}$. So, instead of iterating linearly to find the sum, we could use binary search to find the index that is not lower than $\text{s}-\text{sums[i]}$ in the $\text{sums}$, which can be done using $\text{lower_bound}$ function in C++ STL or could be implemented manually.

**Algorithm**

* Create vector $sums$ of size $n+1$ with : $\text{sums}[0]=0\text{, }\text{sums}[i]=\text{sums}[i-1]+\text{nums}[i-1]$
* Iterate from $i=1$ to $n$:
    * Find the value $\text{to_find}$ in $\text{sum}$ required for minimum subarray starting from index $i$ to have sum greater than $s$, that is: $\text{to_find}=\text{s}+\text{sums}[i-1]$
    * Find the index in $\text{sums}$ such that value at that index is not lower than the $\text{to_find}$ value, say $\text{bound}$
    * If we find the $\text{to_find}$ in $\text{sums}$, then:
        * Size of current subarray is given by: $\text{bound} - (\text{sums.begin}()+i-1)$
        * Compare $ans$ with the current subarray size and store minimum in $ans$

```cpp
int minSubArrayLen(int s, vector<int>& nums)
{
    int n = nums.size();
    if (n == 0)
        return 0;
    int ans = INT_MAX;
    vector<int> sums(n + 1, 0); //size = n+1 for easier calculations
    //sums[0]=0 : Meaning that it is the sum of first 0 elements
    //sums[1]=A[0] : Sum of first 1 elements
    //ans so on...
    for (int i = 1; i <= n; i++)
        sums[i] = sums[i - 1] + nums[i - 1];
    for (int i = 1; i <= n; i++) {
        int to_find = s + sums[i - 1];
        auto bound = lower_bound(sums.begin(), sums.end(), to_find);
        if (bound != sums.end()) {
            ans = min(ans, static_cast<int>(bound - (sums.begin() + i - 1)));
        }
    }
    return (ans != INT_MAX) ? ans : 0;
}
```
**Complexity analysis**

* Time complexity: $O(n\log(n))$.
For each element in the vector, find the subarray starting from that index, and having sum greater than $s$ using binary search. Hence, the time required is $O(n)$ for iteration over the vector and $O(\log(n))$ for finding the subarray for each index using binary search.
Therefore, total time complexity = $O(n*\log(n))$
* Space complexity: $O(n)$. Additional $O(n)$ space for $\text{sums}$ vector

## Approach #4 Using 2 pointers [Accepted]
**Intuition**

Until now, we have kept the starting index of subarray fixed, and found the last position. Instead, we could move the starting index of the current subarray as soon as we know that no better could be done with this index as the starting index. We could keep 2 pointer,one for the start and another for the end of the current subarray, and make optimal moves so as to keep the $\text{sum}$ greater than $s$ as well as maintain the lowest size possible.

Algorithm

* Initialize $\text{left}$ pointer to 0 and $\text{sum}$ to 0
* Iterate over the $\text{nums}$:
* Add $\text{nums}[i]$ to $\text{sum}$
    * While $\text{sum}$ is greater than or equal to $s$:
        * Update $\text{ans}=\min(\text{ans},i+1-\text{left}), where $i+1-\text{left}$ is the size of current subarray
        * It means that the first index can safely be incremented, since, the minimum subarray starting with this index with $\text{sum} \geq s$ has been achieved
        * Subtract $\text{nums[left]}$ from $\text{sum}$ and increment $\text{left}$

```cpp
int minSubArrayLen(int s, vector<int>& nums)
{
    int n = nums.size();
    int ans = INT_MAX;
    int left = 0;
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += nums[i];
        while (sum >= s) {
            ans = min(ans, i + 1 - left);
            sum -= nums[left++];
        }
    }
    return (ans != INT_MAX) ? ans : 0;
}
```

**Complexity analysis**

* Time complexity: $O(n)$. Single iteration of $O(n)$.
    * Each element can be visited atmost twice, once by the right pointer(ii) and (atmost)once by the $\text{left}$ pointer.
* Space complexity: $O(1)$ extra space. Only constant space required for $\text{left}$, $\text{sum}$, $\text{ans}$ and $i$.

# Submissions
---
**Solution: (Binary Search)**
```
Runtime: 88 ms
Memory Usage: 15.2 MB
```
```python
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        N = len(nums)
        if N == 0:
            return 0
        
        ans = float('inf')
        sums = [0]*(N + 1)
        # sums[0] = 0 : Meaning that it is the sum of first 0 elements
        # sums[1] = A[0] : Sum of first 1 elements
        # ans so on...
        for i in range(1, N + 1):
            sums[i] = sums[i - 1] + nums[i - 1]
        for i in range(1, N + 1):
            to_find = s + sums[i - 1]
            bound = bisect.bisect_left(sums, to_find)
            if bound != len(sums):
                ans = min(ans, bound - (i - 1))
                
        return ans if ans != float('inf') else 0
```

**Solution: (Two Pointers)**
```
Runtime: 84 ms
Memory Usage: 16.7 MB
```
```python
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        N = len(nums)
        ans = float('inf')
        left = 0
        sum_ = 0
        for i in range(N):
            sum_ += nums[i]
            while sum_ >= s:
                ans = min(ans, i + 1 - left)
                sum_ -= nums[left]
                left += 1
                
        return ans if ans != float('inf') else 0
```