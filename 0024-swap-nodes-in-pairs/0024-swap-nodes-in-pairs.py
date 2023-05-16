# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        node = head
        
        while node:
            if node.next is None:
                break
                
            else:
                next_node = node.next
                node.val,next_node.val = next_node.val, node.val
                node = next_node.next
            
        return head