class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string = str(x)
        rev = string[::-1]
        if string == rev:
             return True
        return False