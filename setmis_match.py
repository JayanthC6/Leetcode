class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        s=sum(nums)
        s2=sum(set(nums))
        duplicate=s-s2
        missing=(n*(n+1))//2-s2

        return duplicate,missing