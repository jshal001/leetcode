# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 and not list2:
            return list1
        elif not list1 and list2: 
            return list2
        elif list1 and not list2: 
            return list1
        
        temp = dummyHead = ListNode()

        list1Iter = list1
        list2Iter = list2

        while(list1Iter and list2Iter): 
            if(list1Iter.val < list2Iter.val):
                temp.next = list1Iter
                list1Iter = list1Iter.next
                temp = temp.next
            elif(list1Iter.val > list2Iter.val):
                temp.next = list2Iter
                list2Iter = list2Iter.next
                temp = temp.next
            else: 
                temp.next = list1Iter
                list1Iter = list1Iter.next
                temp = temp.next
        #now that one of the lists have been exhausted 
        if(list1Iter): 
            temp.next = list1Iter
        else: 
            temp.next = list2Iter

        return dummyHead.next



        
        


list1 = ListNode(1, ListNode(4, ListNode(7)))
list2 = ListNode(2, ListNode(3, ListNode(8)))


solution = Solution()

mergedList = solution.mergeTwoLists(list1, list2)

temp = mergedList

while(temp): 
    print(temp.val)
    temp = temp.next


#Time Complexity: O(n)

#Space Complexity: O(n)






    


