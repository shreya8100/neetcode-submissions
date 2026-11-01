# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lengthOfList = 0
        current = head
        while current:
            current = current.next
            lengthOfList += 1
        
        indexToDelete = lengthOfList - n

        current = head
        count = 0

        if(indexToDelete == 0):
            return head.next

        while current:
            if(count == indexToDelete-1):
                #nextNode = current.next
                #tempNode = nextNode.next
                #current.next = tempNode
                current.next = current.next.next
                break
            else:
                current = current.next
                count += 1

        return head