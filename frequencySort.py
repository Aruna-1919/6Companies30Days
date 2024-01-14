class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1
        sorted_dict= dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        ans=""
        for char, count in sorted_dict.items():
            ans += char * count

        return ans
        
