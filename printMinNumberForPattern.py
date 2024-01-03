class Solution:
    def cal_x(self, S):
        c = 0
        i = 0
        while i < len(S) and S[i] == "I":
            c += 1
            i += 1
        return c

    def cal_zw(self, S, i):
        j = 0
        while i < len(S):
            if S[i] == "I":
                j += 1
                i += 1
            else:
                j=j-1
                break
        return [j, i]

    def printMinNumberForPattern(self, S):
        res = []
        re = [i for i in range(1, len(S) + 2)]
        i = 0
        while i < len(S):
            if i == 0:
                c1 = self.cal_x(S)
                res.extend(re[:c1])
                re = [i for i in re if i not in res]
                i += c1
            d = 0
            while i < len(S) and S[i] == 'D':
                d += 1
                i += 1
            res.extend(re[:d + 1][::-1])
            re = [i for i in re if i not in res]
            if i < len(S) and S[i] == "I":
                c2, i = self.cal_zw(S, i)
                res.extend(re[:c2])
                re = [i for i in re if i not in res]
        return "".join(map(str, res))
