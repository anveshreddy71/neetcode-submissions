class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_number= 0
        new_max=0
        for i in nums:
            if i ==1:
                new_max+=1
            elif i==0:
                if max_number < new_max:
                    max_number= new_max
                new_max=0
        if max_number < new_max:
            return new_max
        else:
            return max_number              
           