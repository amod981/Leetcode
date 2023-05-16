import heapq
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        
        def get_neighbours(node):
            neighbours = []
            a, b = node
            for dx, dy in [[1,0],[-1,0],[0,1],[0,-1]]:
                nx = a + dx
                ny = b + dy
                if (nx >= 0 and nx < len(grid)) and (ny >= 0 and ny < len(grid[0])):
                    neighbours.append([(nx,ny),grid[nx][ny]])
                 
                
            return neighbours
                    
        # neighbours = get_neighbours((1,0))
        # print('neighbours',neighbours)
        dist = {(i,j):float('inf') for i in range(len(grid)) for j in range(len(grid[0]))}

        def dijkstra(start):
            heap = []
            heapq.heapify(heap)
            dist[start] = grid[start[0]][start[1]]
            heapq.heappush(heap, [dist[start],start])
            visited = set()
            
            while len(heap) > 0:
                current_dist, current_node = heapq.heappop(heap)
                # print(current_node)
                visited.add(current_node)
                
                for node, node_dist in get_neighbours(current_node):
                    if node not in visited:
                        new_dist = max(current_dist,node_dist)
                        if new_dist < dist[node]:
                            dist[node] = new_dist
                            heapq.heappush(heap,[new_dist,node])
                            
        dijkstra((0,0))  
        # print(dist)
        return(dist[len(grid)-1,len(grid[0])-1])
                        