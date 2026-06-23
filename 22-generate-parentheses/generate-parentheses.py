class Solution:
    def is_valid(self,s):
        balance=0
        for i in s:
            if i == "(" : 
                balance+=1
            else:
                balance -=1
            if balance<0:
                return False
        return balance == 0 
    def genrate_all(self,curr,n,res):
        if len(curr)== 2*n:
            if self.is_valid(curr):
                res.append(curr)
            return
        self.genrate_all(curr+"(",n,res)
        self.genrate_all(curr+")",n,res)
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        self.genrate_all("",n,res)
        return res