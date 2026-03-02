class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        bucket={}
        bucket_size= valueDiff+1
        for i,num in enumerate(nums):
            bucket_id=num//bucket_size
            if bucket_id in bucket:
                return True
            if (bucket_id - 1) in bucket and abs(num-bucket[bucket_id-1]) <= valueDiff:
                return True
            if (bucket_id+1) in bucket and abs(num-bucket[bucket_id+1]) <=valueDiff:
                return True
            bucket[bucket_id]=num
            if i >= indexDiff:
                old_num = nums[i - indexDiff]
                old_bucket_id = old_num // bucket_size
                del bucket[old_bucket_id]
        return False            