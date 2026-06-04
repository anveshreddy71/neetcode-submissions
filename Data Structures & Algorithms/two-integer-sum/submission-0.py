class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx,num in enumerate(nums):
            other_number= target-num
            for idx2, num2 in enumerate(nums[idx+1:]):
                if num2==other_number:
                    return [idx,idx+idx2+1]
                else:
                    continue
        return []
        