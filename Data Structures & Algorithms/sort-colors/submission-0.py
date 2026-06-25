class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        map_ = dict()
        for i in nums:
            map_[i]= map_.get(i,0)+1
        
        sorted_dict = dict(sorted(map_.items()))
        

        
        idx = 0
        for key,value in sorted_dict.items():
            for j in range(value):
                nums[idx+j]= key
            idx = idx + value

