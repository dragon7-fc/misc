739. Daily Temperatures

Given a list of daily temperatures `T`, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put `0` instead.

For example, given the list of temperatures `T = [73, 74, 75, 71, 69, 72, 76, 73]`, your output should be `[1, 1, 4, 2, 1, 1, 0, 0]`.

**Note:** The length of temperatures will be in the range `[1, 30000]`. Each temperature will be an integer in the range `[30, 100]`.

# Solution
---
## Approach #1: Next Array [Accepted]
**Intuition**

The problem statement asks us to find the next occurrence of a warmer temperature. Because temperatures can only be in `[30, 100]`, if the temperature right now is say, `[i] = 50` we only need to check for the next occurrence of `51, 52, ..., 100` and take the one that occurs soonest.

**Algorithm**

Let's process each `i` in reverse (decreasing order). At each `T[i]`, to know when the next occurrence of say, temperature `100` is, we should just remember the last one we've seen, `next[100]`.

Then, the first occurrence of a warmer value occurs at `warmer_index`, the minimum of `next[T[i]+1], next[T[i]+2], ..., next[100]`.

```python
class Solution(object):
    def dailyTemperatures(self, T):
        nxt = [float('inf')] * 102
        ans = [0] * len(T)
        for i in xrange(len(T) - 1, -1, -1):
            #Use 102 so min(nxt[t]) has a default value
            warmer_index = min(nxt[t] for t in xrange(T[i]+1, 102))
            if warmer_index < float('inf'):
                ans[i] = warmer_index - i
            nxt[T[i]] = i
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(NW)$, where $N$ is the length of T and $W$ is the number of allowed values for `T[i]`. Since $W = 71$, we can consider this complexity $O(N)$.

* Space Complexity: $O(N + W)$, the size of the answer and the next array.

## Approach #2: Stack [Accepted]
**Intuition**

Consider trying to find the next warmer occurrence at `T[i]`. What information (about `T[j]` for `j > i`) must we remember?

Say we are trying to find `T[0]`. If we remembered `T[10] = 50`, knowing `T[20] = 50` wouldn't help us, as any `T[i]` that has its next warmer ocurrence at `T[20]` would have it at `T[10]` instead. However, `T[20] = 100` would help us, since if `T[0]` were `80`, then `T[20]` might be its next warmest occurrence, while `T[10]` couldn't.

Thus, we should remember a list of indices representing a strictly increasing list of temperatures. For example, `[10, 20, 30]` corresponding to temperatures `[50, 80, 100]`. When we get a new temperature like `T[i] = 90`, we will have `[5, 30]` as our list of indices (corresponding to temperatures `[90, 100]`). The most basic structure that will satisfy our requirements is a stack, where the top of the stack is the first value in the list, and so on.

**Algorithm**

As in Approach #1, process indices `i` in descending order. We'll keep a stack of indices such that `T[stack[-1]] < T[stack[-2]] < ...,` where `stack[-1]` is the top of the stack, `stack[-2]` is second from the top, and so on; and where `stack[-1] > stack[-2] > ...;` and we will maintain this invariant as we process each temperature.

After, it is easy to know the next occurrence of a warmer temperature: it's simply the top index in the stack.

Here is a worked example of the contents of the stack as we work through `T = [73, 74, 75, 71, 69, 72, 76, 73]` in reverse order, at the end of the loop (after we add `T[i]`). For clarity, stack only contains indices `i`, but we will write the value of `T[i]` beside it in brackets, such as `0 (73)`.

* When `i = 7`, `stack = [7 (73)]`. `ans[i] = 0`.
* When `i = 6`, `stack = [6 (76)]`. `ans[i] = 0`.
* When `i = 5`, `stack = [5 (72), 6 (76)]`. `ans[i] = 1`.
* When `i = 4`, `stack = [4 (69), 5 (72), 6 (76)]`. `ans[i] = 1`.
* When `i = 3`, `stack = [3 (71), 5 (72), 6 (76)]`. `ans[i] = 2`.
* When `i = 2`, `stack = [2 (75), 6 (76)]`. `ans[i] = 4`.
* When `i = 1`, `stack = [1 (74), 2 (75), 6 (76)]`. `ans[i] = 1`.
* When `i = 0`, `stack = [0 (73), 1 (74), 2 (75), 6 (76)]`. `ans[i] = 1`.

```python
class Solution(object):
    def dailyTemperatures(self, T):
        ans = [0] * len(T)
        stack = [] #indexes from hottest to coldest
        for i in xrange(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of T and $W$ is the number of allowed values for `T[i]`. Each index gets pushed and popped at most once from the stack.

* Space Complexity: $O(W)$. The size of the stack is bounded as it represents strictly increasing temperatures.

# Submissions
---
**Solution: (Stack)**
```
Runtime: 492 ms
Memory Usage: 16.6 MB
```
```python
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        stack = [] #indexes from hottest to coldest
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans
```

**Solution 2: (Stack)**
```
Runtime: 524 ms
Memory Usage: 53.3 MB
```
```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* dailyTemperatures(int* temperatures, int temperaturesSize, int* returnSize){
    int *ans = calloc(1, temperaturesSize*sizeof(int));
    int *stack = malloc(temperaturesSize*sizeof(int));
    int sz = 0;
    for (int i = temperaturesSize-1; i >= 0; i --) {
        while (sz > 0 && temperatures[i] >= temperatures[stack[sz-1]])
            sz -= 1;
        ans[i] = (sz > 0 ? stack[sz-1] - i: 0);
        stack[sz] = i;
        sz += 1;
    }
    free(stack);
    *returnSize = temperaturesSize;
    return ans;
}
```

**Solution 3: (Stack)**
```
Runtime: 152 ms
Memory Usage: 85.1 MB
```
```c++
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<pair<int, int>> stk;
        vector<int> ans(temperatures.size());
        for (int i = temperatures.size()-1; i >= 0; i--) {
            while (!stk.empty() && stk.top().second <= temperatures[i])
                stk.pop();
            if (!stk.empty())
                ans[i] = stk.top().first - i;
            stk.push({i, temperatures[i]});
        }
        return ans;
    }
};
```

**Solution 4: (Array, Optimized Space)**
```
Runtime: 1740 ms
Memory: 28.2 MB
```
```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        hottest = 0
        answer = [0] * n
        
        for curr_day in range(n - 1, -1, -1):
            current_temp = temperatures[curr_day]
            if current_temp >= hottest:
                hottest = current_temp
                continue
            
            days = 1
            while temperatures[curr_day + days] <= current_temp:
                # Use information from answer to search for the next warmer day
                days += answer[curr_day + days]
            answer[curr_day] = days

        return answer
```

**Solution 5: (Stack)**
```
Runtime: 3665 ms
Memory: 28.7 MB
```
```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        stk = []
        ans = [0]*N
        for j in range(N):
            while stk and temperatures[stk[-1]] < temperatures[j]:
                i = stk.pop()
                ans[i] = j-i
            stk += [j]
        return ans
```

**Solution 6: (Stack, mono dec)**

    73,74,75,71,69,72,76,73
                         73
                      76
                   76 72
                76 72 69
             76 72 71
          76 75
       76 75 74
    76 75 74 73
ans  1  1  4  2  1  1  0  0

```
Runtime: 14 ms, Beats 88.22%
Memory: 102.79 MB, Beats 91.52%
```
```c++
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size(), i;
        stack<int> stk;
        vector<int> ans(n);
        for (i = n-1; i >= 0; i --) {
            while (stk.size() && temperatures[stk.top()] <= temperatures[i]) {
                stk.pop();
            }
            if (stk.size()) {
                ans[i] = stk.top() - i;
            }
            stk.push(i);
        }
        return ans;
    }
};
```
