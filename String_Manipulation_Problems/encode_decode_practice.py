# Design an algo to encode a list of strings to a single string.
# Encoded string is then decoded back to the orignal list of strings
# Input: ["neet", "code", "loves", "you"]
# Input can be any char
# We need to add delimiters, done in encode
# Encode must add delimiter plus a num of how many chars in string since it could contain the delimiter

# Decode will then take string len until delimiter
# using this split string back into list


class Solution():
    def encode(self,myList: list[str]) -> str:
        # Our delimiter will be "/"
        rStr = ""
        for s in myList:
            rStr += str(len(s)) + "/" + s
        
        return rStr
    """
    At this point we will have 4/neet4/code5/loves3/you
    """
    
    def decode(self,myStr: str) -> list[str]:
        i = 0
        rList = []
        # i is now at place of first delimiter, in our case i=1
        # Use j and i as points for string extraction, i will be the start j will be the end
        while i<len(myStr):
            j = i
            while myStr[j] != "/":
                j+=1
            strlen = int(myStr[i:j]) # this will hold val of len of string
            i = j + 1 # i will be the start of next str
            j = strlen + i
            rList.append((myStr[i:j]))
            i = j
        return rList



    
sol = Solution()
input = ["neet", "code", "loves", "you"]
print(sol.decode(sol.encode(input)))

