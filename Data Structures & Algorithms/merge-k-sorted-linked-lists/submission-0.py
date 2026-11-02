# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while(len(lists) > 1):
            mergedLists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = []
                if(i + 1 < len(lists)):
                    list2 = lists[i+1]
                else:
                    list2 = None
                mergedLists.append(self.mergeTwoLists(list1, list2))
            lists = mergedLists
        
        return lists[0]


    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        sortedList = ListNode()

        dummy = sortedList

        while list1 and list2:
            if(list1.val < list2.val):
                sortedList.next = list1
                list1 = list1.next
            else:
                sortedList.next = list2
                list2 = list2.next
            sortedList = sortedList.next
        if list1:
            sortedList.next = list1
        if list2:
            sortedList.next = list2
        
        sortedList = dummy.next
        return sortedList
