#https://leetcode.com/problems/house-robber/

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prevMax = currMax = 0
        for i in nums:
            temp = currMax
            currMax = max(prevMax + i, currMax)
            prevMax = temp
        return currMax
