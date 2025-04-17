from typing import List
from collections import deque

def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    
    q = deque()
    dir = [0, 1, 0, -1, 0]
    m = len(mat)
    n = len(mat[0])

    for r in range(m): 
        for c in range(n): 
            if mat[r][c] == 0: 
                q.append((r, c))
            else: 
                mat[r][c] = -1

    
    while q:
        currR, currC = q.popleft()

        for i in range(len(dir) - 1): 
            if (currR + dir[i] < m and currR + dir[i] >= 0 and currC + dir[i + 1] < n and currC + dir[i + 1] >= 0): 
                if mat[currR + dir[i]][currC + dir[i + 1]] >= 0:
                    continue
                else:     
                    print(mat[currR][currC])
                    mat[currR + dir[i]][currC + dir[i + 1]] = mat[currR][currC] + 1
                    q.append((currR + dir[i], currC + dir[i + 1])) 
    return mat
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #***************************** This solution sucks ************************************#
    
    # uncalculatedMap = {}


    # for i in range(len(mat)):
    #     for j in range(len(mat[0])):
    #         if mat[i][j] == 0: 
    #             uncalculatedMap[str(i) + str(j)] = False
    #             continue 
    #         if(i - 1 >= 0 and not uncalculatedMap[str(i - 1) + str(j)]):
    #             upValue = mat[i - 1][j]
    #         else: 
    #             upValue = -1
    #         if(j - 1 >= 0 and not uncalculatedMap[str(i) + str(j - 1)]):
    #             leftValue = mat[i][j - 1]
    #         else: 
    #             leftValue = -1

    #         if leftValue >= 0 and upValue >= 0:
    #             uncalculatedMap[str(i) + str(j)] = False
    #             mat[i][j] = min(upValue, leftValue) + 1
    #         elif leftValue < 0 and upValue >= 0:
    #             uncalculatedMap[str(i) + str(j)] = False
    #             mat[i][j] = upValue + 1
    #         elif leftValue >= 0 and upValue < 0: 
    #             uncalculatedMap[str(i) + str(j)] = False
    #             mat[i][j] = leftValue + 1
    #         else: 
    #             key = str(i) + str(j)
    #             uncalculatedMap[key] = True
    #             continue
        

    
    # #up/left direction
    # for i in range(len(mat) - 1, -1, -1):
    #     for j in range(len(mat[0]) - 1, -1, -1):
    #         if mat[i][j] == 0: 
    #             continue 
    #         if(i + 1 < len(mat)):
    #             downValue  = mat[i + 1][j]
    #         else: 
    #             downValue  = -1
    #         if(j + 1 < len(mat[0])):
    #             rightValue = mat[i][j + 1]
    #         else: 
    #             rightValue = -1
    #         # if i == 0 and j == 0:
    #         #     mat[i][j] = min(downValue, rightValue) + 1
    #         #     continue 

    #         if rightValue >= 0 and downValue >= 0:
    #             if (uncalculatedMap[str(i) + str(j)]):
    #                 mat[i][j] = min(downValue, rightValue) + 1
    #             else: 
    #                 mat[i][j] = min(min(downValue, rightValue) + 1, mat[i][j])

    #         elif rightValue < 0 and downValue >= 0:
    #             if (uncalculatedMap[str(i) + str(j)]):
    #                 mat[i][j] = downValue + 1
    #             else:
    #                 mat[i][j] = min(downValue + 1, mat[i][j])
    #         elif rightValue >= 0 and downValue < 0: 
    #             if (uncalculatedMap[str(i) + str(j)]):
    #                 mat[i][j] = rightValue + 1
    #             else:   
    #                 mat[i][j] = min(rightValue + 1, mat[i][j])
    #         else: 
    #             continue
    # return mat



mat = [[0,0,0],[0,1,0],[1,1,1]]
print(updateMatrix(mat))
