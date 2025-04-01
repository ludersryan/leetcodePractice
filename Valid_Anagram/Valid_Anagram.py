
class Solution:
    def validAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        countS = {}
        countT = {}
        for i in enumerate(s):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        return countS == countT
        
