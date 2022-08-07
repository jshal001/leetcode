class Solution: 
    def floodFill(self, image, sr, sc, color): 
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        
        if (sr > len(image) - 1) or (sr < 0) or (sc < 0) or (sc > len(image[0]) - 1) or (image[sr][sc] == color):
            return image
        
        else:
            startColor = image[sr][sc]
            image[sr][sc] = color

            if (sc + 1 >= 0) and (sc + 1 <= len(image[0]) - 1) and startColor == image[sr][sc + 1]:
                self.floodFill(image, sr, sc + 1, color)
                
            if (sc - 1 >= 0) and (sc - 1 <= len(image[0]) - 1) and startColor == image[sr][sc - 1]:
                self.floodFill(image, sr, sc - 1, color)

            if (sr + 1 >= 0) and (sr + 1 <= len(image) - 1) and startColor == image[sr + 1][sc]:
                self.floodFill(image, sr + 1, sc, color)

            if (sr - 1 >= 0) and (sr - 1 <= len(image) - 1) and startColor == image[sr - 1][sc]:
                self.floodFill(image, sr - 1, sc, color)
                
                
            return image

solution = Solution()

image = [[0,0,0],[0,0,0], [0,0,0]]
sr = 1
sc = 1
color = 0
print(solution.floodFill(image, sr, sc, color))

#Time Complexity = O(M*N) st. M and N = # of rows and columns 
#Space Complexity = O(M*N) st. M and N = # of rows and columns 