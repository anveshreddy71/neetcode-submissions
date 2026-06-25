import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        arr = self.get_point_to_distance(points)
        heapq.heapify(arr)

        result= []
        for i in range(k):
            distance, x, y = heapq.heappop(arr)
            result.append([x,y])
        return result
    
    def distance(self, point):
        return math.sqrt((point[0])**2 + (point[1])**2)
    
    def get_point_to_distance(self,points):
        result = []
        for each in points:
            distance = self.distance(each)
            result.append([distance]+each)
        return result


        