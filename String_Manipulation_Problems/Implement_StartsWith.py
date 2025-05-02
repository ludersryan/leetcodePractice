class Solution(object):
    def implementStartsWith(self, s1: str, prefix: str) -> bool:
        if len(prefix) > len(s1):
            return False
        for i, char in enumerate(prefix):
            if s1[i] != char:
                return False

        return True
    
sol = Solution()
s = "hello"
prefix = "he"
print(sol.implementStartsWith(s, prefix))