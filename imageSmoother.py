class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        rows,cols=len(img),len(img[0])
        result=[[0]*cols for i in range(rows)]
        for row in range(rows):
            for col in range(cols):
                count=0
                total=0
                for i in range(max(0,row-1),min(row+2,rows)):
                    for j in range(max(0,col-1),min(col+2,cols)):
                        total+=img[i][j]
                        count+=1
                result[row][col]=total//count
        return result

                    
        
