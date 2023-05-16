# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def merge(list1,list2):
            res = None
            head = None
            while list1 is not None and list2 is not None:
                if list1.val <= list2.val:
                    if res is None:
                        res = list1
                        head = list1
                    else:
                        res.next = list1
                        res = list1
                    list1 = list1.next
                else:
                    if res is None:
                        res = list2
                        head = list2
                    else:
                        res.next = list2
                        res = list2
                    list2 = list2.next


            while list1:
                res.next = list1
                res = list1
                list1 = list1.next
            
            while list2:
                res.next = list2
                res = list2
                list2 = list2.next
            return head

        output = None
        for i in range(len(lists)):
            if output is None:
                output = lists[i]
                # print('output updated here',output)
                continue
            else:
                if lists[i] is None:
                    continue
                else:
                    # print('calling with', output)
                    # print('calling with',lists[i])
                    output = merge(output,lists[i])
        return output