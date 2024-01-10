class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        dist=[[float('inf')]*n for _ in range(n)]
        for i in edges:
            dist[i[0]][i[1]]=i[2]
        for i in range(n):
            for j in range(n):
                if i==j:
                    dist[i][j]=0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j]>dist[i][k]+dist[k][j]:
                        dist[i][j]=dist[i][k]+dist[k][j]
                    else:
                        dist[i][j]=min(dist[j][i],dist[i][j])
        city=[0]*n
        for i in range(n):
            for j in range(n):
                if dist[i][j]>=1 and dist[i][j]<=distanceThreshold:
                    city[i]+=1
        last_index = len(city) - 1 -city[::-1].index(min(city))
        return last_index
        

        
