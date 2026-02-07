class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        num=[]
        for i in range(n):
            num.append(nums[i])
            num.append(nums[i+n])
        return num     