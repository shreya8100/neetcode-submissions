# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        listArr = []
        currentNode = head
        while currentNode:
            listArr.append(currentNode)
            currentNode = currentNode.next
        i = 0
        j = len(listArr) - 1
        reorderedArr = [0]*len(listArr)
        count = 0
        while (i < j):
            reorderedArr[count] = listArr[i]
            count = count + 1
            reorderedArr[count] = listArr[j]
            count = count + 1
            i = i + 1
            j = j - 1
        if(i == j):
            reorderedArr[count] = listArr[i]
        for k in range(len(reorderedArr) - 1):
            reorderedArr[k].next = reorderedArr[k + 1]
        reorderedArr[-1].next = None
        