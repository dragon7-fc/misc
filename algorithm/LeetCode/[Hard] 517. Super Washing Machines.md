517. Super Washing Machines

You have **n** super washing machines on a line. Initially, each washing machine has some dresses or is empty.

For each **move**, you could choose **any m** (1 ≤ m ≤ n) washing machines, and pass **one dress** of each washing machine to one of its adjacent washing machines **at the same time** .

Given an integer array representing the number of dresses in each washing machine from left to right on the line, you should find the **minimum number of moves** to make all the washing machines have the same number of dresses. If it is not possible to do it, return -1.

**Example1**
```
Input: [1,0,5]

Output: 3

Explanation: 
1st move:    1     0 <-- 5    =>    1     1     4
2nd move:    1 <-- 1 <-- 4    =>    2     1     3    
3rd move:    2     1 <-- 3    =>    2     2     2   
```

**Example2**
```
Input: [0,3,0]

Output: 2

Explanation: 
1st move:    0 <-- 3     0    =>    1     2     0    
2nd move:    1     2 --> 0    =>    1     1     1     
```

**Example3**
```
Input: [0,2,0]

Output: -1

Explanation: 
It's impossible to make all the three washing machines have the same number of dresses. 
Note:
The range of n is [1, 10000].
The range of dresses number in a super washing machine is [0, 1e5].
```

# Submissions
---
**Solution 1: (Greedy, DP)**

* For each machines, the number of moves it conducts is the number of dresses it sends out.
* Start scanning from left
    * if it has > target dresses, send the surplus to right
    * if it has < targer dresses, let its right neighbor send the deficit to it (regardless of how many dresses this neighbor has at the momnet)
    * Don't worry about the aggregated surplus or deficit, it eventually will be taken care by later machines.

```
Runtime: 96 ms
Memory Usage: 14.8 MB
```
```python
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        N = len(machines)
        S = sum(machines)
        if S % N != 0:
            return -1
        
        target = S // N
        ans = 0
        send_out = [0] * N
        for i in range(N-1):
            if machines[i] > target:
                send_out[i] += machines[i] - target
            elif machines[i] < target:
                send_out[i+1] = target - machines[i]
            machines[i+1] += machines[i] - target
            ans = max(ans, send_out[i], send_out[i+1])
        return ans
```

**Solution 2: (Greedy)**

1. sumneed:record the number of dress needed until i, the step must be larger than abs(sumneed). Because each machine at each step can get at most one dress from one direction.
2. When the number of dress in current machine is larger than ave, it must be offloaded. Each step can only offload one dress.
3. The maximum step is max(1,2).

```
Runtime: 92 ms
Memory Usage: 14.6 MB
```
```python
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        S = sum(machines)
        N = len(machines)
        if S % N!=0:
            return -1
        ave = S // N
        sumneed = 0
        res = 0
        for m in machines:
            sumneed += m-ave
            res = max(res, abs(sumneed), m-ave)
                           -----------   -----
                              pre         cur
            
        return res
```

**Solution 3: (Greedy)**
```
Runtime: 0 ms
Memory: 16.83 MB
```
```c++
class Solution {
public:
    int findMinMoves(vector<int>& machines) {
        int n = machines.size(), a = accumulate(machines.begin(), machines.end(), 0), t, pre, ans = 0;
        if (a%n) {
            return -1;
        }
        t = a/n;
        pre = 0;
        for (auto m: machines) {
            pre += m-t;
            ans = max({ans, abs(pre), m-t});
        }
        return ans;
    }
};
```
