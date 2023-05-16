# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global maximum
        maximum = -1*float('inf')
        
        def right_minimum(node):
            # print('right_minimum for', node.val)
            if node.left is None:
                return node.val
            return right_minimum(node.left)
            
        def left_max(node):
            if node.right is None:
                return node.val
            return left_max(node.right)
            
                
        
        
        def max_sum(node):
            global maximum
            max_sum_left = 0
            max_sum_right = 0
            is_bst_left = True
            is_bst_right = True
            if node.left:
                max_sum_left,is_bst_left = max_sum(node.left)

            if node.right:
                max_sum_right, is_bst_right = max_sum(node.right)

            max_sum_val = max_sum_left + node.val + max_sum_right
            
            if (is_bst_left is True) and (is_bst_right is True):
                # print('entered in if', node.val,node.left, node.right)
                if node.left and node.right:
                    # print('in 1')
                    left_min = left_max(node.left)
                    # print('left minimum calculated',left_min)
                    right_min = right_minimum(node.right)
                    # print('right_minimum calculated',right_min)
                    
                    if left_min < node.val and right_min > node.val:
                        is_bst = True
                    else:
                        is_bst = False
                        
                elif node.left:
                    # print('in 2')
                    left_min = left_max(node.left)
                    if left_min < node.val:
                        is_bst = True
                    else:
                        is_bst = False
                    
                elif node.right:
                    # print('in 3')
                    right_min = right_minimum(node.right)
                    if right_min > node.val:
                        is_bst = True
                    else:
                        is_bst = False
                else:
                    is_bst = True
                        
                # print('for node', node.val, is_bst)
                    
            else:
                is_bst = False
            
            

            if is_bst:
                maximum = max(maximum,max_sum_val)

                
            # print(node.val,max_sum_val, maximum, is_bst)

            
            return max_sum_val, is_bst

        result,is_bst = max_sum(root)
        # print('outside',result,is_bst)
        if is_bst:
            maximum = max(maximum,result)
        # print('maximum after update',maximum)
        if maximum < 0:
            return 0
    
        return maximum