class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if not strs:
            return ""
        if len(strs) == 1: return strs[0]
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]: # compare to first strings index
                    return res
            res += strs[0][i]
        return res

        