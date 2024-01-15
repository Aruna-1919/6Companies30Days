class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d={}
        for i in words:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        d=  dict(sorted(d.items(), key=lambda x: (-x[1], x[0])))
        print(d)
        ll = [key for key, _ in Counter(d).most_common(k)]
        return ll
        
        
