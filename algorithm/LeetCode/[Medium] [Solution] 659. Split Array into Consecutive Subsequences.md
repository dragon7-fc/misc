659. Split Array into Consecutive Subsequences

Given an array `nums` sorted in ascending order, return `true` if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least `3`.

 

**Example 1:**
```
Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5
```

**Example 2:**
```
Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5
```

**Example 3:**
```
Input: [1,2,3,4,4,5]
Output: False
```

**Constraints:**

* `1 <= nums.length <= 10000`

# Solution
---
## Approach #1: Opening and Closing Events [Accepted]
**Intuition**

We can think of the problem as drawing intervals on a number line. This gives us the idea of opening and closing events.

To illustrate this concept, say we have nums = `[10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 12]`, with no `9`s and no `14`s. We must have two sequences start at `10`, two sequences start at `11`, and 3 sequences end at `12`.

In general, when considering a chain of consecutive integers `x`, we must have `C = count[x+1] - count[x]` sequences start at `x+1` when `C > 0`, and `-C` sequences end at `x` if `C < 0`. Even if there are more endpoints on the intervals we draw, there must be at least this many endpoints.

With the above example, `count[11] - count[10] = 2` and `count[13] - count[12] = -3` show that two sequences start at `11`, and three sequences end at `12`.

Also, if for example we know some sequences must start at time `1` and `4` and some sequences end at `5` and `7`, to maximize the smallest length sequence, we should pair the events together in the order they occur: ie., `1` with `5` and `4` with `7`.

**Algorithm**

For each group of numbers, say the number is `x` and there are count of them. Furthermore, say `prev`, `prev_count` is the previous integer encountered and it's count.

Then, in general there are `abs(count - prev_count)` events that will happen: if `count > prev_count` then we will add this many `t`'s to `starts`; and if `count < prev_count` then we will attempt to pair `starts.popleft()` with `t-1`.

More specifically, when we have finished a consecutive group, we will have `prev_count` endings; and when we are in a consecutive group, we may have `count - prev_count` starts or `prev_count - count` endings.

For example, when `nums = [1,2,3,3,4,5]`, then the starts are at `[1, 3]` and the endings are at `[3, 5]`. As our algorithm progresses:

* When `t = 1, count = 1`: `starts = [1]`
* When `t = 2, count = 1`: `starts = [1]`
* When `t = 3, count = 2`: `starts = [1, 3]`
* When `t = 4, count = 1`: `starts = [3]`, since `prev_count - count = 1` we process one closing event, which is accepted as `t-1 >= starts.popleft() + 2`.
* When `t = 5, count = 1`: `starts = [3]`

And at the end, we process `prev_count` more closing events `nums[-1]`.

```python
class Solution(object):
    def isPossible(self, nums):
        prev, prev_count = None, 0
        starts = collections.deque()
        for t, grp in itertools.groupby(nums):
            count = len(list(grp))
            if prev is not None and t - prev != 1:
                for _ in xrange(prev_count):
                    if prev < starts.popleft() + 2:
                        return False
                prev, prev_count = None, 0

            if prev is None or t - prev == 1:
                if count > prev_count:
                    for _ in xrange(count - prev_count):
                        starts.append(t)
                elif count < prev_count:
                    for _ in xrange(prev_count - count):
                        if t-1 < starts.popleft() + 2:
                            return False

            prev, prev_count = t, count

        return all(nums[-1] >= x+2 for x in starts)
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of `nums`. We iterate over the array and every event is added or popped to starts at most once.

* Space Complexity: $O(N)$, the size of starts.

## Approach #2: Greedy [Accepted]
**Intuition**

Call a chain a sequence of `3` or more consecutive numbers.

Considering numbers `x` from left to right, if `x` can be added to a current chain, it's at least as good to add `x` to that chain first, rather than to start a new chain.

Why? If we started with numbers `x` and greater from the beginning, the shorter chains starting from `x` could be concatenated with the chains ending before `x`, possibly helping us if there was a "chain" from `x` that was only length `1` or `2`.

**Algorithm**

Say we have a count of each number, and let `tails[x]` be the number of chains ending right before `x`.

Now let's process each number. If there's a chain ending before `x`, then add it to that chain. Otherwise, if we can start a new chain, do so.

It's worth noting that our solution can be amended to take only $O(1)$ additional space, since we could do our counts similar to Approach #1, and we only need to know the last `3` counts at a time.

```python
class Solution(object):
    def isPossible(self, nums):
        count = collections.Counter(nums)
        tails = collections.Counter()
        for x in nums:
            if count[x] == 0:
                continue
            elif tails[x] > 0:
                tails[x] -= 1
                tails[x+1] += 1
            elif count[x+1] > 0 and count[x+2] > 0:
                count[x+1] -= 1
                count[x+2] -= 1
                tails[x+3] += 1
            else:
                return False
            count[x] -= 1
        return True
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of `nums`. We iterate over the array.

