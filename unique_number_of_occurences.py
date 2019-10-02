#https://leetcode.com/problems/unique-number-of-occurrences/

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dic = {}
        for i in arr:
            if i in dic.keys():
                dic[i]+=1
            else:
                dic[i]=1
        
        return len(set(dic.values()))==len(dic.values())
