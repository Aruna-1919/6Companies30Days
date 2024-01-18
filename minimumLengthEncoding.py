class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        s=""
        words=sorted(words, key=lambda x:len(x),reverse=True)
        print(words)
        for i in words:
            if str(i+'#') not in s:
                s=s+i+'#'
        return len(s)        
