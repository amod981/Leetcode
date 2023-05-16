from copy import deepcopy

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        global cache;
        cache = {}
        seen = set()
        def find_neighbours(node):
            i,j = node
            delta = [[1,0],[0,1],[-1,0],[0,-1]]
            neighbour_nodes = []
            for move in delta:
                a,b = move
                if ((i+a >= 0 and i +a < len(matrix)) and (j + b >= 0 and j + b < len(matrix[0]))):
                    if matrix[i+a][j+b] > matrix[i][j]:
                        neighbour_nodes.append((i+a,j+b))

            return neighbour_nodes

        
        def dfs(node):
            neighbours = find_neighbours(node)
            if len(neighbours) == 0:
                cache[node] = 1
                seen.add(node)
                return 1
            node_level_max = 0
            for neighbour in neighbours:
                if neighbour in seen:
                    count = cache[neighbour] + 1
                else:
                    count = dfs(neighbour) + 1
                node_level_max = max(count,node_level_max)
                
            cache[node] = node_level_max 
            seen.add(node)
            return node_level_max
        
        maximum = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # print(i,j)
                if (i,j) in seen:
                    maximum = max(maximum,cache[(i,j)])
                else:
                    output = dfs((i,j))
                    # print(output)
                    maximum = max(maximum,output)
                # print(cache)
        return maximum
                    
                