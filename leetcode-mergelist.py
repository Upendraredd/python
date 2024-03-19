# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        if not list1 or not list2:
            return list1 if not list2 else list2
        s,t =(list1,list2) if list1.val < list2.val else (list2,list1)
        h = s
        while s and t:
            while s.next and s.next.val < t.val:
                s=s.next
            s.next,t =t,s.next
            s =s.next
        return h