* Space Complexity: $O(N)$, the size of count and tails.

# Submissions
---
**Solution: (Opening and Closing Event)**
```
Runtime: 540 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        prev, prev_count = None, 0
        starts = collections.deque()
        for t, grp in itertools.groupby(nums):
            count = len(list(grp))
            if prev is not None and t - prev != 1:
                for _ in range(prev_count):
                    if prev < starts.popleft() + 2:
                        return False
                prev, prev_count = None, 0

            if prev is None or t - prev == 1:
                if count > prev_count:
                    for _ in range(count - prev_count):
                        starts.append(t)
                elif count < prev_count:
                    for _ in range(prev_count - count):
                        if t-1 < starts.popleft() + 2:
                            return False

            prev, prev_count = t, count

        return all(nums[-1] >= x+2 for x in starts)
```

**Solution: (Greedy, Hash Table)**

**Example 1:**
```
nums - [1,2,3,3,4,5]

step0:
count: {1:1, 2:1, 3:2, 4:1, 5:1}
tails: {}

step1:
x = 1
count: {1:0, 2:0, 3:1, 4:1, 5:1}
tails: {4:1}

step2:
x = 2
continue

step3:
x = 3
count: {1:0, 2:0, 3:0, 4:0, 5:0}
tails: {4:1, 6:1}

step4
x = 4
continue

step5
x = 5
continue

step6
x = 6
continue

return True
```

**Example 2:**
```
nums = [1,2,3,4,4,5]

step0:
count = {1:1, 2:1, 3:1, 4:2, 5:1}
tails = {}

step1:
x = 1
count = {1:0, 2:0, 3:0, 4:2, 5:1}
tails = {4:1}

step2:
x = 2
cotinue

step3:
x = 3
cotinue

step4:
x = 4
count = {1:0, 2:0, 3:0, 4:1, 5:1}
tails = {4:0, 5:1}

step5:
x = 4
return False
```

```
Runtime: 608 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = collections.Counter(nums)
        tails = collections.Counter()  # subsequence tail counter
        for x in nums:
            if count[x] == 0:
                continue
            elif tails[x] > 0:  # extend subsequence length
                tails[x] -= 1
                tails[x+1] += 1
            elif count[x+1] > 0 and count[x+2] > 0:  # check subsequence existence
                count[x+1] -= 1
                count[x+2] -= 1
                tails[x+3] += 1
            else:
                return False
            count[x] -= 1
        return True
```

