def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None or head.next is None:
        return head
    
    prev = None

    while(head is not None):
        temp = head.next
        head.next = prev 
        prev = head
        head = temp
    
    return prev