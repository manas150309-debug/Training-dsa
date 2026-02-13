# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        curr = head
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                # skip duplicate
                curr.next = curr.next.next
            else:
                # move forward
                curr = curr.next
        
        return head
    