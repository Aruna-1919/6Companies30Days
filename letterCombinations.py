class Solution(object):
    def combine_lists(self,list2, list1):
        combined_list = [first + second for first in list1 for second in list2]
        return combined_list
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d={"1":[""],"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        if len(digits)==0:
            return []
        if(len(digits)==1):
            return d[digits]
        else:
            m=[]
            l=[""]
            k=int(digits)
            while k>0:
                l=self.combine_lists(l,d[str(k%10)])
                k=k//10
            return l


        
