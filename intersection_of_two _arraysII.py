#https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 and nums2:
            return []
        
        ans = []
        if len(nums2)>len(nums1):
            nums1, nums2 = nums2, nums1     
        for i in nums1:
            if i in nums2:
                nums2.remove(i)
                ans.append(i)
        return ans
