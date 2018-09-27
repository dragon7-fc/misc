""" 
Subarray Sum Equals K

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

"""


""" Solution: 88 ms """
class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums=dict()
        sums[0]=1
        sm=0
        res=0
        for num in nums:
            sm+=num
            if sm-k in sums:
                res+=sums[sm-k]
            if sm in sums:
                sums[sm]+=1
            else:
                sums[sm]=1
        return res


""" Solution2: 72 ms """
class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_cnt = collections.defaultdict(int)
        sum_cnt[0] = 1
        cur_sum = 0
        cnt = 0
        
        for i in range(len(nums)):
            cur_sum += nums[i]                        
            
            if cur_sum - k in sum_cnt:
                cnt += sum_cnt[cur_sum -k]
            
            sum_cnt[cur_sum] += 1    
        
        return cnt
        