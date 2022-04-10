2233. Maximum Product After K Increments

You are given an array of non-negative integers `nums` and an integer `k`. In one operation, you may choose **any** element from `nums` and **increment** it by `1`.

Return the **maximum product** of `nums` after at most `k` operations. Since the answer may be very large, return it **modulo** `10^9 + 7`.

 

**Example 1:**
```
Input: nums = [0,4], k = 5
Output: 20
Explanation: Increment the first number 5 times.
Now nums = [5, 4], with a product of 5 * 4 = 20.
It can be shown that 20 is maximum product possible, so we return 20.
Note that there may be other ways to increment nums to have the maximum product.
```

**Example 2:**
```
Input: nums = [6,3,3,2], k = 2
Output: 216
Explanation: Increment the second number 1 time and increment the fourth number 1 time.
Now nums = [6, 4, 3, 3], with a product of 6 * 4 * 3 * 3 = 216.
It can be shown that 216 is maximum product possible, so we return 216.
Note that there may be other ways to increment nums to have the maximum product.
```

**Constraints:**

* `1 <= nums.length, k <= 10^5`
* `0 <= nums[i] <= 10^6`

# Submissions
---
**Solution 1: (Heap)**
```
Runtime: 2678 ms
Memory Usage: 24.5 MB
```
```python
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        # creating a heap
        heap = []
        for i in nums:
            heapq.heappush (heap,i)
            
            
        # basic idea here is keep on incrementing smallest number, then only multiplication of that number will be greater
        # so basically till I have operations left I will increment my smallest number
        while k :
            current = heapq.heappop(heap)
            heapq.heappush(heap, current+1)
            k-=1
            
        result =1
        
        # Just Multiply all the numbers in heap and return the value
        while len(heap)>0:
            x= heapq.heappop(heap)
            result =(result*x )% (10**9+7)
            
        return result
```

**Solution 2: (Heap)**
```
Runtime: 735 ms
Memory Usage: 90.9 MB
```
```c++
class Solution {
public:
    int maximumProduct(vector<int>& nums, int k) {
        int mod=pow(10,9)+7;
        priority_queue <int, vector<int>, greater<int>> pq;
        for(int i=0;i<nums.size();i++){
            pq.push(nums[i]);
        }
        while(k>0){
            int x=pq.top();
            pq.pop();
            x=x+1;
            pq.push(x);
            k--;
        }
        long long int ans=1;
        while(pq.size()>0){
            int x=pq.top();
            pq.pop();
            ans=(ans*x)%mod;
        }
        return ans;
    }
};
```

**Solution 3: (Heap)**
```
Runtime: 518 ms
Memory Usage: 82.2 MB
```
```c++
class Solution {
public:
    int maximumProduct(vector<int>& nums, int k) {
        make_heap(begin(nums), end(nums), greater<int>());
        while (k--) {
            pop_heap(begin(nums), end(nums), greater<int>());
            ++nums.back();
            push_heap(begin(nums), end(nums), greater<int>());        
        }
        return accumulate(begin(nums), end(nums), 1LL, [](long long res, int n) { return res * n % 1000000007; });
    }
};
```
