class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        myDict = {'I' : 1, 'V' : 5, 'X' : 10,'L' : 50,'C' : 100,'D' : 500,'M' : 1000}
        result = 0
        i = 0
        while i < len(s):
            if (i+1) < len(s) and myDict[s[i]] < myDict[s[i + 1]]: 
                result += myDict[s[i+1]] - myDict[s[i]]
                i+=2    
            else:
                result += myDict[s[i]]
                i+=1
        return result
    

