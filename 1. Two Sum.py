class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, val in enumerate(nums):
            complement = target - val
            
            if complement in d:
                return [d[complement], i]
            
            d[val] = i
        