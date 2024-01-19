
class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        d={}
        for i in matches:
            if i[0] not in d:
                d[i[0]]=0
            if i[1] not in d:
                d[i[1]]=1
            elif i[1] in d:
                d[i[1]]+=1
        print(d)
        res=[]
        res.append([x for x in d if d[x]==0])
        res.append([x for x in d if d[x]==1])
        res[0].sort()
        res[1].sort()
        print(res)
        return res
