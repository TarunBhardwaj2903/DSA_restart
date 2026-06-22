class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count={}
        for i in range(len(text)):
            if text[i] in count :
                count[text[i]] +=1
            else:
                count[text[i]]=1
        return min(count.get("b",0),count.get("a",0),count.get("l",0)//2,count.get("o",0)//2,count.get("n",0))