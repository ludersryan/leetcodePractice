class Solution():
    def encode(self, strs: list[str]) -> str:
        # add delimiter between strings, along with string length
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "#" + string
        
        return encoded


    def decode(self, s: str) -> list[str]:
        #go through string look for delimiter
        # while looking for delim find len of string positioned before delim
        #append string into list object by using the len char before delimiter
        rList = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#": # find pos of #
                j += 1
            length = int(s[i:j])
            i = j + 1 # Start after '#'
            j = i + length # extract the string
            rList.append(s[i:j])
            i = j
        return rList

s = Solution()
myInput = ["neet","code","love","you"]
print(s.encode(myInput))
print(s.decode(s.encode(myInput)))