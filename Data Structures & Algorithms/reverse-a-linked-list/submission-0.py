# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next  # 1. Save the next node
            curr.next = prev       # 2. Reverse the pointer
            prev = curr            # 3. Move pointers forward
            curr = next_node
            
        return prev  # 'prev' is the new head