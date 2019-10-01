class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace('-','')
        i = len(S)-1-K
        while i>=0:
            print S[i]
            S=S[:i+1]+"-"+S[i+1:]
            i-=K
        return S.upper()
