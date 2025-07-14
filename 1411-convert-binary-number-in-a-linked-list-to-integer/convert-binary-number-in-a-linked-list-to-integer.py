# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode], ans=0) -> int:
        return self.getDecimalValue(head.next, (ans<<1)+head.val) if head else ans
        