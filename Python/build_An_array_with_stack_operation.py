class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res=[]
        index=0 
        for nums in range(1,n+1):
            if index==len(target):
                break
            res.append("Push")
            if nums==target[index]:
                index+=1
            else:
                res.append("Pop")
        return res               