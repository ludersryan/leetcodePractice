from typing import List
from collections import defaultdict

class Solution:
    def productExceptSelf(self, nums: List[int] ) -> List[int]:
        pre = 1
        post = 1
        n = len(nums)
        ans = [1] * n
        for i in range(n):
            ans[i] = pre
            pre = nums[i]*pre
        for i in reversed(range(n)):
            ans[i] = ans[i] * post
            post = post*nums[i]
        return ans

sol = Solution()
nums = [1,2,3,4]
result = sol.productExceptSelf(nums)
print(result)
