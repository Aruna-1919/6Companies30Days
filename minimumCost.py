class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        def floyd_warshall(adj_matrix):
            n = len(adj_matrix)
            dist = [[float('inf')] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if i == j:
                        dist[i][j] = 0
                    elif adj_matrix[i][j] != float('inf'):
                        dist[i][j] = adj_matrix[i][j]

            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        if dist[i][k] != float('inf') and dist[k][j] != float('inf') and dist[i][k] + dist[k][j] < dist[i][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]

            return dist
        
        # Initialize conversion matrix
        kk = [[float('inf')] * 26 for _ in range(26)]
        for i in range(len(original)):
            kk[ord(original[i]) - ord('a')][ord(changed[i]) - ord('a')] = cost[i]

        res = floyd_warshall(kk)
        sum1 = 0
        for i in range(len(source)):
            if source[i] != target[i]:
                if res[ord(source[i]) - ord('a')][ord(target[i]) - ord('a')] == float('inf'):
                    return -1
                else:
                    sum1 += res[ord(source[i]) - ord('a')][ord(target[i]) - ord('a')]
        return sum1
