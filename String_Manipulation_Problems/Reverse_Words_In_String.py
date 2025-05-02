class Solution(object):
    def ReverseWordsInString(self, s: str) -> str:
        #Technically a answer, but want to reverse words while preserving their words
        #finalStr = s[::-1]
        #return finalStr
        finalStr = []
        word = ""
        for char in s:
            if char == ' ':
                if(word):
                    finalStr.insert(0,word)
                    word = ""
            else:
                word += char
        if(word):
            finalStr.insert(0,word)
        return ' '.join(finalStr)

TestObj = Solution()
string = "Will This Reverse"
print(TestObj.ReverseWordsInString(string))
            