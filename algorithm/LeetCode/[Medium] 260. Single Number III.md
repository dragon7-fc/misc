260. Single Number III

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

**Example:**
```
Input:  [1,2,1,3,2,5]
Output: [3,5]
```

**Note:**

* The order of the result is not important. So in the above example, [5, 3] is also correct.
* Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

# Submissions
---
**Solution 1: (Set)**
```
Runtime: 56 ms
Memory Usage: 14.5 MB
```
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = set()
        for x in nums:
            if x in ans:
                ans.remove(x)
            else:
                ans.add(x)
        return list(ans)
```

**Solution 2: (Bit Manipulation)**
```
Runtime: 60 ms
Memory Usage: 14.6 MB
```
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        m = 0
        for i in nums: m ^= i
        #get masking, the "last set bit" (right most 1 bit)
        m &= -m  #just remember it, I cannot explain
        rst = [0, 0]
        for i in nums:
            #the masking help separate the result two unique num into different group
            #because they differs in the masking bit
            if m & i: rst[0] ^= i
            else: rst[1] ^= i
        return rst
```

**Solution 3: (XOR)**
```
Runtime: 40 ms
Memory Usage: 10.1 MB
```
```c++
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        // xor all numbers, so the duplicates are cancelled
        int x = 0;
        for (const int curr: nums) {
            x ^= curr;    
        }

        // find the bit that is set in x.
        int bit;
        for (int i=0; i<32; ++i) {
            if (x & (1<<i)) {
                bit = i;
                break;
            }
        }

        // let the answer be first and second.
        // let first is the number that has the bit set.
        // second does not have the bit set, because x=first^second has the bit set.  
        // now xor all numbers in nums with the bit set.
        // all duplicates will be cancelled
        // only first will remain. second will not be included, as second does not have the bit set.
        int first = 0;
        for (int a: nums) {
            if (a & (1<<bit)) {
                first ^= a;
            }
        }
        // now x=first^second, therefore second = a^first
        int second = first^x;
        return {first, second};
    }
};
```

**Solution 4: (XOR)**
```
Runtime: 64 ms
Memory Usage: 15.5 MB
```
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # xor all numbers, so the duplicates are cancelled
        x = functools.reduce(operator.xor, nums)
        
        # find the bit that is set in x.
        bit = 0
        for i in range(32):
            if x & (1<<i):
                bit = i
                break
                
        # let the answer be first and second.
        # let first is the number that has the bit set.
        # second does not have the bit set, because x=first^second has the bit set.  
        # now xor all numbers in nums with the bit set.
        # all duplicates will be cancelled
        # only first will remain. second will not be included, as second does not have the bit set.
        first = 0
        for a in nums:
            if a & (1<<bit):
                first ^= a

        # now x=first^second, therefore second = a^first
        second = first^x
        return [first, second]
```