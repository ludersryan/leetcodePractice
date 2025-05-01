# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # itr through cur, if cur2 > cur increment cur. if cur2 <= cur insert and increment cur and cur2
        cur = list1 # current head of final list we will use
        cur2 = list2
        while cur:
            if cur2.val <= cur.val:
                
                