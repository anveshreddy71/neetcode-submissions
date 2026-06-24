import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        map_ = self.get_point_to_distance_map(points)

        sorted_dict = dict(sorted(map_.items(), key=lambda x: x[1]))

        sorted_points = [list(x) for x in list(sorted_dict.keys())]

        return sorted_points[:k]

    
    def distance(self, point):
        return math.sqrt((point[0])**2 + (point[1])**2)
    
    def get_point_to_distance_map(self,points):
        map_ = dict()
        for each in points:
            key = tuple(each)
            distance = self.distance(each)
            map_[key]= distance
        return map_


        