# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #Floyd's cycle detection algo
        slow = fast = head

        while(slow and fast and fast.next): 
            slow = slow.next
            fast = fast.next.next
            if(fast == slow):
                return True
        return False

#Time Complexity: O(n)
#Space Complexity: O(1)