**Solution: (Greedy using Heap)**
```
Runtime: 106 ms
Memory Usage: 54.6 MB
```
```c++
class Solution {
public:
    struct Compare {
        bool operator()(array<int, 2> subsequence1, array<int, 2> subsequence2) {
            if (subsequence1[1] == subsequence2[1]) {
                return (subsequence1[1] - subsequence1[0]) > (subsequence2[1] - subsequence2[0]);
            }
            return subsequence1[1] > subsequence2[1];
        }
    };
    
    bool isPossible(vector<int>& nums) {
        priority_queue<array<int, 2>, vector<array<int, 2>>, Compare> subsequences;

        for (int num : nums) {
            //Condition 1 - remove non qualifying subsequences
            while (!subsequences.empty() && subsequences.top()[1] + 1 < num) {
                array<int, 2> currentSubsequence = subsequences.top();
                subsequences.pop();
                int subsequenceLength = currentSubsequence[1] - currentSubsequence[0] + 1;
                if (subsequenceLength < 3) {
                    return false;
                }
            }
            //Condition 2 - create a new subsequence
            if (subsequences.empty() || subsequences.top()[1] == num) {
                subsequences.push({num, num});
            } else {
                //Condition 3 - add num to an existing subsequence
                array<int, 2> currentSubsequence = subsequences.top();
                subsequences.pop();
                subsequences.push({currentSubsequence[0], num});
            }
        }

        //If any subsequence is of length less than 3 return false
        while (!subsequences.empty()) {
            array<int, 2> currentSubsequence = subsequences.top();
            subsequences.pop();
            int subsequenceLength = currentSubsequence[1] - currentSubsequence[0] + 1;
            if (subsequenceLength < 3) {
                return false;
            }
        }
        return true;
    }
};
```

**Solution: (Greedy using Maps)**
```
Runtime: 103 ms
Memory Usage: 58.4 MB
```
```c++
class Solution {
public:
    
    bool isPossible(vector<int>& nums) {
        unordered_map<int, int> subsequences;
        unordered_map<int, int> frequency;
        for (int num : nums) {
            frequency[num]++;
        }
        for (int num : nums) {
            //num already part of a valid subsequence.
            if (frequency[num] == 0) {
                continue;
            }
            //If a valid subsequence exists with last element = num - 1.
            if (subsequences[num - 1] > 0) {
                subsequences[num - 1]--;
                subsequences[num]++;
            } else if (frequency[num + 1] > 0 && frequency[num + 2] > 0) {
                // If we want to start a new subsequence, check if num + 1 and num + 2 exists
                // Update the list of subsequences with the newly created subsequence
                subsequences[num + 2]++;
                frequency[num + 1]--;
                frequency[num + 2]--;
            } else {
                // No valid subsequence is possible with num
                return false;
            }
            frequency[num]--;
        }
        return true;
    }
};
```

**Solution: (Dynamic Programming)**
```
Runtime: 86 ms
Memory Usage: 55.2 MB
```
```c++
class Solution {
private:
    bool isSegmentValid(vector<int> &nums, int start, int end) {
        int noOfUniqueNumbers = nums[end] - nums[start] + 1;

        // Count frequency of each number in the current segment.
        vector<int> frequency(noOfUniqueNumbers);
        
        for (int i = start; i <= end; i++) {
            frequency[nums[i] - nums[start]]++;
        }
        // lengthOneSubsequences[i] holds count of subsequences of length 1 ending with index i
        vector<int> lengthOneSubsequences(noOfUniqueNumbers);

        // lengthTwoSubsequences[i] holds count of subsequences of length 2 ending with index i
        vector<int> lengthTwoSubsequences(noOfUniqueNumbers);

        // totalNoOfSubsequences[i] holds count of all subsequences ending with index i
        vector<int> totalNoOfSubsequences(noOfUniqueNumbers);

        lengthOneSubsequences[0] = totalNoOfSubsequences[0] = frequency[0];

        for (int i = 1; i < noOfUniqueNumbers; i++) {

            // If the frequency[i] is less than total number of subsequences ending with i - 1,
            // we do not have enough subsequences where we can put i.
            if (frequency[i] < lengthOneSubsequences[i - 1] + lengthTwoSubsequences[i - 1]) {
                return false;
            }
            
            //Total number of subsequences of length 2 can be obtained by adding i 
            //to subsequences of length 1 ending with i - 1.
            lengthTwoSubsequences[i] = lengthOneSubsequences[i - 1];
            
            // For the remaining i valued numbers we can either add them to an existing subsequence
            // or create a new one. We first try to add them to the existing subsequences ending 
            // with i - 1. If there are not enough of such subsequences, we start a new subsequence.
            // The existing subsequences ending with i - 1 is denoted by totalNoOfSubsequences[i - 1];
            lengthOneSubsequences[i] = max(0, frequency[i] - totalNoOfSubsequences[i - 1]);
            totalNoOfSubsequences[i] = frequency[i];
        }

        // If there is no remaining subsequence of length one or two, we can return true. 
        // Otherwise, return false.
        return lengthOneSubsequences[noOfUniqueNumbers - 1] == 0 && 
               lengthTwoSubsequences[noOfUniqueNumbers - 1] == 0;
    }
    
public:
    bool isPossible(vector<int>& nums) {
        int n = nums.size();
        int start = 0;

        for (int i = 1; i < n; i++) {
            // Check possibility of a valid segment starting at index start and ending at index i - 1.
            if (nums[i] - nums[i - 1] > 1) {
                if (!isSegmentValid(nums, start, i - 1)) {
                    return false;
                }
                // Update the starting index of the next segment.
                start = i;
            }
        }
        // Check for the last segment
        return isSegmentValid(nums, start, n - 1);
    }
};
```

