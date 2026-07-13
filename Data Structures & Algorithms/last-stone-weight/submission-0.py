import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        nums = [-x for x in stones]
        #heapify the nums
        heapq.heapify(nums)

        #iterations
        while len(nums)>1:
            # pop the biggest(min in negative value heap)
            first = heapq.heappop(nums)
            second = heapq.heappop(nums)

            #diff
            new_stone = first - second

            # append new stone
            heapq.heappush(nums, new_stone)
        
        return -nums[0]
        