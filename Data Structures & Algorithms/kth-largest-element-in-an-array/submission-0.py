import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        new_nums = [-x for x in nums]
        heapq.heapify(new_nums)

        for i in range(k):
            res = heapq.heappop(new_nums)
        
        return -res

        