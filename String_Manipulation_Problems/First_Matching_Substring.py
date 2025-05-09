class Solution():
    def firstMatchingSubstring(self,text: str, pat: str) -> int:
        if not text or len(pat) > len(text):
            return -1
        # iterate over text and check for pat at each char
        if text == pat:
            return 0
        
        i = 0
        while i <= len(text) - len(pat):
            if(text[i:i + len(pat)] == pat):
                return i
            i+= 1
        return -1

sol = Solution()
text = "abracadabra"
pat = "cad"
print(sol.firstMatchingSubstring(text, pat))