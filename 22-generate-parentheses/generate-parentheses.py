class Solution:
    # def is_valid(self,s):
    #     balance=0
    #     for i in s:
    #         if i == "(" : 
    #             balance+=1
    #         else:
    #             balance -=1
    #         if balance<0:
    #             return False
    #     return balance == 0 
    # def genrate_all(self,curr,n,res):
    #     if len(curr)== 2*n:
    #         if self.is_valid(curr):
    #             res.append(curr)
    #         return
    #     self.genrate_all(curr+"(",n,res)
    #     self.genrate_all(curr+")",n,res)
    def backtrack(self,curr,open,close,n,res):
        if len(curr)==2*n:
            res.append(curr)
            return
        if open < n :
            self.backtrack(curr+"(",open+1,close,n,res)
        if close < open :
            self.backtrack(curr+")",open,close+1,n,res)
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        self.backtrack("",0,0,n,res)
        return res