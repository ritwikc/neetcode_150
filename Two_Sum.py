class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_mapper_nums=dict()
        remain_from_target=set()
        for i in range(len(nums)):
            if nums[i] in remain_from_target:
                return[index_mapper_nums[target - nums[i]], i]
            
            if nums[i] not in index_mapper_nums:
                index_mapper_nums[nums[i]] = i
                remain_from_target.add(target-nums[i])
