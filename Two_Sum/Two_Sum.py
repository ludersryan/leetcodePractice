from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    myDict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in myDict.keys():
            return [myDict[complement], i]
        myDict[num] = i
    return []


nums = [2,7,11,15]
target = 9
result = two_sum(nums, target)
print(result)