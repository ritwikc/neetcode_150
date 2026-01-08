class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_vals = set()
        duplicate_flag=False
        for i in nums: 
            if i in unique_vals:
                duplicate_flag=True
                break
            else:
                unique_vals.add(i)
        return(duplicate_flag)
