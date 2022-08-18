'''
Given an m x n 2D binary grid grid which represents a map of 
'1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting 
adjacent lands horizontally or vertically. You may assume all 
four edges of the grid are all surrounded by water.
'''

class Solution(object):
    def findID(self, r, c, i, j):
        return i * c + j
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        # initialize the graph adjacency list
        graph = {}
        # find the number of rows and columns
        c = len(grid[0])
        r = len(grid)
        
        # construct the graph
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ID = self.findID(r, c, i, j)
                if grid[i][j] == '0':
                    continue
                else:
                    graph[ID] = []
                if i > 0 and grid[i - 1][j] == '1':
                    graph[ID].append(self.findID(r,c,i-1,j))
                if i < r - 1 and grid[i + 1][j] == '1':
                    graph[ID].append(self.findID(r,c,i+1,j))
                if j > 0 and grid[i][j - 1] =='1':
                    graph[ID].append(self.findID(r,c,i,j-1))
                if j < c - 1 and grid[i][j + 1] == '1':
                    graph[ID].append(self.findID(r,c,i,j+1))
                    
        # initialize the visited array
        found = {i:False for i in graph.keys()}
        
        # create a dfs function to find the number of islands
        def dfs(vertex):
            found[vertex] = True
            for v in graph[vertex]:
                if not found[v]:
                    dfs(v)
        
        islands = 0
        for vertex in found.keys():
            if not found[vertex]:
                dfs(vertex)
                islands += 1
        return islands