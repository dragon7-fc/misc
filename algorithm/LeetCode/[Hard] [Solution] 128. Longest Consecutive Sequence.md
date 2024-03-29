128. Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

**Example:**
```
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

# Solution
---
## Approach 1: Brute Force
**Intuition**

Because a sequence could start at any number in nums, we can exhaust the entire search space by building as long a sequence as possible from every number.

**Algorithm**

The brute force algorithm does not do anything clever - it just considers each number in `nums`, attempting to count as high as possible from that number using only numbers in `nums`. After it counts too high (i.e. `currentNum` refers to a number that `nums` does not contain), it records the length of the sequence if it is larger than the current best. The algorithm is necessarily optimal because it explores every possibility.

```python
class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0

        for num in nums:
            current_num = num
            current_streak = 1

            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak
```

**Complexity Analysis**

* Time complexity : $O(n^3)$.

The outer loop runs exactly $n$ times, and because `currentNum` increments by 1 during each iteration of the while loop, it runs in $O(n)$ time. Then, on each iteration of the while loop, an $O(n)$ lookup in the array is performed. Therefore, this brute force algorithm is really three nested $O(n)$ loops, which compound multiplicatively to a cubic runtime.

* Space complexity : $O(1)$.

The brute force algorithm only allocates a handful of integers, so it uses constant additional space.

## Approach 2: Sorting
**Intuition**

If we can iterate over the numbers in ascending order, then it will be easy to find sequences of consecutive numbers. To do so, we can sort the array.

Algorithm

Before we do anything, we check for the base case input of the empty array. The longest sequence in an empty array is, of course, 0, so we can simply return that. For all other cases, we sort `nums` and consider each number after the first (because we need to compare each number to its previous number). If the current number and the previous are equal, then our current sequence is neither extended nor broken, so we simply move on to the next number. If they are unequal, then we must check whether the current number extends the sequence (i.e. `nums[i] == nums[i-1] + 1`). If it does, then we add to our current count and continue. Otherwise, the sequence is broken, so we record our current sequence and reset it to `1` (to include the number that broke the sequence). It is possible that the last element of `nums` is part of the longest sequence, so we return the maximum of the current sequence and the longest one.

![sorting](img/128_sorting.png)

Here, an example array is sorted before the linear scan identifies all consecutive sequences. The longest sequence is colored in red.

```python
class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)
```

**Complexity Analysis**

* Time complexity : $O(nlgn)$.

The main for loop does constant work $n$ times, so the algorithm's time complexity is dominated by the invocation of sort, which will run in $O(nlgn)$ time for any sensible implementation.

* Space complexity : $O(1)$ (or $O(n)$).

For the implementations provided here, the space complexity is constant because we sort the input array in place. If we are not allowed to modify the input array, we must spend linear space to store a sorted copy.

## Approach 3: HashSet and Intelligent Sequence Building
**Intuition**

It turns out that our initial brute force solution was on the right track, but missing a few optimizations necessary to reach $O(n)$ time complexity.

**Algorithm**

This optimized algorithm contains only two changes from the brute force approach: the numbers are stored in a HashSet (or Set, in Python) to allow $O(1)$ lookups, and we only attempt to build sequences from numbers that are not already part of a longer sequence. This is accomplished by first ensuring that the number that would immediately precede the current number in a sequence is not present, as that number would necessarily be part of a longer sequence.

```python
class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
```

**Complexity Analysis**

* Time complexity : $O(n)$.

Although the time complexity appears to be quadratic due to the while loop nested within the for loop, closer inspection reveals it to be linear. Because the while loop is reached only when `currentNum` marks the beginning of a sequence (i.e. currentNum-1 is not present in nums), the while loop can only run for $n$ iterations throughout the entire runtime of the algorithm. This means that despite looking like $O(n \cdot n)$ complexity, the nested loops actually run in $O(n + n) = O(n)$ time. All other computations occur in constant time, so the overall runtime is linear.

* Space complexity : $O(n)$.

In order to set up $O(1)$ containment lookups, we allocate linear space for a hash table to store the $O(n)$ numbers in `nums`. Other than that, the space complexity is identical to that of the brute force solution.

# Submissions
---
**Solution: (HashSet and Intelligent Sequence Building)**
```
Runtime: 40 ms
Memory Usage: N/A
```
```python
class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
```

**Solution 1: (Union Find)**
```
Runtime: 76 ms
Memory Usage: 14.9 MB
```
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums = set(nums)
        parent = [i for i in range(len(nums))]
        size = [1 for _ in nums]
        rank = [0 for _ in nums]
        num_index = {}
        for i, num in enumerate(nums):
            num_index[num] = i
        
        def union(x, y):
            fx = find(x)
            fy = find(y)
            if fx!=fy:
                if rank[fx] > rank[fy]:
                    parent[fy] = fx
                    size[fx] += size[fy]
                else:
                    if rank[fx] == rank[fy]:
                        rank[y] += 1
                    parent[fx] = fy
                    size[fy] += size[fx]          
            
        def find(x):
            if parent[x]!=x:
                parent[x] = find(parent[x])
            return parent[x]
        
        for i, num in enumerate(nums):          
            if num - 1 in num_index:
                union(i, num_index[num-1])
            if num + 1 in num_index:
                union(i, num_index[num+1])      
        return max(size)
```

**Solution 2: (DP)**
```
Runtime: 60 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0 for _ in range(len(nums) + 1)]
        dp[0] = 1
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                dp[i] = dp[i - 1] + 1
            elif nums[i] == nums[i - 1]: 
                dp[i] = dp[i - 1]
            else:
                dp[i] = 1
        return max(dp)
```

**Solution 3: (Set)**
```
Runtime: 119 ms
Memory Usage: 30.9 MB
```
```c++
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s;
        for(int i = 0; i< nums.size(); i++) {
            s.insert(nums[i]);
        }
	    int longest = 0;
	    for(int num : s) {
            if (s.count(num - 1)) continue;//t.c is O(N) bcoz just for one element while loop is running so t.c O(N)+O(N)
            int j = 1;
            while (s.count(num + j)) j++; 
            longest = max(longest, j);
        }
        return longest;
    }
};
```
