''' 
Target Sum

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.


'''


''' Solution: 1156 ms '''
class Solution:
        
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        memo = [[-sys.maxsize-1 for _ in range(2001)] for _ in range(len(nums))]
        return self.calculate(nums, 0, 0, S, memo)
        
    def calculate(self, nums, index, sub_sum, target, memo):                                                        
        if index == len(nums):
            if sub_sum == target:
                return 1
            else:
                return 0                                                  
        else:
            if memo[index][sub_sum + 1000] != -sys.maxsize-1:
                return memo[index][sub_sum + 1000]                                                   
            add = self.calculate(nums, index+1, sub_sum + nums[index], target, memo)
            subtract = self.calculate(nums, index+1, sub_sum - nums[index], target, memo)
            memo[index][sub_sum + 1000] = add + subtract
            return memo[index][sub_sum + 1000]


''' Solution2: 1396 ms '''
class Solution:
        
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        l = sum(nums)
        if S>l or S<-l:
            return 0
        dp = [[0 for _ in range(-l,l+1)] for _ in range(0,len(nums)+1)]
        dp[0][0] = 1
        for i in range(1,len(nums)+1):
            for j in range(-l,l+1):
                n = 0
                n+=dp[i-1][j-nums[i-1]]
                n+=dp[i-1][j+nums[i-1]]
                dp[i][j] = n
        return dp[len(nums)][S]


''' Solution3: 300 ms '''
class Solution:
        
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        count = {0: 1}
        for x in nums:
            count2 = {}
            for tmpSum in count:
                count2[tmpSum + x] = count2.get(tmpSum + x, 0) + count[tmpSum]
                count2[tmpSum - x] = count2.get(tmpSum - x, 0) + count[tmpSum]
            count = count2
        return count.get(S, 0)
        