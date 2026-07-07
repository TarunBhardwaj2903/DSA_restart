class Solution:
    def sumAndMultiply(self, n: int) -> int:
        new_num=str(n)
        empty=""
        sum1=0
        if n==0:
            return 0
        for i in new_num:
            if int(i)==0:
                continue
            else:
                empty+=i
                sum1+=int(i)
        return int(empty)*sum1