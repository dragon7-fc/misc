""" 
Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

 



The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

 

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

"""


""" Solution: 92 ms """
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        maxarea = 0
        while (i < j):
            if height[i] < height[j]:
                area = height[i] * (j-i)
                if area > maxarea:
                    maxarea = area
                i += 1
            else:
                area = height[j] * (j-i)
                if area > maxarea: 
                    maxarea = area
                j -= 1
        return maxarea


""" Solution2: 80 ms """
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, res = 0, len(height)-1, 0
        while left < right:
            area = (right-left) * min(height[right], height[left])
            res = max(res, area)
            if height[right] < height[left]: right-=1  
            else: left+=1
        return res