**Solution: (Optimal Space)**
```
Runtime: 97 ms
Memory Usage: 54.5 MB
```
```c++
class Solution {
private:
    bool isSegmentValid(vector<int> &nums, int start, int end) {
        int frequency = 0;

        //lengthOneSubsequences holds count of subsequences of length 1.
        int lengthOneSubsequences = 0;

        //lengthTwoSubsequences holds count of subsequences of length 2.
        int lengthTwoSubsequences = 0;

        //totalNoOfSubsequences holds count of all subsequences.
        int totalNoOfSubsequences = 0;

        for (int i = start; i <= end; i++) {
            if (i > start && nums[i] == nums[i - 1]) {
                frequency++;
            } else if (frequency < lengthOneSubsequences + lengthTwoSubsequences) {
                // If the frequency[i] is less than total number of subsequences ending with i - 1,
                // we do not have enough subsequences where we can put i.
                return false;
            } else {
                // Total number of subsequences of length 2 can be obtained by
                // adding i to subsequences of length 1 ending with i - 1.
                lengthTwoSubsequences = lengthOneSubsequences;
                lengthOneSubsequences = max(0, frequency - totalNoOfSubsequences);
                totalNoOfSubsequences = frequency;
                frequency = 1;
            }
        }
        // For the last element in the segment.
        lengthTwoSubsequences = lengthOneSubsequences;
        lengthOneSubsequences = max(0, frequency - totalNoOfSubsequences);
        // If there is no remaining subsequence of length one or two, we can return true. 
        // Otherwise, return false.
        return lengthOneSubsequences == 0 && lengthTwoSubsequences == 0;
    }
    
public:
    bool isPossible(vector<int>& nums) {
        int n = nums.size();
        int start = 0;

        for (int i = 1; i < n; i++) {
            //Check possibility of a valid segment starting at index start and ending at index i - 1.
            if (nums[i] - nums[i - 1] > 1) {
                if (!isSegmentValid(nums, start, i - 1)) {
                    return false;
                }
                //Update the starting index of the next segment.
                start = i;
            }
        }
        //Check for the last segment
        return isSegmentValid(nums, start, n - 1);
    }
};
```

**Solution 1: (Heap)**
```
Runtime: 664 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        d = collections.defaultdict(list)
        for e in nums:
            if d[e-1]: # there is sequence ending with e-1
                minLen = heapq.heappop(d[e-1]) # the shortest sequence
                heapq.heappush(d[e], minLen+1)
            else:
                heapq.heappush(d[e], 1) # create a new sequence
        for h in d.values():
            for hl in h:
                if hl < 3:
                    return False
        return True
```
