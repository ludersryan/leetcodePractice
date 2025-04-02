class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefixSum = [0] * len(nums)  # Create a new list for prefix sums
        self.prefixSum[0] = nums[0]  # First value is the same

        for i in range(1, len(nums)):
            self.prefixSum[i] = self.prefixSum[i - 1] + nums[i]  # Compute prefix sum

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.prefixSum[right]
        return self.prefixSum[right] - self.prefixSum[left - 1]




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)