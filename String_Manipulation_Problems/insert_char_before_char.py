

class Solution():
	def insertChar(self, s: str, c: str, ichar: str) -> str:
            i = 0
            while i < len(s):
                if s[i] == c:
                    #print(s[0:i], s[i: len(s)])
                    #happy ha ppy
                    print(len(s))
                    s = s[:i] + ichar + s[i:]
                    i += 1
                i +=1
            return s
    
sol = Solution()
s = "happy"
c = "p"
ichar = "/"
#print(len(c), len(ichar))
print(sol.insertChar(s,c, ichar))
