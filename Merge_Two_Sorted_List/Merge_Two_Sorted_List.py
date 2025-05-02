# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # itr through cur, if cur2 > cur increment cur. if cur2 <= cur insert and increment cur and cur2. NOT GOOD SOLUTION
        # Instead we will make a new list and use a loop comparing val of list1 and 2, build a new list choosing smaller one
        result = ListNode(0)
        current = result
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        # Append any remaining nodes
        current.next = list1 if list1 else list2

        return result.next  # Skip init node

                
                
                