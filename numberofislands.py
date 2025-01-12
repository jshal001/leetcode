from collections import deque

def numIslands(grid):

    countIslands = 0
    rows, cols = len(grid), len(grid[0])

    visited = set()

    def bfs(i, j):
        #set up queue to go through a breadth first search, adding tuples as you go 

        bfsQueue = deque()
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]

        bfsQueue.append((i,j))

        while bfsQueue: 
            r, c = bfsQueue.popleft()

            #check all directions 
            for currR, currC in directions:
                if (currR + r in range(rows)
                    and currC + c in range(cols) 
                    and grid[currR + r][currC + c] == "1"
                    and (currR + r, currC + c) not in visited):
                    bfsQueue.append((currR + r, currC + c))
                    visited.add((currR + r, currC + c))
            


    for i in range(rows):
        for j in range(cols): 
            if grid[i][j] == "1" and (i,j) not in visited:
                visited.add((i,j))
                #this must be a new island
                countIslands += 1
                #call bfs function to append plots of land to the island
                bfs(i,j)
                
    return countIslands


grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]] 
print(numIslands(grid))