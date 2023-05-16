class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        global seen,output_set,output
        seen = set()
        output_set = set()
        output = []

        def dfs(node):
            global seen,output_set,output
            # print('output_set at beginning', output_set)
            # print('output at beginning', output)
            if node.left is None and node.right is None:
                # print('reached end case')
                current = (node.val,None,None)
                subtree = current
                
                if subtree not in seen:
                    seen.add(subtree)
                    # if subtree not in output_set:
                    #     output.append(node)
                    #     output_set.add(subtree)
                else:
                    if subtree not in output_set:
                        output.append(node)
                        output_set.add(subtree)

                    
                # print('level 1 subtree',subtree)
                return subtree
            
            if node.left and node.right:
                left_subtree = dfs(node.left)
                right_subtree = dfs(node.right)
                current = (node.val,)
                subtree =  current + left_subtree + right_subtree
                
                if subtree not in seen:
                    seen.add(subtree)
                    # if subtree not in output_set:
                    #     output.append(node)
                    #     output_set.add(subtree)
                else:
                    if subtree not in output_set:
                        output.append(node)
                        output_set.add(subtree)

                        
                # print('level 4 subtree', subtree)
                return subtree
            
                
            elif node.left:
                
                left_subtree = dfs(node.left)
                current = (node.val,)
                # print(type(current), type(left_subtree))
                subtree =  current + left_subtree + (None,)
                
                if subtree not in seen:
                    seen.add(subtree)
                    # if subtree not in output_set:
                    #     output.append(node)
                    #     output_set.add(subtree)
                else:
                    if subtree not in output_set:
                        output.append(node)
                        output_set.add(subtree)

                # print('level 2 subtree', subtree)
                return subtree
            
            elif node.right:
                
                right_subtree = dfs(node.right)
                current = (node.val,)
                subtree = current + (None,) + right_subtree
                if subtree not in seen:
                    seen.add(subtree)
                    # if subtree not in output_set:
                    #     output.append(node)
                    #     output_set.add(subtree)
                else:
                    if subtree not in output_set:
                        output.append(node)
                        output_set.add(subtree)
                        
                # print('level 3 subtree', subtree)
                return subtree
            else:
                pass
                        
                
        
        # print(output_set)
        dfs(root)
        return output