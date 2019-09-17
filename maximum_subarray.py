#https://leetcode.com/problems/maximum-subarray/

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        cur_s = max_s = nums[0]
        
        for i in range(1, n):
            cur_s = max(nums[i], cur_s + nums[i])
            max_s = max(max_s, cur_s)
        
        return max_s
