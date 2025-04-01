from typing import List
from collections import defaultdict

def two_sum(nums: List[int], target: int) -> List[int]:
    sums = defaultdict(int)
    for i, num in enumerate(nums):
        complement = target - num
        if complement in sums:
            return [sums[complement], i]
        sums[num] = i

    return []

nums = [2,7,11,15]
target = 9
result = two_sum(nums, target)
print(result)