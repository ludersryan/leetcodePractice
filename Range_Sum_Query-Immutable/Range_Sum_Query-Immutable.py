class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        subarray_sum=0
        array = nums

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        
        
        for k in range(left, right + 1):
            subarray_sum += array[k]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)