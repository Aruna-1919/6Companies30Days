class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """

        count=0
        seat_grid=[[0]*10 for _ in range(n)]
        #print(seat_grid)
        for i in reservedSeats:
            seat_grid[i[0]-1][i[1]-1]=1
        #print(seat_grid)
        for i in range(n):
            if seat_grid[i][1]==0 and seat_grid[i][2]==0 and seat_grid[i][3]==0 and seat_grid[i][4]==0:
                count+=1
                seat_grid[i][1]=1
                seat_grid[i][2]=1
                seat_grid[i][3]=1
                seat_grid[i][4]=1
            if seat_grid[i][3]==0 and seat_grid[i][4]==0 and seat_grid[i][5]==0 and seat_grid[i][6]==0:
                count+=1
                seat_grid[i][3]=1
                seat_grid[i][4]=1
                seat_grid[i][5]=1
                seat_grid[i][6]=1
            if seat_grid[i][5]==0 and seat_grid[i][6]==0 and seat_grid[i][7]==0 and seat_grid[i][8]==0:
                count+=1
                seat_grid[i][5]=1
                seat_grid[i][6]=1
                seat_grid[i][7]=1
                seat_grid[i][8]=1
        return count


        
        
